================
Profile Pushdown
================

Convert the profile menu into a pushdown with much richer information
while saving space in the global toolbar.

Background
==========

In UX2, the global toolbar has a "profile menu" on the right:

.. image:: /specs/images/personal-pushdown-1.png

This has some issues:

- *Too much width*. If the person's name is very long,
  it takes up space in the global toolbar. Later, when we have more
  tools, or the searchbox is in there, or we translate to French and
  have longer labels, we'll need all the space we can get.

- *I know my name*. Why show a person their name? They know their name.

- *Logout is rarely used*. We don't need to reserve space for Logout.
  In fact, when transparent login lands, staff users won't even be able
  to logout.

In addition to the issues, we have some needs for presenting
information focused on the user, originally planned for Radar:

- Quickly jumping to my communities, reducing a page load to get there

- Quickly visiting some content that I was recently working on

Other sites, such as Twitter and LinkedIn, treat that part of the UX as
a dropdown. This proposal follows that lead.

Proposal
========

Under this proposal, we will make a much smaller box in the global
toolbar which triggers a pushdown:

.. raw:: html

  <img height="46" width="725"
   src="https://agendaless.mybalsamiq.com/projects/karl/Profile+Pushdown+Basics.png"
   />

The global toolbar's profile menu has been replaced:

- "My Profile" instead of the full name

- The thumbnail+label is pushdown button that activates the pushdown

- Move "logout" into the pushdown

- Question: Chatter doesn't have a triangle. Should it,
  to distinguish pushdown menus from normal navigation menus? Or should
  this profile pushdown conform to the current spec and not have a
  triangle?

When activated, here is the pushdown panel:

.. raw:: html

  <img height="522" width="725"
   src="https://agendaless.mybalsamiq.com/projects/karl/Profile+Pushdown+Full.png"
   />

The pushpanel will then have the following spec:

- Logout

- Open the full profile

- Just a summary, not a replacement for the profile page

- Not too tall, leave enough room for the current view to show up below

- Need a place for the quick links: Visit the full profile, Logout

- Perhaps the left column isn't as wide as the other two

- Show the preferred communities from the My Communities portlet

- Follow the styles and convention from the Chatter pushdown where
  possible

Narrow Layouts
==============

UX2 currently handles the personal menu poorly on tablet/phone
dimensions: the menu just disappears!

As part of this project, reduce the personal menu to just an icon which
activates the pushdown.

In the pushdown:

- In tablet landscape, stay as above

- In tablet portrait, move right column below other two columns

- In iPhone, either dimension, just go to the profile page

Miscellaneous
=============

- Change the profile page to include a "Logout" action in the action
  menu. Get with Chris Rossi to make sure that this doesn't get impacted
  by the Kerberos transparent login work
