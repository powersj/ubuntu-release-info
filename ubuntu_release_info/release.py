# This file is part of ubuntu-release-info. See LICENSE for license infomation.
"""Ubuntu Release Info Release class."""


class Release:
    """Release object.

    Contains the meta-data information for a particular Ubuntu release.
    """

    def __init__(self, codename, name, version, supported, lts=False):
        """Create an UbuntuRelease Object.

        Args:
            codename: string, single word, lower-case (e.g. bionic)
            name: string, full, multi-word name (e.g. Bionic Beaver LTS)
            version: string, like 'YY.MM[.#] [LTS]' (e.g. '18.04.1 LTS')
            supported: boolean, if supported or not
            lts: boolean, if LTS or not
        """
        self.codename = codename
        self.full_codename = name
        self.name = "Ubuntu %s (%s)" % (version, name)
        self.version = version.replace(" LTS", "")
        self.is_supported = supported
        self.is_lts = lts
        self.is_dev = False

    def __eq__(self, other):
        """Return equality boolean."""
        if not isinstance(other, Release):
            return False

        if self.version == other.version:
            return True

        return False

    def __ge__(self, other):
        """Return greater than or equal boolean."""
        if self.year < other.year:
            return False
        elif self.year > other.year:
            return True
        elif self.month < other.month:
            return False
        elif self.month > other.month:
            return True
        elif self.point < other.point:
            return False
        elif self.point > other.point:
            return True

        return True

    def __gt__(self, other):
        """Return greater than boolean."""
        if self.year < other.year:
            return False
        elif self.year > other.year:
            return True
        elif self.month < other.month:
            return False
        elif self.month > other.month:
            return True
        elif self.point < other.point:
            return False
        elif self.point > other.point:
            return True

        return False

    def __le__(self, other):
        """Return less than or equal boolean."""
        return not self.__ge__(other)

    def __lt__(self, other):
        """Return less than boolean."""
        return not self.__gt__(other)

    def __ne__(self, other):
        """Return not equal boolean."""
        if isinstance(other, Release):
            return False

        return not self.__eq__(other)

    def __repr__(self):
        """Return formal string of release."""
        return self.codename

    @property
    def year(self):
        """Return year of release."""
        return int(self.version.split(".")[0])

    @property
    def month(self):
        """Return month of release."""
        return int(self.version.split(".")[1])

    @property
    def point(self):
        """Return point of release."""
        try:
            return int(self.version.split(".")[2])
        except IndexError:
            return 0
