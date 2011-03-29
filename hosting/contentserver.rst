==============
Content Server
==============

The machines running the app servers are considered disposible VMs.
They get their content from a content server.  That is, a PostgreSQL
database for RelStorage and pgtextindex.

Architecture
============

In phase 1, we'll keep ZEO but run it on the content server VM.

- blobs
- memcache

Hosting Team Responsibilities
=============================

- Backup/restore
- Rotate log files as needed
- Monitoring and restart
- Software upgrades as appropriate
- Memcache
