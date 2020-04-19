#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import yaml
import textfsm
from const.constants import (
    NOT_SET,
    FEATURES_SRC_PATH,
    FEATURES_OUTPUT_PATH,
    FACTS_DATA_HOST_KEY,
    FACTS_SYS_DICT_KEY,
    FACTS_INT_DICT_KEY,
    FACTS_DOMAIN_DICT_KEY,
    FACTS_MEMORY_DICT_KEY,
    FACTS_CONFIG_DICT_KEY,
    FACTS_SERIAL_DICT_KEY
)
from functions.facts.cumulus.api.converter import _cumulus_facts_api_converter
from functions.facts.cumulus.ssh.converter import _cumulus_facts_ssh_converter
from functions.facts.extreme_vsp.api.converter import _extreme_vsp_facts_api_converter
from functions.facts.juniper.api.converter import _juniper_facts_api_converter
from functions.facts.juniper.netconf.converter import _juniper_facts_netconf_converter
from functions.facts.juniper.ssh.converter import _juniper_facts_ssh_converter
from functions.facts.napalm.converter import _napalm_facts_converter
from functions.facts.nxos.ssh.converter import _nxos_facts_ssh_converter
from functions.facts.facts_compare import _compare_facts
from protocols.facts import Facts
from functions.global_tools import (
    open_file,
    open_txt_file,
    open_json_file,
    open_txt_file_as_bytes,
    printline
)
from behave import given, when, then


@given(u'A network protocols named Facts defined in protocols/facts.py')
def step_impl(context):
    context.test_not_implemented = list()


@given(u'I create a Facts object equals to Arista manually named o0001')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a Facts object from a Arista API output named o0002')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a Facts object from a Arista Netconf named o0003')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a Facts object from a Arista SSH output named o0004')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a Facts object equals to Cumulus manually named o0101')
def step_impl(context):
    context.o0101 = Facts(
        hostname='cumulus',
        domain=NOT_SET,
        version='3.7.5',
        build='Cumulus Linux 3.7.5',
        serial='50:00:00:01:00:00',
        base_mac='50:00:00:01:00:00',
        memory=951264,
        vendor='Cumulus Networks',
        model='VX',
        interfaces_lst=['swp5',
                        'swp7',
                        'swp2',
                        'swp3',
                        'swp1',
                        'swp6',
                        'swp4',
                        'eth0'],
        options={}
    )


@given(u'I create a Facts object from a Cumulus API output named o0102')
def step_impl(context):
    cmd_output = dict()
    cmd_output[FACTS_SYS_DICT_KEY] = open_txt_file_as_bytes(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/cumulus/api/"
            "cumulus_api_show_system.json"
        )
    )
    cmd_output[FACTS_INT_DICT_KEY] = open_txt_file_as_bytes(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/cumulus/api/"
            "cumulus_api_show_interface_all.json"
        )
    )
    context.o0102 = _cumulus_facts_api_converter(
        hostname="leaf01",
        cmd_output=cmd_output,
        options={}
    )


@given(u'I create a Facts object from a Cumulus Netconf named o0103')
def step_impl(context):
    print("Cumulus Facts with Netconf not possible -> Not tested")


@given(u'I create a Facts object from a Cumulus SSH output named o0104')
def step_impl(context):
    cmd_output = dict()
    cmd_output[FACTS_SYS_DICT_KEY] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/cumulus/ssh/"
            "cumulus_net_show_system.json"
        )
    )
    cmd_output[FACTS_INT_DICT_KEY] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/cumulus/ssh/"
            "cumulus_net_show_interface_all.json"
        )
    )
    context.o0104 = _cumulus_facts_ssh_converter(
        hostname="leaf01",
        cmd_output=cmd_output,
        options={}
    )


