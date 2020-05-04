#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from nornir.core import Nornir
from nornir.core.filter import F
from nornir.plugins.functions.text import print_result
from functions.verbose_mode import verbose_mode
from functions.base_selection import host_vars_ok
from functions.base_selection import (
    base_selection,
    device_not_compatible_with_napalm
)
from functions.facts.arista.facts_arista import (
    _arista_get_facts_api,
    _arista_get_facts_netconf,
    _arista_get_facts_ssh
)
from functions.facts.cumulus.facts_cumulus import (
    _cumulus_get_facts_api,
    _cumulus_get_facts_netconf,
    _cumulus_get_facts_ssh
)
from functions.facts.extreme_vsp.facts_extreme_vsp import (
    _extreme_vsp_get_facts_api,
    _extreme_vsp_get_facts_netconf,
    _extreme_vsp_get_facts_ssh
)
from functions.facts.ios.facts_ios import (
    _ios_get_facts_api,
    _ios_get_facts_netconf,
    _ios_get_facts_ssh
)
from functions.facts.iosxr.facts_iosxr import (
    _iosxr_get_facts_api,
    _iosxr_get_facts_netconf,
    _iosxr_get_facts_ssh
)
from functions.facts.juniper.facts_juniper import (
    _juniper_get_facts_api,
    _juniper_get_facts_netconf,
    _juniper_get_facts_ssh
)
from functions.facts.napalm.facts_napalm import (
    _generic_facts_napalm
)
from functions.facts.nxos.facts_nxos import (
    _nxos_get_facts_api,
    _nxos_get_facts_netconf,
    _nxos_get_facts_ssh
)
from const.constants import (
    NOT_SET,
    LEVEL1,
    LEVEL2,
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
    NAPALM_CONNECTION,
)


MAPPING_FUNCTION = {
    ARISTA_PLATEFORM_NAME: {
        API_CONNECTION: _arista_get_facts_api,
        SSH_CONNECTION: _arista_get_facts_ssh,
        NETCONF_CONNECTION: _arista_get_facts_netconf,
        NAPALM_CONNECTION: _generic_facts_napalm
    },
    CUMULUS_PLATEFORM_NAME: {
        API_CONNECTION: _cumulus_get_facts_api,
        SSH_CONNECTION: _cumulus_get_facts_ssh,
        NETCONF_CONNECTION: _cumulus_get_facts_netconf,
        NAPALM_CONNECTION: device_not_compatible_with_napalm
    },
    EXTREME_PLATEFORM_NAME: {
        API_CONNECTION: _extreme_vsp_get_facts_api,
        SSH_CONNECTION: _extreme_vsp_get_facts_ssh,
        NETCONF_CONNECTION: _extreme_vsp_get_facts_netconf,
        NAPALM_CONNECTION: device_not_compatible_with_napalm
    },
    CISCO_IOS_PLATEFORM_NAME: {
        API_CONNECTION: _ios_get_facts_api,
        SSH_CONNECTION: _ios_get_facts_ssh,
        NETCONF_CONNECTION: _ios_get_facts_netconf,
        NAPALM_CONNECTION: _generic_facts_napalm
    },
    CISCO_IOSXR_PLATEFORM_NAME: {
        API_CONNECTION: _iosxr_get_facts_api,
        SSH_CONNECTION: _iosxr_get_facts_ssh,
        NETCONF_CONNECTION: _iosxr_get_facts_netconf,
        NAPALM_CONNECTION: _generic_facts_napalm
    },
    JUNOS_PLATEFORM_NAME: {
        API_CONNECTION: _juniper_get_facts_api,
        SSH_CONNECTION: _juniper_get_facts_ssh,
        NETCONF_CONNECTION: _juniper_get_facts_netconf,
        NAPALM_CONNECTION: _generic_facts_napalm
    },
    NEXUS_PLATEFORM_NAME: {
        API_CONNECTION: _nxos_get_facts_api,
        SSH_CONNECTION: _nxos_get_facts_ssh,
        NETCONF_CONNECTION: _nxos_get_facts_netconf,
        NAPALM_CONNECTION: _generic_facts_napalm
    },
}


HEADER = "[netests - get_facts]"


def get_facts(nr: Nornir, options={}):
    if (
        'from_cli' in options.keys() and
        options.get('from_cli') is not None and
        options.get("from_cli") is True and
        isinstance(options.get("from_cli"), bool)
    ):
        devices = nr.filter(F(groups__contains="netests"))
        os.environ["NETESTS_VERBOSE"] = LEVEL1
    else:
        devices = nr.filter()

    if len(devices.inventory.hosts) == 0:
        print(f"[{HEADER}] no device selected.")

    else:
        output = devices.run(
            task=generic_facts_get,
            on_failed=True,
            options=options
        )
        if verbose_mode(
            user_value=os.environ.get("NETESTS_VERBOSE", NOT_SET),
            needed_value=LEVEL2
        ):
            print_result(output)


def generic_facts_get(task, options={}):
    if host_vars_ok(
        hostname=task.host.name,
        platform=task.host.platform,
        connection_mode=task.host.data.get("connexion")
    ):
        base_selection(
            platform=task.host.platform,
            connection_mode=task.host.data.get("connexion"),
            functions_mapping=MAPPING_FUNCTION
        )(task, options)