# This file is part of ubuntu-release-info. See LICENSE file for license info.
# pylint: disable=comparison-with-itself, unneeded-not
"""Test view module."""
from .release import Release

artful = Release("artful", "Artful Aardvark", "17.10", False, False)
bionic = Release("bionic", "Bionic Beaver LTS", "18.04 LTS", True, True)
bionic_ = Release("bionic", "Bionic Beaver LTS", "18.04.1 LTS", True, True)
cosmic = Release("cosmic", "Cosmic Cuttlefish", "18.10", True, False)
disco = Release("disco", "Dingo Disco", "19.04", True, False)


def test_codename():
    """Test basic codename."""
    assert str(bionic) == "bionic"


def test_eq():
    """Test equality."""
    assert bionic == bionic
    assert not bionic == cosmic
    assert not bionic == ""


def test_not_eq():
    """Test not equality."""
    assert bionic != []
    assert not bionic != cosmic


def test_gt_or_lt():
    """Test greater than and less than."""
    assert artful < disco
    assert disco > artful
    assert bionic < cosmic
    assert cosmic > bionic
    assert bionic < bionic_
    assert bionic_ > bionic
    assert not bionic > bionic


def test_ge_or_le():
    """Test greater than or equal or less than equal."""
    assert artful <= disco
    assert disco >= artful
    assert bionic <= cosmic
    assert cosmic >= bionic
    assert bionic <= bionic_
    assert bionic_ >= bionic
    assert bionic >= bionic