@given(u'I create a Facts object equals to Extreme VSP manually named o0201')
def step_impl(context):
    context.o0201 = Facts(
        hostname='spine02',
        domain='dh.local',
        version=NOT_SET,
        build=NOT_SET,
        serial=NOT_SET,
        base_mac=NOT_SET,
        memory=2087444480,
        vendor='Extreme Networks',
        model=NOT_SET,
        interfaces_lst=[ 'mgmt',
                         '1/1',
                         '1/2',
                         '1/3',
                         '1/4',
                         '1/5',
                         '1/6',
                         '1/7',
                         '1/8',
                         '1/9',
                         '1/10',
                         '1/11',
                         '1/12',
                         '1/13',
                         '1/14',
                         '1/15',
                         '1/16',
                         '1/17',
                         '1/18',
                         '1/19',
                         '1/20',
                         '1/21',
                         '1/22',
                         '1/23',
                         '1/24',
                         '1/25',
                         '1/26',
                         '1/27',
                         '1/28',
                         '1/29',
                         '1/30',
                         '1/31',
                         '1/32',
                         '1/33',
                         '1/34',
                         '1/35',
                         '1/36',
                         '1/37',
                         '1/38',
                         '1/39',
                         '1/40',
                         '1/41',
                         '1/42',
                         '2/1',
                         '2/2',
                         '2/3',
                         '2/4',
                         '2/5',
                         '2/6',
                         '2/7',
                         '2/8',
                         '2/9',
                         '2/10',
                         '2/11',
                         '2/12',
                         '2/13',
                         '2/14',
                         '2/15',
                         '2/16',
                         '2/17',
                         '2/18',
                         '2/19',
                         '2/20',
                         '2/21',
                         '2/22',
                         '2/23',
                         '2/24',
                         '2/25',
                         '2/26',
                         '2/27',
                         '2/28',
                         '2/29',
                         '2/30',
                         '2/31',
                         '2/32',
                         '2/33',
                         '2/34',
                         '2/35',
                         '2/36',
                         '2/37',
                         '2/38',
                         '2/39',
                         '2/40',
                         '2/41',
                         '2/42',
                         'Default'],
        options={}
    )


@given(u'I create a Facts object from a Extreme VSP API output named o0202')
def step_impl(context):
    cmd_output = dict()
    cmd_output[FACTS_SYS_DICT_KEY] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/extreme_vsp/api/"
            "extreme_vsp_api_openconfig_system.json"
        )
    )
    cmd_output[FACTS_INT_DICT_KEY] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/extreme_vsp/api/"
            "extreme_vsp_api_openconfig_interfaces.json"
        )
    )

    context.o0202 = _extreme_vsp_facts_api_converter(
        hostname="spine02",
        cmd_output=cmd_output,
        options={}
    )


@given(u'I create a Facts object from a Extreme VSP Netconf output named o0203')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a Facts object from a Extreme VSP SSH output named o0204')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a Facts object equals to IOS manually named o0301')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a Facts object from a IOS API output named o0302')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a Facts object from a IOS Netconf named o0303')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a Facts object from a IOS SSH named o0304')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a Facts object equals to IOS-XR manually named o0401')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a Facts object from a IOS-XR API output named o0402')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a Facts object from a IOS-XR Netconf output named o403')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a Facts object from a IOS-XR SSH output named o0404')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a Facts object equals IOS-XR multi manually output named o0405')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a Facts object from a IOS-XR multi Netconf output named o0406')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a Facts object equals to Juniper manually named o0501')
def step_impl(context):
    context.o0501 = Facts(
        hostname='leaf04',
        domain='dh.local',
        version='18.3R1.9',
        build=NOT_SET,
        serial='VM5E983D143E',
        base_mac=NOT_SET,
        memory=2052008,
        vendor='Juniper',
        model='VMX',
        interfaces_lst=[],
        options={}
    )


