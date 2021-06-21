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
    """Atom Date Construct (default UTC)."""

    time: datetime.datetime
    timeformat: Optional[str] = "%Y-%m-%dT%H:%M:%SZ"

    def __str__(self) -> str:
        return self.time.strftime(self.timeformat)

    @classmethod
    def from_timestamp(cls, timestamp: str, timeformat: Optional[str] = None):
        """Create AtomDate from timestamp as defined in rfc4287 #3.3"""

        if timeformat is None:
            timeformat = cls.timeformat
        time = datetime.datetime.strptime(timestamp, timeformat)
        return cls(time, timeformat)


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

    """Base class for an Atom Feed"""

    title: Any  # TODO
    updated: AtomDate
    authors: List[AtomPerson]  # TODO: only optional if all entries have author
    generator: Any  # TODO
    icon: Any  # TODO
    id: AtomId  # pylint: disable=invalid-name
    link: str
    logo: Any  # TODO
    rights: Any  # TODO
    subtitle: Any  # TODO
    categories: Optional[List[AtomCategory]] = None
    contributors: Optional[List[AtomPerson]] = None
    entries: Optional[List[FeedEntry]] = None
