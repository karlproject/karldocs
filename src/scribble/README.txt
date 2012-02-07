--------
Scribble
--------

Scribble provides a JSON based RESTish web API for storing and retrieving simple
collections.

The resources available are repositories, collections and items.  A particular 
deployment of scribble contains one repositor which contains a number of 
collections which each contain a number of items.  All interactions with 
scribble start with a repository URI, eg: http://my.host/repo/.

Repository API
==============

GET http://my.host/repo/

Returns ['collection1', 'collection2', ..., 'collectionN']

Collection API
==============

GET http://my.host/repo/collection1

Returns [
    {id: 1, ...}
    {id: 2, ...}
]

POST http://my.host/repo/collection1 {...}

Returns id, an integer

Adds an arbitrary item to the collection.  The item is arbitrary JSON.  'id' is
assigned by scribble and should not be included in the posted data.

Item API
========

GET http://my.host/repo/collection1/1

returns {id: 1, ...}

Retrieves an item's JSON representation.

PUT http://my.host/repo/collection1/1 {...}

Returns nothing

Updates an item's JSON data.  'id', if included in the post data, will be 
ignored.

DELETE http://my.host/repo/collection1/1

Returns nothing

Removes an item from the respository.

