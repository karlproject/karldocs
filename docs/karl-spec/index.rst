==================
KARL Specification
==================

What is KARL? What promises does it make? If you were going to
re-implement KARL, what features and policies would you need to
implement?

The KARL Specification answers these questions. Below is a summary of
the important features and policies for major parts of the system,
along with a link to a full specification.

Access Control
==============

KARL has a powerful but simple security model that reduces many
possibilities down to simple ideas of roles and permissions. This
security model is pervasive, extending to operations such as search
(results filtered by what you are allowed to see), the people
directory (only show people you are allowed to see),
email and distribution lists, and more.

- KarlStaff sees more content and can perform more operations than
  KarlAffiliate

- Communities can be public or private

- Individual content resources can be private inside a public community

- Named groups managed by GSA can have more management permissions in
  certain parts of the intranet

More: :doc:`acl`

Admin View
==========

Users in the KarlAdmin group can perform administrative functions using
an admin screen.

More: :doc:`admin`

Attachments
===========

Some content types (blog entries, blog attachments, calendar events,
etc.) can "contain" one or more file attachments. These attachments
inherit the security model of the resource and can be searched and
navigated to just like Files.

- See which files are attached and download a file

- Attach one or more files to a resource

- Remove an attachment

More: :doc:`attachments`

Authentication
==============

Proving to KARL who you are via a username and password. Contains many
special policies and extra subsystems.

- Provide username and password with a choice to "Remember Me" for
  persistent login

- (OSF-only) KarlStaff passwords driven by external system via GSA Sync

- Forgot and change password (staff vs. affiliate)

More: :doc:`authentication`

Blog
====

Time-oriented compendium of blog entries by members of a community with
comments by others in the community. Blog entries and comments can
originate from email.

- Different security model from other community content (voice of the
  author)

- Each community blog has a unique email address so that content can be
  emailed-in (new blog entries or comments to existing) with attachments

- Non-member KarlStaff can have lightweight participation by commenting
  on a public blog entry in a public community

More: :doc:`blog`

Calendar
========

Multi-layered, web-base events calendar with many views for internal
and external calendaring. All calendar operations inherit the security
features from :doc:`acl`.

- Layers which subdivide a calendar based on calendar event categories
  and can pull in events from other calendars

- Many views (list, day, week, month, print, jump to day)

- A global "staff" calendar tab that appears on all pages for KarlStaff

- Import an event into your desktop calendar

More: :doc:`calendar`

Chatter
=======

(Unreleased) Twitter-style messaging and social networking via
"following". Also includes private messages. Developed in UX2 only.

- Quickly post short bursts of distraction-free content under your
  profile

- Find people and follow what they have to say

- Replies, mentions

- Private conversations

More: :doc:`chatter`

Communities
===========

KARL uses a Community for internal and external collaboration. The
ability for any staff member to create a community and invite outsiders
is a unique and powerful part of the KARL vision.

In a system with many communities, you need rich and useful ways to
list and find communities. You also need a Community that holds the
basic information about itself.

- List and search active and all communities

- My Communities and "Set Preferred"

- Add/join a community

- Manage community settings and add/invite new users

More: :doc:`communities`

Content Feeds
=============

Automatically-updating list of recent happenings across all KARL,
security-filtered based on what the user is allowed to see.

- Real-time listing with friendly timestamps

- Filter listing by: all activity, activity in any of my communities,
  changes to my content

- Color coded based on activity type, with excerpts, a profile
  picture of the author, and concise, hyperlinked detail of the context

More: :doc:`content_feeds`

Customization
=============

Other organizations are using KARL with configuration changes (logo)
and software customizations (extra featues in add-on software.)

More: :doc:`customization`

Development
===========

KARL is developed using a software tracking process, testing regime,
and open source access to the code.

More: :doc:`development`

Editor
======

TinyMCE open source rich text editor with customizations for cleaning
up HTML from Office, uploading images, and embedding media from Kaltura.

