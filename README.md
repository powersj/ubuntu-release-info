# Ubuntu Distro Info

[![Build Status](https://travis-ci.org/powersj/ubuntu-distro-info.svg?branch=master)](https://travis-ci.org/powersj/ubuntu-distro-info) [![Snap Status](https://build.snapcraft.io/badge/powersj/ubuntu-distro-info.svg)](https://build.snapcraft.io/user/powersj/ubuntu-distro-info)

Ubuntu distribution release information

Similar to the 'distro-info' package, this class parses and contains
the Ubuntu release information. Instead of a static data file, this
instead downloads the the meta-release information from
changelogs.ubuntu.com, and parses it to determine the most recent
release information.

## Install

Users can obtain ubuntu-iso-download as a snap:

```shell
snap install ubuntu-distro-info
```

Or via PyPI:

```shell
pip3 install ubuntu-distro-info
```

## Usage

A user needs to provide at the very last the flavor of ISo to download.
By default, this will then download the latest released LTS of that
flavor:

```shell
ubuntu-distro-info
```

A specific, supported release can be specified as well:

```shell
# Ubuntu Xenial of Ubuntu server
ubuntu-iso-download server xenial
# Ubuntu Cosmic of Xubuntu
ubuntu-iso-download xubuntu cosmic
```
