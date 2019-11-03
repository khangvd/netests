#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

"""
Add a description ....

"""

__author__ = "Dylan Hamel"
__maintainer__ = "Dylan Hamel"
__version__ = "1.0"
__email__ = "dylan.hamel@protonmail.com"
__status__ = "Prototype"
__copyright__ = "Copyright 2019"

########################################################################################################################
#
# HEADERS
#
ERROR_HEADER = "Error import [lldp_converters.py]"
HEADER_GET = "[netests - lldp_converters]"

########################################################################################################################
#
# Import Library
#
try:
    from const.constants import *
except ImportError as importError:
    print(f"{ERROR_HEADER} const.constants")
    exit(EXIT_FAILURE)
    print(importError)

try:
    from protocols.lldp import LLDP, ListLLDP
except ImportError as importError:
    print(f"{ERROR_HEADER} protocols.lldp")
    exit(EXIT_FAILURE)
    print(importError)

try:
    import json
except ImportError as importError:
    print(f"{ERROR_HEADER} json")
    exit(EXIT_FAILURE)
    print(importError)

########################################################################################################################
#
# Functions
#

# ----------------------------------------------------------------------------------------------------------------------
#
# Cumulus Networks LLDP converter
#
def _cumulus_lldp_converter(hostname:str(), cmd_output:json) -> ListLLDP:

    lldp_neighbors_lst = ListLLDP(list())

    if "lldp" in cmd_output.keys():
        if cmd_output.get('lldp', NOT_SET) is NOT_SET:
            return ListLLDP(list())

        else:

            for lldp_neighbor in cmd_output.get('lldp', NOT_SET)[0].get("interface", NOT_SET):

                neighbor_type_lst = list()

                if lldp_neighbor.get("chassis", NOT_SET)[0].get("descr", NOT_SET) == NOT_SET:
                    neighbor_os = NOT_SET
                else:
                    neighbor_os = lldp_neighbor.get("chassis", NOT_SET)[0].get("descr", NOT_SET)[0].get("value", NOT_SET)

                for capability in lldp_neighbor.get("chassis", NOT_SET)[0].get("capability", NOT_SET):
                    neighbor_type_lst.append(capability.get("type", NOT_SET))


                lldp_obj = LLDP(
                    local_name=hostname,
                    local_port=_mapping_interface_name(lldp_neighbor.get("name", NOT_SET)),
                    neighbor_mgmt_ip=lldp_neighbor.get("chassis", NOT_SET)[0].get("mgmt-ip", NOT_SET)[0].get("value", NOT_SET),
                    neighbor_name=lldp_neighbor.get("chassis", NOT_SET)[0].get("name", NOT_SET)[0].get("value", NOT_SET),
                    neighbor_port=_mapping_interface_name(
                        lldp_neighbor.get("port", NOT_SET)[0].get("id", NOT_SET)[0].get("value", NOT_SET)),
                    neighbor_os=neighbor_os,
                    neighbor_type=neighbor_type_lst
                )

                lldp_neighbors_lst.lldp_neighbors_lst.append(lldp_obj)

    return lldp_neighbors_lst


# ----------------------------------------------------------------------------------------------------------------------
#
# Cisco Nexus NXOS LLDP converter
#
def _nexus_lldp_converter(hostname:str(), cmd_output:json) -> ListLLDP:

    lldp_neighbors_lst = ListLLDP(list())

    if "TABLE_nbor_detail" in cmd_output.keys():

            for lldp_neighbor in cmd_output.get('TABLE_nbor_detail', NOT_SET).get("ROW_nbor_detail", NOT_SET):

                neighbor_type_lst = list()

                for sys_capability in lldp_neighbor.get("system_capability", NOT_SET):
                    neighbor_type_lst.append(_mapping_sys_capabilities(sys_capability))

                lldp_obj = LLDP(
                    local_name=hostname,
                    local_port=_mapping_interface_name(lldp_neighbor.get("l_port_id", NOT_SET)),
                    neighbor_mgmt_ip=lldp_neighbor.get("mgmt_addr", NOT_SET),
                    neighbor_name=lldp_neighbor.get("sys_name", NOT_SET),
                    neighbor_port=_mapping_interface_name(lldp_neighbor.get("port_id", NOT_SET)),
                    neighbor_os=lldp_neighbor.get("sys_desc", NOT_SET),
                    neighbor_type=neighbor_type_lst
                )

                lldp_neighbors_lst.lldp_neighbors_lst.append(lldp_obj)

    return lldp_neighbors_lst

