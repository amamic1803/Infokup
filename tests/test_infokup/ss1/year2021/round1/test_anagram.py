import os
import unittest
from tests.test_infokup.utils import InfokupTest
import infokup.ss1.year2021.round1.anagram as script


class TestScript(InfokupTest):
    def test_script(self):
        self.run_io_tests(script, os.path.join(os.path.dirname(__file__), "test-data", "anagram"))


if __name__ == '__main__':
    unittest.main()
