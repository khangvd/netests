#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from netests.getters.bgp_get import GetterBGP
from netests.getters.bgp_up_get import GetterBGPUp
from netests.getters.cdp_get import GetterCDP
from netests.getters.facts_get import GetterFacts
from netests.getters.lldp_get import GetterLLDP
from netests.getters.ospf_get import GetterOSPF
from netests.getters.ping_get import GetterPing
from netests.getters.vlan_get import GetterVLAN
from netests.getters.vrf_get import GetterVRF
from netests.protocols.bgp import BGPSession
from netests.protocols.cdp import CDP
from netests.protocols.facts import Facts
from netests.protocols.lldp import LLDP
from netests.protocols.ospf import OSPF
from netests.protocols.ping import PING
from netests.protocols.vlan import VLAN
from netests.protocols.vrf import VRF
from netests.constants import (
    BGP_SESSIONS_HOST_KEY,
    CDP_DATA_HOST_KEY,
    FACTS_DATA_HOST_KEY,
    LLDP_DATA_HOST_KEY,
    OSPF_SESSIONS_HOST_KEY,
    PING_DATA_HOST_KEY,
    VLAN_DATA_HOST_KEY,
    VRF_DATA_KEY,
    ARISTA_PLATEFORM_NAME,
    CUMULUS_PLATEFORM_NAME,
    EXTREME_PLATEFORM_NAME,
    CISCO_IOS_PLATEFORM_NAME,
    CISCO_IOSXR_PLATEFORM_NAME,
    JUNOS_PLATEFORM_NAME,
    NEXUS_PLATEFORM_NAME,
    API_CONNECTION,
    NETCONF_CONNECTION,
    SSH_CONNECTION,
    NAPALM_CONNECTION
)


MAPPING_PROTOCOLS = {
    "bgp": {
        "proto": BGPSession,
        "class": GetterBGP,
        "filename": "bgp.yml",
        "key_store": BGP_SESSIONS_HOST_KEY
    },
    "bgp_up": {
        "proto": BGPSession,
        "class": GetterBGPUp,
        "filename": None,
        "key_store": BGP_SESSIONS_HOST_KEY
    },
    "cdp": {
        "proto": CDP,
        "class": GetterCDP,
        "filename": "cdp.yml",
        "key_store": CDP_DATA_HOST_KEY,
    },
    "facts": {
        "proto": Facts,
        "class": GetterFacts,
        "filename": "facts.yml",
        "key_store": FACTS_DATA_HOST_KEY
    },
    "lldp": {
        "proto": LLDP,
        "class": GetterLLDP,
        "filename": "lldp.yml",
        "key_store": LLDP_DATA_HOST_KEY
    },
    "ospf": {
        "proto": OSPF,
        "class": GetterOSPF,
        "filename": "ospf.yml",
        "key_store": OSPF_SESSIONS_HOST_KEY
    },
    "ping": {
        "proto": PING,
        "class": GetterPing,
        "filename": "ping.yml",
        "key_store": PING_DATA_HOST_KEY
    },
    "vlan": {
        "proto": VLAN,
        "class": GetterVLAN,
        "filename": "vlan.yml",
        "key_store": VLAN_DATA_HOST_KEY
    },
    "vrf": {
        "proto": VRF,
        "class": GetterVRF,
        "filename": "vrf.yml",
        "key_store": VRF_DATA_KEY
    }
}


MAPPING_CONNEXION_PLATFORM = {
    ARISTA_PLATEFORM_NAME: {
        API_CONNECTION: True,
        NETCONF_CONNECTION: True,
        SSH_CONNECTION: True,
        NAPALM_CONNECTION: True
    },
    CUMULUS_PLATEFORM_NAME: {
        API_CONNECTION: True,
        NETCONF_CONNECTION: False,
        SSH_CONNECTION: True,
        NAPALM_CONNECTION: False
    },
    EXTREME_PLATEFORM_NAME: {
        API_CONNECTION: True,
        NETCONF_CONNECTION: False,
        SSH_CONNECTION: True,
        NAPALM_CONNECTION: False
    },
    CISCO_IOS_PLATEFORM_NAME: {
        API_CONNECTION: True,
        NETCONF_CONNECTION: True,
        SSH_CONNECTION: True,
        NAPALM_CONNECTION: True
    },
    CISCO_IOSXR_PLATEFORM_NAME: {
        API_CONNECTION: True,
        NETCONF_CONNECTION: True,
        SSH_CONNECTION: True,
        NAPALM_CONNECTION: True
    },
    JUNOS_PLATEFORM_NAME: {
        API_CONNECTION: True,
        NETCONF_CONNECTION: True,
        SSH_CONNECTION: True,
        NAPALM_CONNECTION: True
    },
    NEXUS_PLATEFORM_NAME: {
        API_CONNECTION: True,
        NETCONF_CONNECTION: True,
        SSH_CONNECTION: True,
        NAPALM_CONNECTION: True
    }
}
