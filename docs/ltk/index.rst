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

.. toctree::
    :maxdepth: 1

    text-extraction
    supervisor
    load-balancing
    production-updates
    blob-storage
    logging
    monitoring
    backup
    snapshots
    postgresql
    memcache
    redis
    ssl-certificates
    kerberos
    replication

Devops Base
============

Some of the devops functions follow "best practices" that apply to any
Pyramid project we operate.

Below are LTK components that might be slotted into this layer.

.. toctree::
    :maxdepth: 1

    karlserve
    buildout
    layouts
    relstorage-zodb
    juicing
    evolution
    package-repository
    dev-staging-production
    single-instance-services
    graphite
    continuous-integration

Substance D
===========

An existing project to bring Zope-like development to Pyramid.

Below are LTK components that might be slotted into this layer.

.. toctree::
   :maxdepth: 1

   menus
   catalog-search
   i18n
   dump-reload
   deferred-indexing
   content-types
   relationships

Gumball
=======

A set of Substance D add-on packages for software that is generic,
repeatable, and common enough to warrant community ownership
and development.

Below are LTK components that might be slotted into this layer.

.. toctree::
    :maxdepth: 1

    search++
    extensibility
    mail-in
    ttw-types

    grid
    date-formats
    form-widgets
    ordered-folders
    authorization
    identity-authentication
    mail-out
    versioning
    trash
    admin-view
    image-service
    feeds-syndication
    workflow
    static-files
    streaming-blobs
    extensible-profiles
    scheduled-jobs
    collections
    acl-widget
    timezones

Popper
======

A set of add-ons atop Gumball that, while unique to KARL,
are still generic enough to be recast for customized KARL-like
applications. High affinity with KARL governance.

Below are LTK components that might be slotted into this layer.

.. toctree::
    :maxdepth: 1

    livesearch
    chatter
    relevance-tuning
    community
    blog
    wiki
    calendar
    file
    folder
    mailing-list
    analytics
    social

KARL
====

The KARL application itself.

Below are LTK components that might be slotted into this layer.

.. toctree::
    :maxdepth: 1

    ux2
    intranets
    network-news
    network-events
    forums
    reference-manuals
    gsa-sync
    invitations
    content-feeds
    staff-calendar
    low-bandwidth-mode
    user-deactivation

Customer/Customization
======================

Features and components that are intended to be unique to a deployment
of KARL.

Below are LTK components that might be slotted into this layer.

- Logo

- Name of KARL

.. toctree::
   :maxdepth: 1





