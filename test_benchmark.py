from pathlib import Path
import unittest

from benchmark import calibration, load_scores, metrics


class BenchmarkTest(unittest.TestCase):
    def test_synthetic_fixture_comparisons(self):
        scores = load_scores(Path(__file__).with_name("synthetic-histograms.csv"))
        observed = {
            name: (row["detected_every"], row["detected_any"], row["false_reject_any_seed"])
            for name, row in scores.items()
        }
        self.assertEqual(observed, {
            "fixed-examples": (3, 4, 0),
            "broader-checks": (4, 6, 0),
            "strict-mix": (5, 6, 2),
        })

    def test_one_intermittent_miss_changes_strict_detection(self):
        row = metrics([0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0])
        self.assertEqual((row["detected_every"], row["detected_any"]), (1, 2))
        self.assertEqual((row["false_accept_any_seed"], row["false_accept_all_seeds"]), (1, 0))
        self.assertEqual(row["false_reject_any_seed"], 1)
        self.assertEqual(row["per_seed_detection"], 0.9)

    def test_calibration_needs_a_valid_alternate_and_a_defect(self):
        self.assertEqual(calibration(), {"reference": (True, True),
                         "valid alternate": (False, True), "known defect": (False, False)})
