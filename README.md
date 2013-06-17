DominosNotifier
===============

DominosNotifier is a script that sends you notifications on the status updates for your Domino's delivery.


Features
=====

Currently only works on OSX (and probably windows) with growl. (Needs the gntp python package).
The script takes one argument, which is the URL to the progress iframe page and then polls it every 20 seconds to then display a notification if there was an update.
This probably only works for the german Dominos page. If you want to make it work for other dominos pages, feel free.

ToDo
====
- Linux support (libnotify)
- Mountain Lion NotificationCenter support
- configurable checking time
- better input handling via argparse