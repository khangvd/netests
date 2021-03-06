#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import yaml
import textfsm
from netests.comparators.bgp_compare import _compare_bgp
from netests.mappings import get_bgp_state_brief, get_bgp_peer_uptime
from netests.converters.bgp.arista.api import _arista_bgp_api_converter
from netests.converters.bgp.arista.ssh import _arista_bgp_ssh_converter
from netests.converters.bgp.cumulus.api import _cumulus_bgp_api_converter
from netests.converters.bgp.cumulus.ssh import _cumulus_bgp_ssh_converter
from netests.converters.bgp.extreme_vsp.ssh  import _extreme_vsp_bgp_ssh_converter
from netests.converters.bgp.ios.api import _ios_bgp_api_converter
from netests.converters.bgp.ios.nc import _ios_bgp_nc_converter
from netests.converters.bgp.ios.ssh import _ios_bgp_ssh_converter
from netests.converters.bgp.iosxr.nc import _iosxr_bgp_nc_converter
from netests.converters.bgp.iosxr.ssh import _iosxr_bgp_ssh_converter
from netests.converters.bgp.juniper.api import _juniper_bgp_api_converter
from netests.converters.bgp.juniper.nc import _juniper_bgp_nc_converter
from netests.converters.bgp.juniper.ssh import _juniper_bgp_ssh_converter
from netests.converters.bgp.napalm.converter import _napalm_bgp_converter
from netests.converters.bgp.nxos.api import _nxos_bgp_api_converter
from netests.converters.bgp.nxos.api import _nxos_bgp_api_converter
from netests.converters.bgp.nxos.ssh  import _nxos_bgp_ssh_converter
from netests.constants import (
    NOT_SET,
    FEATURES_SRC_PATH,
    BGP_SESSIONS_HOST_KEY,
    BGP_UPTIME_FORMAT_MS
)
from netests.protocols.bgp import (
    BGPSession,
    ListBGPSessions,
    BGPSessionsVRF,
    ListBGPSessionsVRF,
    BGP
)
from netests.tools.file import (
    open_file,
    open_txt_file,
    open_json_file,
    open_txt_file_as_bytes
)
from behave import given, when, then


@given(u'A network protocols named BGP defined in netests/protocols/bgp.py')
def step_impl(context):
    context.test_not_implemented = list()


@given(u'I create a BGP object equals to Arista manually named o0001')
def step_impl(context):
    bgp_sessions_vrf_lst = ListBGPSessionsVRF(
        list()
    )

    bgp_sessions_lst = ListBGPSessions(
        list()
    )

    bgp_sessions_lst.bgp_sessions.append(
        BGPSession(
            src_hostname="leaf03",
            peer_ip="100.100.100.100",
            peer_hostname=NOT_SET,
            remote_as="100",
            state_brief=get_bgp_state_brief(
                "Idle"
            ),
            session_state="Idle",
            state_time=1588518931.27118,
            prefix_received=0
        )
    )

    bgp_sessions_vrf_lst.bgp_sessions_vrf.append(
        BGPSessionsVRF(
            vrf_name="CUSTOMER_WEJOB",
            as_number="1111",
            router_id="1.2.3.4",
            bgp_sessions=bgp_sessions_lst
        )
    )

    bgp_sessions_lst = ListBGPSessions(
        list()
    )

    bgp_sessions_lst.bgp_sessions.append(
        BGPSession(
            src_hostname="leaf03",
            peer_ip="11.11.11.11",
            peer_hostname=NOT_SET,
            remote_as="11",
            state_brief=get_bgp_state_brief(
                "Idle"
            ),
            session_state="Idle",
            state_time=1588518176.788854,
            prefix_received=0
        )
    )

    bgp_sessions_lst.bgp_sessions.append(
        BGPSession(
            src_hostname="leaf03",
            peer_ip="12.12.12.12",
            peer_hostname=NOT_SET,
            remote_as="12",
            state_brief=get_bgp_state_brief(
                "Idle"
            ),
            session_state="Idle",
            state_time=1588518913.789179,
            prefix_received=0
        )
    )

    bgp_sessions_vrf_lst.bgp_sessions_vrf.append(
        BGPSessionsVRF(
            vrf_name="CUSTOMER_NETESTS",
            as_number="1111",
            router_id="66.66.66.66",
            bgp_sessions=bgp_sessions_lst
        )
    )

    context.o0001 = BGP(
        hostname="leaf03",
        bgp_sessions_vrf_lst=bgp_sessions_vrf_lst
    )


@given(u'I create a BGP object from a Arista API output named o0002')
def step_impl(context):
    cmd_output = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/arista/api/"
            "arista_api_get_bgp.json"
        )
    )
    context.o0002 = _arista_bgp_api_converter(
        hostname="leaf03",
        cmd_output=cmd_output,
        options={}
    )


@given(u'I create a BGP object from a Arista Netconf named o0003')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a BGP object from a Arista SSH output named o0004')
def step_impl(context):
    cmd_output=dict()
    cmd_output['default'] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/arista/ssh/"
            "arista_show_ip_bgp_summary_default.json"
        )
    )
    cmd_output['CUSTOMER_WEJOB'] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/arista/ssh/"
            "arista_show_ip_bgp_summary_one_peer.json"
        )
    )
    cmd_output['CUSTOMER_NETESTS']=open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/arista/ssh/"
            "arista_show_ip_bgp_summary_many_peers.json"
        )
    )
    context.o0004=_arista_bgp_ssh_converter(
        hostname="leaf03",
        cmd_output=cmd_output,
        options={}
    )


