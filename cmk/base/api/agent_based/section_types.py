#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
"""Types and classes used by the API for agent_based plugins
"""
from typing import Any, Callable, Generator, List, NamedTuple, Optional

from cmk.utils.type_defs import SectionName, ParsedSectionName

from cmk.snmplib.type_defs import SNMPDetectSpec, SNMPTable, SNMPTree

from cmk.base.check_utils import AgentSectionContent
from cmk.base.discovered_labels import HostLabel

AgentParseFunction = Callable[[AgentSectionContent], Any]

# we do *not* use SNMPSectionContent here, because List[SNMPTable]
# is more specific.
SNMPParseFunction = Callable[[List[SNMPTable]], Any]

HostLabelFunction = Callable[[Any], Generator[HostLabel, None, None]]

AgentSectionPlugin = NamedTuple(
    "AgentSectionPlugin",
    [
        ("name", SectionName),
        ("parsed_section_name", ParsedSectionName),
        ("parse_function", AgentParseFunction),
        ("host_label_function", HostLabelFunction),
        ("supersedes", List[SectionName]),
        ("module", Optional[str]),  # not available for auto migrated plugins.
    ])

SNMPSectionPlugin = NamedTuple(
    "SNMPSectionPlugin",
    [
        ("name", SectionName),
        ("parsed_section_name", ParsedSectionName),
        ("parse_function", SNMPParseFunction),
        ("host_label_function", HostLabelFunction),
        ("supersedes", List[SectionName]),
        ("detect_spec", SNMPDetectSpec),
        ("trees", List[SNMPTree]),
        ("module", Optional[str]),  # not available for auto migrated plugins.
    ])
