from pyramid.view import view_config

from scribble.models import SphinxDocument


@view_config(context=SphinxDocument, renderer='sphinxdoc.pt')
def view_sphinx_document(context, request):
    import pprint
    pprint.pprint(context.__dict__)
    return {}
