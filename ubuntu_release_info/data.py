# This file is part of ubuntu-release-info. See LICENSE for license infomation.
"""Ubuntu Release Info Data class."""

import logging
from operator import attrgetter
import sys

import requests
import yaml

from .release import Release

logging.getLogger('requests').setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class Data:
    """Data Object."""

    url_release = 'https://changelogs.ubuntu.com/meta-release'
    url_release_dev = 'https://changelogs.ubuntu.com/meta-release-development'

    def __init__(self):
        """Initialize object.

        This set of classes build Ubuntu release information based on the
        meta-data found in https://changelogs.ubuntu.com/. Essentially, the
        meta-release file is read that contains all the released, past and
        present releases, with flags as to support status.

        The meta-release-development file is used to determine what the current
        development release is.
        """
        self._log = logging.getLogger(__name__)
        self.releases = self._parse_meta_url(self.url_release)

        # now find the development release and add it as supported
        dev_releases = self._parse_meta_url(self.url_release_dev)
        for codename, release in dev_releases.items():
            if codename not in self.releases:
                release.is_dev = True
                release.is_supported = True
                self.releases[codename] = release

    def _parse_meta_url(self, url):
        """Parse meta-data from URL and return releases found.

        Exits if unable to download from URL.

        Args:
            url: url to get meta-data from

        Returns:
            dictionary of releases, codename as key

        """
        releases = {}

        meta_data = requests.get(url)
        if not meta_data.ok:
            self._log.error(
                'Oops: could not download Ubuntu meta-release from: %s', url
            )
            sys.exit(1)

        for release in meta_data.content.decode('utf-8').split('\n\n'):
            # use the baseloader to prevent it from munging the version
            # from a string to some odd integer value
            data = yaml.load(release, Loader=yaml.BaseLoader)

            supported = False
            if data['Supported'] == '1':
                supported = True

            lts = False
            if 'LTS' in data['Version']:
                lts = True

            releases[data['Dist']] = Release(
                data['Dist'], data['Name'], data['Version'], supported, lts
            )

        return releases

    def by_codename(self, codename):
        """Return release given a specific codename.

        Exits on unknown release.

        Args:
            codename: string of codename to find

        Returns:
            Release object of matching release

        """
        try:
            return self.releases[codename]
        except KeyError:
            self._log.error(
                'Oops: unknown release codename \'%s\'!'
                ' Please choose from:\n%s',
                codename, [release.codename for release in self.supported])
            sys.exit(1)

    @property
    def all(self):
        """Return all releases.

        Return:
            List of all Release objects.

        """
        return sorted(self.releases)

    @property
    def devel(self):
        """Return devel release.

        Return:
            Release object that is devel or none.

        """
        for _, release in self.releases.items():
            if release.is_dev:
                return release

        return 'none'

    @property
    def lts(self):
        """Return latest LTS.

        Returns:
            Release object that is the latest LTS.

        """
        lts = []
        for _, release in self.releases.items():
            if release.is_lts and not release.is_dev:
                lts.append(release)

        return max(lts, key=attrgetter('year'))

    @property
    def stable(self):
        """Return latest stable release.

        Returns:
            Release object that is the stable release.

        """
        supported = []
        for _, release in self.releases.items():
            if release.is_supported and not release.is_dev:
                supported.append(release)

        return max(supported)

    @property
    def supported(self):
        """Return supported releases.

        Returns:
            List of Release objects that are supported.

        """
        supported = []
        for _, release in self.releases.items():
            if release.is_supported:
                supported.append(release)

        return sorted(supported)

    @property
    def unsupported(self):
        """Return unsupported releases.

        Returns:
            List of Release objects that are unsupported.

        """
        unsupported = []
        for _, release in self.releases.items():
            if not release.is_supported:
                unsupported.append(release)

        return sorted(unsupported)
