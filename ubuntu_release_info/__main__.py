# This file is part of ubuntu-release-info. See LICENSE for license infomation.
"""Ubuntu Release Info main module."""

import argparse
import sys

from .data import Data


def parse_args():
    """Set up command-line arguments."""
    parser = argparse.ArgumentParser('ubuntu-release-info')
    subparsers = parser.add_subparsers()
    subparsers.required = True
    subparsers.dest = 'command'

    subparsers.add_parser(
        'lts',
        help='latest long term support (LTS) version'
    )
    subparsers.add_parser(
        'stable',
        help='latest stable version'
    )
    subparsers.add_parser(
        'devel',
        help='latest development version'
    )
    subparsers.add_parser(
        'all',
        help='list all known versions'
    )
    subparsers.add_parser(
        'supported',
        help='list all supported versions'
    )
    subparsers.add_parser(
        'unsupported',
        help='list all unsupported versions'
    )

    return parser.parse_args()


def launch():
    """Launch ubuntu-release-info."""
    args = parse_args()

    ubuntu = Data()

    if args.command == 'all':
        for key in ubuntu.all:
            print(key)
    elif args.command == 'devel':
        print(ubuntu.devel)
    elif args.command == 'lts':
        print(ubuntu.lts)
    elif args.command == 'stable':
        print(ubuntu.stable)
    elif args.command == 'supported':
        for release in ubuntu.supported:
            print(release)
    elif args.command == 'unsupported':
        for release in ubuntu.unsupported:
            print(release)


if __name__ == '__main__':
    sys.exit(launch())
