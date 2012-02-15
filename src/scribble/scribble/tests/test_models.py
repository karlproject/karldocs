import mock
import unittest


class TestSphinxDocument(unittest.TestCase):

    def get_class(self):
        from scribble.models import SphinxDocument
        return SphinxDocument

    def make_one(self, sphinx, path):
        return self.get_class()(sphinx, path)

    def test_constructor(self):
        sphinx = mock.Mock()
        sphinx.get_document.return_value = {
            'foo': 'bar',
            'bees': 'knees'}
        doc = self.make_one(sphinx, '/')
        sphinx.get_document.assert_called_once_with('')
        self.assertEqual(doc.foo, 'bar')
        self.assertEqual(doc.bees, 'knees')

    def test_getitem(self):
        sphinx = mock.Mock()
        sphinx.get_document.return_value = {}
        doc = self.make_one(sphinx, '/')
        sphinx.get_document = mock.Mock()
        sphinx.get_document.return_value = {}
        subdoc = doc['subdoc']
        self.assertEqual(subdoc.__parent__, doc)
        self.assertEqual(subdoc.__name__, 'subdoc')
        sphinx.get_document.assert_called_once_with('subdoc')

    def test_getitem_keyerror(self):
        from sphinx.websupport.errors import DocumentNotFoundError
        sphinx = mock.Mock()
        sphinx.get_document.return_value = {}
        doc = self.make_one(sphinx, '/')
        sphinx.get_document = mock.Mock()
        sphinx.get_document.side_effect = DocumentNotFoundError
        with self.assertRaises(KeyError):
            doc['subdoc']


class TestSiteRoot(unittest.TestCase):

    def get_class(self):
        from scribble.models import SiteRoot
        return SiteRoot

    def make_one(self, datadir):
        return self.get_class()(
            {'sphinx_data': datadir,
             'collections': 'friends enemies'})

    @mock.patch('scribble.models.WebSupport')
    def test_constructor(self, WebSupport):
        sphinx = mock.Mock()
        sphinx.get_document.return_value = {
            'foo': 'bar',
            'bees': 'knees'}
        WebSupport.return_value = sphinx
        doc = self.make_one('/path/to/sphinx/docs')
        WebSupport.assert_called_once_with(datadir='/path/to/sphinx/docs')
        sphinx.get_document.assert_called_once_with('')
        self.assertEqual(doc.foo, 'bar')
        self.assertEqual(doc.bees, 'knees')

    @mock.patch('scribble.models.WebSupport')
    def test_getitem(self, WebSupport):
        sphinx = mock.Mock()
        sphinx.get_document.return_value = {}
        WebSupport.return_value = sphinx
        doc = self.make_one('/path/to/sphinx/docs')
        sphinx.get_document = mock.Mock()
        sphinx.get_document.return_value = {}
        subdoc = doc['subdoc']
        self.assertEqual(subdoc.__parent__, doc)
        self.assertEqual(subdoc.__name__, 'subdoc')
        sphinx.get_document.assert_called_once_with('subdoc')

    @mock.patch('scribble.models.WebSupport')
    def test_getitem_collections(self, WebSupport):
        from scribble.models import Collections
        sphinx = mock.Mock()
        sphinx.get_document.return_value = {}
        WebSupport.return_value = sphinx
        doc = self.make_one('/path/to/sphinx/docs')
        collections = doc['collections']
        self.assertIsInstance(collections, Collections)
        self.assertEqual(collections.__parent__, doc)
        self.assertEqual(collections.__name__, 'collections')


class TestCollections(unittest.TestCase):

    def get_class(self):
        from scribble.models import Collections
        return Collections

    def make_one(self):
        return self.get_class()({'collections': 'friends enemies'})

    @mock.patch('scribble.models.redis.Redis')
    def test_getitem(self, Redis):
        from scribble.models import Collection
        collections = self.make_one()
        friends = collections['friends']
        self.assertIsInstance(friends, Collection)
        self.assertEqual(friends.__parent__, collections)
        self.assertEqual(friends.__name__, 'friends')

    @mock.patch('scribble.models.redis.Redis')
    def test_keys(self, Redis):
        collections = self.make_one()
        self.assertEqual(set(collections.keys()), set(['friends', 'enemies']))


def dummy_uuid():
    return 12345


def dummy_time():
    return 42.0


