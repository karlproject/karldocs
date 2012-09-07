====================
LiveSearch Component
====================

Operations and views available in a context under certain circumstances,
done in a customizable fashion.

Background
==========

Applications like KARL present various menus, allowing users choices
for navigation or operation. In KARL, some examples include:

- The list of tools available on a community

- The content types that are addable in a container

- Other operations

- The "submenus" for different views on, for example,
  a Wiki (front page, index, trash)

In these cases, the listing is dependent on a number of factors:

- The permissions required and the groups the current user is in

- The context of the container...if you are on the community side
  versus the intranet side

- Capabilities added or removed by a customization package

KARL Implementation
===================

KARL tried to framework this in the beginning by adding a menu
capability to ``lemonade``, and early attempt to bring CMF-like
facilities to ``BFG``. We didn't see all the patterns needed so we
stopped using that machinery.

Blue Sky
========

- l10n on menu choices

Recommendation
==============

