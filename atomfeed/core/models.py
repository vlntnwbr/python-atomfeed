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

from typing import List, NewType, Optional, Union
from uuid import UUID, uuid4


EtreeAttribute = Union[bytes, str]


# Atom Common Constructs
@dataclasses.dataclass(frozen=True)
class AtomText:
    """An Atom Text construct"""

    content: str
    type: str = "text"


@dataclasses.dataclass(frozen=True)
class AtomPerson:
    """An Atom Person construct"""

    name: str
    uri: Optional[str] = None
    email: Optional[str] = None


@dataclasses.dataclass(frozen=True)
class AtomDate:
    """An Atom Date construct (default UTC)."""

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


AtomUri = NewType("AtomUri", str)


# Atom Metadata Elements
@dataclasses.dataclass(frozen=True)
class AtomCategory:
    """An Atom Category construct"""

    term: str
    scheme: Optional[str] = None
    label: Optional[str] = None


@dataclasses.dataclass(frozen=True)
class AtomGenerator:
    """An Atom Generator construct"""

    name: AtomText
    uri: Optional[AtomUri] = None
    version: Optional[AtomText] = None


class AtomId(UUID):
    """Class for urn:uuid identifier for atom feed and entries"""

    def __init__(self, urn: Optional[str] = None) -> None:

        if urn is None:
            urn = uuid4().urn

        super().__init__(urn)


@dataclasses.dataclass(frozen=True)
class AtomSource:  # TODO
    """An Atom Source construct"""


@dataclasses.dataclass(frozen=True)
class AtomLink:  # TODO
    """An Atom Link construct"""

    href: AtomUri


# Atom Container Elements
@dataclasses.dataclass(frozen=True)
class AtomContent:  # TODO
    """An Atom Content construct"""


@dataclasses.dataclass(frozen=True)
class FeedEntry:  # pylint: disable=too-many-instance-attributes
    """An entry for an Atom feed"""

    title: AtomText
    updated: AtomDate
    id: AtomId  # pylint: disable=invalid-name
    content: AtomContent
    authors: Optional[List[AtomPerson]] = None
    # TODO: optional if source with author is given
    #       or the parent feed has an author element
    categories: Optional[List[AtomCategory]] = None
    contributors: Optional[List[AtomPerson]] = None
    links: Optional[List[AtomLink]] = None
    # TODO: required if content is empty.
    # Then it must have the attributes
    # 'rel'='alternate', and same combination of 'type' & 'hreflang'
    published: Optional[AtomDate] = None
    rights: Optional[AtomText] = None  # TODO: optional
    source: Optional[AtomSource] = None
    summary: Optional[AtomText] = None
    # TODO: required if content has 'src' attribute and is thus empty
    #       or content is base64 encoded


@dataclasses.dataclass(frozen=True)
class AtomFeed:  # pylint: disable=too-many-instance-attributes
    """Base class for an Atom Feed"""

    title: AtomText
    updated: AtomDate
    id: AtomId  # pylint: disable=invalid-name
    authors: Optional[List[AtomPerson]] = None  # TODO: only optional if all entries have author
    categories: Optional[List[AtomCategory]] = None
    contributors: Optional[List[AtomPerson]] = None
    generator: Optional[AtomGenerator] = AtomGenerator()
    icon: Optional[AtomUri] = None
    links: Optional[List[AtomLink]] = None
    # TODO: should contain link with attribute 'self' that points to feed
    #       must not contain more than one with 'rel'='alternate
    #       and same combination of 'type' and 'hreflang'
    logo: Optional[AtomUri] = None
    rights: Optional[AtomText] = None
    subtitle: Optional[AtomText] = None
    entries: Optional[List[FeedEntry]] = None
