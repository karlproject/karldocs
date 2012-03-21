import json

from pyramid.httpexceptions import HTTPBadRequest
from pyramid.view import view_config

from scribble.models import Collections
from scribble.models import Collection
from scribble.models import Item


@view_config(context=Collections, request_method='GET', renderer='json')
def get_collections(context, request):
    return context.keys()


@view_config(context=Collection, request_method='GET', renderer='json')
def get_collection(context, request):
    request.response.last_modified = context.mtime()
    return [(id, json.loads(item)) for id, item in context.items()]


@view_config(context=Collection, request_method='POST', renderer='json')
def add_item(context, request):
    try:
        json.loads(request.body)
    except ValueError, e:
        return HTTPBadRequest(str(e))
    return context.add(request.body)


@view_config(context=Item, request_method='GET')
def get_item(context, request):
    response = request.response
    response.last_modified = context.mtime
    response.headers['X-Scribble-Id'] = context.__name__
    response.body = context
    response.content_type = 'application/json'
    return response


@view_config(context=Item, request_method='PUT')
def update_item(context, request):
    try:
        json.loads(request.body)
    except ValueError, e:
        return HTTPBadRequest(str(e))
    context.__parent__[context.__name__] = request.body
    request.response.content_type = 'application/json'
    return request.response # blank


@view_config(context=Item, request_method='DELETE')
def delete_item(context, request):
    del context.__parent__[context.__name__]
    request.response.content_type = 'application/json'
    return request.response # blank
