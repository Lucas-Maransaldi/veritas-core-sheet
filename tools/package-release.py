"""Build the Foundry release assets, including every runtime asset directory."""

import json
from pathlib import Path
import re
import zipfile


def build_release(root, output_dir):
    manifest = json.loads((root / "module.json").read_text(encoding="utf-8"))
    files = {"module.json": root / "module.json", "README.md": root / "README.md"}
    for directory in ("assets", "lang", "scripts", "styles", "templates"):
        folder = root / directory
        if not folder.is_dir():
            raise ValueError(f"Missing runtime directory: {directory}")
        for path in sorted(folder.rglob("*")):
            if path.is_file():
                files[path.relative_to(root).as_posix()] = path

    required = set(manifest.get("esmodules", []))
    required.update(manifest.get("scripts", []))
    required.update(manifest.get("styles", []))
    required.update(language["path"] for language in manifest.get("languages", []))
    asset_pattern = re.compile(
        r'''src=["']modules/''' + re.escape(manifest["id"]) + r'''/([^"']+)["']'''
    )
    for template in (root / "templates").rglob("*.hbs"):
        for asset in asset_pattern.findall(template.read_text(encoding="utf-8")):
            if "{{" not in asset:
                required.add(asset)
    missing = required - files.keys()
    if missing:
        raise ValueError(f"Missing packaged files: {', '.join(sorted(missing))}")

    output_dir.mkdir(parents=True, exist_ok=True)
    archive_path = output_dir / f"{manifest['id']}.zip"
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, path in sorted(files.items()):
            archive.write(path, arcname=name)
    with zipfile.ZipFile(archive_path) as archive:
        if archive.testzip() is not None or set(archive.namelist()) != set(files):
            raise ValueError("Release archive validation failed")
        (output_dir / "module.json").write_bytes(archive.read("module.json"))
    print(f"Built {archive_path} ({len(files)} files), version {manifest['version']}")
    return archive_path


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent.parent
    build_release(project_root, project_root / "dist")
