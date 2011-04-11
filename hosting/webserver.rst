==========
Web Server
==========

HostingTeam will use nginx as the front-end web server, proxying to
the app server over HTTP.  The app server will use Paste HTTP server
to listen for requests.

- Manage SSL cert
- Conf files
- Rotate logs
- Run log file analysis and publish at URL
- Monitoring and restart, anything related to keeping it running
- Software upgrades as appropriate

Hoster Responsibilities
=======================

- Manage proxy connection to KARL/Paster
