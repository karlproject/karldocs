import mock
import unittest


class TestBuildSphinxData(unittest.TestCase):

    @mock.patch('scribble.build_sphinx_data.sys.argv', ['/test/bin/python'])
    @mock.patch('scribble.build_sphinx_data.os.path.exists')
    @mock.patch('scribble.build_sphinx_data.WebSupport')
    @mock.patch('scribble.build_sphinx_data.loadapp')
    def test_it(self, loadapp, WebSupport, exists):
        from scribble.build_sphinx_data import main
        settings = {'sphinx_src': 'sphinx_src', 'sphinx_build': 'sphinx_build'}
        loadapp.return_value.registry.settings = settings
        exists.return_value = True
        main()
        WebSupport.assert_called_once_with(
            srcdir='sphinx_src', builddir='sphinx_build', status=None)
        WebSupport.return_value.build.assert_called_once_with()
