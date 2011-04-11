=============================
Production Server and Updates
=============================


Premise
=======

- *Reliable and simple*.  Automate the process as much as possible to
  make it easy, documented, and automatic to do a production update.

- *Minimize downtime*. Do most of the software/content work for an
   update, then have a small window of time where production needs to
   go down to get the last stragglers.

- *Recovery*.  Never do in-place updates.  Allow the software and
  content to be reverted back to the previous rollout, should
  something horrible be discovered post-update.

Gameplan
========

osf-karl.hoster.com - proposed name until the switchover

- multi-process



Updates
=======

Our goals on updates reflect our experience in many iterations of KARL
operations and architecture.  In a nutshell: make frequent production
updates low on stress, and do-able by various people on the team.

At a high-level, here is how an update runs:

- Check out the buildout into a new subdirectory and run it

- Prep the data, making a new copy of the production data, into a new
  area

- Put the production server into maintenance mode, copy any
  stragglers, switch over to the new app and data

- Run any evolve steps on the data, if evolve is needed

- Make the update "live"

We have created some automated tools that implement our methodology
for doing an update.

Hoster Responsibilities
=======================



Devteam Responsibilities
========================

- *Post-update testing*.  The dev team should poke around after an
  update, but *not* with Selenium or another automated tool.  Things
  shouldn't have changed between the staging setup and the production
  setup enough to justify putting a bunch of fake content into
  production.  The devteam has to test a bug/feature as fixed in
  production before it can close it, so that's enough.
