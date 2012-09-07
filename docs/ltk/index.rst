====================
Long Term KARL (LTK)
====================

In August 2012 a process was started to catalog all the parts of KARL,
then slot these parts in a re-imagined stack. LTK is the science
fiction documentation for that hypothetical, re-imagined KARL universe.

Background
==========

.. toctree::
   :maxdepth: 1

Cloud/Hosting
=============

As complete coverage on slotting every discussion point imaginable,
we need to keep track of discussions that go down to the machine and
storage level.

Below are LTK components that might be slotted into this layer.

- Virtual Machine

- CPU

- Disk/SAN

- SSD

- RAID

- SMTP out/in

- Spam filtering

- SSH with distributed login

- Cron


.. toctree::
   :maxdepth: 1

Custom Cloud
============

These days, cloud companies are providing "Platform as a Service" (aka
PaaS) capabilities atop generic hosting. In current KARL,
the hosting and development teams have simulated some of this.

Below are LTK components that might be slotted into this layer.

- Load balancing

- SSL certificates

- Logging

- Monitoring

- Backup

- Replication

- Blob storage

- Snapshots

- Production updates

- PostgreSQL

- Memcache

- Redis

- Kerberos

- Text extraction

- Supervisor


.. toctree::
   :maxdepth: 1

Devops Base
============

Some of the devops functions follow "best practices" that apply to any
Pyramid project we operate.

Below are LTK components that might be slotted into this layer.

- Buildout

- Layouts

- Juicing

- Dev/staging/prod

- Continuous Integration

- karlserve

- repoze.evolution

- Graphite

- Single-instance services


.. toctree::
   :maxdepth: 1

Substance D
===========

An existing project to bring Zope-like development to Pyramid.

Below are LTK components that might be slotted into this layer.

- Menus

- i18n/l10n

- Dump/reload

- Deferred indexing

- Catalog/search

- Content types

- Relationships


.. toctree::
   :maxdepth: 1

Gumball
=======

A set of Substance D add-on packages for software that is generic,
repeatable, and common enough to warrant community ownership
and development.

Below are LTK components that might be slotted into this layer.

- Grid

- Collections

- Search++

- ACL widget

- Timezones

- Date formats

- Form widgets

- Ordered Folder

- Authorization

- Identity/Authentication

- Mail-out

- Mail-in

- Versioning

- Trash

- Text extraction

- Extensible profiles

- Scheduled jobs

- TTW Types

- Admin View

- Image/thumbnail service

- Feeds and syndication

- Workflow (and workflow states leading to security)

- Serving static files with FFE

- Streaming blobs

.. toctree::
   :maxdepth: 1

Popper
======

A set of add-ons atop Gumball that, while unique to KARL,
are still generic enough to be recast for customized KARL-like
applications. High affinity with KARL governance.

Below are LTK components that might be slotted into this layer.

- LiveSearch

- Chatter and social

- Search+++ (manual boosting, keywords, etc.)

- Community

- Blog

- Wiki

- Calendar

- File

- Mailing List

- Analytics

.. toctree::
   :maxdepth: 1

KARL
====

The KARL application itself.

Below are LTK components that might be slotted into this layer.

- UX2

- Intranet

- Network News

- Network Events

- Forums

- Reference Manual

- GSA

- Invitations

- Content Feeds

- Staff Calendar

- Low-bandwidth mode

- User deactivation

.. toctree::
   :maxdepth: 1

Customer/Customization
======================

Features and components that are intended to be unique to a deployment
of KARL.

Below are LTK components that might be slotted into this layer.

- Logo

- Name of KARL

.. toctree::
   :maxdepth: 1





