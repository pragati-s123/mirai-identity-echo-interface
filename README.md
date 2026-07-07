# mirai-identity-echo-interface

# The Signal Vault

A Streamlit assignment for MirAI School of Technology's AI Builder Track (Summer Internship 2026).

## What it does
Collects a user's name and message, validates the inputs on submission, and returns a
personalized confirmation. Includes a bonus token-cost estimator that calculates the
approximate token consumption of the submitted message (using the standard ~4 characters
per token heuristic).

## Features
- Multi-field data collection (name + message)
- Button-gated execution (no processing until "Transmit" is clicked)
- Edge case handling for empty fields (error/warning states)
- Formatted success output using f-strings
- Token count estimator based on message length

## Tech
- Python
- Streamlit

## Run locally
```bash
pip install streamlit
streamlit run app.py
```
