import os
import unittest
from tests.test_infokup.utils import InfokupTest
import infokup.ss1.year2020.round1.hb as script


class TestScript(InfokupTest):
    def test_script(self):
        self.run_io_tests(script, os.path.join(os.path.dirname(__file__), "test-data", "hb"))


if __name__ == '__main__':
    unittest.main()
