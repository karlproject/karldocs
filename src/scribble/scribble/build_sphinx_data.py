import os
import sys
from paste.deploy import loadapp
from sphinx.websupport import WebSupport


def main():
    exe = os.path.abspath(sys.argv[0])
    env = os.path.dirname(os.path.dirname(exe))
    ini = os.path.join(env, 'etc', 'scribble.ini')
    app = loadapp('config:%s' % ini)
    build_sphinx_data(app.registry.settings)


def build_sphinx_data(settings, quiet=True):
    sphinx_dst = settings['sphinx_build']
    if not os.path.exists(sphinx_dst):
        os.makedirs(sphinx_dst)
    sphinx = WebSupport(srcdir=settings['sphinx_src'], builddir=sphinx_dst,
                        status=None)
    sphinx.build()
