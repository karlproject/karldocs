===================
Profile View Screen
===================

A profile represents a user in the system.

Features
========

- View personal details about users

- See your tags, communities, and recent content, as well as that for
  other users

Specifications
===============

- Profile field labels and values floated to right of photo

- Show the Last login in a timeago format

- Bold the field labels

- Deal sensibly with values that overflow

- Put the bio with left margin same as left margin on the photo,
  and right margin inset a little from right margin on the field
  values

- Email field value is a mailto: link

- Don't show field labels if there is no field value

- Show a ghost profile image if there is no uploaded profile image

- Recent Changes

  - Uses the :doc:`../panels/recent_activity` panel, without the column
    showing the modifier person

- My Communities

  - Uses the :doc:`../panels/my_communities` panel, whether looking at
    your own profile or someone else's

- My Tags

  - Show first N tags, with tag count, sorted descending by tag count

  - If overflow, show "All Firstname's Tags" as link at bottom

- In the :doc:`../panels/actions_menu`, have a pushdown (the gear) with
  menu items for :doc:`profile_managecommunities` and
  :doc:`../profile_managetags`

Details
=======

=====================   =========================================
Item                    Value
=====================   =========================================
Page Title              Profile: Firstname Lastname
Sidebar panels          Tagbox, My Communities, My Tags
Action menu             Edit (admin/regular)
Actions pushdown        Manage Communities, Manage Tags, Advanced
=====================   =========================================