- Spellchecking, autosave, locking

More: :doc:`editor`

Email
=====

From its inception, KARL provided facilities to tap into email as a
two-way medium. Users can create blog content by email and be notified
about community content generated by other members. Over time,
more email features were added, including organizational email lists.

- Email-in of blog entry and blog comments, including attachments

- Email alerts for notification of community content additions

- Distribution lists for inbound-outbound communication in GSA-managed
  organizational entities

- System-generated emails for moderator changes, deactivation,
  invitations, and admin-generated mass emails

- Users can manage the frequency of email alerts on a per-community basis

More: :doc:`email`

Folders and Files
=================

Let users upload files and organize into folders and subfolders,
just like the Windows Desktop, using a high-performance grid with
sortable columns. File content is integrated into the rest of KARL
services (tagging, security, searching, alerts, syndication, etc.)

- Single file upload with email alerts

- Bulk upload many files at once

- Re-organize content by moving between folders

- History to see/restore past versions, as well as a Trash to
  see/restore deleted files and folders

More: :doc:`folders_files`

Forums
======

Intranet-oriented message board for announcements and staff posts in
topics under forums in office intranets.

- Reverse-chronological listing of posts

- Commenting and file attachments

- All forums view which spans per-office intranets

- Portlets to show recent forum posts on configured office home page
  columns

More: :doc:`forums`

GSA Sync
========

GSA manages information about staff users. KARL integrates via GSA
Sync, a KARL-side system which contacts GSA every 3 minutes to get
changes in staff user information.

- OSF-specific add-on

- Sync definition of active and inactive staff members

- Update usernames and passwords in KARL, as well as other profile
  information and security groups, including staff deactivation process

- Provide detail about organizational entities used in the People
  directory

More: :doc:`gsa_sync`

History and Trash
=================

Users make mistakes when working with content and need to recover from
the mistakes, or see previous versions of the content. History and
Trash are two facilities for Folders, Files, and Wiki Pages that make
working with content safer.

- See a list of all changes to certain resources, with time and person
  making the change

- Preview an earlier revision of a resource, or restore the revision to
  the current official resource

- List and restore deleted resources

- Re-make a folder hierarchy if needed on restore

- Option to permanently delete a resource from the trash

More: :doc:`history_trash`

Intranets
=========

Every staff user has the browser home page set to an intranet home page
in KARL for their office. The intranet organizes office-specific and
cross-organizational content for staff users.

- A per-office left-hand navigation of menus and sub-menus,
  editable by KarlAdmin

- A cross-organizational center column with a
  communications-administered "Feature", plus a syndication portlet
  with the feed from OSF's public website, as well as other portlets (e
  .g. global calendar portlet)

- A right-hand column with office-specific portlets

- A footer with office contact information

- Other staff-only content inside a particular office or shared
  between offices

More: :doc:`intranets`

LiveSearch
==========

Quickly finding a resource in KARL without leaving the current page is
a useful function. LiveSearch provides a quick way to see search
results grouped by content types.

- As you type, results are displayed atop the current page,
  in several groups

- Results can be formatted in a way useful for that group (e.g. show
  the phone number without leaving the page)

- "Sticky" options for limiting the search results to focus on a
  particular group (e.g. only People)

- Links to see more results for a particular group or the full search
  results

- Security-aware results

More: :doc:`livesearch`

Localization
============

Allow dates/times and numbers to be formatted by U.S. vs. European
standards.

- Users can change this in their profile

- Affects the formatting of certain values in many different screens in
  KARL

- Developed mostly to benefit non-OSF (Oxfam, Ariadne, etc.)

More: :doc:`localization`

Network News and Events
=======================

News items and general events tailored to the intranets and intranet
home pages.

- A minimal content type that goes in a specially-marked Folder,
  along with special display features (e.g. a graphic or attachment)

