# Copyright (c) 2013 Qumulo, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

# XXX: Please add types to the functions in this file. Static type checking in
# Python prevents bugs!
# mypy: ignore-errors


import qumulo.lib.opts
import qumulo.rest.node_state as node_state


class GetNodeState(qumulo.lib.opts.Subcommand):
    NAME = 'node_state_get'
    SYNOPSIS = 'Get the operational state of the node'

    @staticmethod
    def main(conninfo, credentials, _args):
        print(node_state.get_node_state(conninfo, credentials))
