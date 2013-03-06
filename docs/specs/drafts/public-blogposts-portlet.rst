=========================
Public Blog Posts Portlet
=========================

Ariadne has requested an intranet home page portlet that shows the five
most recent blog posts marked as "public".

Specifications
==============

- A URL that can be pasted into the intranet setup screen,
  allowing a portlet in a column, at a position

- This portlet will find the five most recent blog posts marked as
  "Public" (independent of the current viewers security)

- Items will be sorted in reverse order

- Heading is "Recent Blog Posts"

- No "see more" link in the footer

- Each item is formatted like the calendar portlet entries: date then
  title. Date is format-aware (US vs. European per profile setting)

- Except, add the name of the community in italics with a newline (br)
  between the blog post title and the community name, e.g::

    03/06/2013   The words in the title of the blog post
                 which might wrap to the next line
                 *Disabilities Community*

Implementation
==============

- Tres will add support in the main KARL source code for having
  portlets use optional named adapters.

- Everything else will be in the Ariadne customization package

- As such, it is up to Ariadne to test whether future KARL updates
  impact this feature

- This project is complete when it is accepted on multikarl staging.
  Getting into production, and bug fixing after "acceptance",
  is a separate matter and statement of work.

Questions
=========

None.
