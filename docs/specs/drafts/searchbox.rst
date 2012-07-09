============================================
Search Results Preview With Searchbox
============================================

The searchbox (formerly LiveSearch) shows a useful subset of the full
searchresults in a non-disruptive, in-page panel *as you type*.

Mockup
======

.. raw:: html

  <img height="916" width="1004"
   src="https://agendaless.mybalsamiq.com/projects/karl/Searchbox.png"
   />

.. note::

  To get the 2 column layout, we are giving up on menu navigation by
  cursor.

Goals
=====

- Make the panel look more like UX2

- Try harder to get all the results in the viewport without scrolling

- Speedup the dominant case (looking for a person)

- Give some options for improving performance via narrowing by default

Details
=======

- Try to get the search box into the global header by making it
  narrower and smaller font size

- Consider making the panel that appears on keystroke into a pushdown,
  giving it all the width. We'll have to do extra work to make it
  obvious how to dismiss it (pressing escape, an (x) symbol in the
  searchbox that dismisses, an explicit "close" link)

- If a pushpanel, give the same pushdown treatment, where you highlight
  the square behind it

- Issue the search for People in parallel with the search for the rest,
  allowing us to quickly show the faster-performing search (people) that
  is the dominant use case (finding a phone number)

- Make a place in the panel for knobs, including the context picker

- The "Staff only content" and "Modified in past year" knobs default to
  being selected. The selections are "sticky".

- Get rid of 3 character minimum if we switch back ends to expand
  prefixes, or speed up in some other way (limiting by date or staff)

- Use the oval format that Chatter uses for each row if possible,
  but the extra padding might take up too much vertical space

- "show more" expands that kind of result to take up all the space in
  the column, eliminating the other groups, and toggles to say "show
  less". This does not require a server trip, as we already have the
  data. Don't show a "show more" link if there aren't more to show.
  This replaces the drop down used previously to narrow by content.
  This is *not* sticky, as sticky was primarily for the "People" use
  case.

- Dismiss when the (x) is clicked, or there are no letters, or any other
  way that pushpanels get dismissed

- Small font sizes are ok if needed

- We will need to show fewer items per group in order to fit without
  scrolling. The "show more" help make that less of an issue.

- Look at the OSF LiveSearch results for information in presented in
  each group's formatter (TODO Paul get all those details baked into
  the mockup)

- Ensure that everything fits on two lines

- File icon types for the kinds of files (PDF, etc.)

- Context picker is not sticky

- Leave enough content on the bottom (targetting 1024x768) to ensure
  this feels like a pushpanel

- Address responsive design adaptation to smaller form factors

- To get into the header, change Person Name to My Profile

- Caching result data for searches in this session and not repeating
  search if you backspace and type the same search again

- Throttle input at a certain buffer period (to prevent firing off a
  bunch of searches when people type very fast.) Current LiveSeach has
  this policy.

- Have a place to show error messages.

- Try to prevent multiple requests in the queue at once.

Questions
=========

- Should we continue doing prefix searches, with no constraints,
  on the People group? I don't think we want those expanded to the most
  popular word, or limited by staff, or limited to create/modify in
  last year

- Do we want the date limit to be create date or modified date?