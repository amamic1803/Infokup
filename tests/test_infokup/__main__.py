import os
import sys
import unittest


if __name__ == "__main__":
    start_dir = os.path.dirname(__file__)
    suite = unittest.TestLoader().discover(start_dir, pattern='test_*.py')
    runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
    runner.run(suite)
