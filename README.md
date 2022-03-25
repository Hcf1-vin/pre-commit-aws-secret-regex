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

## Credit

This project was inspired by the detect-aws-credentials pre-commit hook.

* <https://github.com/pre-commit/pre-commit-hooks/blob/main/pre_commit_hooks/detect_aws_credentials.py>
