=================================
Staging Server and Branch Testing
=================================

When updating production, we need to do acceptance testing on the
trunk.  We thus need a staging site.

We also need a staging site for other reasons.  For example, when
working on new features we commit code to a branch.  Before merging to
the trunk, we need a site with production data where OSF can do
acceptance testing of the branch.

This document describes the staging server operations for satisfying
both needs.


karltest.gocept.com/test3/osf

we limit mailin processing to one branch per customer

- staging server
- branch
- customer
- whole URL is the branch site
- branch1 is the mailin-enabled branch
- 4 total branches, including "staging"
- svn switch
- same buildout, buildouts rarely branch
- branch1 is always mail
- osf/ariadne.karltest.hoster.com for staged mail on branch1

karl04 (app server, same configuration as karl02)
karl05 (db server, same configuration as karl03 but 500 GB disk)

osf-karl.hoster.com - proposed name until the switchover

- single universal staging, one ssl certificate, https

- continuous integration

- consumes lots of disk space, ram, but not cpu

###

[11:12am] chrisrossi: like i mentioned above, we might need to ask them to bump RAM on karl04, taking into account runnig multiple branches.
[11:12am] chrisrossi: getting new production syncing nightly with old production
[11:13am] repaul: ok
[11:13am] chrisrossi: setting up tools for staging that know about branching setup.
[11:13am] chrisrossi: getting nightly syncs from new production to staging
[11:14am] chrisrossi: figuring out how to see if svn or git have new checkins before doing update in order to do frequent polling (but not frequent building) for continuous integration on staging branches.
[11:14am] chrisrossi: i screwed up and forgot to kick off a manual sync from old production to new production last night.
[11:15am] chrisrossi: i wanted to see how long it took.
[11:15am] chrisrossi: the last one took over 14 hours which is ridiculous, but if we get it going every night hopeuflly that number goes way down.
[11:16am] repaul: yeh
[11:17am] repaul: so on that list above, wanna take a stab at a date?
[11:18am] chrisrossi: ok for, old prod -> new prod sync, i'll do one manually tonight and then put it in cron for tomorrow night forward.
[11:18am] repaul: ok
[11:20am] chrisrossi: hopefully by tomorrow i should also have reconfigured staging to work with syncing from new prod (worked before but needs to sync from zodb instead of relstorage), be able to update all of the branches at once, and maybe have continuous integration.
[11:21am] rmarianski: chrisrossi: as you do the manual one tonight, would it be possible for you to document the steps?
[11:21am] chrisrossi: yeah.
[11:21am] rmarianski: i owe you guys an update on the documentation, i was going to update the docs that paul started
[11:21am] chrisrossi: i can document it now:
[11:21am] chrisrossi: $ /home/chris/production/current/bin/karlserve upgrade --migrate
[11:21am] chrisrossi: wait many, many hours.
[11:21am] chrisrossi: done
[11:22am] chrisrossi: oops.
[11:22am] chrisrossi:  /home/karl/etc...
[11:24am] rmarianski: in terms of the important config options for that though ... sync.zodb_uri dsn ... that kinda thing
###


Premise
=======

#. We want to be able to easily setup evaluation sites for acceptance
   testing on branches of development.

#. *Convenient and reliable*. Such setup should be convenient and
   automated.  OSF or any developer/hoster can read simple
   instructions and do it.

#. *Fast*. Updating code and data in an existing branch site shouldn't
   take long, either in manpower or execution time.

#. *Multiple customers*.  One staging server should host many
   branches, each with more than one customer, to ensure something
   that works for OSF doesn't break someone else.

#. *SSL*.  Staging/branch sites should be served of SSL.  We thus want
   a naming system that avoids needing multiple certificates for every
   branch/customer combination.

#. *Email capable*.  We need the ability to test email-in and
   email-out on occassion.  Not universally, but when needed..

Gameplan
========

The hoster will set up an appserver virtual machine (``karl04``
hostname) at ``karltest.hoster.com`` where we stage the trunk and
branches for different customers.  This appserver will be paired with
a dbserver virtual machine (``karl05`` hostname).

For the website, the URL scheme will work as follows::

  https://karltest.hoster.com/branch1/osf
  https://karltest.hoster.com/branch1/anothercustomer

Dissecting this:

- ``https`` signifies that we are indeed running this over SSL.

- ``karltest`` is the hostname in the hoster's domain used for staging
  of branches.

- ``hoster.com`` is the hoster's domain.

- ``branch1`` is the branch of the KARL source code being evaluated.
  See below on *Buildouts and Branches* for more information.

Buildouts and Branches
======================

We intend to rarely branch the buildout.  As such, each branch site is
really tying a URL to a version of the KARL source software.

This is done manually.  When you configure the branch directory, you
"switch" the branch being used by the software.  In some rare cases,
the "customization package" is also on a branch and needs to be
switched.


Create
==========

#. ``cd /path/to/branch2``

#. ``bin/develop co karl``  (uses ``mr.developer`` to get trunk)

#. ``cd devel/karl`` (branch where KARL is checked out)

#. ``svn switch svn+ssh://url.of.branch`` (or git)

Any customer instances for that branch (e.g. ``/branch2/osf``) are
configured in the ``etc/instances.ini`` of the buildout.

While we have a manual step to select the correct branch to use for
``src/karl``, we have the benefit of not needing a branch on the
buildout (except in rare cases.)

Update
=========

#. ``cd /path/to/branch2``

#. Run Rossi's update tool

Q
===

- Overview of updater tool

- What is left in the customization package?
