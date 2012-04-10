=============
Gridbox Panel
=============


Features
========

- Client-side (send all the data at once) for small data sets,
  server-side (get data as needed) for large data sets

- Sortable (forward/backward) columns

- Column picker

- Column resizing (manual per column, autosizing)

- Infinite scrolling (instead of pagination)

- Responsive design

- Multiple selection

- Client-side "formatters" per column

Styling
=======

- Use the Popper/Bootstrap family of fonts, header/footer boxes,
  column styles, icons, etc.

Specifications
===============

- Dates should conform to the localization specification

- Infinite scrolling

  - If the amount of data is above X, don't send all the data to the
    client, but instead, load data as needed. Not as speedy on local
    operations (scrolling, sorting) but faster on first page load

  - Load data from server on scrolling, sort changing, operations in
    options

- Limitation: each row has to be the same height

Responsive Design
=================

- Allow one line row height at above 900px (or whatever), two lines
  below

- Understand that we can't re-layout when browser resizes after page
  load

Futures
=======

- Allow adapting the sort between client-side or server-side

- Inline editing

- Ordering (Reference Manuals)

- Column for actions

Details
=======

=====================   =================================
Item                    Value
=====================   =================================
=====================   =================================
