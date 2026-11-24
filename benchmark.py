"""Offline replay of a synthetic verdict fixture plus a calibration example."""
import csv
from pathlib import Path


def metrics(defects, accepts):
    return {
        "defects": sum(defects), "acceptable": sum(accepts),
        "detected_every": defects[5], "detected_any": sum(defects[1:]),
        "false_accept_any_seed": sum(defects[:5]), "false_accept_all_seeds": defects[0],
        "false_reject_any_seed": sum(accepts[1:]),
        "per_seed_detection": sum(i * n for i, n in enumerate(defects)) / (5 * sum(defects)),
    }


def load_scores(path):
    counts = {}
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            labels = counts.setdefault(row["method"], {})
            label = row["label"]
            bins = [int(row[str(i)]) for i in range(6)]
            if label not in {"defect", "accept"} or label in labels or min(bins) < 0:
                raise ValueError("Invalid histogram")
            labels[label] = bins
    if not counts:
        raise ValueError("Empty dataset")
    for labels in counts.values():
        if set(labels) != {"defect", "accept"} or sum(labels["defect"]) != 6 or sum(labels["accept"]) != 4:
            raise ValueError("Invalid cohort totals")
    return {name: metrics(labels["defect"], labels["accept"]) for name, labels in counts.items()}


def calibration():
    # The contract permits any item tied for the highest score.
    scores = {"pear": 3, "plum": 3, "apple": 2}
    choices = {"reference": "pear", "valid alternate": "plum", "known defect": "apple"}
    return {case: (choice == "pear", scores[choice] == max(scores.values()))
            for case, choice in choices.items()}


if __name__ == "__main__":
    scores = load_scores(Path(__file__).with_name("synthetic-histograms.csv"))
    print("Synthetic fixture replay (6 defective, 4 acceptable, 5 seeds)")
    print("Method           Detect every/any   False accept ever/always   False reject ever   Seed detection")
    for name, row in scores.items():
        print(f"{name:16} {row['detected_every']:>2}/{row['detected_any']:<12} "
              f"{row['false_accept_any_seed']:>2}/{row['false_accept_all_seeds']:<23} "
              f"{row['false_reject_any_seed']:>2}                 {row['per_seed_detection']:6.1%}")
    print("\nCalibration example (exact check, contract check)")
    for case, verdicts in calibration().items():
        print(f"{case:16} {verdicts}")
