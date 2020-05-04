#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from ncclient import manager
from xml.etree import ElementTree
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_command
from const.constants import NOT_SET, LEVEL2, VRF_DATA_KEY, IOS_GET_VRF
from functions.verbose_mode import verbose_mode
from functions.http_request import exec_http_call
from functions.vrf.ios.api.converter import _ios_vrf_api_converter
from functions.vrf.ios.ssh.converter import _ios_vrf_ssh_converter
from functions.vrf.ios.netconf.converter import _ios_vrf_netconf_converter


def _ios_get_vrf_api(task, options={}):
    vrf_config = exec_http_call(
        hostname=task.host.hostname,
        port=task.host.port,
        username=task.host.username,
        password=task.host.password,
        endpoint="data/Cisco-IOS-XE-native:native"
    )

    ElementTree.fromstring(vrf_config)

    task.host[VRF_DATA_KEY] = _ios_vrf_api_converter(
        hostname=task.host.name,
        cmd_output=vrf_config,
        options=options
    )


def _ios_get_vrf_netconf(task, options={}):
    with manager.connect(
        host=task.host.hostname,
        port=task.host.port,
        username=task.host.username,
        password=task.host.password,
        hostkey_verify=False,
        device_params={'name': 'iosxe'}
    ) as m:

        vrf_config = m.get_config(
            source='running',
            filter=(
                'subtree',
                '''
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"/>
                '''
            )
        ).data_xml

        ElementTree.fromstring(vrf_config)

        task.host[VRF_DATA_KEY] = _ios_vrf_netconf_converter(
            hostname=task.host.name,
            cmd_output=vrf_config,
            options=options
        )


def _ios_get_vrf_ssh(task, options={}):
    output = task.run(
        name=f"{IOS_GET_VRF}",
        task=netmiko_send_command,
        command_string=f"{IOS_GET_VRF}",
    )
    if verbose_mode(
        user_value=os.environ.get("NETESTS_VERBOSE", NOT_SET),
        needed_value=LEVEL2
    ):
        print_result(output)

    task.host[VRF_DATA_KEY] = _ios_vrf_ssh_converter(
        hostname=task.host.name,
        cmd_output=output.result,
        options=options
    )