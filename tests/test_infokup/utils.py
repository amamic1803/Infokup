import io
import os
import unittest
from unittest.mock import patch


class InfokupTest(unittest.TestCase):
    def run_io_tests(self, script, test_data):
        for input_file in filter(lambda f: ".in." in f, os.listdir(test_data)):
            output_file = input_file.replace(".in.", ".out.")

            with open(os.path.join(test_data, input_file), encoding="UTF-8") as file:
                input_text = file.read()
            with open(os.path.join(test_data, output_file), encoding="UTF-8") as file:
                output_text = file.read()

            with patch('sys.stdin', io.StringIO(input_text)), patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                script.main()
                actual_output = mock_stdout.getvalue()

            self.assertEqual(actual_output, output_text, msg=f"Test failed for input file: {input_file}")
