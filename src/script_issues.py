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
