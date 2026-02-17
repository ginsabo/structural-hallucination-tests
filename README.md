# structural-hallucination-tests
Regression tests for detect# Structural Hallucination Tests for LLMs

A small regression suite for detecting structurally plausible but logically impossible LLM outputs.

Includes:
- Cross-domain causality failures
- Identifier-dependent assertions without primary sources
- Retroactive fee claims without explicit authorization
- Temporal merging (roadmap vs release mismatch)

Run:
python runner/run_tests.py
ing structural hallucinations in LLM outputs.
