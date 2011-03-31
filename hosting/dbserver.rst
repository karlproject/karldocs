=========
DB Server
=========

The machines running the app servers are considered disposible VMs.
They get their content from a database server.  That is, a PostgreSQL
database for RelStorage and pgtextindex.

Architecture
============

In phase 1, we'll keep ZEO but run it on the db server VM.

- blobs
- history-free
- memcache
- pgtextindex

Hosting Team Responsibilities
=============================

- Backup/restore
- Rotate log files as needed
- Monitoring and restart
- Software upgrades as appropriate
- Memcache
