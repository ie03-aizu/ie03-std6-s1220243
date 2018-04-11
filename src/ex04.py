#!/usr/bin/python3

import argparse
import subprocess

def rec (args):
	pass

def eval (args):
	pass

def main ():
	# TODO: impliment argparser
	root_parser = argparse.ArgumentParser (allow_abbrev = False)
	subparser = root_parser.add_subparsers (help = "command", dest='subparser_name')
	# for rec command
	rec_parser = subparser.add_parser ("rec")
	rec_parser.add_argument ('user_id', type = int, metavar = "<USER ID>")
	rec_parser.set_defaults (func = rec)

	rec_parser = subparser.add_parser ("rec")
	rec_parser.add_argument ('user_id', type = int, metavar = "<USER ID>")
	rec_parser.add_argument ('user_id', type = int, metavar = "<BOOK NUMBER>")
	rec_parser.set_defaults (func = rec)

	# for eval command
	eval_parser = subparser.add_parser ("eval")
	eval_parser.set_defaults (func = eval)

	args = root_parser.parse_args()

	if args.subparser_name:
		args.func (args)
	else:
		root_parser.print_help()

if __name__ == "__main__":
	main()
