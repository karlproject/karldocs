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
computer logged into ActiveDirectory.



Notes
=====

- Devteam development/testing against anything requiring ActiveDirectory
  is a logistical challenge

- Try to use WSO2 for the Kerberos part...or not

- Staff-only, removes their password from the KARL database

  - This will then make staging testing of staff users quite hard in the
    future, as the dev team won't have accounts that exist in the AD

- Changes to the CSV upload

- Skinning the login screens



- Yasso is skinned

- Yasso can send people to a KARL URL