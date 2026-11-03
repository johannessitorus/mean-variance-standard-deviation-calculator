"""Run a sample calculation and the included unit tests."""

import pprint
import unittest

from mean_var_std import calculate


if __name__ == "__main__":
    print("Hasil perhitungan untuk [0, 1, 2, 3, 4, 5, 6, 7, 8]:")
    pprint.pprint(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]), sort_dicts=False)
    print("\nMenjalankan unit tests...\n")
    suite = unittest.defaultTestLoader.discover(".", pattern="test_module.py")
    unittest.TextTestRunner(verbosity=2).run(suite)
