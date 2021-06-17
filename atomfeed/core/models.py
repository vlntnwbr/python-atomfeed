##
#   Copyright (c) 2021 Valentin Weber
#
#   This file is part of the software python-atomfeed.
#
#   The software is licensed under the European Union Public License
#   (EUPL) version 1.2 or later. You should have received a copy of
#   the english license text with the software. For your rights and
#   obligations under this license refer to the file LICENSE or visit
#   https://joinup.ec.europa.eu/community/eupl/og_page/eupl to view
#   official translations of the licence in another language of the EU.
##

"""Data models for python-atomfeed according to rfc4287"""

import dataclasses
import datetime

from typing import Optional, Union
from uuid import UUID, uuid4


EtreeAttribute = Union[bytes, str]


class AtomId(UUID):
    """Class for urn:uuid identifier for atom feed and entries"""

    def __init__(self, urn: Optional[str] = None) -> None:
        
        if urn is None:
            urn = uuid4().urn       
        
        super().__init__(urn)


@dataclasses.dataclass(frozen=True)
class AtomPerson:
    """An Atom Person Construct"""

    name: str
    uri: Optional[str] = None
    email: Optional[str] = None


@dataclasses.dataclass(frozen=True)
class AtomDate:
    """An Atom Date Construct defaults to UTC if no timefmt is given."""

    time: datetime.datetime
    timefmt: Optional[str] = "%Y-%m-%dT%H:%M:%SZ"

    def __str__(self) -> str:
        return self.time.strftime(self.timefmt)

    @classmethod
    def from_timestamp(cls, timestamp: str, timefmt: Optional[str] = None):
        """Create AtomDate from timestamp as defined in rfc4287 #3.3"""

        if timefmt is None:
            timefmt = cls.timefmt
        print(timefmt)
        time = datetime.datetime.strptime(timestamp, timefmt)
        return cls(time, timefmt)


@dataclasses.dataclass(frozen=True)
class AtomCategory:
    """An Atom Category construct"""

    term: str
    scheme: Optional[str] = None
    label: Optional[str] = None


@dataclasses.dataclass(frozen=True)
class FeedEntry:
    """An entry for an Atom feed"""


@dataclasses.dataclass(frozen=True)
class AtomFeed:
    """Base class for an Atom Feed"""