@given(u'I create a BGP object equals to Cumulus manually named o0101')
def step_impl(context):
    bgp_sessions_vrf_lst = ListBGPSessionsVRF(
        list()
    )

    bgp_sessions_lst = ListBGPSessions(
        list()
    )

    bgp_sessions_lst.bgp_sessions.append(
        BGPSession(
            src_hostname="leaf01",
            peer_ip="10.1.1.2",
            peer_hostname=NOT_SET,
            remote_as="65102",
            state_brief=get_bgp_state_brief(
                "Connect"
            ),
            session_state="Connect",
            state_time=get_bgp_peer_uptime(
                value=0,
                format=BGP_UPTIME_FORMAT_MS
            ),
            prefix_received=NOT_SET
        )
    )

    bgp_sessions_vrf_lst.bgp_sessions_vrf.append(
        BGPSessionsVRF(
            vrf_name="default",
            as_number="65101",
            router_id="1.1.1.1",
            bgp_sessions=bgp_sessions_lst
        )
    )

    bgp_sessions_lst = ListBGPSessions(
        list()
    )

    bgp_sessions_lst.bgp_sessions.append(
        BGPSession(
            src_hostname="leaf01",
            peer_ip="10.1.2.2",
            peer_hostname=NOT_SET,
            remote_as="65203",
            state_brief=get_bgp_state_brief(
                "Connect"
            ),
            session_state="Connect",
            state_time=get_bgp_peer_uptime(
                value=0,
                format=BGP_UPTIME_FORMAT_MS
            ),
            prefix_received=NOT_SET
        )
    )

    bgp_sessions_vrf_lst.bgp_sessions_vrf.append(
        BGPSessionsVRF(
            vrf_name="IOS_XR_VRF",
            as_number="65201",
            router_id="10.10.10.10",
            bgp_sessions=bgp_sessions_lst
        )
    )

    context.o0101 = BGP(
        hostname="leaf01",
        bgp_sessions_vrf_lst=bgp_sessions_vrf_lst
    )


@given(u'I create a BGP object from a Cumulus API output named o0102')
def step_impl(context):
    cmd_output = dict()
    cmd_output['default'] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/cumulus/api/"
            "cumulus_api_get_vrf_default.json"
        )
    )
    cmd_output['IOS_XR_VRF'] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/cumulus/api/"
            "cumulus_api_get_vrf_xyz.json"
        )
    )
    context.o0102 = _cumulus_bgp_api_converter(
        hostname="leaf01",
        cmd_output=cmd_output,
        options={}
    )


@given(u'I create a BGP object from a Cumulus Netconf named o0103')
def step_impl(context):
    print("Cumulus BGP with Netconf not possible -> Not tested")


@given(u'I create a BGP object from a Cumulus SSH output named o0104')
def step_impl(context):
    cmd_output = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/cumulus/ssh/"
            "cumulus_ssh_get_vrf.json"
        )
    )
    context.o0104 = _cumulus_bgp_api_converter(
        hostname="leaf01",
        cmd_output=cmd_output,
        options={}
    )


@given(u'I create a BGP object equals to Extreme VSP manually named o0201')
def step_impl(context):
    bgp_sessions_vrf_lst = ListBGPSessionsVRF(
        list()
    )

    bgp_sessions_lst = ListBGPSessions(
        list()
    )

    bgp_sessions_lst.bgp_sessions.append(
        BGPSession(
            src_hostname="spine02",
            peer_ip="10.1.1.1",
            peer_hostname=NOT_SET,
            remote_as="65101",
            state_brief=get_bgp_state_brief(
                "Idle"
            ),
            session_state="Idle",
            state_time=get_bgp_peer_uptime(
                value="10892000",
                format=BGP_UPTIME_FORMAT_MS
            ),
            prefix_received=NOT_SET
        )
    )

    bgp_sessions_vrf_lst.bgp_sessions_vrf.append(
        BGPSessionsVRF(
            vrf_name="default",
            as_number="65101",
            router_id="2.2.2.2",
            bgp_sessions=bgp_sessions_lst
        )
    )

    bgp_sessions_lst = ListBGPSessions(
        list()
    )

    bgp_sessions_lst.bgp_sessions.append(
        BGPSession(
            src_hostname="spine02",
            peer_ip="10.20.20.2",
            peer_hostname=NOT_SET,
            remote_as="65202",
            state_brief=get_bgp_state_brief(
                "Idle"
            ),
            session_state="Idle",
            state_time=get_bgp_peer_uptime(
                value=0,
                format=BGP_UPTIME_FORMAT_MS
            ),
            prefix_received=NOT_SET
        )
    )

    bgp_sessions_vrf_lst.bgp_sessions_vrf.append(
        BGPSessionsVRF(
            vrf_name="mgmt_vrf",
            as_number="65101",
            router_id="20.20.20.20",
            bgp_sessions=bgp_sessions_lst
        )
    )

    context.o0201 = BGP(
        hostname="spine02",
        bgp_sessions_vrf_lst=bgp_sessions_vrf_lst
    )


