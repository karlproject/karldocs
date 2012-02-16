import unittest


class FunctionalTests(unittest.TestCase):
    collections = 'books lps'

    def setUp(self):
        self.clear_data()

        from scribble import main
        from webtest import TestApp
        import os
        import pkg_resources
        import tempfile
        self.tmp = tmp = tempfile.mkdtemp('.scribble-tests')
        sphinx_build = os.path.join(tmp, 'sphinx_build')
        sphinx_src = pkg_resources.resource_filename(
            'scribble.tests', 'sphinxdocs')
        config = {'sphinx_src': sphinx_src, 'sphinx_build': sphinx_build,
                  'collections': self.collections, 'redis.prefix': 'test'}
        self.app = TestApp(main(config))

    def tearDown(self):
        import shutil
        self.clear_data()
        shutil.rmtree(self.tmp)

    def clear_data(self):
        import redis
        service = redis.Redis()
        for name in self.collections.split():
            key = 'test.%s' % name
            members = service.smembers(key)
            pipe = service.pipeline()
            for member in members:
                pipe.delete(member)
                pipe.delete('%s.mtime' % member)
            pipe.delete(key)
            pipe.delete('%s.mtime' % key)
            pipe.execute()

    def test_sphinx_docs(self):
        response = self.app.get('/')
        self.assertEqual(response.status, '200 OK')
        response = self.app.get('/one')
        self.assertEqual(response.status, '200 OK')
        response = self.app.get('/two')
        self.assertEqual(response.status, '200 OK')

    def test_collections_api(self):
        from json import loads
        response = self.app.get('/collections')
        self.assertEqual(loads(response.body), ['books', 'lps'])
        response = self.app.get('/collections/books')
        self.assertEqual(loads(response.body), [])
        response = self.app.post('/collections/books',
                                 '{"foo": "bar", "abc": "123"}')
        id1 = loads(response.body)
        item1 = str('/collections/books/%s' % id1)
        response = self.app.get(item1)
        self.assertEqual(loads(response.body), {'foo': 'bar', 'abc': '123'})
        self.assertEqual(response.headers['X-Scribble-Id'], id1)
        response = self.app.get('/collections/books')
        self.assertEqual(loads(response.body), [
            [id1, {'foo': 'bar', 'abc': '123'}]])
        response = self.app.post('/collections/books',
                                 '{"hat": "trick", "beer": "belly"}')
        id2 = loads(response.body)
        item2 = str('/collections/books/%s' % id2)
        response = self.app.get(item2)
        self.assertEqual(loads(response.body),
                         {'hat': 'trick', 'beer': 'belly'})
        self.assertEqual(response.headers['X-Scribble-Id'], id2)
        response = self.app.get('/collections/books')
        self.assertEqual(loads(response.body), [
            [id1, {'foo': 'bar', 'abc': '123'}],
            [id2, {'hat': 'trick', 'beer': 'belly'}]
        ])
        self.app.put(item2, '{"hat": "cat", "jelly": "belly"}')
        response = self.app.get(item2)
        self.assertEqual(loads(response.body),
                         {'hat': 'cat', 'jelly': 'belly'})
        response = self.app.get('/collections/books')
        self.assertEqual(loads(response.body), [
            [id1, {'foo': 'bar', 'abc': '123'}],
            [id2, {'hat': 'cat', 'jelly': 'belly'}]
        ])
        self.app.delete(item1)
        response = self.app.get('/collections/books')
        self.assertEqual(loads(response.body), [
            [id2, {'hat': 'cat', 'jelly': 'belly'}]
        ])






