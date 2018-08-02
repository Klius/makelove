#!/usr/bin/env python
__author__ = 'Klius'
import argparse
import sys
import zipfile
import os
verbose = False
def	zip_folder(folder_path):
	"""Zip	the	contents of	an entire folder (with that	folder included
	in	the	archive). Empty	subfolders will	be included	in the archive
	as	well.
	"""
	output_path = (folder_path+"game.love")
	parent_folder = os.path.dirname(folder_path)
	# Retrieve	the	paths of the folder	contents.
	contents =	os.walk(folder_path)
	try:
		zip_file = zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED)
		for root,	folders, files in contents:
			# Include all subfolders, including empty ones.
			for folder_name in folders:
				absolute_path =	os.path.join(root, folder_name)
				relative_path =	absolute_path.replace(parent_folder,'')
				if verbose:
					print "Adding '%s' to archive."	% absolute_path
				zip_file.write(absolute_path, relative_path)
			for file_name in	files:
				absolute_path =	os.path.join(root, file_name)
				relative_path =	absolute_path.replace(parent_folder,'')
				if verbose:
					print "Adding '%s' to archive."	% absolute_path
				zip_file.write(absolute_path, relative_path)
		if verbose:
			print	"'%s' created successfully." % output_path
	except	IOError, message:
		print	message
		sys.exit(1)
	except	OSError, message:
		print	message
		sys.exit(1)
	except	zipfile.BadZipfile,	message:
		print	message
		sys.exit(1)
	finally:
		zip_file.close()

def	main(argv):
	global verbose
	parser	= argparse.ArgumentParser(description='Generate	love file')
	parser.add_argument("dir",help="Directory containing all love files")
	parser.add_argument("-v","--verbose",action='store_true',help="Displays info about the process")
	args =	parser.parse_args()
	if	bool(args.dir):
		verbose = bool(args.verbose)
		zip_folder(args.dir)
	else:
		parser.print_help()
		sys.exit(2)
	
if __name__	== "__main__":
	main(sys.argv[1:])

