#!/bin/python


import sys
import os
import subprocess


def printall(args):
	for i in xrange(0,len(args)):
		print args[i]

def _checkFileType(file_type):
	file_type_temp = []
	print file_type
	print file_type.find('j')
	print file_type.find('s')
	if file_type == None or file_type.find('a') >= 0 or file_type.find('A') >= 0:
		return "all"
	if file_type.find('j') >= 0:
		file_type_temp.append('java' )
	if file_type.find('c') >= 0:
		file_type_temp.append('c' )
	if file_type.find('p') >= 0:
		file_type_temp.append('cpp' )
	if file_type.find('m') >= 0:
		file_type_temp.append('mk' )
	if file_type.find('x') >= 0:
		file_type_temp.append('xml' )
	if file_type.find('s') >= 0:
		file_type_temp.append('s' )
	return file_type_temp

def _MkdirIfNecessary(dest_file):
	if os.path.isdir(dest_file):
		return
	else:
		

def cscope_online(src_file,dest_file,file_type):
	m_src_file = None
	m_dest_file = None
	m_file_type = None
	if not src_file == None  and os.path.isdir(src_file):
		m_src_file = src_file
	
	if not dest_file == None  and os.path.isdir(dest_file):
		m_dest_file = dest_file

	if _checkFileType(file_type):
		m_file_type = _checkFileType(file_type)
	printall([m_src_file,m_dest_file,m_file_type])

	if m_src_file == None or m_dest_file == None or m_file_type == None:
		print "some thing is None"
	if m_file_type == 'all':
		_MkdirIfNecessary(m_dest_file)


