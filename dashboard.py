"""Streamlit dashboard for Safety Probe Lab. Run: streamlit run dashboard.py"""
import streamlit as st
import pandas as pd
from probe_eval import evaluate
st.set_page_config(page_title="Safety Probe Lab",layout="wide")
st.title("Safety Probe Lab")
st.warning("Heuristic markers are triage signals only, not a validated safety score.")
model=st.text_input("Model ID","distilgpt2")
device=st.selectbox("Device",["auto","cuda","mps","cpu"])
tokens=st.slider("Maximum new tokens",32,256,120,step=16)
if st.button("Run probe suite",type="primary"):
    with st.spinner("Evaluating probes…"):
        summary=evaluate(model,device=device,max_new_tokens=tokens)
    st.metric("Probes",summary["probes"])
    st.metric("Marker signals",summary["heuristic_signals"])
    payload=__import__("json").loads(open("outputs/probes/probe-results.json",encoding="utf-8").read())
    st.dataframe(pd.json_normalize(payload["results"])[["id","category","response","marker_count","heuristic_signal"]],use_container_width=True)
    st.json(summary)
