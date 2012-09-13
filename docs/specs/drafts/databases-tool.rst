==============
Databases Tool
==============

Small first step towards site-specific content types.

Specifications
==============

- We will develop a new community tool that adds a "DATABASES" tab to a
  community

- In Ariadne's KARL site, we will manually add a certain tool to a
  certain community, hiding the presence of this tool from all other
  communities

- The tool will contain a folder "X Database" containing this
  database project

- The tool will not allow, the root, adding/editing/deleting anything.
  We will manually add "X Database" to the tool folder.

- The X Database database/folder will have a title and
  description.

- Inside this folder, the Add menu allows only one content type:
  "X Project"

- The action menu for the X Database folder contains: "Add
  X Project"

- The X Database screen has a search column on the right and a
  listing of entries on the right, like the Search Results screen

- The "X Project" content type is based on the Page content
  type, with extra fields:

  - Title

  - Body text

  - Donor Name (could be a foundation or a person)

  - Point of Contact

  - Contact information

  - Recipient of grant (NGO, organisation)

  - Grant purpose (pre-populated check boxes, + 'Other' field to fill
    in)

  - Location of Impact (city, [county/state] country)

  - Amount of grant (in Euros)

  - Keywords (pre-populated check boxes, + 'Other' field to fill in)

- The "Grant Purpose" and "Keywords" come from a vocabulary that is
  stored in the software (meaning, changes to this vocabulary require a
  developer and a production update)

- The KARL-wide and community-wide search uses only title for now as
  searchable text

- No email-alerts or KARL-style tagging

- UX1 and UX2 screens (lest we forget)

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

