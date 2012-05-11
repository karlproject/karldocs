====================
Chatter Posts Screen
====================

Show the posts that are relevant for a user.

.. image:: https://agendaless.mybalsamiq.com/projects/karl/Chatter+Posts.png
   :width: 904px
   :height: 713px

General Specification
=====================

- Shows a list of Chatter posts

- Details on the :doc:`../panels/chatterpost`

  - Help text should not mention ``#this``


List Specification
==================

- Shows posts which are: you are following, my posts and reposts,
  posts and reposts from people I follow, posts that mention any
  community I am in, posts that mention me

- Each chatter post should show:

  - A thumbnail of the user's profile, mouseover shows full name

  - Their username as a hyperlink to *Chatter Posts* for that user

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

- Button for loading more posts

Stats Box
=========

- Provide a box above "Show Only" with the  stats: X Posts,
  Y Following, Z Followers

- Each of those are links to the relevant section menu for that
  person's Chatter page

Find New Posts Box
==================

- Used to find posts that you don't ordinarily see, and thus sign up
  to follow new people or topics

- Typing in a searchterm and pressing enter does a search of all posts,
  whether you are watching that post's author or topic, or not

- The page reloads, shows a new list of posts matching the searchterm

- The searchterm appears in the box, with a circle x ``(x)`` to clear
  the search (and return to the normal listing)

Future Work
===========

- URL shortener

- Use infinite scrolling to load more post from the past as needed

- Autocomplete on completing names

- Attachments

- Security/visibility

To Do
=====

- Get Following and Followers as section menu items, linked from the
  stats links

- Document on all chatter screens which parts disappear if you are
  looking at someone else

- Ensure we have a view that shows all the posts in a conversation

