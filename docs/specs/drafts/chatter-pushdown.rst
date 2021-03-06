================================
Chatter Phase 1, Pushdown
================================

We are breaking the Chatter work in phases, for
analysis/development/deployment simplicity.

This phase is focused on the Chatter functionality available in the
Chatter pushdown panel. This is not enough functionality to deploy a
basic Chatter, but is a useful starting point. Since we don't have the
full UX, we might have to dummy up some data (e.g. friends, messages.)

.. note::

   The word ``quip`` is a placeholder for the final word we'll use to
   name an item that is Chattered.

Features
========

Details
=======

User Stories
============

Below are users stories related to that panel.

Jane sees that she has new quips
--------------------------------

UX2 (the UX in Bottlecap) checks with KARL every N seconds to see if
there is anything new. Jane sees
her Chatter's notification box change to say there is one new quip. She
clicks Chatter to see what's new, thus activating the pushdown panel.

Spec:

- Show the number of "unread" items based on what Notification says is
  for Chatter, for you

Questions:

- How do we track the concept of unread, especially if we can't show
  all the items in the first 5 batch-full?


Jane quick-scans recent quips
-----------------------------

The Chatter pushpanel provides a short list (e.g. 5) of the most recent
messages. As shown in the screenshot above, there are two lists:

- Quips "about" Jane, either quips she has posted, quips that
  mention her, or direct messages

- Quips from people or tags that Jane is watching

Spec:

- Show the N most recent items in each list, where N is under the
  control of the server, likely to be 5 to start with

- Each column corresponds to a view in the full Chatter UX

- Below each column, provide a link to visit that view in Chatter,
  e.g. to get the full listing of quips

- If the pushdown panel is open and new stuff comes in,
  it gets inserted in a visual way (e.g. animate in-place),
  to give the user a visual cue that something arrived


Jane quick-adds a new quip
--------------------------

Jane is on an interesting page in KARL and wants to chatter about it.
She clicks the pushdown which has a box on the left that lets her post
a quip.

Spec:

- Provide visual cues that show something is being transmitted,
  has been received correctly in KARL, or had an error

- Always provide some way to bail out and clear a hung transmission

- Regular textarea, no visual formatting

- Interprets ``@`` and ``#`` correctly

- Has a gesture for referring quickly to the page you are on and
  chattering about it

- Other features (reply, re-chatter, attachments, private messaging) are
  in other specs


Jane visits the full Chatter UX
-------------------------------

Notes
=====

- Explain read vs. unread

- Display read vs. unread in different colors

- Ellipsis when there are more read, "1 more new item" for more unread

- Always show a minimum number, even if read

- Avatars for people

- Notifications in-KARL

- Connection to Feeds

- Vectors

  - People (me, friends, colleagues, staff, all)

  - Topics (aka tags)

  - References (retweets)

  - Replies

  - Featured

- Explain @ and #, as well as #this, tags

- Explain the drop-down on Speak

- See that I have new quips.

- Quick-add a new quip

- Direct a quip at a @person or a @topic

- Quick-view a list of quips directed at me

- Quick-view a list of quips that I'm interested in

- Start/stop watching someone in KARL

- Quick-requip a quip that I am reading