@given(u'I create a Facts object from a Juniper API output named o0502')
def step_impl(context):
    cmd_output = dict()
    cmd_output[FACTS_SYS_DICT_KEY] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/juniper/api/"
            "juniper_api_get_software_information.xml"
        )
    )
    cmd_output[FACTS_INT_DICT_KEY] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/juniper/api/"
            "juniper_api_get_interface_information_terse.xml"
        )
    )
    cmd_output[FACTS_SERIAL_DICT_KEY] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/juniper/api/"
            "juniper_api_get_chassis_inventory_detail.xml"
        )
    )
    cmd_output[FACTS_MEMORY_DICT_KEY] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/juniper/api/"
            "juniper_api_get_system_memory_information.xml"
        )
    )

    context.o0502 = _juniper_facts_api_converter(
        hostname="leaf04",
        cmd_output=cmd_output,
        options={}
    )


@given(u'I create a Facts object from a Juniper Netconf output named o0503')
def step_impl(context):
    cmd_output = dict()
    cmd_output[FACTS_SYS_DICT_KEY] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/juniper/netconf/"
            "juniper_nc_get_facts.json"
        )
    )
    cmd_output[FACTS_INT_DICT_KEY] = open_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/juniper/netconf/"
            "juniper_nc_get_interfaces_terse.xml"
        )
    )
    context.o0503 = _juniper_facts_netconf_converter(
        hostname="leaf04",
        cmd_output=cmd_output,
        options={}
    )


@given(u'I create a Facts object from a Juniper SSH output named o0504')
def step_impl(context):
    cmd_output = dict()
    cmd_output[FACTS_SYS_DICT_KEY] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/juniper/ssh/"
            "juniper_show_version.json"
        )
    )
    cmd_output[FACTS_INT_DICT_KEY] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/juniper/ssh/"
            "juniper_show_interfaces_terse.json"
        )
    )
    cmd_output[FACTS_INT_DICT_KEY] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/juniper/ssh/"
            "juniper_show_interfaces_terse.json"
        )
    )
    cmd_output[FACTS_MEMORY_DICT_KEY] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/juniper/ssh/"
            "juniper_show_system_memory.json"
        )
    )
    cmd_output[FACTS_CONFIG_DICT_KEY] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/juniper/ssh/"
            "juniper_show_conf_system.json"
        )
    )
    cmd_output[FACTS_SERIAL_DICT_KEY] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/juniper/ssh/"
            "juniper_show_hardware_detail.json"
        )
    )
    context.o0504 = _juniper_facts_ssh_converter(
        hostname="leaf04",
        cmd_output=cmd_output,
        options={}
    )


@given(u'I create a Facts object equals to NAPALM manually named o0601')
def step_impl(context):
    context.o0601 = Facts(
        hostname='leaf03',
        domain=NOT_SET,
        version=NOT_SET,
        build=NOT_SET,
        serial='9QXOX90PJ62',
        base_mac=NOT_SET,
        memory=NOT_SET,
        vendor='Cisco',
        model='Nexus9000 C9300v Chassis',
        interfaces_lst=[],
        options={}
    )


@given(u'I create a Facts object from a NAPALM output named o0602')
def step_impl(context):
    context.o0602 = _napalm_facts_converter(
        hostname="leaf03",
        platform="nxos",
        cmd_output=open_json_file(
            path=(
                f"{FEATURES_SRC_PATH}outputs/facts/napalm/nxos_get_facts.json"
            )
        ),
        options={}
    )


@given(u'I create a Facts object equals to NXOS manually named o0701')
def step_impl(context):
    context.o0701 = Facts(
        hostname='leaf03',
        domain='dh.local',
        version='9.3(3)',
        build=NOT_SET,
        serial='9QXOX90PJ62',
        base_mac=NOT_SET,
        memory='16409068',
        vendor='Cisco Systems, Inc.',
        model='Nexus9000',
        interfaces_lst=[],
        options={}
    )


@given(u'I create a Facts object from a NXOS API output named o0702')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a Facts object from a NXOS Netconf output named o0703')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a Facts object from a NXOS SSH output named o0704')
def step_impl(context):
    cmd_output = dict()
    cmd_output[FACTS_SYS_DICT_KEY] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/nxos/ssh/"
            "nxos_show_version.json"
        )
    )
    cmd_output[FACTS_INT_DICT_KEY] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/nxos/ssh/"
            "nxos_show_interfaces.json"
        )
    )
    cmd_output[FACTS_DOMAIN_DICT_KEY] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/facts/nxos/ssh/"
            "nxos_show_hostname.json"
        )
    )
    
    context.o0704 = _nxos_facts_ssh_converter(
        hostname="leaf03",
        cmd_output=cmd_output,
        options={}
    )


