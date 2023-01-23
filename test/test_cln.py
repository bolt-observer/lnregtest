import os
import sys
import tempfile
import time
import unittest
import warnings

from lnregtest.lib.network import Network
from lnregtest.lib.network_components import CLN, Bitcoind
from lnregtest.lib.utils import format_dict, dict_comparison
from lnregtest.lib.common import logger_config

import logging.config
logging.config.dictConfig(logger_config)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.handlers[0].setLevel(logging.DEBUG)

test_dir = os.path.dirname(os.path.realpath(__file__))
test_data_dir = os.path.join(test_dir, 'test_data')


class TestCLN(unittest.TestCase):
    def setUp(self) -> None:
        self.test_dir = tempfile.mkdtemp()
        logger.info(f"Testdir: {self.test_dir}")
        self.bitcoind = Bitcoind(self.test_dir)
        node_properties = {
            'port': 9735,
            'base_fee_msat': 10,
            'fee_rate': 0.0001,
        }
        self.cln = CLN('A', node_properties, self.test_dir)

    def test_run(self):
        self.bitcoind.start()
        self.cln.start()
        time.sleep(1)
        self.cln.stop()
        self.bitcoind.stop()

class TestCLNMasterNode(unittest.TestCase):
    def test_network_start(self):
        """
        Each node has a different view of the network, which is why the
        graph has to be assembled from all the nodes via the listchannels
        command.
        """
        graph_fixture = \
            {
                "A": {
                    "1": {
                        "remote_name": "B",
                        "capacity": 4000000,
                        "local_balance": 2105264,
                        "remote_balance": 1894736,
                    },
                    "2": {
                        "remote_name": "C",
                        "capacity": 5000000,
                        "local_balance": 2631579,
                        "remote_balance": 2368421,
                    }
                },
                "B": {
                    "1": {
                        "remote_name": "A",
                        "capacity": 4000000,
                        "local_balance": 1894736,
                        "remote_balance": 2072684,
                    },
                    "3": {
                        "remote_name": "C",
                        "capacity": 100000,
                        "local_balance": 96530,
                        "remote_balance": 0,
                    }
                },
                "C": {
                    "3": {
                        "remote_name": "B",
                        "capacity": 100000,
                        "local_balance": 0,
                        "remote_balance": 96530,
                    },
                    "2": {
                        "remote_name": "A",
                        "capacity": 5000000,
                        "local_balance": 2368421,
                        "remote_balance": 2598999,
                    }
                }
            }

        testnet = Network(
            network_definition_location='star_ring_cln', from_scratch=True,
            node_limit='C')

        # this try-finally construct has to be employed to keep a network
        # running asynchronously, while accessing some of its properties
        try:
            testnet.run_nocleanup()
            graph_dict = testnet.assemble_graph()
            # to create a fixture, convert lower-case bool output to proper
            # python bools:
            logger.info("Complete assembled channel graph:")
            logger.info(format_dict(graph_dict))
            #self.assertTrue(
            #    dict_comparison(graph_dict, graph_fixture, show_diff=True))
        finally:
            testnet.cleanup()
