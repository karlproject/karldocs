===================================
External Authentication with OAuth2
===================================

.. note::

  This specification does not include any of the OSF-specific work to
  handle different flavors of staff. Instead, it is just the minimum
  get staff authentication outside of KARL.

Scenario
========

Gina is a staff person at Oxfam. She is working remotely and isn't on a
computer logged into ActiveDirectory. Gina goes to a page in KARL and,
since she hasn't logged in recently and isn't on AD,
is sent to a login screen.

Bob, an administrator for KARL, is asked to change the mapping for the
AD username for a KARL user. Bob ....

Implementation
==============

- Goal is to remove staff passwords from the KARL database.

- Oxfam will provide and support an on-premises host,
  running an app server stack (web server, Python) that we provide.

- The devteam won't support that part, as we'll have no access.

- This app server will run the "Yasso" OAuth2 authentication provider
  application.

- The app server will connect to the AD domain via LDAP to validate
  supplied usernames and passwords.

- KARL and Oxfam's Yasso work together in an OAuth2 fashion.

- Usernames in AD (and Kerberos) are mapped to usernames in KARL in a
  flexible way (XXX Chris, help explain)

- Once someone logs in at the Yasso Oxfam, they are redirected back to
  the resource they were trying to reach in KARL.

- Once that happens in KARL, they are given the same kind of "auth
  ticket" cookie in KARL as if they used a KARL username/password

Effort
======

Including deployment, but not including the at-Oxfam work: 15h for
Oxfam.

Issues
======

- *Testing will be hard*. Your production KARL will point at an
  ActiveDirectory that doesn't have any accounts for the KARL dev team.
  We thus won't be able to do production testing or debugging for parts
  that use the Kerberos transparent login or this external
  authentication.)

- *SSL*. You will certainly want SSL for the Yasso server at Oxfam.
  Most likely you will want an SSL certificate that is valid.

- *Monitoring*. Oxfam should hook the Yasso service up to your
  internal monitoring, so if something goes wrong, you'll be alerted.

- *CSV Upload*. Need to determine what this means for the future of
  that tool.

- *Skinning the Yasso screens*. You can work with Matt to make these
  look however you'd like.

- *Users still have to exist in KARL*. Just like with Kerberos,
  we aren't eliminating the step to make an account. Rather,
  we're just making identity/authentication handled by a different
  system.
