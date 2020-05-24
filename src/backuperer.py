#!/usr/bin/env python3

import argparse
import subprocess
import sys
import gnupg

parser = argparse.ArgumentParser()

parser.add_argument(
    "-R",
    "--raw-size",
    help="Specify whether to show the total raw size of the backup.",
    action="store_true",
)
parser.add_argument(
    "-p",
    "--path",
    help="A folder path, or a list of folders defined in a file.",
    type=str,
    default="",
)

parser.add_argument(
    "-k",
    "--key-id",
    help="""Specify the GPG key ID associated with the encryption key you wish
    to use.""",
    type=str,
    required=True,
)

args = parser.parse_args()

if args.raw_size:
    if args.path != "":
        path = args.path
        subprocess.Popen(f"du -csh {path}", shell=True)
    else:
        sys.exit("Folder path required.")

if args.key_id:
    gpg = gnupg.GPG()
    publicKeys = gpg.list_keys('/home/jack/.gpupg/')
    print(publicKeys)

sys.exit(0)
