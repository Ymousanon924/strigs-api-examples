const product = process.argv[2];
const apiKey = process.env.STRIGS_API_KEY;

if (!apiKey) throw new Error("Set STRIGS_API_KEY before running this example.");

const requests = {
  firmsignaliq: {
    url: "https://firmsignaliq.strigsapi.com/v1/company?domain=openai.com",
    method: "GET",
  },
  webintel: {
    url: "https://webintel.strigsapi.com/v1/compare",
    method: "POST",
    body: {
      before_html: "<main><h1>Pro</h1><p>$49/month</p></main>",
      after_html: "<main><h1>Pro</h1><p>$79/month</p></main>",
      category: "pricing",
    },
  },
  dependsignal: {
    url: "https://dependsignal.strigsapi.com/v1/compare/json",
    method: "POST",
    body: {
      before: { customer: { id: 123, email: "sample@example.com" } },
      after: { customer: { id: "123" } },
    },
  },
  spreadintel: {
    url: "https://spreadintel.strigsapi.com/v1/formula/generate",
    method: "POST",
    body: { platform: "excel", instruction: "Sum cells A1 through A10" },
  },
};

const selected = requests[product];
if (!selected) throw new Error(`Choose one of: ${Object.keys(requests).join(", ")}`);

const response = await fetch(selected.url, {
  method: selected.method,
  headers: {
    "X-API-Key": apiKey,
    ...(selected.body ? { "Content-Type": "application/json" } : {}),
  },
  body: selected.body ? JSON.stringify(selected.body) : undefined,
});

const data = await response.json();
if (!response.ok) throw new Error(`${response.status}: ${JSON.stringify(data)}`);
console.log(JSON.stringify(data, null, 2));