@given(u'I create a BGP object from a Extreme VSP API output named o0202')
def step_impl(context):
    print("Extreme VSP BGP with Netconf not possible -> Not tested")


@given(u'I create a BGP object from a Extreme VSP Netconf output named o0203')
def step_impl(context):
    print("Extreme VSP BGP with Netconf not possible -> Not tested")


@given(u'I create a BGP object from a Extreme VSP SSH output named o0204')
def step_impl(context):
    dict_output = dict()
    dict_output['default'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/extreme_vsp/ssh/"
            "extreme_vsp_show_ip_bgp_summary.txt"
        )
    )
    dict_output['mgmt_vrf'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/extreme_vsp/ssh/"
            "extreme_vsp_show_ip_bgp_summary_vrf.txt"
        )
    )
    context.o0204 = _extreme_vsp_bgp_ssh_converter(
        hostname="spine02",
        cmd_output=dict_output,
        options={}
    )


@given(u'I create a BGP object equals to IOS manually named o0301')
def step_impl(context):
    bgp_sessions_vrf_lst = ListBGPSessionsVRF(
        list()
    )

    bgp_sessions_lst = ListBGPSessions(
        list()
    )

    bgp_sessions_lst.bgp_sessions.append(
        BGPSession(
            src_hostname="leaf05",
            peer_ip="33.3.3.3",
            peer_hostname=NOT_SET,
            remote_as="3",
            state_brief=get_bgp_state_brief(
                "Idle"
            ),
            session_state="Idle",
            state_time=get_bgp_peer_uptime(
                value=0,
                format=BGP_UPTIME_FORMAT_MS
            ),
            prefix_received=NOT_SET
        )
    )

    bgp_sessions_lst.bgp_sessions.append(
        BGPSession(
            src_hostname="leaf05",
            peer_ip="33.33.33.33",
            peer_hostname=NOT_SET,
            remote_as="3",
            state_brief=get_bgp_state_brief(
                "Idle"
            ),
            session_state="Idle",
            state_time=get_bgp_peer_uptime(
                value=0,
                format=BGP_UPTIME_FORMAT_MS
            ),
            prefix_received=NOT_SET
        )
    )

    bgp_sessions_vrf_lst.bgp_sessions_vrf.append(
        BGPSessionsVRF(
            vrf_name="CUSTOMER_APPLE",
            as_number="33333",
            router_id="33.33.33.33",
            bgp_sessions=bgp_sessions_lst
        )
    )

    bgp_sessions_lst = ListBGPSessions(
        list()
    )

    bgp_sessions_lst.bgp_sessions.append(
        BGPSession(
            src_hostname="leaf05",
            peer_ip="15.15.15.15",
            peer_hostname=NOT_SET,
            remote_as="15",
            state_brief=get_bgp_state_brief(
                "fsm-idle"
            ),
            session_state="fsm-idle",
            state_time=get_bgp_peer_uptime(
                value=0,
                format=BGP_UPTIME_FORMAT_MS
            ),
            prefix_received=NOT_SET
        )
    )

    bgp_sessions_vrf_lst.bgp_sessions_vrf.append(
        BGPSessionsVRF(
            vrf_name="CUSTOMER_NETESTS",
            as_number="33333",
            router_id="33.33.33.33",
            bgp_sessions=bgp_sessions_lst
        )
    )

    context.o0301 = BGP(
        hostname="leaf05",
        bgp_sessions_vrf_lst=bgp_sessions_vrf_lst
    )


@given(u'I create a BGP object from a IOS API output named o0302')
def step_impl(context):
    dict_output = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/ios/api/"
            "ios_api_get_bgp.json"
        )
    )
    context.o0302 = _ios_bgp_api_converter(
        hostname="leaf05",
        cmd_output=dict_output,
        options={}
    )


@given(u'I create a BGP object from a IOS Netconf named o0303')
def step_impl(context):
    dict_output = open_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/ios/netconf/"
            "ios_nc_get_bgp.xml"
        )
    )
    context.o0303 = _ios_bgp_nc_converter(
        hostname="leaf05",
        cmd_output=dict_output,
        options={}
    )


@given(u'I create a BGP object from a IOS SSH named o0304')
def step_impl(context):
    dict_output = dict()
    dict_output['CUSTOMER_APPLE'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/ios/ssh/"
            "ios_ssh_get_bgp_vrf.txt"
        )
    )
    dict_output['CUSTOMER_NETESTS'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/ios/ssh/"
            "ios_ssh_get_bgp_vrf_2.txt"
        )
    )
    context.o0304 = _ios_bgp_ssh_converter(
        hostname="leaf05",
        cmd_output=dict_output,
        options={}
    )


@given(u'I create a BGP object equals to IOS-XR manually named o0401')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a BGP object from a IOS-XR API output named o0402')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a BGP object from a IOS-XR Netconf output named o0403')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a BGP object from a IOS-XR SSH output named o0404')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a BGP object equals IOS-XR multi manually output named o0405')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a BGP object from a IOS-XR multi Netconf output named o0406')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a BGP object equals to IOS-XR no config manually named o0411')
def step_impl(context):
    context.o0411 = BGP(
        hostname="spine03",
        bgp_sessions_vrf_lst=list()
    )


