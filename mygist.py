#!/usr/bin/python

import argparse, getpass, os
from builtins import input
from scripts.gists import Gist

parser = argparse.ArgumentParser(description="Auxiliar script to handle migraines related data")
parser.add_argument("-u", "--username", default = None, help="Username of the GitHub account")
parser.add_argument("-p", "--password", default = None, help="Password of the GitHub account")
parser.add_argument("-c", "--create", action="store_true", help="To create a new gist")
parser.add_argument("-t", "--title", default=None, help="Title of the new gist")
parser.add_argument("-f", "--files", default=None, help="File names to use as content")
parser.add_argument("-b", "--public", action="store_true", help="Specifies if the gist will be public")
parser.add_argument("-d", "--delete", default = None, help="To delete an existing gist (by id)")
parser.add_argument("-l", "--list", action = "store_true", help="List the previosly created gists")

args = parser.parse_args()

# Examples:
# Delete a gist: python mygist.py -u [USERNAME] -d [GIST_ID]
# Create a gist: python mygist.py -t [TITLE] -f [FILE_NAME] -p
# List gists: python mygist.py -l
# See the help: python mygist.py -h

#print(args)

if args.username is None:
	args.username = input("Enter your github user name: ")

if args.password is None:
	args.password = getpass.getpass("Enter your github password: ")

gists = Gist(args.username, args.password)

if args.delete is not None:
	if gists.delete(args.delete):
		print("Deleted succesfully")
	else:
		print("There was a problem deleting the gist")

elif args.list:
	gists.list()  # It would be better to retrieve the gists data and make here the prints

else:  # Create as default action
	if args.title is None:
		args.title = input("Enter the description for the gist: ")

	if not args.public:
		args.public = input("Make this gist public (y/n): ") in ("y", "Y")

	files = args.files.split(",") if args.files else ""
	existing_files = list(filter(os.path.exists, files))

	if args.files is None or len(existing_files) == 0:
		print("No existing files were specified")
		alt_file = ""

		while len(existing_files) == 0:
			alt_file = input("Enter the file names (separated with commas): ")
			files = list(map(lambda s: s.strip(), alt_file.split(",")))
			existing_files = list(filter(os.path.exists, files))

			if len(existing_files) == 0:
				print("No existing files were specified")
			elif len(existing_files) != len(files):
				print("Warning! The following files do not exist:")
				for f in files:
					if f not in existing_files:
						print(f)
				if input("Continue anyway? (y/n): ") not in ("y", "Y"):
					existing_files = []


	file_pairs = []  # (name, content)
	for file_path in existing_files:
		with open(file_path, "r") as myfile:
			file_pairs.append((os.path.basename(file_path), myfile.read()))

	gist_id = gists.create(args.title, file_pairs, args.public)

	if gist_id is not None:
		print("Created succesfully. Gist ID: %s" % gist_id)
	else:
		print("There was a problem creating the gist")
