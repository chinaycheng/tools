from optparse import OptionParser
from optparse import OptionGroup

#define a function which will be call by some option
def my_callback(option, opt_str, value, parser):
	print option 
	print opt_str
	print value
	print parser

#add usage and version property
parser = OptionParser(usage="%prog [-f] [-q]", version="%prog 1.0")

"""
add some singal property
-f --file : option which user will input
action    : what we do when user write the option 
            store_true -> change the filename as true
			store_false -> change the filename as false
			callback   -> call the specify function 
help      : describe the option
metavar   : populate the option description
"""
parser.add_option("-f", "--file", action="store_true",dest="filename",
		 help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
		 action="store_false", dest="verbose", default=True,
		 help="don't print status messages to stdout")

"""add a group of property"""
group=OptionGroup(parser, "Dangerous Options",
		"Caution: use these options at your own risk."
		"It is believed that some of them bite.")
parser.add_option_group(group)
group = OptionGroup(parser, "Debug Options")
group.add_option("-d", "--debug", action="store_true",
                 help="Print debug information")
group.add_option("-s", "--sql", action="store_true",
                 help="Print all SQL statements executed")
group.add_option("-e", action="store_true", help="Print every action done")
group.add_option("-c", action="callback",callback=my_callback, help="do a callback")
def record_foo_seen(option, opt_str, value, parser):
	    parser.values.saw_foo = True
parser.add_option("--foo", action="callback", callback=record_foo_seen)
parser.add_option_group(group)



(options, args) = parser.parse_args()
print "%s" % options
print "%s" % args

