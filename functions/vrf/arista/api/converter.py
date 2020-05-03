#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from const.constants import NOT_SET, LEVEL1, LEVEL3
from protocols.vrf import VRF, ListVRF
from functions.global_tools import printline
from functions.verbose_mode import verbose_mode
import pprint
PP = pprint.PrettyPrinter(indent=4)


def _arista_vrf_api_converter(
    hostname: str(),
    cmd_output,
    options={}
) -> ListVRF:

    if not isinstance(cmd_output['result'][0], dict):
        cmd_output = json.loads(cmd_output['result'][0])
    else:
        cmd_output = cmd_output['result'][0]

    if verbose_mode(
        user_value=os.environ.get("NETESTS_VERBOSE", NOT_SET),
        needed_value=LEVEL3
    ):
        printline()
        print(cmd_output)

    vrf_list = ListVRF(list())
    for vrf_name, facts in cmd_output.get('vrfs').items():
        if (
            facts.get('routeDistinguisher', NOT_SET) == NOT_SET or
            facts.get('routeDistinguisher', NOT_SET) == ''
        ):
            rd = NOT_SET
        else:
            rd = facts.get('routeDistinguisher', NOT_SET)

        vrf_list.vrf_lst.append(
            VRF(
                vrf_name=vrf_name,
                vrf_id=NOT_SET,
                vrf_type=NOT_SET,
                l3_vni=NOT_SET,
                rd=rd,
                rt_imp=NOT_SET,
                rt_exp=NOT_SET,
                imp_targ=NOT_SET,
                exp_targ=NOT_SET,
                options=options
            )
        )

    if verbose_mode(
        user_value=os.environ.get("NETESTS_VERBOSE", NOT_SET),
        needed_value=LEVEL1
    ):
        printline()
        print(f">>>>> {hostname}")
        PP.pprint(vrf_list.to_json())

    return vrf_list
