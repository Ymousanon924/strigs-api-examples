# Contributing

Bug reports and small example improvements are welcome. Please describe the API,
expected result, actual result, and a minimal request with all secrets removed.

Do not submit customer data, private endpoint credentials, API keys, webhook
secrets, or copied proprietary API specifications.

## Local validation

Run the same checks used by CI:

```bash
python -m compileall examples/python
node --check examples/javascript/quickstart.mjs
```

Changes to request payloads should include a short explanation of the expected
API response and should use synthetic data only.
