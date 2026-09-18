# Strigs API examples

Runnable examples for the four Strigs API products. Each API returns structured
JSON, exposes an OpenAPI document, and has a no-key health or demo endpoint.

| Product | Job | Documentation | No-key demo |
| --- | --- | --- | --- |
| [FirmSignalIQ](https://firmsignaliq.strigsapi.com/) | Turn a company domain into sourced website and technology signals | [OpenAPI](https://firmsignaliq.strigsapi.com/openapi.json) | [Health](https://firmsignaliq.strigsapi.com/health) |
| [WebIntel](https://webintel.strigsapi.com/) | Turn meaningful website changes into structured events | [OpenAPI](https://webintel.strigsapi.com/openapi.json) | [Demo](https://webintel.strigsapi.com/v1/demo) |
| [DependSignal](https://dependsignal.strigsapi.com/) | Detect API failures, response drift, and supported contract changes | [OpenAPI](https://dependsignal.strigsapi.com/openapi.json) | [Demo](https://dependsignal.strigsapi.com/v1/demo) |
| [SpreadIntel](https://spreadintel.strigsapi.com/) | Generate, repair, explain, and translate spreadsheet formulas | [OpenAPI](https://spreadintel.strigsapi.com/openapi.json) | [Health](https://spreadintel.strigsapi.com/health) |

## Quick start

Set one product-specific key. Keys are deliberately read from environment
variables and must never be committed.

```bash
export STRIGS_API_KEY="your-key"
python examples/python/quickstart.py firmsignaliq
node examples/javascript/quickstart.mjs webintel
```

Supported example names are `firmsignaliq`, `webintel`, `dependsignal`, and
`spreadintel`.

## DependSignal in CI

[`depend-signal.yml`](examples/github-actions/depend-signal.yml) is a reusable
starting point for comparing an OpenAPI document against an approved baseline.
Store the API key as the repository secret `DEPENDSIGNAL_API_KEY`.

DependSignal reports a documented OpenAPI 3.x rule subset. A reported difference
should be reviewed in context; it is not a universal compatibility guarantee.

## Product boundaries

- FirmSignalIQ observes public company websites and DNS. It does not provide
  employee counts, funding data, or personal contacts.
- WebIntel analyzes static public HTML and does not bypass access challenges.
- DependSignal probes public HTTPS endpoints without target credentials.
- SpreadIntel returns validated spreadsheet logic, but callers should test
  formulas against their own workbook structure and spreadsheet version.

For support, open an issue in this repository or email
`ray.finesse@outlook.com`.

## Security

Do not include customer data, API keys, private endpoint credentials, or webhook
secrets in an issue. Report sensitive security matters privately by email.

## License

The example code in this repository is available under the MIT License. The
hosted APIs and their output remain subject to the terms published on each
product site.
