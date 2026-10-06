"""Run with: python quickstart.py <product>. Uses only the standard library."""

import json
import os
import sys
import urllib.error
import urllib.request


PRODUCTS = {
    "firmsignaliq-preview": (
        "https://firmsignaliq.strigsapi.com/v1/preview",
        None,
    ),
    "firmsignaliq": (
        "https://firmsignaliq.strigsapi.com/v1/company?domain=openai.com",
        None,
    ),
    "webintel": (
        "https://webintel.strigsapi.com/v1/compare",
        {
            "before_html": "<main><h1>Pro</h1><p>$49/month</p></main>",
            "after_html": "<main><h1>Pro</h1><p>$79/month</p></main>",
            "category": "pricing",
        },
    ),
    "dependsignal": (
        "https://dependsignal.strigsapi.com/v1/compare/json",
        {
            "before": {"customer": {"id": 123, "email": "sample@example.com"}},
            "after": {"customer": {"id": "123"}},
        },
    ),
    "spreadintel": (
        "https://spreadintel.strigsapi.com/v1/formula/generate",
        {"platform": "excel", "instruction": "Sum cells A1 through A10"},
    ),
}


def main() -> None:
    product = sys.argv[1] if len(sys.argv) > 1 else ""
    if product not in PRODUCTS:
        raise SystemExit("Choose one of: " + ", ".join(PRODUCTS))
    api_key = os.environ.get("STRIGS_API_KEY")
    if product != "firmsignaliq-preview" and not api_key:
        raise SystemExit("Set STRIGS_API_KEY before running this example.")

    url, payload = PRODUCTS[product]
    if product == "firmsignaliq-preview":
        if len(sys.argv) < 3:
            raise SystemExit("Usage: python quickstart.py firmsignaliq-preview your-public-domain.com")
        payload = {"domain": sys.argv[2]}
    body = json.dumps(payload).encode() if payload is not None else None
    headers = {"X-API-Key": api_key} if api_key and product != "firmsignaliq-preview" else {}
    if body is not None:
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=body, headers=headers)

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            print(json.dumps(json.load(response), indent=2))
    except urllib.error.HTTPError as error:
        raise SystemExit(f"{error.code}: {error.read().decode()}") from error


if __name__ == "__main__":
    main()
