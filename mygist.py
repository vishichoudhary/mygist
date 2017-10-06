#!/usr/bin/python

import argparse, getpass, os, sys
from builtins import input
from scripts.gists import GistHandler, Gist

parser = argparse.ArgumentParser(description="Auxiliar script to handle migraines related data")
parser.add_argument("-u", "--username", default = None, help="Username of the GitHub account")
parser.add_argument("-p", "--password", default = None, help="Password of the GitHub account")
parser.add_argument("-c", "--create", action="store_true", help="To create a new gist")
parser.add_argument("-d", "--description", default=None, help="Description of the new gist")
parser.add_argument("-f", "--files", default=None, help="File names to use as content")
parser.add_argument("-b", "--public", action="store_true", help="Specifies if the gist will be public")
parser.add_argument("-r", "--remove", default = None, help="To delete an existing gist (by id)")
parser.add_argument("-l", "--list", action = "store_true", help="List the gists of an user (with authentication)")
parser.add_argument("-la", "--list_anonimously", action = "store_true", help="List the gists of an user (without authentication)")
parser.add_argument("-i", "--info", default = None, help="Get detailed info of a gist (by id)")
parser.add_argument("-s", "--star", default = None, help="Star an existing gist (by id)")
parser.add_argument("-n", "--unstar", default = None, help="Untar an existing gist (by id)")

args = parser.parse_args()

# Examples:
# Remove a gist: python mygist.py -u [USERNAME] -r [GIST_ID]
# Create a gist: python mygist.py -d [DESCRIPTION] -f [FILE_NAME] -p
# List gists: python mygist.py -l
# See the help: python mygist.py -h

#print(args)
if args.info is None:
    if args.username is None:
            args.username = input("Enter your github user name: ")

if args.info is None and not args.list_anonimously:
    if args.password is None:
            args.password = getpass.getpass("Enter your github password: ")

gists = GistHandler(args.username, args.password)

if args.star is not None:
	starred = gists.star(args.star)

	if not starred:
		raise Exception("Invalid gist ID")
elif args.unstar is not None:
	unstarred = gists.unstar(args.unstar)

	if not unstarred:
		raise Exception("Invalid gist ID")
elif args.info is not None:
	gist = gists.retrieve(args.info)

	if gist is None:
		raise Exception("Invalid gist ID")

	print("\nId: %s" % gist.id)
	print("Description: %s" % gist.description)
	print("Public: %s" % ("Yes" if gist.public else "No"))
	print("Owner: %s" % gist.owner)
	print("Created_at: %s" % gist.created_at)
	print("Updated_at: %s" % gist.updated_at)

	print("\nFiles:")
	for position, gist_file in enumerate(gist.files):
		print("\t(%d)" % (position + 1))
		print("\tFilename: %s" % gist_file.filename)
		print("\tLanguage: %s" % gist_file.language)
		print("\tSize: %s bytes\n" % gist_file.size)

elif args.remove is not None:
	if gists.delete(args.remove):
		print("Deleted succesfully!")
	else:
		raise Exception("Invalid gist ID")

elif args.list:
	gists.list()  # It would be better to retrieve the gists data and make here the prints
	
elif args.list_anonimously:
	gists.list(anonymous = True)

else:  # Create as default action
	if args.description is None:
		args.description = input("Enter the description for the gist: ")

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

	gist_id = gists.create(args.description, file_pairs, args.public)

	if gist_id is not None:
		print("Created succesfully. Gist ID: %s" % gist_id)
	else:
		print("There was a problem creating the gist")
