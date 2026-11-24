# Reading an evaluator replay

The CSV represents outcomes as histograms. Each strategy has a row for defective candidates and one for acceptable candidates. Columns `0` through `5` indicate how many seeds rejected a candidate. For example, `fixed-examples` gives one defect one rejection and three defects five rejections each. Two defects receive zero rejections.

- **Every-seed detection** counts defects rejected on all five seeds. **Any-seed detection** counts defects rejected at least once.
- **False acceptance** counts defects accepted on one or more seeds. The script separately counts defects accepted on all five seeds. **False rejection** counts acceptable candidates rejected at least once.
- **Seed detection** divides the number of defect rejections by 30 opportunities, using six defects across five seeds.

The labels, strategy names and counts are constructed for illustration. The scripts summarize the saved fixture and exercise a calibration example. The example cannot measure the performance of actual evaluators, estimate uncertainty across candidates or establish cross-model generalization.

The calibration example allows either item tied for the highest score. The exact-answer check accepts the reference option. The contract check accepts both tied choices and rejects a lower-scoring one.
