=========
DB Server
=========

The machines running each :term:`appserver` are considered disposible
VMs.  They get their content from a :term:`dbserver`.  That is, a
PostgreSQL database for RelStorage and pgtextindex.

Phase 1 Architecture
====================

In phase 1, we'll keep ZEO but run it on the :term:`dbserver` VM.
Some details:

- Blobs are stored on disk under ``var``.

- Each customer runs as a different system user for ZEO.

Phase 2 Architecture
====================

- RelStorage with PostgreSQL

- History-free

- Memcache

- pgtextindex

- Each customer gets its own database username/password, to provide
  isolation

Hosting Team Responsibilities
=============================

- Backup/restore

- Rotate log files as needed (either via Supervisor or some other
  facility.)

- Monitoring and restart

- Software upgrades as appropriate

- Memcache