@given(u'I create a BGP object from a IOS-XR no config API output named o0412')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a BGP object from a IOS-XR no config Netconf output named o0413')
def step_impl(context):
    dict_output = open_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/iosxr/netconf/"
            "iosxr_nc_get_bgp_no_config.xml"
        )
    )
    context.o0413 = _iosxr_bgp_nc_converter(
        hostname="spine03",
        cmd_output=dict_output,
        options={}
    )


@given(u'I create a BGP object from a IOS-XR no config SSH output named o0414')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a BGP object equals to IOS-XR one vrf manually named o0421')
def step_impl(context):
    bgp_sessions_vrf_lst = ListBGPSessionsVRF(
        list()
    )

    bgp_sessions_lst = ListBGPSessions(
        list()
    )

    bgp_sessions_lst.bgp_sessions.append(
        BGPSession(
            src_hostname="spine03",
            peer_ip="15.15.15.15",
            peer_hostname=NOT_SET,
            remote_as="1515",
            state_brief="DOWN",
            session_state="Active",
            state_time=NOT_SET,
            prefix_received=NOT_SET
        )
    )

    bgp_sessions_vrf_lst.bgp_sessions_vrf.append(
        BGPSessionsVRF(
            vrf_name="CUSTOMER_NETESTS",
            as_number="1515",
            router_id="2.2.2.2",
            bgp_sessions=bgp_sessions_lst
        )
    )

    context.o0421 = BGP(
        hostname="spine03",
        bgp_sessions_vrf_lst=bgp_sessions_vrf_lst
    )


@given(u'I create a BGP object from a IOS-XR one vrf config API output named o0422')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a BGP object from a IOS-XR one vrf config Netconf output named o0423')
def step_impl(context):
    dict_output = open_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/iosxr/netconf/"
            "iosxr_nc_get_bgp_one_vrf.xml"
        )
    )
    context.o0423 = _iosxr_bgp_nc_converter(
        hostname="spine03",
        cmd_output=dict_output,
        options={}
    )


@given(u'I create a BGP object from a IOS-XR one vrf config SSH output named o0424')
def step_impl(context):
    dict_output = dict()
    dict_output['default'] = dict()
    dict_output['CUSTOMER_NETESTS'] = dict()

    dict_output['CUSTOMER_NETESTS']['peers'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/iosxr/ssh/"
            "iosxr_cli_get_bgp_peers_vrf.txt"
        )
    )
    dict_output['CUSTOMER_NETESTS']['rid'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/iosxr/ssh/"
            "iosxr_cli_get_bgp_rid_vrf.txt"
        )
    )

    dict_output['default']['peers'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/iosxr/ssh/"
            "iosxr_cli_get_bgp_peers.txt"
        )
    )
    dict_output['default']['rid'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/iosxr/ssh/"
            "iosxr_cli_get_bgp_rid.txt"
        )
    )
    
    context.o0424 = _iosxr_bgp_ssh_converter(
        hostname="spine03",
        cmd_output=dict_output,
        options={}
    )


@given(u'I create a BGP object equals to Juniper manually named o0501')
def step_impl(context):
    bgp_sessions_vrf_lst = ListBGPSessionsVRF(
        list()
    )

    bgp_sessions_lst = ListBGPSessions(
        list()
    )

    bgp_sessions_lst.bgp_sessions.append(
        BGPSession(
            src_hostname="leaf04",
            peer_ip="10.1.1.1",
            peer_hostname=NOT_SET,
            remote_as="65333",
            state_brief=get_bgp_state_brief(
                "Idle"
            ),
            session_state="Idle",
            state_time=NOT_SET,
            prefix_received=NOT_SET
        )
    )

    bgp_sessions_lst.bgp_sessions.append(
        BGPSession(
            src_hostname="leaf04",
            peer_ip="10.2.2.2",
            peer_hostname=NOT_SET,
            remote_as="65333",
            state_brief=get_bgp_state_brief(
                "Idle"
            ),
            session_state="Idle",
            state_time=NOT_SET,
            prefix_received=NOT_SET
        )
    )

    bgp_sessions_vrf_lst.bgp_sessions_vrf.append(
        BGPSessionsVRF(
            vrf_name="CUSTOMER_AWS",
            as_number="65444",
            router_id="9.9.9.9",
            bgp_sessions=bgp_sessions_lst
        )
    )

    context.o0501 = BGP(
        hostname="leaf04",
        bgp_sessions_vrf_lst=bgp_sessions_vrf_lst
    )


@given(u'I create a BGP object from a Juniper API output named o0502')
def step_impl(context):
    dict_output = dict()
    dict_output['default'] = dict()
    dict_output['default']['bgp'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/juniper/api/"
            "juniper_api_get_bgp_peers.xml"
        )
    )
    dict_output['default']['rid'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/juniper/api/"
            "juniper_api_get_bgp_rid.xml"
        )
    )

    dict_output['CUSTOMER_AWS'] = dict()
    dict_output['CUSTOMER_AWS']['bgp'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/juniper/api/"
            "juniper_api_get_bgp_peers_vrf.xml"
        )
    )
    dict_output['CUSTOMER_AWS']['rid'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/juniper/api/"
            "juniper_api_get_bgp_rid_vrf.xml"
        )
    )

    context.o0502 = _juniper_bgp_api_converter(
        hostname="leaf04",
        cmd_output=dict_output,
        options={}
    )


