=========
MultiKARL
=========

For smaller KARLs that don't need customization, consume few
resources, and all run the same version of software, Hosters can offer
"MultiKARL".

With MultiKARL, you run many KARLs in a single, common WSGI process
(or pool of common processes.)  The first hop in the URL maps to a
KARL site.  Each KARL site gets its own content server connection, so
no data is shared between KARLs.
