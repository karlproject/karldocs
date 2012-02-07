--------
Scribble
--------

Scribble provides a JSON based RESTish web API for storing and retrieving simple
collections.

The resources available are repositories, collections and items.  A particular 
deployment of scribble contains one repository which contains a number
of collections which each contain a number of items.  All interactions with
scribble start with a repository URI, eg: http://my.host/repo/.

Repository API
==============

GET http://my.host/repo/

Returns ['collection1', 'collection2', ..., 'collectionN']

Collection API
==============

GET http://my.host/repo/collection1

Returns [
    [id1, {...}],
    [id2, {...}]
]

Last-Modified header is set appropriately

POST http://my.host/repo/collection1 {...}

Returns id of new item

Adds an arbitrary item to the collection.  The item is arbitrary JSON.  'id' is
assigned by scribble.

Item API
========

GET http://my.host/repo/collection1/1

returns {...}

Last-Modified header is set appropriately. X-Scribble-Id is set to item's id.

Retrieves an item's JSON representation.

PUT http://my.host/repo/collection1/1 {...}

Returns nothing

Updates an item's JSON data.

DELETE http://my.host/repo/collection1/1

Returns nothing

Removes an item from the repository.

