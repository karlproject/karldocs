.. _extensible-ui:

==========================
Extensible User Interfaces
==========================

Allow custom KARL deployments to override commonly requested portions of
the KARL user interface (UI).

Background
==========

Although originally developed to meet OSF's needs, KARL aims to be reusable
by other institutions which have similar requrements.   To that end, it
should be feasible for the integrators who deploy KARL for other institutions
to make reasonable changes to KARL's UI.  Desired changes might include.:

- Replace the organization logo.
- Tailor the color scheme. 
- Move / replace some elements of the site's look-and-feel (footer,
  etc.).


KARL Implementation
===================

The current production UI for KARL ("UX1") is strongly driven by OSF's
historical requrements, and can be difficult to customize for other
institutions' needs.  E.g.

- The ``TemplateAPI`` used by nearly every top-level view cannot be
  extended without "monkey-patching".  Replacing it wholesale is also
  infeasible, as the views import and use it directly.

- KARL has some unwanted complexity to support some OSF requirements,
  e.g., that "staff" users should not be allowed to edit their job title.
  See :ref:`extensible-content-types`.

- Many UI elements are driven by "snippets", which in UX1 are defined
  as ZPT macros within a single template.  Replacing a single snippet
  means forking (and them maintaining) the whole template.

- Some deployments have different policies for how particular elements
  (e.g., dates / times) are rendered:  these policies might even vary
  based on where in the site the view is located, or even on a per-user
  basis.  KARL should do something sensible by default, but permit
  integrators to override such choices with minimal duplication of
  code / templates.

The not-yet-released "UX2" version of the KARL UI address some of these
concernss:

- It factors the top-level templates into "layouts" (pluggable elements
  which define the overall page UI) into which the view can inject its
  local markup.  Layouts are defined / accessed by names using the Zope
  Component Architecture's facilities for "named utilities".

- Lower-level reusable elements are defined as "panels", which can be
  replaced like layouts using the ZCA.

Blue Sky
========

- Extend the layout / panel model to permit conditional replacement of
  elements using "predicates".

- Allow for the widgets used to render form fields to be replaceable
  using the ZCA;  make them use "predicates" as well.

- Extend / alias the "panels" to correspond to other renderable markup
  fragments and the corresponding logic (e.g., to deal with the date / time
  rendering requirement).

Recommendation
==============
