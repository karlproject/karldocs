import mock
import unittest


class TestAPI(unittest.TestCase):

    def test_get_collections(self):
        from scribble.api import get_collections
        context = mock.Mock()
        context.keys.return_value = ['joe', 'mama']
        self.assertEqual(get_collections(context, None), ['joe', 'mama'])

    def test_get_collection(self):
        from scribble.models import Item
        from scribble.api import get_collection
        item1 = Item('"abc"')
        item1.__name__ = '123'
        item2 = Item('"def"')
        item2.__name__ = '456'
        context = mock.Mock()
        context.mtime.return_value = 42.0
        context.items.return_value = [item1, item2]
        request = mock.Mock()
        collection = get_collection(context, request)
        self.assertEqual(collection, [('123', u'abc'), ('456', u'def')])
        self.assertEqual(request.response.last_modified, 42.0)

    def test_add_item(self):
        from scribble.api import add_item
        context = mock.Mock()
        context.add.return_value = '12345'
        request = mock.Mock()
        request.body = '"Howdy!"'
        self.assertEqual(add_item(context, request), '12345')
        context.add.assert_called_once_with('"Howdy!"')

    def test_get_item(self):
        from scribble.api import get_item
        context = mock.Mock()
        context.__name__ = '12345'
        context.mtime = 42.0
        request = mock.Mock()
        request.response.headers = {}
        response = get_item(context, request)
        self.assertEqual(response.body, context)
        self.assertEqual(response.headers['X-Scribble-Id'], '12345')
        self.assertEqual(response.last_modified, 42.0)
        self.assertEqual(response.content_type, 'application/json')

    def test_update_item(self):
        from scribble.api import update_item
        context = mock.Mock()
        context.__parent__ = {}
        context.__name__ = '12345'
        request = mock.Mock()
        request.body = '"New Data"'
        update_item(context, request)
        self.assertEqual(context.__parent__['12345'], '"New Data"')
        self.assertEqual(request.response.content_type, 'application/json')

    def test_delete_item(self):
        from scribble.api import delete_item
        context = mock.Mock()
        context.__parent__ = {'12345': None}
        context.__name__ = '12345'
        request = mock.Mock()
        delete_item(context, request)
        self.assertNotIn('12345', context.__parent__)
        self.assertEqual(request.response.content_type, 'application/json')
