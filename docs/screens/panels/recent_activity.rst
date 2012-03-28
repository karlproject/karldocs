====================
Recent Changes Panel
====================

Certain screens want to show a box of content recently changed in a
certain context. For example, the
:doc:`../communities/community_overview`
screen has a box on it showing recent changes in a community. Also,
:doc:`../profiles/profile_view` shows content recently changed by a user.

This panel provides this functionality, allowing some options on
information displayed.

Features
========

- Show recently modified content

- Click on the link for a resource to visit it

- Scroll through all the content you've ever edited

Specifications
===============

- Columnar display with infinite scrolling

- Shows content in reverse chronological order based on modification
  time, as the default sort

- Done as a SlickGrid

- Columns available: Modified, Title (with link), Type, Modified By

- Modified by doesn't show the creator, but the last modifier

- "Recent Activity" is the title of the panel

- Show date using the localized format

- Sortable columns: Modified, Title

- Infinite scrolling, but with server requests for server-side sorting
  and batching

- No column picker or grid options are needed

Details
=======

=====================   =================================
Item                    Value
=====================   =================================
=====================   =================================
