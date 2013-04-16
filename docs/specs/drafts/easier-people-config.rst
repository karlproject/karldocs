======================================
Easier Configuration of People Reports
======================================

KARL has a browser-based admin tool for configuring PEOPLE reports.
This tool has some usability issues. In this writeup,
we document all the capabilities of KARL PEOPLE report configuration and

Capabilities
============

- Add/edit/list "categories" (departments, entities, offices)

- Edit category (title/description)

- Go "up" in breadcrumb hierarchy

- Add/edit/delete/re-order "sections" (tabs)

Categories
----------

- Add/edit category: name, title (e.g. ``departments`` and
  ``Departments``)

- OSF has department/entity/office category values

- Add/edit/list the values (CategoryItem) for each category

- Edit the Title and Description (html blob) on a CategoryItem

Section
-------

Capabilities in a section:

- Add/edit/delete/re-order Column, ReportGroup, Report, Redirector

Report
------

- Edit: Title, Link Title, CSS Class, Columns

Issues
======

- Easy to get lost in hierarchy

- Hard to connect categories to actual existing values

- Needless edit/admin schism

- Get an "Edit" or "Admin" link, either in ``/people`` actions menu
  or in the ADMIN screen

- On a Report, you have  link on ``entities`` that shows a meaningless
  ``Contents`` and a link for ``edit`` which actually does something

- Ditto on CategoryItem


Primary Proposal
================

We plan to focus on two recurring tasks that account for 80% of the
requests to the development team: adding a new report in a group and
changing the setup on an existing report. These are essentially the
same use case.

In priority order:

#. *Easier to get into People ADMIN*. Either add a link in
   ``ADMIN`` or put an action in the actions menu.

#. Rather than type in the value for a category,
   choose it from a dropdown. *Note: This will mean you can't add a
   report until, for example, the new Department starts appearing in
   GSA data.

#. Replace ``Up`` with actual breadcrumbs.

#. Make Category/Entity/Department first class parts of the UI,
   instead of adding a kind of filter then editing it

Other Ideas
===========

- Get rid of the redirector objects. No hits in March or April.

- Get rid of "Contents" links that lead to something that has no real
  meaning (Report -> Entities, CategoryItem)

