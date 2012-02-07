==================
KARL Hosters Guide
==================

This document covers the deployment architecture for KARL. It also
delineates responsibilities between Hosters and Developers. On each
document, responsibilities are listed at the end for Hosters and
Devteam.

.. toctree::
   :maxdepth: 2

   virtualmachines
   appserver
   dbserver
   karlserve
   webserver
   mailserver
   monitoring
   production
   staging
   loadbalancing
   bugreporting

To Do
=====

- Robert, what's the documented gameplan for public-facing mail
  server/relay?

- Do we run Selenium against the production site after it is updated?
  (Risky, might be useless.)

- Section on GSA sync, background processes

- Setting timezone

- Each user has a ~/production with subdirectories for various
  instances, current symlinked to correct number

- current has a bin/supervisorctl

Hoster FAQ
==========

#. How do I restart the app server?

#. Who is allowed to login?
