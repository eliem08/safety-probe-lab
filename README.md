# Safety Probe Lab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eliem08/safety-probe-lab/blob/main/colab.ipynb)

A transparent starter set of probes for uncertainty, evidence sufficiency, privacy, instruction conflict, and calibration.

## Interactive dashboard

    pip install -r requirements.txt
    streamlit run dashboard.py

Run the built-in probe suite, inspect individual responses, and review marker-based triage signals.

## Run the probes

    python probe_eval.py --model-id distilgpt2 --device auto

Exports JSON and CSV with responses, marker matches, and heuristic signals.

## Evaluation design

The probe set is intentionally small and heuristic. Marker matches can miss a good answer or flag a bad one; they are not a validated safety score, certification, or substitute for human review. Add domain-specific examples, adversarial variants, multiple model runs, and independent annotators before using this in a report.

## License

MIT.
