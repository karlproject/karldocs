==============
Databases Tool
==============

Simple, limited step towards defining forms that can be completed and
analysed.

Goals
=====

- KARL sites can collect and download custom information from certain
  communities

- Available initially for only one KARL partner, but an ongoing project
  that can incrementally add new features and become part of the core

- In this stage, performance/productivity for 20 "databases" per KARL
  with 150 or so filled in forms per "database"

Features
========

- A new type of community tool called "DATABASES" that can be added to
  any community

- Each "DATABASE" tool in each community has "Libraries" (i.e. projects)
  with Forms

- Each project is searchable across KARL (not the filled in forms,
  just the project itself)

- Community members can manage their own completed forms (add, view,
  edit, delete) but for forms completed by other community members,
  they can only search, view, and download

- Moderators can see completed forms, as well as: search forms,
  download form results, view a form, edit and delete a form

- Moderators (but most likely, some power user) can define new
  libraries and new forms

- Some fields can have controlled vocabulary

- Export as CSV

- Email alert to moderators when a new form is submitted to a
  community database tool (this is new data, e.g., a new grant added
  to database)

- The "address" field type shows up in the report as link that says
  "View Map". This opens a new browser window pointed at Google Maps
  with that address shown. No attempt will be made to ensure the
  address that was typed in is valid. Just one long sequence,
  as you would type it into Google.

- You can click on an item in the listing and see a page for just that
  completed form

- Numeric columns (integer, decimal, currency) can have an optional
  "total" at the bottom of the column

Security
========

Community members can create form entries, and view/edit/delete their
own entries.

Community moderators can list form entries, search, and download as
CSV. They can also view/add/edit/delete form entries.

Community moderators can also add/edit/delete Libraries and Forms.

Search
=======

For the fielded text search, we'll save time/money by simply
brute-forcing it and doing substring matching on that field.  We thus
won't inherit any of the richer searching on a per-field basis.

- A checkbox on fields saying whether the field should be on search form

- No integration into site-wide search

Constraints
===========

- No attempt to limit community members to filling out a form repeatedly

- Once data starts coming in, you can't make certain structural changes
  on forms. However, we'll try to allow all but the most problematic of
  changes.

- No approval workflow

- Use the staging site for testing

- No versioning, email alerts, or tagging

- No UX2 version of the UI

- Only one security model

- Field types: string, integer, decimal, date, choice, richtext,
  address, euros (decimal with 2 digits and the symbol in front)

- Only targeted (email, security, etc.) to members in a community

Questions
=========

- Do you want community members to be able to see form entries filled
  out by other community members?