# ----------------------------------------------------------------------------------------------------------------------
#
# Arista vEOS LLDP converter
#
def _arista_lldp_converter(hostname:str(), cmd_output:json) -> ListLLDP:

    lldp_neighbors_lst = ListLLDP(list())

    if "lldpNeighbors" in cmd_output.keys():

        for interface_name, facts in cmd_output.get("lldpNeighbors", NOT_SET).items():
            if len(facts.get("lldpNeighborInfo")) > 0:
                for data in facts.get("lldpNeighborInfo", NOT_SET):

                    neighbor_type_lst = list()
                    for sys_capability in data.get("systemCapabilities", NOT_SET):
                        neighbor_type_lst.append((str(sys_capability).capitalize()))

                    neighbor_mgmt_ip = str()
                    for address in data.get("managementAddresses", NOT_SET):
                        if address.get("addressType", NOT_SET) == "ipv4":
                            neighbor_mgmt_ip = address.get("address", NOT_SET)

                    lldp_obj = LLDP(
                        local_name=hostname,
                        local_port=_mapping_interface_name(interface_name),
                        neighbor_mgmt_ip=neighbor_mgmt_ip,
                        neighbor_name=data.get("systemName", NOT_SET),
                        neighbor_port=_mapping_interface_name(
                            data.get("neighborInterfaceInfo", NOT_SET).get("interfaceDescription", NOT_SET)),
                        neighbor_os=data.get("systemDescription", NOT_SET),
                        neighbor_type=neighbor_type_lst
                    )

                    lldp_neighbors_lst.lldp_neighbors_lst.append(lldp_obj)

    return lldp_neighbors_lst

# ----------------------------------------------------------------------------------------------------------------------
#
# LLDP sysem compability converter
#
def _mapping_sys_capabilities(code) -> str():
    """
    This function will return systeme capability name regarding the abreviation given in parameter

    Output extract from Cisco Nexus9000 9000v Chassis NXOS: version 7.0(3)I7(5a)

    Capability codes:
    (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
    (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other

    :param codes: str()
    :return str(): that contains system capability name
    """

    if code == "R":
        return "Router"
    elif code == "B":
        return "Bridge"
    elif code == "T":
        return "Telephone"
    elif code == "C":
        return "DOCSIS Cable Device"
    elif code == "W":
        return "WLAN Access Point"
    elif code == "P":
        return "Repeater"
    elif code == "S":
        return "Station"
    elif code == "O":
        return "Other"
    else:
        return NOT_SET

# ----------------------------------------------------------------------------------------------------------------------
#
# Mapping inter converter
#
def _mapping_interface_name(int_name) -> str():
    """
    This function will receive an interface name in parameter and return the standard interface name.

    For example:
        * (Arista) Ethernet3 => Eth1/3

    :param int_name:
    :return:
    """

    if "Ethernet1/" in int_name:
        number = ""
        slash_index = int_name.find("/")
        for char in int_name[slash_index:]:
            if str(char).isdigit():
                number = number + str(char)
        return "Eth1/" + number

    elif "Ethernet" in int_name:
        number = ""
        for char in int_name:
            if str(char).isdigit():
                number = number + str(char)
        return "Eth1/" + number

    else:
        return int_name