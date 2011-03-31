================
Virtual Machines
================

Hosters will generally deploy a series of processes for hosting KARL.
In some cases, these logical units will be mapped to virtual machines.

VMs
===

OSF will use the following suite of VMs:

- ``osf-karl`` refers to the production app server, running on
  ``karl02`` initially.  Later, if we add multiple app server
  processes and processors (VMs), we'll use the nomenclature
  ``osf-karl1``, ``osf-karl2``, etc.

- ``osf-karldb`` refers to the production database server.

- ``osf-karltest`` refers to the staging app server.  It is used for
  testing the trunk prior to a production update ("staging"), as well
  as deploying a limited set of branches for acceptance testing.

- ``osf-karltestdb`` is the staging database server.

Sites and URLs
==============

The URL address space doesn't map perfectly to VM space.  We might
have a production website spread across multiple VMs.  Or we might
have multiple services (e.g. staging) sharing a single VM.

Thus, we'll use shorthand names for the outside world (OSF testers and
management) to use when they are referring to a "site".

- ``osf-karl`` means the production site

- ``osf-test1`` means a branch, usually the trunk.  Other branches
  will be setup on up to 3 other instances: ``osf-test2`` and
  ``osf-test3``.

- We might, via karlserve, have many staging customers on one staging
  instance.  So there might be ``osf-test1`` and
  ``anothercustomer-test1``.  These will be the same branch.

Here are some possible URLs::

  https://osf-karl.hoster.com/
  https://karltest.hoster.com/test1/osf
  https://karltest.hoster.com/test1/anothercustomer
  https://karltest.hoster.com/test2/osf
  https://karltest.hoster.com/test2/anothercustomer
  https://karltest.hoster.com/test3/osf
  https://karltest.hoster.com/test3/anothercustomer

*Note: Even branch sites will have an SSL certificate.*

Notes
=====

- The VMs might not be ssh-able from the outside.  You might have to
  go through a proxy to reach them.

