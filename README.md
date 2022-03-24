# Pre-commit-aws-secret-regex

Git pre-commit hook to search for aws access keys and secrets

```yaml
---
default_stages: ["commit", "push", "manual"]
repos:
  - repo: "https://github.com/Hcf1-vin/pre-commit-aws-secret-regex"
    rev: "0.0.1"
    hooks:
      - id: "aws-secret-regex"
```
