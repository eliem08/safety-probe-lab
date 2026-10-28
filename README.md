# Safety Probe Lab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eliem08/safety-probe-lab/blob/main/colab.ipynb)

A transparent starter set of probes for uncertainty, evidence sufficiency, privacy, instruction conflict, and calibration.

## Run the probes

    pip install -r requirements.txt
    python probe_eval.py --model-id distilgpt2

Exports outputs/probes/probe-results.json and .csv, including model responses, marker matches, and a triage signal. Use --device cuda for a GPU or --device auto to choose available hardware.

## Evaluation design

The probe set is intentionally small and heuristic. Marker matches can miss a good answer or flag a bad one; they are not a validated safety score, certification, or substitute for human review. Add domain-specific examples, adversarial variants, multiple model runs, and independent annotators before using this in a report.

## Quickstart

    python main.py

The original demo uses random weights only to validate the code path. Use a pretrained model for meaningful qualitative review.

## License

MIT.
