======================================
Seeing New Activity with Notifications
======================================

Content gets created in KARL that might need attention by a user. If
they don't reload a page, they won't know there's something for them.

Notifications is a system to check with the KARL server every N seconds
and visually let the UX tell the person something new is waiting for
them.

Goals
=====

- Tell the user that KARL has new stuff for them on a certain panel

- Give visual feedback when KARL is talking to the server or has a
  problem

Details
=======

- One polling for all consumer panels on the page

- Visually, this is done by making one of the Notifier boxes the
  "primary". It is the one that talks to the server. More detail below.

Primary Notifier
================

As mentioned above, only one of the Notifier widgets talks to the
server. This is the "primary". It has some extra details:

- When a request is in progress, the box acts like a throbber. This
  gives a visual cue that something is actually happening.

- If the request is handled correctly, the data is stored and the
  Notifier widgets are handed the data, likely via events.

- If the request encounters a problem, that Notifier widget box changes
  to show an error color/icon. A tooltip appears as well with a link
  that offers more information plus the ability to turn off polling.

- Unlike the Feeds notifier icon, we can't make it clickable to show
  more info, turn on/off polling, etc. That's because this icon is the
  click target for the pushdown panel. That means we'll live without
  managed polling, or else have some secret backdoor (cntrl-click) that
  makes it appear.
