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
        return self.get_class()(datadir)

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


