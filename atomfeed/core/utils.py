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

"""Utility for python-atomfeed"""

from typing import Any, Dict, Optional, Union

from lxml import etree

from .models import EtreeAttribute

def make_subelement(
    parent: etree._Element,
    tag: EtreeAttribute,
    text: EtreeAttribute,
    attrib: Dict[EtreeAttribute, EtreeAttribute] = {},
    nsmap: Optional[EtreeAttribute] = None,
    **extra: Optional[EtreeAttribute]
    ) -> etree.SubElement:
    """Create lxml.etree.SubElement with text"""
    elem = etree.SubElement(parent, tag, attrib, nsmap, **extra)
    elem.text = text
    return elem


def write_xml(
    xml: etree._Element,
    filename: str, 
    encoding: Optional[str] = "UTF-8"
    ) -> None:
    """Write pretty-printed, encoded lxml.etree.tostring to filename"""

    xml_str = etree.tostring(
        xml, pretty_print=True, xml_declaration=True, encoding=encoding
    ).decode(encoding)

    with open(filename, "w", encoding=encoding) as xml_file:
        xml_file.write(xml_str)