@given(u'I create a BGP object from a Juniper Netconf output named o0503')
def step_impl(context):
    dict_output = dict()
    dict_output['default'] = dict()
    dict_output['default']['bgp'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/juniper/netconf/"
            "juniper_nc_get_bgp_peers.xml"
        )
    )
    dict_output['default']['rid'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/juniper/netconf/"
            "juniper_nc_get_bgp_rid.xml"
        )
    )

    dict_output['CUSTOMER_AWS'] = dict()
    dict_output['CUSTOMER_AWS']['bgp'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/juniper/netconf/"
            "juniper_nc_get_bgp_peers_vrf.xml"
        )
    )
    dict_output['CUSTOMER_AWS']['rid'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/juniper/netconf/"
            "juniper_nc_get_bgp_rid_vrf.xml"
        )
    )

    context.o0503 = _juniper_bgp_nc_converter(
        hostname="leaf04",
        cmd_output=dict_output,
        options={}
    )


@given(u'I create a BGP object from a Juniper SSH output named o0504')
def step_impl(context):
    dict_output = dict()
    dict_output['default'] = dict()
    dict_output['default']['bgp'] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/juniper/ssh/"
            "juniper_cli_get_bgp_peers.json"
        )
    )
    dict_output['default']['rid'] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/juniper/ssh/"
            "juniper_cli_get_bgp_rid.json"
        )
    )

    dict_output['CUSTOMER_AWS'] = dict()
    dict_output['CUSTOMER_AWS']['bgp'] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/juniper/ssh/"
            "juniper_cli_get_bgp_peers_vrf.json"
        )
    )
    dict_output['CUSTOMER_AWS']['rid'] = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/juniper/ssh/"
            "juniper_cli_get_bgp_rid_vrf.json"
        )
    )

    context.o0504 = _juniper_bgp_ssh_converter(
        hostname="leaf04",
        cmd_output=dict_output,
        options={}
    )


@given(u'I create a BGP object equals to NAPALM manually named o0601')
def step_impl(context):
    print("NAPALM BGP doesn't retrieve ROUTER-ID -> Not tested")


@given(u'I create a BGP object from a NAPALM output named o0602')
def step_impl(context):
    cmd_output = open_json_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/napalm/"
            "napalm_get_bgp.json"
        )
    )

    context.o0602 = _napalm_bgp_converter(
        hostname="leaf04",
        cmd_output=cmd_output,
        options={}
    )


@given(u'I create a BGP object equals to NXOS manually named o0701')
def step_impl(context):
    bgp_sessions_vrf_lst = ListBGPSessionsVRF(
        list()
    )

    bgp_sessions_lst = ListBGPSessions(
        list()
    )

    bgp_sessions_lst.bgp_sessions.append(
        BGPSession(
            src_hostname="leaf02",
            peer_ip="172.16.0.2",
            peer_hostname=NOT_SET,
            remote_as="65535",
            state_brief=get_bgp_state_brief(
                "Idle"
            ),
            session_state="Idle",
            state_time=NOT_SET,
            prefix_received=NOT_SET
        )
    )
    bgp_sessions_vrf_lst.bgp_sessions_vrf.append(
        BGPSessionsVRF(
            vrf_name="default",
            as_number="65535",
            router_id="172.16.0.1",
            bgp_sessions=bgp_sessions_lst
        )
    )

    bgp_sessions_lst = ListBGPSessions(
        list()
    )
    bgp_sessions_lst.bgp_sessions.append(
        BGPSession(
            src_hostname="leaf02",
            peer_ip="11.1.1.1",
            peer_hostname=NOT_SET,
            remote_as="1",
            state_brief=get_bgp_state_brief(
                "Idle"
            ),
            session_state="Idle",
            state_time=NOT_SET,
            prefix_received=NOT_SET
        )
    )
    bgp_sessions_lst.bgp_sessions.append(
        BGPSession(
            src_hostname="leaf02",
            peer_ip="22.2.2.2",
            peer_hostname=NOT_SET,
            remote_as="2",
            state_brief=get_bgp_state_brief(
                "Idle"
            ),
            session_state="Idle",
            state_time=NOT_SET,
            prefix_received=NOT_SET
        )
    )

    bgp_sessions_vrf_lst.bgp_sessions_vrf.append(
        BGPSessionsVRF(
            vrf_name="CUSTOMER_GOOGLE",
            as_number="65535",
            router_id="0.0.0.0",
            bgp_sessions=bgp_sessions_lst
        )
    )

    bgp_sessions_lst = ListBGPSessions(
        list()
    )


    context.o0701 = BGP(
        hostname="leaf02",
        bgp_sessions_vrf_lst=bgp_sessions_vrf_lst
    )


@given(u'I create a BGP object from a NXOS API output named o0702')
def step_impl(context):
    dict_output = dict()
    dict_output['default'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/nxos/api/"
            "nxos_api_get_bgp_default.json"
        )
    )
    dict_output['management'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/nxos/api/"
            "nxos_api_get_bgp_vrf_mgmt.json"
        )
    )
    dict_output['CUSTOMER_GOOGLE'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/nxos/api/"
            "nxos_api_get_bgp_vrf_customer.json"
        )
    )
    context.o0702 = _nxos_bgp_api_converter(
        hostname="leaf02",
        cmd_output=dict_output,
        options={}
    )


