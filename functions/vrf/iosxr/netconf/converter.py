#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from const.constants import (
    NOT_SET,
    LEVEL1,
    LEVEL4
)
from protocols.vrf import (
    VRF,
    ListVRF
)
from functions.global_tools import printline
from functions.verbose_mode import verbose_mode
from functions.netconf_tools import format_xml_output
import pprint
PP = pprint.PrettyPrinter(indent=4)


def _iosxr_vrf_netconf_converter(hostname: str, cmd_output) -> ListVRF:
    if cmd_output.get('VRF') is not None:
        cmd_output['VRF'] = format_xml_output(cmd_output.get('VRF'))
    if cmd_output.get('BGP') is not None:
        cmd_output['BGP'] = format_xml_output(cmd_output.get('BGP'))

    if verbose_mode(
        user_value=os.environ.get("NETESTS_VERBOSE", NOT_SET),
        needed_value=LEVEL4
    ):
        printline()
        print(type(cmd_output))
        PP.pprint(cmd_output)

    vrf_list = ListVRF(vrf_lst=list())

    for v in cmd_output.get('VRF').get('data').get('vrfs').get('vrf'):
        rias = None
        riin = None
        reas = None
        rein = None
        if (
            'afs' in v.keys() and 'af' in v.get('afs').keys() and
            'bgp' in v.get('afs').get('af').keys()
        ):
            rias = v.get('afs').get('af').get('bgp') \
                                         .get('import-route-targets') \
                                         .get('route-targets') \
                                         .get('route-target') \
                                         .get('as-or-four-byte-as') \
                                         .get('as')

            riin = v.get('afs').get('af').get('bgp') \
                                         .get('import-route-targets') \
                                         .get('route-targets') \
                                         .get('route-target') \
                                         .get('as-or-four-byte-as') \
                                         .get('as-index')

            reas = v.get('afs').get('af').get('bgp') \
                                         .get('export-route-targets') \
                                         .get('route-targets') \
                                         .get('route-target') \
                                         .get('as-or-four-byte-as') \
                                         .get('as')

            rein = v.get('afs').get('af').get('bgp') \
                                         .get('export-route-targets') \
                                         .get('route-targets') \
                                         .get('route-target') \
                                         .get('as-or-four-byte-as') \
                                         .get('as-index')

        rd = NOT_SET
        if (
            cmd_output.get('BGP') is not None and
            'data' in cmd_output.get('BGP').keys() and
            'bgp' in cmd_output.get('BGP')
                               .get('data').keys() and
            'instance' in cmd_output.get('BGP')
                                    .get('data')
                                    .get('bgp').keys() and
            'instance-as' in cmd_output.get('BGP')
                                       .get('data')
                                       .get('bgp')
                                       .get('instance').keys() and
            'four-byte-as' in cmd_output.get('BGP')
                                       .get('data')
                                       .get('bgp')
                                       .get('instance')
                                       .get('instance-as').keys() and
            'vrfs' in cmd_output.get('BGP')
                                .get('data')
                                .get('bgp')
                                .get('instance')
                                .get('instance-as')
                                .get('four-byte-as').keys() and
            'vrf' in cmd_output.get('BGP')
                                .get('data')
                                .get('bgp')
                                .get('instance')
                                .get('instance-as')
                                .get('four-byte-as')
                                .get('vrfs').keys()
        ):
            if isinstance(cmd_output.get('BGP')
                                    .get('data')
                                    .get('bgp')
                                    .get('instance')
                                    .get('instance-as')
                                    .get('four-byte-as')
                                    .get('vrfs')
                                    .get('vrf'), dict):
                vrf = cmd_output.get('BGP') \
                                .get('data') \
                                .get('bgp') \
                                .get('instance') \
                                .get('instance-as') \
                                .get('four-byte-as') \
                                .get('vrfs') \
                                .get('vrf')
                if vrf.get('vrf-name') == v.get('vrf-name'):
                    if (
                        'vrf-global' in vrf.keys() and
                        'route-distinguisher' in vrf.get('vrf-global').keys()
                    ):
                        rd = vrf.get('vrf-global') \
                                .get('route-distinguisher') \
                                .get('as') + ":" + \
                            vrf.get('vrf-global') \
                                .get('route-distinguisher') \
                                .get('as-index')

            elif isinstance(cmd_output.get('BGP')
                                      .get('data')
                                      .get('bgp')
                                      .get('instance')
                                      .get('instance-as')
                                      .get('four-byte-as')
                                      .get('vrfs')
                                      .get('vrf'), list):

                for vrf in cmd_output.get('BGP') \
                                     .get('data') \
                                     .get('bgp') \
                                     .get('instance') \
                                     .get('instance-as') \
                                     .get('four-byte-as') \
                                     .get('vrfs') \
                                     .get('vrf'):
                    if vrf.get('vrf-name') == v.get('vrf-name'):
                        if (
                            'vrf-global' in vrf.keys() and
                            'route-distinguisher' in
                            vrf.get('vrf-global').keys()
                        ):
                            rd = vrf.get('vrf-global') \
                                    .get('route-distinguisher') \
                                    .get('as') + ":" + \
                                 vrf.get('vrf-global') \
                                    .get('route-distinguisher') \
                                    .get('as-index')

        vrf_list.vrf_lst.append(
            VRF(
                vrf_name=v.get('vrf-name'),
                vrf_id=NOT_SET,
                vrf_type=NOT_SET,
                l3_vni=NOT_SET,
                rd=rd,
                rt_imp=f"{rias}:{riin}" if rias is not None else NOT_SET,
                rt_exp=f"{reas}:{rein}" if reas is not None else NOT_SET,
                imp_targ=NOT_SET,
                exp_targ=NOT_SET
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