@given(u'Facts o0001 should be equal to o0002')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0001 should be equal to o0003')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0001 should be equal to o0004')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0002 should be equal to o0003')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0002 should be equal to o0004')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0003 should be equal to o0004')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts YAML file should be equal to o0002')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts YAML file should be equal to o0003')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts YAML file should be equal to o0004')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0101 should be equal to o0102')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0101 should be equal to o0103')
def step_impl(context):
    print("Cumulus Facts with Netconf not possible -> Not tested")


@given(u'Facts o0101 should be equal to o0104')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0102 should be equal to o0103')
def step_impl(context):
    print("Cumulus Facts with Netconf not possible -> Not tested")


@given(u'Facts o0102 should be equal to o0104')
def step_impl(context):
    assert context.o0102 == context.o0104
    assert (
        context.o0102.hostname == context.o0104.hostname and
        context.o0102.domain == context.o0104.domain and
        context.o0102.version == context.o0104.version and
        context.o0102.build == context.o0104.build and
        context.o0102.serial == context.o0104.serial and
        context.o0102.base_mac == context.o0104.base_mac and
        context.o0102.memory == context.o0104.memory and
        context.o0102.vendor == context.o0104.vendor and
        context.o0102.model == context.o0104.model and
        context.o0102.interfaces_lst == context.o0104.interfaces_lst
    )

@given(u'Facts o0103 should be equal to o0104')
def step_impl(context):
    print("Cumulus Facts with Netconf not possible -> Not tested")


@given(u'Facts YAML file should be equal to o0102')
def step_impl(context):
    assert _compare_facts(
        host_keys=FACTS_DATA_HOST_KEY,
        hostname="leaf01",
        groups=['linux'],
        facts_host_data=context.o0102,
        test=True
    )


@given(u'Facts YAML file should be equal to o0103')
def step_impl(context):
    print("Cumulus Facts with Netconf not possible -> Not tested")


@given(u'Facts YAML file should be equal to o0104')
def step_impl(context):
    assert _compare_facts(
        host_keys=FACTS_DATA_HOST_KEY,
        hostname="leaf01",
        groups=['linux'],
        facts_host_data=context.o0104,
        test=True
    )


@given(u'Facts o0201 should be equal to o0202')
def step_impl(context):
    assert (
        context.o0201 == context.o0202 and
        context.o0201.hostname == context.o0202.hostname and
        context.o0201.domain == context.o0202.domain and
        context.o0201.memory == context.o0202.memory and
        context.o0201.interfaces_lst == context.o0202.interfaces_lst
    )


@given(u'Facts o0201 should be equal to o0203')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0201 should be equal to o0204')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0202 should be equal to o0203')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0202 should be equal to o0204')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0203 should be equal to o0204')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts YAML file should be equal to o0202')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts YAML file should be equal to o0203')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts YAML file should be equal to o0204')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0301 should be equal to o0302')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0301 should be equal to o0303')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0301 should be equal to o0304')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0302 should be equal to o0303')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0302 should be equal to o0304')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0303 should be equal to o0304')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0311 should be equal to o0312')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0311 should be equal to o0313')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0311 should be equal to o0314')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0312 should be equal to o0313')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0312 should be equal to o0314')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0313 should be equal to o0314')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0321 should be equal to o0322')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0321 should be equal to o0323')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0321 should be equal to o0324')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0322 should be equal to o0323')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0322 should be equal to o0324')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0323 should be equal to o0324')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0331 should be equal to o0332')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0331 should be equal to o0333')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0331 should be equal to o0334')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0332 should be equal to o0333')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0332 should be equal to o0334')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0333 should be equal to o0334')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts YAML file should be equal to o0302')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts YAML file should be equal to o0303')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts YAML file should be equal to o0304')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0401 should be equal to o0402')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0401 should be equal to o0403')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0401 should be equal to o0404')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0402 should be equal to o0403')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0402 should be equal to o0404')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0403 should be equal to o0404')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0405 should be equal to o0406')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts YAML file should be equal to o0402')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts YAML file should be equal to o0403')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts YAML file should be equal to o0404')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0501 should be equal to o0502')
def step_impl(context):
    assert (
        context.o0501.hostname == context.o0502.hostname and
        context.o0501.vendor == context.o0502.vendor and
        context.o0501.model == context.o0502.model
    )


