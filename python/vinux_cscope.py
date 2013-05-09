"""************************************************************************
	> File Name: vinux_cscope.py
	> Author: chinaycheng
	> Mail: s_yangcheng@cqcyit.com 
 ************************************************************************"""

#!/bin/python

import os
import sys
import optparse
import gen_cscope

init_optparse = optparse.OptionParser(usage="sdsds")

group = init_optparse.add_option_group("Mode selected")
group.add_option('-i','--interface',
				 dest="interface", action="store_true", default=False,
				 help="Visualization operations")
group.add_option('-c','--command',
                 dest="interface", action="store_false",
				 help="Command operations")
group = init_optparse.add_option_group("option selected")
group.add_option('-s','--sources',
				 dest="src_file",
				 help="cscope sources comes from",
				 metavar="FILE")

group.add_option('-d','--dest_document',
				 dest='dest_file',
				 help="where the cscope will go to",
				 metavar="FILE")
group.add_option('-t','--type',
				 dest='type',
				 help="Type of the files which we need")
class _Options:
	help = False
	interface = False

def _ParseArguments(args):
	cmd = "create"
	opt = _Options()
	arg = []
	for i in xrange(0, len(args)):
		a = args[i]
		if a == '-h' or a == '--help':
			opt.help = True
			break
		elif a == '-i' or a == '--interface':
			opt.interface = True
			break
	if not opt.help == True and not opt.interface == True:
		arg = args
	return cmd, opt, arg
	
def _CheckArguments():
	(options, args) = init_optparse.parse_args()
	if args:
		print "show error"

def _CheckOptions(opt):
	if opt.help == True:
		return "help"
	elif opt.interface == True:
		return "interface"
	else:
		return "command"



def _ParseFileAttribute(arg):
	src_file = None
	dest_file = None
	file_type = None
	for i in xrange(0,len(arg)):
		a = arg[i]
		if a.startswith('-'):
			if a == '-s' or a == '--sources':
				if not arg[i+1].startswith('-'):
					src_file = arg[i+1]
			elif a == '-d' or a == '--dest_document':
				if not arg[i+1].startswith('-'):
					dest_file = arg[i+1]
			elif a == '-t' or a == '--type':
				if not arg[i+1].startswith('-'):
					file_type = arg[i+1]
	return src_file, dest_file, file_type

def main(orig_args):
	_CheckArguments()
	cmd,opt,arg = _ParseArguments(orig_args)
	if cmd == "create":
		mode = _CheckOptions(opt)
		if mode == "command":
			print "mode ==> command"
			src_file,dest_file,file_type = _ParseFileAttribute(arg)
			gen_cscope.cscope_online(src_file,dest_file,file_type)
		elif mode == "interface":
			print "interface"
		elif mode == "help":
			print "help"
		else:
			print "do nothing"
if __name__ == '__main__':
	main(sys.argv[1:])

