import requests
import json

GITHUB_TOKEN = "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"
HEADERS = {"Authorization": f"token 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"}
URL = "https://api.github.com/repos/vercel/next.js/issues"
PARAMS = {"state": "closed", "labels": "bug", "per_page": 100}

issues = []
for page in range(1, 4):  # Pega até 3 páginas (300 issues no máximo)
    response = requests.get(URL, headers=HEADERS, params={**PARAMS, "page": page})
    issues.extend(response.json())

with open("issues_dump.json", "w") as f:
    json.dump(issues, f, indent=2)
