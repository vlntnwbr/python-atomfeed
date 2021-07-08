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

"""Utilities for python-atomfeed."""

from typing import Dict, Optional

from xml.dom import minidom
from xml.etree import ElementTree as ET  # nosec (not used for parsing)

from .models import EtreeAttribute


def make_subelement(
    parent: ET.Element,
    tag: EtreeAttribute,
    text: EtreeAttribute,
    attrib: Optional[Dict[EtreeAttribute, EtreeAttribute]] = None,
    **extra: Optional[EtreeAttribute]
) -> ET.SubElement:
    """Create lxml.etree.SubElement with text."""
    if attrib is None:
        attrib = {}
    elem = ET.SubElement(parent, tag, attrib, **extra)
    elem.text = text
    return elem


def write_xml(
    xml: ET.Element,
    filename: str,
    encoding: Optional[str] = "UTF-8"
) -> None:
    """Write pretty, encoded lxml.etree.tostring to filename."""
    xml_str = minidom.parseString(ET.tostring(xml, xml_declaration=True))
    with open(filename, "wb") as xml_file:
        xml_file.write(xml_str.toprettyxml(encoding=encoding))