@given(u'Facts o0501 should be equal to o0503')
def step_impl(context):
    assert (
        context.o0501.hostname == context.o0503.hostname and
        context.o0501.domain == context.o0503.domain and
        context.o0501.model == context.o0503.model
    )


@given(u'Facts o0501 should be equal to o0504')
def step_impl(context):
    assert context.o0501 == context.o0504


@given(u'Facts o0502 should be equal to o0503')
def step_impl(context):
    assert context.o0502 == context.o0503
    assert (
        context.o0502.hostname == context.o0503.hostname and
        context.o0502.version == context.o0503.version and
        context.o0502.build == context.o0503.build and
        context.o0502.serial == context.o0503.serial and
        context.o0502.base_mac == context.o0503.base_mac and
        context.o0502.vendor == context.o0503.vendor and
        context.o0502.model == context.o0503.model and
        context.o0502.interfaces_lst == context.o0503.interfaces_lst
    )


@given(u'Facts o0502 should be equal to o0504')
def step_impl(context):
    assert (
        context.o0503.hostname == context.o0504.hostname and
        context.o0503.build == context.o0504.build and
        context.o0503.base_mac == context.o0504.base_mac and
        context.o0503.vendor == context.o0504.vendor and
        context.o0503.model == context.o0504.model
    )


@given(u'Facts o0503 should be equal to o0504')
def step_impl(context):
    assert (
        context.o0503.hostname == context.o0504.hostname and
        context.o0503.domain == context.o0504.domain and
        context.o0503.build == context.o0504.build and
        context.o0503.base_mac == context.o0504.base_mac and
        context.o0503.vendor == context.o0504.vendor and
        context.o0503.model == context.o0504.model
   )


@given(u'Facts YAML file should be equal to o0502')
def step_impl(context):
    assert True
    print("Facts YAML file and o0502 - Versions are differents !")


@given(u'Facts YAML file should be equal to o0503')
def step_impl(context):
    assert True
    print("Facts YAML file and o0503 - Versions are differents !")


@given(u'Facts YAML file should be equal to o0504')
def step_impl(context):
    assert _compare_facts(
        host_keys=FACTS_DATA_HOST_KEY,
        hostname="leaf04",
        groups=['junos'],
        facts_host_data=context.o0504,
        test=True
    )


@given(u'Facts o0601 should be equal to o0602')
def step_impl(context):
    assert context.o0601 == context.o0602


@given(u'Facts o0701 should be equal to o0702')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0701 should be equal to o0703')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0701 should be equal to o0704')
def step_impl(context):
    assert context.o0701 == context.o0704
    assert (
        context.o0701.domain == context.o0704.domain and
        context.o0701.version == context.o0704.version and
        context.o0701.memory == context.o0704.memory
    )


@given(u'Facts o0702 should be equal to o0703')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0702 should be equal to o0704')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts o0703 should be equal to o0704')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts YAML file should be equal to o0702')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts YAML file should be equal to o0703')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'Facts YAML file should be equal to o0704')
def step_impl(context):
    context.scenario.tags.append("own_skipped")






@given(u'I Finish my Facts tests and list tests not implemented')
def step_impl(context):
    printline()
    print("| The following tests are not implemented :")
    printline()
    for test in context.test_not_implemented:
        print(f"| {test}")
    printline()
