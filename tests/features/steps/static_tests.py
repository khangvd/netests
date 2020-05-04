#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import yaml
import textfsm
from behave import given, when, then
from const.constants import (
    STATIC_DATA_HOST_KEY,
    FEATURES_SRC_PATH,
    FEATURES_OUTPUT_PATH
)
from functions.static.static_converters import _arista_static_converter, _juniper_static_converter
from functions.static.static_compare import _compare_static
from protocols.static import ListNexthop, Nexthop, ListStatic, Static
from functions.global_tools import open_file
    

@given(u'I create a Static python object manually named object_01')
def create_a_static_object_manually(context) -> None:
    """
    Create a Static object manually

    :param context:
    :return None:
    """

    static_routes_lst = ListStatic(
        static_routes_lst=list()
    )

    #
    ## 1st Object
    #
    nexthop_lst = ListNexthop(
        list()
    )

    nexthop_lst.nexthops_lst.append(
        Nexthop(
            ip_address='10.22.33.1',
            is_in_fib=True,
            out_interface='eth1/3',
            preference='1',
            metric='0',
            active=True
        )
    )

    static_routes_lst.static_routes_lst.append(
        Static(
            vrf_name='default',
            prefix='10.255.255.202',
            netmask='255.255.255.255',
            nexthop=nexthop_lst
        )
    )

    #
    ## 2nd Object
    #
    nexthop_lst = ListNexthop(
        list()
    )

    nexthop_lst.nexthops_lst.append(
        Nexthop(
            ip_address='10.1.3.1',
            is_in_fib=True,
            out_interface='eth1/1',
            preference='1',
            metric='0',
            active=True
        )
    )

    static_routes_lst.static_routes_lst.append(
        Static(
            vrf_name='default',
            prefix='10.255.255.101',
            netmask='255.255.255.255',
            nexthop=nexthop_lst
        )
    )

    #
    ## 3rd Object
    #
    nexthop_lst = ListNexthop(
        list()
    )

    nexthop_lst.nexthops_lst.append(Nexthop(
            ip_address='10.0.5.1',
            is_in_fib=True,
            out_interface='mgmt1',
            preference='1',
            metric='0',
            active=True
        )
    )

    static_routes_lst.static_routes_lst.append(
        Static(
            vrf_name='mgmt',
            prefix='0.0.0.0',
            netmask='0.0.0.0',
            nexthop=nexthop_lst
        )
    )

    context.object_01 = static_routes_lst


@given('I retrieve data from a YAML file corresponding to devices to create an Static python object named object_02')
def create_a_static_object_from_a_json(context) -> None:
    """
    Retrieve data from a YAML file to compare with a Static object

    :param context:
    :return None:
    """

    yaml_content = open_file(
        path=f"{FEATURES_SRC_PATH}static_tests.yml"
    )

    context.object_02 = yaml_content


@given('I create a Static python object from a Arista output command named object_03')
def create_a_static_object_from_a_arista_output_command(context) -> None:
    """
    Create a Static object from a Arista output

    :param context:
    :return None:
    """

    cmd_outputs = list()

    cmd_outputs.append(
        open_file(
            path=f"{FEATURES_OUTPUT_PATH}arista_show_ip_route_static_default.json"
        )
    )

    cmd_outputs.append(
        open_file(
            path=f"{FEATURES_OUTPUT_PATH}arista_show_ip_route_static_mgmt.json"
        )
    )

    context.object_03 = _arista_static_converter(
        hostname="leaf03",
        cmd_outputs=cmd_outputs
    )


@given('I create a Static python object from a Juniper output command named object_04')
def create_a_static_object_from_a_juniper_output_command(context) -> None:
    """
    Create a Static object from a Arista output

    :param context:
    :return None:
    """

    cmd_outputs = open_file(
        path=f"{FEATURES_OUTPUT_PATH}juniper_show_route_protocol_static.json"
    )

    context.object_04 = _juniper_static_converter(
        hostname="leaf04",
        cmd_outputs=cmd_outputs
    )


@then('Static object_01 should be equal to object_02')
def step_impl(context) -> None:
    """
    Compare object_01 and object_02

    :param context:
    :return:
    """
    assert _compare_static(
        host_keys=STATIC_DATA_HOST_KEY,
        hostname="leaf03",
        groups=['eos'],
        static_host_data=context.object_01,
        test=True,
        own_vars={},
        task=None
    )


@then('Static object_01 should be equal to object_03')
def compare_static_object_01_and_object_03(context) -> None:
    """
    Compare object_01 and object_03

    :param context:
    :return:
    """
    assert context.object_01 == context.object_03


@then('Static object_02 should be equal to object_03')
def step_impl(context) -> None:
    """
    Compare object_02 and object_03

    :param context:
    :return:
    """
    assert _compare_static(
        host_keys=STATIC_DATA_HOST_KEY,
        hostname="leaf03",
        groups=['eos'],
        static_host_data=context.object_03,
        test=True,
        own_vars={},
        task=None
    )


@then('Static object_02 should be equal to object_04')
def step_impl(context) -> None:
    """
    Compare object_02 and object_04

    :param context:
    :return:
    """
    assert _compare_static(
        host_keys=STATIC_DATA_HOST_KEY,
        hostname="leaf03",
        groups=['junos'],
        static_host_data=context.object_03,
        test=True,
        own_vars={},
        task=None
    )


@then('Static object_03 should not be equal to object_04')
def step_impl(context) -> None:
    """
    Compare object_03 and object_04

    :param context:
    :return:
    """
    assert context.object_03 != context.object_04