==========================================
Transparent Login With Kerberos
==========================================

ActiveDirectory users logged into a domain have browsers that can
transparently provide AD credentials to servers. In this work,
we change KARL to transparently ask for and use these credentials,
thus eliminating a login step and remembering KARL-only credentials.

Background
==========

We are starting an authentication project, first for Oxfam then for
OSF. The project has 2 separately-deployed steps:

1) Use Kerberos authentication (aka Windows Login) so that anybody
   with a valid ActiveDirectory login is implicitly authenticated by
   KARL.

2) Staff users who are on the road (not on AD) use OpenID running at
   Oxfam to authenticate. We can then remove the staff passwords from
   the KARL database.

As much as possible, we are ignoring (2) so we can quickly make
some progress on (1).

"Transparent Login" - Unintended Consequences
=============================================

As originally conceived, users with the Kerberos header would
automatically be identified/authenticated whenever they went to a
page. There would be no separate step for "login" and no ability to
"logout". If AD trusts you, we trust you.

As I thought through it, though, eliminating these things led to a
number of side effects:

- Profiles in KARL, and other important parts of the system, depend
  on "last login time" as an important marker. I believe this is only
  updated when the user actually logs in. (Meaning, the auth ticket
  cookie expires.)

- At some point we'll be asked to do logout for Kerberos. Perhaps
  someone doesn't want people sneaking onto KARL when they are way from
  their AD-logged-in computer. Perhaps people want to login to KARL
  using someone else's computer.

- Some users will have both the Kerberos header and (from an earlier
  login) the auth ticket header. This gets into some weird gotchas on
  knowing what parts of the UI to show (e.g. logout, forgot password,
  change password.)

- We might need a UI for showing things related to login/logout (for
  example, temporarily turn off transparent login so someone else can
  use the computer). If it is all invisible, there is no place to do
  this.

Proposal
=========

It would be nice to avoid 2 very different modes for authentication
with wide ranging implications for features and UX. Here's a modest
proposal in the spirit of other SSO systems which retain an explicit
screen/step where you can communicate some things.

Instead of eliminating "login", keep it. But instead of sending to the
view that asks for a login, send to an intermediate view which
challenges for the header:

1) Joe is a user who is logged into AD. He hasn't used KARL in 15 days
  (meaning, his cookie has expired.)

2) Joe goes to karl.oxfam.org.uk/intranets/oxfam-house. He isn't logged
   in, so he gets redirected to
   ``karl.oxfam.org.uk/duncans-cool-redirector``

3) The duncans-cool-redirector view does this:

   - Challenge for the Kerberos ticket.

   - If the ticket is presented in the header, and is valid, go through
     the normal login process. Meaning, assign one of our normal auth
     tickets and redirect to the URL that Joe was trying for.

   - If no Kerberos ticket is provided, they aren't on the AD,
    so redirect to the normal login screen.

   - If they present an invalid Kerberos ticket....send them to
     the normal login screen.

With this, nothing in KARL's feature set or UX changes except the
login screen. Once every 2 or so weeks, Oxfam users get sent to a
series of redirects, invisibly arriving at the page they were requesting.

Logout
------

Clicking Logout would clear the Karl auth ticket and redirect to
login.html. It bypasses the page that does the Kerberos stuff so you
just login normally. Of course having clicked logout if you change your
mind and go off to another Karl page you'll be logged in automatically
so it doesn't prevent access it just gives you a chance to login as a
different user.

Forgot/Change Password
----------------------

Forgot password and change password would do what they currently do,
i.e. change your Karl password not the one for AD.

Implementation
==============

- KARL does *not* make any connection to Windows or ActiveDirectory.
  This is all implemented using a Python library which decodes the
  validity of Kerberos ticket against the AD domain certificate.

Questions
=========

- Does Oxfam only have one AD domain/certificate? If not, can Matt's
  library support multiple domains?

- Can Oxfam ensure that all usernames in AD match up to KARL usernames?


Notes
=====

- Oxfam is IE7 and Chrome on XP

- Devteam development/testing against anything requiring ActiveDirectory
  is a logistical challenge

- Changes to the CSV upload

