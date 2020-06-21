# Ubuntu Release Info

[![Build Status](https://travis-ci.com/powersj/ubuntu-release-info.svg?branch=master)](https://travis-ci.com/powersj/ubuntu-release-info) [![Snap Status](https://build.snapcraft.io/badge/powersj/ubuntu-release-info.svg)](https://build.snapcraft.io/user/powersj/ubuntu-release-info)

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/ubuntu-release-info)

Ubuntu distribution release information

Similar to the 'distro-info' package, this class parses and contains
the Ubuntu release information. Instead of a static data file, this
instead downloads the the meta-release information from
changelogs.ubuntu.com, and parses it to determine the most recent
release information.

## Install

Users can obtain ubuntu-release-download as a snap:

```shell
snap install ubuntu-release-info
```

Or via PyPI:

```shell
pip3 install ubuntu-release-info
```

## Usage

Run the command with the flag to see the codenames matching that flag:

```shell
ubuntu-release-info
```

Options:

* all:
* lts:
* devel:
* supported:
* unsupported:
