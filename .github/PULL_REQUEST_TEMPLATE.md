---
name: Pull Request Template
about: Create a pull request
title: ''
labels: ''
assignees: ''
---

## Description
Please include a summary of the changes and the related issue. Please also include relevant motivation and context.

Fixes # (issue)

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Refactoring/cleanup

## Testing
Have you tested your changes?

- [ ] Yes, I've added tests for my changes
- [ ] Yes, I've verified existing tests still pass
- [ ] No, tests need to be added
- [ ] Not applicable (documentation changes only)

If yes, please describe the tests you ran:
```bash
# Commands you ran
uv run pytest tests/test_module/
uv run ruff check src/
```

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] I have updated the CHANGELOG.md file
- [ ] I have read the [CONTRIBUTING.md](../../CONTRIBUTING.md) document

## Additional Notes
Add any other context about the PR here.
