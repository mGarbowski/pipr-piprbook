"""Utility functions for importing resource files"""

from pathlib import Path


def _resources_dir() -> Path:
    """Get directory of resources directory"""
    return Path(__file__).resolve().parent


def get_placeholder_picture() -> bytes:
    """Get binary data of placeholder profile picture"""
    resources_dir = _resources_dir()
    placeholder_path = resources_dir / "profile-picture-placeholder.png"
    with open(placeholder_path, mode="rb") as placeholder_picture:
        return placeholder_picture.read()
