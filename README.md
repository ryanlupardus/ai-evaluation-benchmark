# AI Evaluation Benchmark

An offline replay that shows how evaluator choices affect missed defects and false rejections. The bundled histogram is **synthetic**, with hand-specified verdict counts for ten hypothetical candidates over five seeds. It uses the same replay method as an earlier archived benchmark. The historical dataset, study results and candidate programs are outside this release.

## Synthetic example

| Illustrative strategy | Detected on all five seeds, out of 6 | Detected at least once, out of 6 | Acceptable candidates rejected at least once, out of 4 |
| --- | ---: | ---: | ---: |
| Fixed examples | 3 | 4 | 0 |
| Broader checks | 4 | 6 | 0 |
| Strict mix | 5 | 6 | 2 |

The constructed example shows how stricter detection can increase false rejections. The separate calibration exercise tests a known-valid alternative and a known defect. [Fixture and metric definitions](CASE-STUDY.md)

## Reproduce locally

Run from the repository root with Python 3.10 or later. The replay runs offline using the standard library and [bundled fixture](synthetic-histograms.csv).

```sh
python -B benchmark.py
python -B -m unittest -v
```

The tests check the fixture totals, an intermittent miss and the calibration outcomes. Local verification used Windows with Python 3.10.11 and 3.14.7. GitHub Actions is configured for Windows and Linux with both Python series. [Hosted GitHub Actions CI](https://github.com/ryanlupardus/ai-evaluation-benchmark/actions/runs/45376569344) passed all four jobs on Windows and Linux with Python 3.10 and 3.14.

The portfolio founder commissioned the sample and set the evidence and disclosure requirements. Codex prepared the implementation, fixtures and checks. [Contributions and AI assistance](CONTRIBUTIONS.md)

## Reuse

This portfolio sample carries no open-source license grant.
