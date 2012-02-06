===========
Mail Server
===========

Architecture
============

- A mail relay is the public facing mail server for inbound/outbound

- The mail relay performance basic spam and black list operations

- The mail relay delivers to a mail server for KARL, which only
  accepts mail from the mail relay

Hosting Team Responsibilities
=============================

- Externally-facing Postfix

- Spam, black list fixing

- Transferring to KARL-side Postfix

- Outbound delivery

- Rotate log files as needed

- Make log files available to KARL team for forensics

- Monitoring and restart, anything related to keeping it running

- Software upgrades as appropriate

- Analyzing inbound/outbound log files looking for problems, on an
  hourly basis

Anti-responsibilities:

- Basics of filters and vacation lists

- Subprocess that connects to repoze.postoffice

To Do
=====

- Access to mail.log (#8827)

