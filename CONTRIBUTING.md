# Contributing to dataweave

## What We're Looking For

We welcome bug fixes, documentation improvements, and new transformation types.

**Before opening a PR:**
- Check if there's an existing issue for your change
- For bug fixes with an existing issue, PRs are welcome directly
- For new features or significant changes, open an issue first to discuss
- For refactoring proposals, open a discussion in GitHub Discussions — we want
  community input before committing to architectural changes

**We are unlikely to accept:**
- Large refactoring PRs without prior discussion and maintainer buy-in
- Changes that rewrite working code for stylistic preferences
- PRs that don't reference an issue or discussion

## Code Style

We use `black` and `ruff`. Run `make lint` before submitting.

## Commit Messages

Use imperative mood: "Add warning for unknown keys", not "Added..."
No prefix convention required.

## Testing

Include tests for new functionality. Run `make test` before submitting.
Use the shared fixtures in `tests/conftest.py` where applicable.

## Changelog

Update `CHANGELOG.md` for any user-facing change under an `[Unreleased]` section.
