import json
import os


def ensure_patch_file_newline(patch_path):
    """
    Normalize a patch file so it is valid for `patch` command:
    - Ensure every line ends with newline (fixes "patch unexpectedly ends in middle of line").
    - Ensure file ends with exactly one newline (required for valid patch format).
    Reference: poly1227-workversion/dgm handles newline when writing; this adds a check before use.
    """
    if not os.path.isfile(patch_path):
        return
    with open(patch_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    if not content.strip():
        return
    # Rebuild so every line is properly terminated (fixes middle-of-line issues)
    lines = content.splitlines()
    normalized = '\n'.join(lines) + '\n'
    if normalized != content:
        with open(patch_path, 'w', encoding='utf-8') as f:
            f.write(normalized)


def read_file(file_path):
    """
    Read a file and return its contents as a string.
    """
    with open(file_path, 'r') as f:
        content = f.read().strip()
    return content

def load_json_file(file_path):
    """
    Load a JSON file and return its contents as a dictionary.
    """
    with open(file_path, 'r') as file:
        return json.load(file)
