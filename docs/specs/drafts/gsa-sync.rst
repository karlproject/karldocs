========
GSA Sync
========

Synchronize internal user databases for staff users, with KARL.

.. note::

    This is *not* a proposal to implement a nice system. Instead,
    this is merely documenting how OSF's KARL syncs with the
    (unfortunately named) GSA  internal system.

Background
==========

OSF manages its staff users in an internal, SQL-Server-oriented system
called GSA (Global Staff Administrator). To synchronize this system
with KARL, a "GSA Sync" was developed.

Overview
========

- A console script in KARL runs every X minutes.

- The console script issues an SSL web request to a web service at OSF

- The request includes a parameter with the date/time of the last
  successful request

- The OSF web service connects to the internal user database and
  collects all records that have changed since the parameter.

- The OSF web service then returns an XML serialization of all the
  relevant data

- The console script updates KARL

- If successful, the console script updates its "last success" date/time

Out of Scope
============

- The GSA Sync approach badly needs a complete rewrite. This isn't that
  project.

XML Payload
===========

.. note::

  This XML "schema" was not designed by the KARL team. It is extremely
  repetitive and verbose.

In general, the XML structure looks like this::

  users
    user
      some properties
      categories
        category type=entities
            some category_item nodes
        category type=offices
            some category_item nodes
        category type=departments
            some category_item nodes
      groups
        some group nodes

Below is a snippet of some records in the XML payload:

.. literalinclude:: gsa_sync.xml
    :language: xml
    :linenos:


Some comments on the grammar:

- If you're asking yourself "This grammar doesn't really repeat the
  same information about the same category and group entries,
  over and over for each user", well, yes it does

Entities, Offices, and Departments
==================================

More detail needed.

Notes
=====

- *Staff only*. This is intended for internal users.

- *Passwords*. GSA Sync can send over SHA-encrypted passwords,
  but we won't be using that.

- *Inactive*. OSF has an internal policy about former staff called
  "deactivation". We won't be re-using that.

- *Profile photos*. Some profile data, such as photos,
  is still stored in KARL and is not in the sync.

- *Finicky*. This sync is one of the two most finicky parts of OSF's
  KARL. Keeping two systems in sync is hard.

To Do
=====

- Explain the difference on kinds of entities

- Document how reports are made TTW
