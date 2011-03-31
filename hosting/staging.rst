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
branches for different customers.  The appserver won't consume many
CPU resources, but will require a decent amount of RAM for
simultaneous testing.  Very little disk space is needed.

This appserver will be paired with
a dbserver virtual machine (``karl05`` hostname), which will require a
big disk (for all the duplicate copies of content.)

For the website, the URL scheme will work as follows::

  https://karltest.hoster.com/branch1/osf
  https://karltest.hoster.com/branch1/anothercustomer

Dissecting this:

- ``https`` signifies that we are indeed running this over SSL.  With
  this scheme, only one SSL certificate is needed for staging multiple
  branches for multiple customers.

- ``karltest`` is the hostname in the hoster's domain used for staging
  of branches.

- ``hoster.com`` is the hoster's domain.

- ``branch1`` is the branch of the KARL source code being evaluated.
  See below on *Buildouts and Branches* for more information.

Mail URLs work as follows::

  some-community@osf.karlstaging.hoster.com
  some-community@anothercustomer.karlstaging.hoster.com

Since we only have one axis available (osf.* and anothercustomer.*),
we can't easily route incoming mail to multiple branches.  Thus, by
convention, staging mail gets sent to::

  https://karltest.hoster.com/branch1/osf
  https://karltest.hoster.com/branch1/anothercustomer

We will have up to four branch URLs/directories available for use at
once.  Any of these can be switched to some branch that needs testing.
By convention, branch1 will be the "staging" branch for the trunk, to
test before going into production.

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

Continuous Integration
======================

The update process makes it very cheap/fast to get a branch site
incrementally updated with production content.  In fact, there is no
good reason not to automate that process and have a branch that gets
updated nightly/hourly.

With such a model we can also update the trunk continuously, thus
offering a model of "continuous integration" of software and content.

