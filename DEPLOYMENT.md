# Deployment Checklist

Use this checklist when deploying a new version of unik to PyPI.

## Pre-Release Checklist

- [ ] All tests passing (`pytest tests/`)
- [ ] Code is documented with docstrings
- [ ] README.md is up to date
- [ ] Version number updated in:
  - [ ] `pyproject.toml`
  - [ ] `unik/__init__.py`
- [ ] CHANGELOG updated (if you maintain one)
- [ ] All changes committed to git
- [ ] No uncommitted changes (`git status`)

## Testing Checklist

- [ ] Run tests: `pytest tests/`
- [ ] Build package: `python -m build`
- [ ] Check package: `twine check dist/*`
- [ ] Test install locally: `pip install dist/unik-*.whl`
- [ ] Run example script: `python example.py`

## PyPI Deployment Checklist

### First Time Setup
- [ ] Create PyPI account at https://pypi.org
- [ ] Create TestPyPI account at https://test.pypi.org
- [ ] Generate API tokens for both
- [ ] Configure trusted publishing (optional but recommended)

### Test Deployment (TestPyPI)
- [ ] Clean old builds: `rm -rf dist/ build/ *.egg-info`
- [ ] Build package: `python -m build`
- [ ] Upload to TestPyPI: `twine upload --repository testpypi dist/*`
- [ ] Test install from TestPyPI: `pip install --index-url https://test.pypi.org/simple/ unik`
- [ ] Verify installation works

### Production Deployment (PyPI)
- [ ] Clean old builds: `rm -rf dist/ build/ *.egg-info`
- [ ] Build package: `python -m build`
- [ ] Check package: `twine check dist/*`
- [ ] Upload to PyPI: `twine upload dist/*`
- [ ] Verify on PyPI: https://pypi.org/project/unik/
- [ ] Test install: `pip install unik`

## Post-Release Checklist

- [ ] Create git tag: `git tag v0.1.0`
- [ ] Push tag: `git push origin v0.1.0`
- [ ] Create GitHub release
- [ ] Update documentation if needed
- [ ] Announce release (optional)

## Automated Deployment (GitHub Actions)

If using GitHub Actions (recommended):

1. Configure trusted publishing in PyPI:
   - Go to https://pypi.org/manage/account/publishing/
   - Add GitHub as trusted publisher
   - Fill in: repository owner, name, workflow name, environment (optional)

2. Create a release on GitHub:
   - Go to repository releases
   - Click "Create a new release"
   - Create new tag (e.g., v0.1.0)
   - Add release notes
   - Publish release

3. GitHub Actions will automatically:
   - Run tests
   - Build package
   - Upload to PyPI

## Version Numbering

Follow semantic versioning (semver):
- **MAJOR**: Breaking changes (1.0.0 → 2.0.0)
- **MINOR**: New features, backwards compatible (0.1.0 → 0.2.0)
- **PATCH**: Bug fixes, backwards compatible (0.1.0 → 0.1.1)

## Common Issues

### "Package already exists"
- You cannot replace an existing version on PyPI
- Increment version number and rebuild

### "Invalid credentials"
- Check your PyPI username/token
- Use `__token__` as username with API token
- Configure `.pypirc` file properly

### "Metadata validation failed"
- Run `twine check dist/*` to see errors
- Fix issues in `pyproject.toml`
- Rebuild package

## Resources

- PyPI: https://pypi.org
- TestPyPI: https://test.pypi.org
- Packaging Guide: https://packaging.python.org
- Twine: https://twine.readthedocs.io
- Trusted Publishing: https://docs.pypi.org/trusted-publishers/
