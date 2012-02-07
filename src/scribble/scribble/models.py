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

    def __init__(self, sphinx_data):
        SphinxDocument.__init__(self, WebSupport(datadir=sphinx_data), '')
