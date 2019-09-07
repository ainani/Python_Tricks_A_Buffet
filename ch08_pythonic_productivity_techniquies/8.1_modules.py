#!/usr/bin/python

import datetime
print dir(datetime)
print dir(datetime.date)

print "Prints only dates from datetime:", [_ for _ in dir(datetime) if 'date' in _.lower()]
print help(datetime)
print help(datetime.date)
