==============================
Bulk Import of Content (Oxfam)
==============================

Oxfam has a lot of content to migrate into KARL. They need a web API
that their developers can use to load content extracted from other
systems.

This KIP describes bulk import and a web API for loading content into
KARL.

Goals
=====

- Allow frequent bulk import of external content (primarily from Plone),
  into full-fledged KARL content

- Productive to use

- Performant

- Reasonably expressive regarding metadata and KARL policies (e.g.
  security ACLs)

Out of Scope
============

- Incremental import for content already imported,
  but changed and needing re-importing

- Creation of new content types

- Bulk loading of users, profiles, people directory report
  configurations

- Loading of non-content such as external search items


Details
=======

- One-way, one-time import on a pile of content, not edited in Plone
  afterwards

- Oxfam's focus is on intranet content

Proposed Process
================

#. Oxfam extracts a batch of content from Plone, to files on disk in a
   directory.

#. A special "control file" is created in that directory,
   with information about every resource to be imported. This
   information includes the metadata on each item,
   but also information controlling the entire batch (e.g. the target,
   the overwrite flag discussed below, etc.)

#. A zip file is made of that directory's content.

#. The zip file is uploaded to a certain URL using a standard tool such
   as ``curl`` or ``wget`` which can encode the authentication.

#. If there was a problem in KARL during import, the error is returned
   to the HTTP client.

Details
=======

- Bundle into a ZIP file, done as one transaction (but perhaps with
  subtransactions on ours side)

- Specify the target folder in the control file

- By default, raise an error if loading a resource that already exists,
  but allow a flag that indicates content can be overwritten

- Handle a hierarchy of folders

- Text extraction for indexing done in KARL

- Raise an error if a resource's creator/owner isn't valid

- Allow uploading into existing containers. Use case: a folder contains
  100 Mb of data. You want to break it in to chunks.

- A flag that allows overwriting

- Possibly Page needs attachability

- Order matters in the RC file, might need to create a target before
  you can put stuff in it

- The RC entry points at the filename in the zipfile for the Page/File
  contents

Metadata
========

- TODO

Questions
==========

- Need a list of the content types that things will be mapped to

- What things are part of a particular intranet, vs. at the intranets
  level

- Big uploads with long transactions (especially, slow text extraction)
  will be prone to conflict errors. Do we design for that? Do smaller
  upload zips? Put production into read-only mode?