class TestCollection(unittest.TestCase):

    def setUp(self):
        self.redis = mock.Mock()

    def get_class(self):
        from scribble.models import Collection
        return Collection

    def make_one(self):
        return self.get_class()(self.redis, 'friends')

    @mock.patch('scribble.models.time.time', dummy_time)
    @mock.patch('scribble.models.uuid.uuid1', dummy_uuid)
    def test_add(self):
        friends = self.make_one()
        self.assertEqual(friends.add('"Test Data"'), '12345')
        pipe = self.redis.pipeline.return_value
        pipe.sadd.assert_called_once_with(
            'scribble.collection.friends', '12345')
        self.assertEqual(pipe.set.mock_calls, [
            mock.call('12345', '"Test Data"'),
            mock.call('scribble.collection.friends.mtime', '42.0'),
            mock.call('12345.mtime', '42.0')])
        pipe.execute.assert_called_once_with()


    def test_getitem_not_a_member(self):
        self.redis.sismember.return_value = False
        with self.assertRaises(KeyError):
            self.make_one()['12345']
        self.redis.sismember.assert_called_once_with(
            'scribble.collection.friends', '12345')

    def test_getitem(self):
        self.redis.sismember.return_value = True
        pipe = self.redis.pipeline.return_value
        pipe.execute.return_value = ['"Test Data"', '42.0']
        friends = self.make_one()
        item = friends['12345']
        self.assertEqual(item, '"Test Data"')
        self.assertEqual(item.__parent__, friends)
        self.assertEqual(item.__name__, '12345')
        self.assertEqual(item.mtime, 42.0)
        self.assertEqual(pipe.get.mock_calls, [
            mock.call('12345'), mock.call('12345.mtime')])
        self.redis.sismember.assert_called_once_with(
            'scribble.collection.friends', '12345')

    def test_setitem_not_a_member(self):
        self.redis.sismember.return_value = False
        with self.assertRaises(KeyError):
            self.make_one()['12345'] = '"Different Data"'
        self.redis.sismember.assert_called_once_with(
            'scribble.collection.friends', '12345')

    @mock.patch('scribble.models.time.time', dummy_time)
    def test_setitem(self):
        self.redis.sismember.return_value = True
        self.make_one()['12345'] = '"Different Data"'
        pipe = self.redis.pipeline.return_value
        self.assertEqual(pipe.set.mock_calls, [
            mock.call('12345', '"Different Data"'),
            mock.call('12345.mtime', '42.0'),
            mock.call('scribble.collection.friends.mtime', '42.0')])
        pipe.execute.assert_called_once_with()

    def test_delitem_not_a_member(self):
        self.redis.sismember.return_value = False
        with self.assertRaises(KeyError):
            del self.make_one()['12345']
        self.redis.sismember.assert_called_once_with(
            'scribble.collection.friends', '12345')

    @mock.patch('scribble.models.time.time', dummy_time)
    def test_delitem(self):
        self.redis.sismember.return_value = True
        del self.make_one()['12345']
        pipe = self.redis.pipeline.return_value
        self.assertEqual(pipe.delete.mock_calls,
                         [mock.call('12345'), mock.call('12345.mtime')])
        pipe.srem.assert_called_once_with(
            'scribble.collection.friends', '12345')
        pipe.set.assert_called_once_with(
            'scribble.collection.friends.mtime', '42.0')
        pipe.execute.assert_called_once_with()


    def test_items_empty(self):
        self.redis.smembers.return_value = None
        self.assertEqual(self.make_one().items(), [])

    def test_items(self):
        self.redis.smembers.return_value = ['12345', '23456']
        pipe = self.redis.pipeline.return_value
        pipe.execute.return_value = ['"Test One"', '42.0', '"Test Two"', '43.0']
        friends = self.make_one()
        (id1, item1), (id2, item2) = friends.items()
        self.assertEqual(id1, '12345')
        self.assertEqual(item1, '"Test One"')
        self.assertEqual(item1.__parent__, friends)
        self.assertEqual(item1.__name__, '12345')
        self.assertEqual(id2, '23456')
        self.assertEqual(item2, '"Test Two"')
        self.assertEqual(item2.__parent__, friends)
        self.assertEqual(item2.__name__, '23456')
        self.assertEqual(pipe.get.mock_calls, [
            mock.call('12345'), mock.call('12345.mtime'),
            mock.call('23456'), mock.call('23456.mtime')])
        pipe.execute.assert_called_once_with()

    @mock.patch('scribble.models.time.time', dummy_time)
    def test_mtime_not_set(self):
        self.redis.get.return_value = None
        self.assertEqual(self.make_one().mtime(), 42.0)
        self.redis.get.assert_called_once_with(
            'scribble.collection.friends.mtime')
        self.redis.set.assert_called_once_with(
            'scribble.collection.friends.mtime', '42.0')

    def test_mtime(self):
        self.redis.get.return_value = '56.0'
        self.assertEqual(self.make_one().mtime(), 56.0)
        self.redis.get.assert_called_once_with(
            'scribble.collection.friends.mtime')
