==========
App Server
==========

The machines running the KARL application are considered "dataless".

Architecture
============

- 64 Mb on memcache
- X database connections, thread pool
- X objects in ZEO cache
- Paste can only be connected to by localhost
- Poll-interval option

Hosting Team Responsibilities
=============================

- Rotate log files
- Hook us/you up to monitoring
- Know how to do a restart of supervisor, appserver, etc.


To Do
=====

- Turn off any unnecessary processes (clamd, apache, qrunner)
