import redis
import time
import uuid

from pyramid.decorator import reify

from sphinx.websupport import WebSupport
from sphinx.websupport.errors import DocumentNotFoundError


class SphinxDocument(object):
    __parent__ = None
    __name__ = None
    sphinx = None

    def __init__(self, sphinx, path):
        path = path.lstrip('/')
        self.sphinx = sphinx
        self.path = path
        self.__dict__.update(sphinx.get_document(path))

    def __getitem__(self, name):
        try:
            item = SphinxDocument(self.sphinx, '%s/%s' % (self.path, name))
            item.__parent__ = self
            item.__name__ = name
            return item
        except DocumentNotFoundError:
            raise KeyError(name)


class SiteRoot(SphinxDocument):

    def __init__(self, settings):
        self.settings = settings
        sphinx_data = settings['sphinx_data']
        SphinxDocument.__init__(self, WebSupport(datadir=sphinx_data), '')

    def __getitem__(self, name):
        if name == 'collections':
            return self.collections
        return super(SiteRoot, self).__getitem__(name)

    @reify
    def collections(self):
        collections = Collections(self.settings)
        collections.__parent__ = self
        return collections


class Collections(object):
    __name__ = 'collections'

    def __init__(self, settings):
        args = dict([(k[6:], v) for k, v in settings.items()
                     if k.startswith('redis.')])
        self.prefix = args.pop('prefix', 'scribble.collection')
        self.redis = redis.Redis(**args)
        self.collections = collections = {}
        for name in settings['collections'].split():
            collections[name] = None

    def __getitem__(self, name):
        collections = self.collections
        collection = collections[name]
        if collection is None:
            collections[name] = collection = Collection(
                self.redis, name, self.prefix)
            collection.__parent__ = self
        return collection

    def keys(self):
        return self.collections.keys()


class Collection(object):

    def __init__(self, redis, name, prefix):
        self.redis = redis
        self.__name__ = name
        self.key = '%s.%s' % (prefix, name)
        self.mtime_key = '%s.mtime' % self.key

    def add(self, data):
        id = str(uuid.uuid1())
        now = str(time.time())
        pipe = self.redis.pipeline()
        pipe.sadd(self.key, id)
        pipe.set(id, data)
        pipe.set(self.mtime_key, now)
        pipe.set('%s.mtime' % id, now)
        pipe.execute()
        return id

    def __getitem__(self, id):
        redis = self.redis
        if not redis.sismember(self.key, id):
            raise KeyError(id)
        pipe = redis.pipeline()
        pipe.get(id)
        pipe.get('%s.mtime' % id)
        data, mtime = pipe.execute()

        item = Item(data)
        item.__parent__ = self
        item.__name__ = id
        item.mtime = float(mtime)
        return item

    def __setitem__(self, id, data):
        redis = self.redis
        if not redis.sismember(self.key, id):
            raise KeyError(id)
        now = str(time.time())
        pipe = redis.pipeline()
        pipe.set(id, data)
        pipe.set('%s.mtime' % id, now)
        pipe.set(self.mtime_key, now)
        pipe.execute()

    def __delitem__(self, id):
        redis = self.redis
        if not redis.sismember(self.key, id):
            raise KeyError(id)
        now = str(time.time())
        pipe = redis.pipeline()
        pipe.delete(id)
        pipe.delete('%s.mtime' % id)
        pipe.srem(self.key, id)
        pipe.set(self.mtime_key, now)
        pipe.execute()

    def items(self):
        # WARNING: expensive for large collections
        redis = self.redis
        ids = redis.smembers(self.key)
        if not ids:
            return []
        ids = sorted(ids)
        pipe = redis.pipeline()
        for id in ids:
            pipe.get(id)
            pipe.get('%s.mtime' % id)
        items = []
        pipedata = pipe.execute()
        for id in ids:
            item = Item(pipedata.pop(0))
            item.mtime = float(pipedata.pop(0))
            item.__parent__ = self
            item.__name__ = id
            items.append((id, item))
        assert not pipedata # sanity check, pipedata should be exhausted
        return items

    def mtime(self):
        mtime = self.redis.get(self.mtime_key)
        if mtime:
            mtime = float(mtime)
        else:
            mtime = time.time()
            self.redis.set(self.mtime_key, str(mtime))
        return mtime


class Item(str):
    pass

