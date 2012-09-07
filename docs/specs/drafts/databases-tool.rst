==============
Databases Tool
==============

- Uses KARL security (users, security model)

- Tab on a community

- Tab is called "Databases", allows adding a Folder for each Database

- Searchable at KARL and community level

- Alerts contain fields

- Constrained vocabularies and datatypes on add/edit

- Derived from Page/WikiPage

- Tagging, Advanced

- Title, body

Constraints
===========

- *Community Tool, hidden*. We will do this first as a tool that can be
  added to a community. We will hide that tool so that it won't be
  addable by regular staff. Instead, we (a KARL developer) might have to
  manually attach this tool to the community.

- *Security*. We will make this use Blog Tool security. That first
  means it inherits community public/private and all that this entails.
  Second, it means database entries will be editable only by the author
  and by a KarlAdmin. If you want different security,
  you'll have to use the (somewhat byzantine) "Edit ACL" screen.

- *Text search*. For the fielded text search, we'll save time/money by
  simply brute-forcing it and doing substring matching on that field.
  We thus won't inherit any of the richer searching on a per-field basis.

Ariadne Questions
=================

- Is a title/body needed? Answer: yes

- Is this Wiki-like?

- Is it the Blog Entry security model or the community content security
  model? Answer: blog

- What does "projects and tag them" mean? Is "tag" just a way of saying
  "fill in fields"? Answer: fill in fields

- Is normal access model (KarlAdmin/KarlStaff/KarlAffiliate,
  community member and moderator) ok? Answer: yes

- Do we need alert capabilities?

Tres/Paul Questions
===================

- UX1 vs. UX2

- Responsive design layouts

- In the beginning, needs to be conditional, tab only addable on one
  community in one KARL

- Content migration on schema change

- Use a grid with filters?

- Need fielded text search on custom fields...does this mean custom
  catalog?

- Running as separate app, shared login (as well as, CRM project)

Later
=====

- Richer indexing

- Export as CSV

- SGT

- Faceted-style drill-down