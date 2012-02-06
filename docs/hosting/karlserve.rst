=========
karlserve
=========

For smaller KARLs that don't need customization, consume few
resources, and all run the same version of software, Hosters can offer
"karlserve".

With karlserve, you run many KARLs in a single, common Python process.
This Python process (the KarlServer) dispatches requests to different
WSGI applications.  Each KARL customer has its own WSGI application,
and thus its own customization package, ZCML registry, database
connection and connection string, etc.

To provide scaling, this logical model can scale across multiple CPUs
or VMs, with load balancing to distribute requests.

For example, as documented in the staging chapter, the staging server
uses URLs as follows:

  https://karltest.hoster.com/branch1/osf
  https://karltest.hoster.com/branch1/anothercustomer

In this model, ``karltest.hoster.com/osf`` is a WSGI process answering
requests for a particular branch of KARL software.  ``/osf`` and
``/anothercustomer`` are customer KARL sites.  While both share a
common Python process and KARL software package, each has an isolated
registry from their customization package.

Benefits
========

- Data isolation via separate connection strings per customer

- Lower cost of setup, operation, and maintenance

- Still able to do customization packages

- Very easy to make someone have a dedicated VM by only routing
  certain request paths to them

Customization Packages
======================

You can start with a vanilla KARL that has no customization.  If some
customization is needed beyond the existing configuration knobs, you
can point a customer site to customization package via a command::

  $ bin/karlserve settings set mycustomer package somecustomization

Such configuration is persistent, stored in the customer's ZODB.
Doing so tells that customer's site to load its ZCML registry from the
customizaton package, rather than the vanilla ZCML in the core.

The ``somecustomization`` package needs to be available on the
``PYTHONPATH``.