@given(u'I create a BGP object from a NXOS Netconf output named o0703')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a BGP object from a NXOS SSH output named o0704')
def step_impl(context):
    dict_output = dict()
    dict_output['default'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/nxos/ssh/"
            "nxos_show_bgp_session_vrf_default.json"
        )
    )
    dict_output['management'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/nxos/ssh/"
            "nxos_show_bgp_session_vrf_mgmt.json"
        )
    )
    dict_output['CUSTOMER_GOOGLE'] = open_txt_file(
        path=(
            f"{FEATURES_SRC_PATH}outputs/bgp/nxos/ssh/"
            "nxos_show_bgp_session_vrf_customer.json"
        )
    )
    context.o0704 = _nxos_bgp_ssh_converter(
        hostname="leaf02",
        cmd_output=dict_output,
        options={}
    )


@given(u'BGP o0001 should be equal to o0002')
def step_impl(context):
    assert context.o0001 == context.o0002


@given(u'BGP o0001 should be equal to o0003')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0001 should be equal to o0004')
def step_impl(context):
    assert context.o0001 == context.o0004


@given(u'BGP o0002 should be equal to o0003')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0002 should be equal to o0004')
def step_impl(context):
    assert context.o0002 == context.o0004


@given(u'BGP o0003 should be equal to o0004')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP YAML file should be equal to o0002')
def step_impl(context):
    assert _compare_bgp(
        host_keys=BGP_SESSIONS_HOST_KEY,
        hostname="leaf03",
        groups=['eos'],
        bgp_host_data=context.o0002,
        test=True
    )



@given(u'BGP YAML file should be equal to o0003')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP YAML file should be equal to o0004')
def step_impl(context):
    assert _compare_bgp(
        host_keys=BGP_SESSIONS_HOST_KEY,
        hostname="leaf03",
        groups=['eos'],
        bgp_host_data=context.o0004,
        test=True
    )


@given(u'BGP o0101 should be equal to o0102')
def step_impl(context):
    assert context.o0101 == context.o0102


@given(u'BGP o0101 should be equal to o0103')
def step_impl(context):
    print("Cumulus BGP with Netconf not possible -> Not tested")


@given(u'BGP o0101 should be equal to o0104')
def step_impl(context):
    assert context.o0101 == context.o0102


@given(u'BGP o0102 should be equal to o0103')
def step_impl(context):
    print("Cumulus BGP with Netconf not possible -> Not tested")


@given(u'BGP o0102 should be equal to o0104')
def step_impl(context):
    assert context.o0102 == context.o0104


@given(u'BGP o0103 should be equal to o0104')
def step_impl(context):
    print("Cumulus BGP with Netconf not possible -> Not tested")


@given(u'BGP YAML file should be equal to o0102')
def step_impl(context):
    assert _compare_bgp(
        host_keys=BGP_SESSIONS_HOST_KEY,
        hostname="leaf01",
        groups=['linux'],
        bgp_host_data=context.o0102,
        test=True
    )


@given(u'BGP YAML file should be equal to o0103')
def step_impl(context):
    print("Cumulus BGP with Netconf not possible -> Not tested")


@given(u'BGP YAML file should be equal to o0104')
def step_impl(context):
    assert _compare_bgp(
        host_keys=BGP_SESSIONS_HOST_KEY,
        hostname="leaf01",
        groups=['linux'],
        bgp_host_data=context.o0104,
        test=True
    )


@given(u'BGP o0201 should be equal to o0202')
def step_impl(context):
    print("Extreme VSP BGP with Netconf not possible -> Not tested")


@given(u'BGP o0201 should be equal to o0203')
def step_impl(context):
    print("Extreme VSP BGP with Netconf not possible -> Not tested")


@given(u'BGP o0201 should be equal to o0204')
def step_impl(context):
    assert context.o0201 == context.o0204


@given(u'BGP o0202 should be equal to o0203')
def step_impl(context):
    print("Extreme VSP BGP with Netconf not possible -> Not tested")


@given(u'BGP o0202 should be equal to o0204')
def step_impl(context):
    print("Extreme VSP BGP with Netconf not possible -> Not tested")


@given(u'BGP o0203 should be equal to o0204')
def step_impl(context):
    print("Extreme VSP BGP with Netconf not possible -> Not tested")


@given(u'BGP YAML file should be equal to o0202')
def step_impl(context):
    print("Extreme VSP BGP with Netconf not possible -> Not tested")


@given(u'BGP YAML file should be equal to o0203')
def step_impl(context):
    print("Extreme VSP BGP with Netconf not possible -> Not tested")


@given(u'BGP YAML file should be equal to o0204')
def step_impl(context):
    assert _compare_bgp(
        host_keys=BGP_SESSIONS_HOST_KEY,
        hostname="spine02",
        groups=['extreme_vsp'],
        bgp_host_data=context.o0204,
        test=True
    )

@given(u'BGP o0301 should be equal to o0302')
def step_impl(context):
    assert context.o0301 == context.o0302


