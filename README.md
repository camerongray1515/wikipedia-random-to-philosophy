wikipedia-random-to-philosophy
==============================

This simple Python script tests the theory that by clicking the first link on a random Wikipedia page and any subsequent pages (or the next link if the first link has already been visited) will eventually lead to /wiki/Philosophy

More information about this phenominon can be seen here: http://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy

Installation
------------
* Install all requirements in requirements.txt
* Run main.py

This will now pick a random article and click the first link on each page until /wiki/Philosophy is
reached.  The process will also stop if a page is reached that contains no new links (either we are
stuck in an infinite loop or the page actually has no links to other articles)