- Network News can have a graphic with a caption

- Custom navigation in the folder for searching or moving around based
  on time, etc.

- A portlet that can be displayed in the middle or right column of an
  intranet home page

More: :doc:`network_news_events`

Operations
==========

Policies and procedures for testing, deploying, and maintaining OSF's
production KARL site.

- Hosted in Germany

- Dev, staging, and production instances

- Multiple app servers with load balancing and database server

- Monitoring with emails on problems

More: :doc:`operations`

Other
=====

- Commitment to non-OSF KARLs

More: :doc:`other`

Pages
=====

A simple content type for the intranet only. Allows document-oriented
content with embedded images and attached files, stored in an Intranet
Folder.

- Rich text editor with image drawer

- Attachments, tagging, staff-only security model

- No self-organizing navigation like WikiPages

More: :doc:`pages`

People
======

A directory of staff and affiliate profile information. The People
directory is organized into security-aware "tabs",
with columns and groups that lead to reports. This can all be
configured using a web browser.

- Sections (tabs) that are visible based on staff vs. affiliate

- Columns and groups leading to configurable reports with users in that
  report and office contact information

- Rich filtering, sorting, and views (table, picture, print,
  download to spreadsheet)

- A report can be turned into an email distribution list

- Driven from organization categories and entities in GSA

More: :doc:`people`

Profiles
========

Information and operations unique to a particular staff member or
affiliate.

- View information about users that you are allowed to see (profile
  information, their communities that are visible to you, their tags,
  and their recent content)

- Edit your profile information (staff sees a reduced set),
  manage your tags and communities, change password (affiliates),
  set your preferred communities

- Administrators can edit extra information

More: :doc:`profiles`

Reference Manuals
=================

A structured collection of information arranged hierarchically in
outline, ordered format. A manual has one or more sections,
each containing pages and files. Only for specially-marked intranet
folders.

- Add one or more reference manuals

- Organize into sections/subsections, then dynamically order (move
  up/down) the sections, subsections, and pages

- Automatically-generated table of contents, special print views, and
  view all

More: :doc:`reference_manuals`

Search
======

Text search across all KARL content with advanced-search drill-down.

- Security-aware (only shows the content that you are allowed to see)

- Advanced-search lets you drill-down results based on several criteria
  (date, type, author, tag) or sort by relevance vs. date

- Results are formatted in rich ways, including highlighting the
  matching term

- Ability for admins to visit a particular resource and boost its
  relevance weight

More: :doc:`search`

Syndication
===========

Make listings of recently-changed community content available to
syndication clients.

- Atom/RSS protocol

- Community as a whole or per-tool (Files, Wiki, etc.)

- Security-aware

Tags
====

Bottom-up content organization by users of the system. Free-form
labeling of content.

- Site-wide and per-community tagging

- Anybody that can view a resource can add a tag (with autosuggest),
  edit the tags they put on the resource, or see other tags (and the
  people that placed the tag)

- Visualize the collection of tags as a "cloud", a listing,
  or see related tags at either site-wide or community level

- Users can manage their tags via their profiles

More: :doc:`tags`

UX2
===

A completely new re-implementation of every screen in KARL. Intended as
a fresh look to get users to give KARL a fresh look.

- Developed, deployed, tested, and enabled for beta testers,
  but not made the default UX (and now obsoleted)

- Built with responsive design to optimize for mobile and tablet displays

- Less distractions, focus more on content, fewer clicks,
  better forms and grids

More: :doc:`ux2`

Wiki
====

Page-oriented content in a community. Allows content self-organization
using the wikilink idea.

- Rich text editor with images, tagging, alerts, security, history,
  trash, and other KARL services

- A flat organizational space with wiki pages that link to other wiki
  pages

- An "index" view that shows a dynamically-generated table of contents,
  with sortable columns, filtering by title, grouping by tags,
  and showing/hiding columns

More: :doc:`wiki`