@given(u'BGP o0301 should be equal to o0303')
def step_impl(context):
    assert context.o0301 == context.o0303


@given(u'BGP o0301 should be equal to o0304')
def step_impl(context):
    assert context.o0301 == context.o0304


@given(u'BGP o0302 should be equal to o0303')
def step_impl(context):
    assert context.o0302 == context.o0303


@given(u'BGP o0302 should be equal to o0304')
def step_impl(context):
    assert context.o0302 == context.o0304


@given(u'BGP o0303 should be equal to o0304')
def step_impl(context):
    assert context.o0303 == context.o0304


@given(u'BGP YAML file should be equal to o0302')
def step_impl(context):
    assert _compare_bgp(
        host_keys=BGP_SESSIONS_HOST_KEY,
        hostname="leaf05",
        groups=['ios'],
        bgp_host_data=context.o0302,
        test=True
    )


@given(u'BGP YAML file should be equal to o0303')
def step_impl(context):
    assert _compare_bgp(
        host_keys=BGP_SESSIONS_HOST_KEY,
        hostname="leaf05",
        groups=['ios'],
        bgp_host_data=context.o0303,
        test=True
    )


@given(u'BGP YAML file should be equal to o0304')
def step_impl(context):
    assert _compare_bgp(
        host_keys=BGP_SESSIONS_HOST_KEY,
        hostname="leaf05",
        groups=['ios'],
        bgp_host_data=context.o0304,
        test=True
    )


@given(u'BGP o0401 should be equal to o0402')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0401 should be equal to o0403')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0401 should be equal to o0404')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0402 should be equal to o0403')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0402 should be equal to o0404')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0403 should be equal to o0404')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0405 should be equal to o0406')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP YAML file should be equal to o0402')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP YAML file should be equal to o0403')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP YAML file should be equal to o0404')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0411 should be equal to o0412')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0411 should be equal to o0413')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0411 should be equal to o0414')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0412 should be equal to o0413')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0412 should be equal to o0414')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0413 should be equal to o0414')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0421 should be equal to o0422')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0421 should be equal to o0423')
def step_impl(context):
    print("Cisco IOS-XR doesn't get STATE => Not tested")
    #assert context.o0421 == context.o0423


@given(u'BGP o0421 should be equal to o0424')
def step_impl(context):
    assert context.o0421 == context.o0424


@given(u'BGP o0422 should be equal to o0423')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0422 should be equal to o0424')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0423 should be equal to o0424')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0501 should be equal to o0502')
def step_impl(context):
    assert context.o0501 == context.o0502


@given(u'BGP o0501 should be equal to o0503')
def step_impl(context):
    assert context.o0501 == context.o0503


@given(u'BGP o0501 should be equal to o0504')
def step_impl(context):
    assert context.o0501 == context.o0504


@given(u'BGP o0502 should be equal to o0503')
def step_impl(context):
    assert context.o0502 == context.o0503


@given(u'BGP o0502 should be equal to o0504')
def step_impl(context):
    assert context.o0502 == context.o0504


@given(u'BGP o0503 should be equal to o0504')
def step_impl(context):
    assert context.o0503 == context.o0504


@given(u'BGP YAML file should be equal to o0502')
def step_impl(context):
    assert _compare_bgp(
        host_keys=BGP_SESSIONS_HOST_KEY,
        hostname="leaf04",
        groups=['junos'],
        bgp_host_data=context.o0502,
        test=True
    )


@given(u'BGP YAML file should be equal to o0503')
def step_impl(context):
    assert _compare_bgp(
        host_keys=BGP_SESSIONS_HOST_KEY,
        hostname="leaf04",
        groups=['junos'],
        bgp_host_data=context.o0503,
        test=True
    )


@given(u'BGP YAML file should be equal to o0504')
def step_impl(context):
    assert _compare_bgp(
        host_keys=BGP_SESSIONS_HOST_KEY,
        hostname="leaf04",
        groups=['junos'],
        bgp_host_data=context.o0504,
        test=True
    )


@given(u'BGP o0601 should be equal to o0602')
def step_impl(context):
    print("NAPALM BGP doesn't retrieve ROUTER-ID -> Not tested")


@given(u'BGP o0701 should be equal to o0702')
def step_impl(context):
    assert context.o0701 == context.o0702


@given(u'BGP o0701 should be equal to o0703')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0701 should be equal to o0704')
def step_impl(context):
    assert context.o0701 == context.o0704


@given(u'BGP o0702 should be equal to o0703')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP o0702 should be equal to o0704')
def step_impl(context):
    assert context.o0702 == context.o0704


@given(u'BGP o0703 should be equal to o0704')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP YAML file should be equal to o0702')
def step_impl(context):
    assert _compare_bgp(
        host_keys=BGP_SESSIONS_HOST_KEY,
        hostname="leaf02",
        groups=['nxos'],
        bgp_host_data=context.o0702,
        test=True
    )


@given(u'BGP YAML file should be equal to o0703')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'BGP YAML file should be equal to o0704')
def step_impl(context):
    context.scenario.tags.append("own_skipped")


