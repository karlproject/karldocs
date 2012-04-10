===============
Searchbox Panel
===============

- Formerly known as LiveSearch

- Cursor support later

- Relation to selected menu items, results and what groups disappear

- Work hard to get all results on a normal viewport without scrolling


Existing
========

- First result highlighted

- Caching searches in this session and not repeating

- Throttles (Keypress delay, 3 char minimum)

- Error displays

- Try to prevent multiple requests in the queue at once

Searchterm Typing Behavior
==========================

Architecture
============

Features
========

- Abstract grouping of content types

- Limit searches by abstract groups, one or more container contexts

- Sticky selections

Specifications
===============

- Each column has fixed-width, fixed-height entries,
  but different from the two columns

- Chop off long lines, but provide a way to see full info

- Chatter-style on-hovers

- Each group has a more/less toggle and a search link

- "more" makes that group the only group and shows more results,
  then changes to "less" to toggle back

- Don't show "more" if there isn't more

- On content, show a thumbnail of the author, mouseover shows the full
  name

- Show file subtype (PDF, Word) icon

- Issue search for the People part separate from the others

- Immediately draw the outer window, with a message saying "waiting for
  results"

- "all KARL" needs to be "all systemname"

- Two filters, both checked by default. These dramatically increase
  performance.

  - "Staff-only" shows resources that have a creator who was staff at
    the time the resource was last edited. This checkbox is only shown
    for requests coming from staff.

  - "Modified this year" filters results to a more-manageable pile.

  - The searchbox is just a quick search. People who don't like these
    knobs can uncheck them (the choice is sticky, so it remembers) or
    just use the full search

- Mousing over a result should give the cursor:pointer with the status
  bar showing the URL, just like a normal link

Details
=======

=====================   =================================
Item                    Value
=====================   =================================
=====================   =================================
