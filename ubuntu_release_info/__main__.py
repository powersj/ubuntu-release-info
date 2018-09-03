# This file is part of ubuntu-release-info. See LICENSE for license infomation.
"""Ubuntu Release Info main module."""

import argparse
import sys

from .data import Data


def parse_args():
    """Set up command-line arguments."""
    parser = argparse.ArgumentParser('ubuntu-release-info')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '--all',
        action='store_true',
        help='list all known versions'
    )
    group.add_argument(
        '--devel',
        action='store_true',
        help='latest development version'
    )
    group.add_argument(
        '--lts',
        action='store_true',
        help='latest long term support (LTS) version'
    )
    group.add_argument(
        '--stable',
        action='store_true',
        help='latest stable version'
    )
    group.add_argument(
        '--supported',
        action='store_true',
        help='list all supported versions'
    )
    group.add_argument(
        '--unsupported',
        action='store_true',
        help='list all unsupported versions'
    )

    return parser.parse_args()


def launch():
    """Launch ubuntu-release-info."""
    args = parse_args()

    ubuntu = Data()

    if args.all:
        for key in ubuntu.all:
            print(key)
    elif args.devel:
        print(ubuntu.devel)
    elif args.lts:
        print(ubuntu.lts)
    elif args.stable:
        print(ubuntu.stable)
    elif args.supported:
        for release in ubuntu.supported:
            print(release)
    elif args.unsupported:
        for release in ubuntu.unsupported:
            print(release)


if __name__ == '__main__':
    sys.exit(launch())