@given(u'I create a BGP object to test compare function named o9999')
def step_impl(context):
    bgp_sessions_vrf_lst = ListBGPSessionsVRF(
        list()
    )

    bgp_sessions_lst = ListBGPSessions(
        list()
    )

    bgp_sessions_lst.bgp_sessions.append(
        BGPSession(
            src_hostname="leaf04",
            peer_ip="10.1.1.1",
            peer_hostname=NOT_SET,
            remote_as="65333",
            state_brief=get_bgp_state_brief(
                "Idle"
            ),
            session_state="Idle",
            state_time=NOT_SET,
            prefix_received=NOT_SET
        )
    )

    bgp_sessions_lst.bgp_sessions.append(
        BGPSession(
            src_hostname="leaf04",
            peer_ip="10.2.2.2",
            peer_hostname=NOT_SET,
            remote_as="65333",
            state_brief=get_bgp_state_brief(
                "Idle"
            ),
            session_state="Idle",
            state_time="12:12",
            prefix_received=123
        )
    )

    bgp_sessions_vrf_lst.bgp_sessions_vrf.append(
        BGPSessionsVRF(
            vrf_name="CUSTOMER_AWS",
            as_number="65444",
            router_id="9.9.9.9",
            bgp_sessions=bgp_sessions_lst
        )
    )

    context.o9999 = BGP(
        hostname="leaf04",
        bgp_sessions_vrf_lst=bgp_sessions_vrf_lst
    )


@given(u'I create a BGP object to test compare function with <session_state> named o9982')
def step_impl(context):
    options = {
        'compare': {
            'session_state': True
        }
    }
    context.o9982 = create_bgp_obj_for_compare(options)


@given(u'I create a BGP object to test compare equal to o9982 without <session_state> named o9983')
def step_impl(context):
    options = {}
    context.o9983 = create_bgp_obj_for_compare(options)


@given(u'I compare BGP o9982 and o9999 with a personal function - should not work')
def step_impl(context):
    assert context.o9982 != context.o9999


@given(u'I compare BGP o9983 and o9999 with a personal function - should work')
def step_impl(context):
    assert context.o9983 == context.o9999


@given(u'I create a BGP object to test compare function with <state_time> named o9984')
def step_impl(context):
    options = {
        'compare': {
            'state_time': True
        }
    }
    context.o9984 = create_bgp_obj_for_compare(options)


@given(u'I create a BGP object to test compare equal to o9984 without <state_time> named o9985')
def step_impl(context):
    options = {}
    context.o9985 = create_bgp_obj_for_compare(options)


@given(u'I compare BGP o9984 and o9999 with a personal function - should not work')
def step_impl(context):
    assert context.o9984 != context.o9999


@given(u'I compare BGP o9985 and o9999 with a personal function - should work')
def step_impl(context):
    assert context.o9985 == context.o9999


@given(u'I create a BGP object to test compare function with <prefix_received> named o9986')
def step_impl(context):
    options = {
        'compare': {
            'prefix_received': True
        }
    }
    context.o9986 = create_bgp_obj_for_compare(options)


@given(u'I create a BGP object to test compare equal to o9986 without <prefix_received> named o9987')
def step_impl(context):
    options = {}
    context.o9987 = create_bgp_obj_for_compare(options)


@given(u'I compare BGP o9986 and o9999 with a personal function - should not work')
def step_impl(context):
    assert context.o9986 != context.o9999


@given(u'I compare BGP o9987 and o9999 with a personal function - should work')
def step_impl(context):
    assert context.o9987 == context.o9999


def create_bgp_obj_for_compare(options):
    bgp_sessions_vrf_lst = ListBGPSessionsVRF(
        list()
    )

    bgp_sessions_lst = ListBGPSessions(
        list()
    )

    bgp_sessions_lst.bgp_sessions.append(
        BGPSession(
            src_hostname="leaf04",
            peer_ip="10.1.1.1",
            peer_hostname=NOT_SET,
            remote_as="65333",
            state_brief=get_bgp_state_brief(
                "Idle"
            ),
            session_state="Idle",
            state_time=NOT_SET,
            prefix_received=NOT_SET,
            options=options
        )
    )

    bgp_sessions_lst.bgp_sessions.append(
        BGPSession(
            src_hostname="leaf04",
            peer_ip="10.2.2.2",
            peer_hostname=NOT_SET,
            remote_as="65333",
            state_brief=get_bgp_state_brief(
                "WRONG_STATE"
            ),
            session_state="UNKNOW_STATE",
            state_time="DJEIOJDOWIEJIW",
            prefix_received="DJOEWDJEWODJEOWIDJ",
            options=options
        )
    )

    bgp_sessions_vrf_lst.bgp_sessions_vrf.append(
        BGPSessionsVRF(
            vrf_name="CUSTOMER_AWS",
            as_number="65444",
            router_id="9.9.9.9",
            bgp_sessions=bgp_sessions_lst
        )
    )

    return BGP(
        hostname="leaf04",
        bgp_sessions_vrf_lst=bgp_sessions_vrf_lst
    )


@given(u'I Finish my BGP tests and list tests not implemented')
def step_impl(context):
    assert _compare_bgp(
        host_keys=BGP_SESSIONS_HOST_KEY,
        hostname="leaf02",
        groups=['nxos'],
        bgp_host_data=context.o0704,
        test=True
    )
