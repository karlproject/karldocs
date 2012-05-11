==================
Chatter Post Panel
==================

Re-usable panel for typing in a new Chatter Post.

Specifications
==============

- Used in:

  - :doc:`../chatter/chatter_posts` (both the main one and inline as a
    reply)

  - :doc:`../chatter/chatter_messages`

  - :doc:`../chatter/chatter_pushdown`

- Ensure that @username creates a link to the chatter_creators. For
  example::

    So @staff1 what's up buddy:

  ...should make "So" and "what's up buddy" a link to the post,
  while @staff1 is a link to the chatter_creators.

- Doing ``@username`` or ``@communityname`` triggers a "mention"

- Help text should explain ``@username``, ``&communityname``,
  ``#topic``, and on the pushdown, ``#this``

- Put some kind of character limit, perhaps at 300

- Detect URLs and turn into hyperlinks. For example, this::

    This is pretty neat http://karl.soros.org/community/longurl

  ...becomes:

    this is pretty neat <a href="url above">link</a>

- If possible, clicking ``Speak`` to submit a post does so in the
  background with a reload of the post list, to avoid a full page
  reload