====================
Chatter Posts Screen
====================

Show the posts that are relevant for a user.

.. image:: https://agendaless.mybalsamiq.com/projects/karl/Chatter+Posts.png
   :width: 904px
   :height: 713px

General Specification
=====================

- The unread badge on the Chatter menu is the sum of the unread badges
  on the Posts and Messages section menus

- Ensure the unread badges are updated appropriately (server and
  browser)

Postbox Specification
=====================

- Ensure that @username creates a link to the chatter_creators. For
  example::

    So @staff1 what's up buddy:

  ...should make "So" and "what's up buddy" a link to the post,
  while @staff1 is a link to the chatter_creators.

- Remove ``#this`` from the help text on this screen (but not in the
  pushpanel version of the postbox)

- Put some kind of character limit, perhaps at 300

- Detect URLs and turn into hyperlinks

List Specification
==================

- This list should update every 30 seconds and insert anything new that
  has come in, without destroying your current list (similar to how KARL
  Feeds works)

- Use infinite scrolling to load more post from the past as needed

- Shows posts which are: you are following, my posts and reposts,
  posts and reposts from people I follow, posts that mention any
  community I am in, posts that mention me

- Each chatter post should show:

  - A thumbnail of the user's profile, mouseover shows full name

  - Their username as a hyperlink to :doc:`chatter_creator`

  - The timeago format of the chatter post's create date

  - The text of the message, with any relevant parts converted to
    hyperlinks (see below)

- The post itself is not a hyperlink to :doc:`chatterpost_view` (change
  from current implementation)

- Ensure ``@`` and ``#`` and ``&`` all render into hyperlinks

- Mousing over a post in the list gives an overlay with the following
  links: Reply, Repost, View

- This overlay is right justified, starting at the right edge of the
  timeago date, and lays over any text to the left of it

- Clicking ``Reply`` opens a new postbox, inline with the post being
  replied to, filled with ``@whomever``

  - This flavor of the postbox has a Cancel which throws away the
    content and makes the postbox go away

- Clicking ``Retweet`` pops up a confirmation dialog box

- Clicking ``View`` goes to the URL for that particular post

- A post that originated as a repost should have a link to the original
  poster. Let's say Susan is reading her stream and sees something from
  Bob, someone she is following. Bob reposts something from Mary,
  making it show up in Susan's stream. The stream should have a link to
  Mary (allowing Susan to read more posts and start following Mary.)

- When someone puts ``&community_name`` in a post,
  it shows up under Posts for anybody in that community at the time of
  the post

Stats Box
=========

- Provide a box above "Show Only" with the  stats: X tweets,
  X following, X followers, with those as links


To Do
=====

- Get Following and Followers as section menu items, linked from the
  stats links

- Document on all chatter screens which parts disappear if you are
  looking at someone else

- Explain that the URL shortener might be a challenge for Q2

- Explain that autocomplete might be a post-Q2 thing

- Infinite scrolling might be a post-Q2 thing

- Ensure we have a view that shows all the posts in a conversation

Questions
=========

- Ok with the unread marks?

- How hard is URL shortener?

- Infinite scrolling?

- Do we retain enough data about replies or reposts that we can show a
  screen with all the posts in a conversation? Is that just the normal
  screen for viewing a post?


