#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from netests.getters.routing_get import GetterRouting
from netests.constants import OSPF_SESSIONS_HOST_KEY
from netests.workers.arista_api import OSPFAristaAPI
from netests.workers.arista_ssh import OSPFAristaSSH
from netests.workers.cumulus_api import OSPFCumulusAPI
from netests.workers.cumulus_nc import CumulusNC
from netests.workers.cumulus_ssh import OSPFCumulusSSH

HEADER = "[netests - get_ospf]"


class GetterOSPF(GetterRouting):

    def __init__(
        self,
        nr,
        options,
        from_cli,
        num_workers,
        verbose,
        print_task_output
    ):
        super().__init__(
            nr,
            options,
            from_cli,
            num_workers,
            verbose,
            print_task_output
        )
        self.init_mapping_function()

    def run(self):
        self.get_vrf()
        self.devices.run(
            task=self.generic_get,
            on_failed=True,
            num_workers=self.num_workers
        )
        self.print_result()

    def print_result(self):
        self.print_protocols_result(OSPF_SESSIONS_HOST_KEY, "OSPF")

    def init_mapping_function(self):
        self.MAPPING_FUNCTION = {
            self.ARISTA_PLATEFORM_NAME: {
                self.API_CONNECTION: OSPFAristaAPI,
                self.NETCONF_CONNECTION: "pass",
                self.SSH_CONNECTION: OSPFAristaSSH,
                self.NAPALM_CONNECTION: self.device_not_compatible_with_napalm
            },
            self.CUMULUS_PLATEFORM_NAME: {
                self.API_CONNECTION: OSPFCumulusAPI,
                self.NETCONF_CONNECTION: CumulusNC,
                self.SSH_CONNECTION: OSPFCumulusSSH,
                self.NAPALM_CONNECTION: self.device_not_compatible_with_napalm
            }
        }
