"""Local tests (not the official freeCodeCamp test suite)."""

import unittest

from mean_var_std import calculate


class CalculateTests(unittest.TestCase):
    def setUp(self):
        self.result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_dictionary_keys(self):
        self.assertEqual(
            set(self.result),
            {"mean", "variance", "standard deviation", "max", "min", "sum"},
        )

    def test_mean(self):
        self.assertEqual(self.result["mean"], [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0])

    def test_variance(self):
        self.assertEqual(
            self.result["variance"],
            [[6.0, 6.0, 6.0], [2.0 / 3] * 3, 20.0 / 3],
        )

    def test_standard_deviation(self):
        expected = [[6.0**0.5] * 3, [(2.0 / 3) ** 0.5] * 3, (20.0 / 3) ** 0.5]
        for actual_group, expected_group in zip(self.result["standard deviation"][:2], expected[:2]):
            for actual, wanted in zip(actual_group, expected_group):
                self.assertAlmostEqual(actual, wanted)
        self.assertAlmostEqual(self.result["standard deviation"][2], expected[2])

    def test_max_min_sum(self):
        self.assertEqual(self.result["max"], [[6, 7, 8], [2, 5, 8], 8])
        self.assertEqual(self.result["min"], [[0, 1, 2], [0, 3, 6], 0])
        self.assertEqual(self.result["sum"], [[9, 12, 15], [3, 12, 21], 36])

    def test_output_lists(self):
        for entries in self.result.values():
            self.assertIsInstance(entries, list)
            self.assertIsInstance(entries[0], list)
            self.assertIsInstance(entries[1], list)

    def test_invalid_length(self):
        for bad_data in ([1, 2, 3], list(range(10))):
            with self.subTest(bad_data=bad_data):
                with self.assertRaisesRegex(ValueError, r"^List must contain nine numbers\.$"):
                    calculate(bad_data)


if __name__ == "__main__":
    unittest.main()
