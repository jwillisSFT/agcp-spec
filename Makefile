export PYTHONDONTWRITEBYTECODE := 1

PYTHON ?= python3

.PHONY: sync-version check-version validate build-release

sync-version:
	$(PYTHON) governance/sync_release_version.py --write

check-version:
	$(PYTHON) governance/sync_release_version.py --check

validate:
	$(PYTHON) governance/build_release.py --validate-only

build-release:
	$(PYTHON) governance/build_release.py
