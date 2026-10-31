"""Study resource loading helpers."""

import json
from pathlib import Path


RESOURCE_FILE = Path(__file__).with_name("resources.json")


def get_resources():
    """Return all study resources from the JSON content file."""
    try:
        with RESOURCE_FILE.open(encoding="utf-8") as file:
            resources = json.load(file)
    except (OSError, json.JSONDecodeError):
        return []
    return resources if isinstance(resources, list) else []


def get_resource_by_slug(slug):
    """Return one resource by slug, or None when it does not exist."""
    return next((resource for resource in get_resources()
                 if resource.get("slug") == slug), None)
