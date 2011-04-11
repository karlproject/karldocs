==========
App Server
==========

The machines running the KARL application are considered "dataless".

Architecture
============

- 32 bit OS
- 64 Mb on memcache
- X database connections, thread pool
- X objects in ZEO cache
- Paste can only be connected to by localhost
- Poll-interval option

Operations
==========

The KARL application runs as a WSGI application managed by Supervisor.
It cannot be connected to by the outside world.  Instead, it only
accepts connections from the :term:`webserver`.

XXX discuss daemon/cron jobs that do background work, as well as an
operations.  Discuss how user accounts and logins work.

Restart Supervisor
------------------

Restart KARL
------------

Rotate Log Files
----------------

GSA Sync
--------

OSF has an internal application called Global Staff Administrator
(GSA).  It manages usernames, passwords, profile information, and
other data about KarlStaff users.

KARL periodically (every few minutes) synchronizes with GSA. This is
triggered by XXX (cron/daemon) which makes an authenticate HTTP
request to GSA, passing in the date of the last successful sync.  GSA
then returns an XML document with all the relevant changes.

Hoster Responsibilities
=======================

- Hook KARL up to hoster monitoring

- Rotate log files

- Know how to do a restart of supervisor, appserver, etc.

- Ensure VHM connection to 
