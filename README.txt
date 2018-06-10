This repository is available via

  git clone https://github.com/noabospam/abospam.git

It can be updated via

  git pull https://github.com/noabospam/abospam.git

In addition to LICENSE.txt and this README.txt it contains two files:

1. banlist

A list of patterns that hopefully ban the spam subscriptions to
various lists all around the world.

Each pattern ends with '(ABOSPAM)?' that indicates that the pattern
is from this project.

2. update_banlist.py

This file updates the ban_list of a specific list with help of
mailman's withlist command.

Copy it to a location in sys.path, mailman's bin directory seems to be a
reasonable place, at least on Debian 8 "Jessie" this should work:

  cp update_banlist.py /usr/lib/mailman/bin/

After this you can start it via withlist:

  withlist --lock --quiet --run update_banlist <listname> <banlist file>

To let it operate on all the mailing lists on your server you can run it as:

  withlist --lock --quiet --run update_banlist --all <banlist file>
