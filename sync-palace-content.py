#!/usr/bin/env python3
"""
Palace Content Sync — Option B: Copy published notes from vault to content/

Usage:
  python3 sync-palace-content.py

What it does:
  1. Removes ALL symlinks in content/Sunflower Land/
  2. Copies only notes with `publish: true` from vault, preserving directory structure
  3. Single Attachments/ folder at Sunflower Land/ root for all images
  4. Images referenced by notes are copied to Sunflower Land/Attachments/
  5. Handles index.md at Sunflower Land/ root
"""

import os
import re
import shutil
import stat
from pathlib import Path

VAULT = Path(os.path.expanduser(
    "~/Library/Mobile Documents/iCloud~md~obsidian/Documents/EZRP"
))
CONTENT = Path(os.path.expanduser("~/Developer/palace/content"))
SFL_VAULT = VAULT / "05. Resources/01. Sunflower Land"
SFL_CONTENT = CONTENT / "Sunflower Land"
VAULT_ATTACHMENTS = VAULT / "07. Archives/Attachments"
SFL_ATTACHMENTS = SFL_CONTENT / "Attachments"

PUBLISHED_COUNT = 0
SYMLINKS_REMOVED = 0
FILES_COPIED = 0
IMAGES_COPIED = 0

def has_publish_true(filepath: Path) -> bool:
    """Check if a .md file has 'publish: true' in its frontmatter."""
    if not filepath.exists():
        return False
    try:
        content = filepath.read_text(encoding='utf-8', errors='replace')
        if content.startswith('---'):
            end = content.find('---', 3)
            if end > 0:
                frontmatter = content[3:end]
                return 'publish: true' in frontmatter
        return False
    except Exception:
        return False


def remove_symlinks(directory: Path):
    """Recursively remove symlinks in a directory tree."""
    global SYMLINKS_REMOVED
    if not directory.exists():
        return
    for item in directory.iterdir():
        if item.is_symlink():
            item.unlink()
            SYMLINKS_REMOVED += 1
            print(f"  🗑️ Removed symlink: {item.relative_to(CONTENT)}")
        elif item.is_dir():
            if item.name != '.git':
                remove_symlinks(item)


def extract_image_refs(content: str) -> list[str]:
    """Extract image references from markdown content.
    Handles wikilink syntax ![[]] (used in vault).
    Returns list of unique image filenames (basename only)."""
    images = []
    # Wikilink syntax: ![[image.png]]
    wikilinks = re.findall(r'!\[\[([^\]]+\.(?:png|jpg|jpeg|gif|webp))\]\]', content, re.IGNORECASE)
    images.extend(wikilinks)
    # Markdown syntax (already converted): ![alt](../Attachments/image.png)
    markdown_refs = re.findall(r'!\[[^\]]*\]\(([^)]+\.(?:png|jpg|jpeg|gif|webp))\)', content, re.IGNORECASE)
    for ref in markdown_refs:
        images.append(Path(ref).name)
    return list(set(images))  # deduplicate


def convert_wikilinks_to_markdown(content: str, depth: int = 0) -> str:
    """Convert Obsidian wikilink image syntax to markdown relative paths.
    
    Args:
        content: Markdown content
        depth: Depth of the note file from Sunflower Land root
               (0 = root, 1 = Mechanics/, 2 = Mechanics/Sub/, etc.)
    
    Returns:
        Content with wikilinks converted to ![alt](../Attachments/image.png) etc.
    """
    # Determine prefix for relative path
    prefix = '../' * max(1, depth)  # at least one level up to reach root Attachments
    
    def replace_wikilink(match):
        img_name = match.group(1)
        # Remove any path prefix, keep only filename
        img_name = Path(img_name).name
        return f'![{img_name}]({prefix}Attachments/{img_name})'
    
    # Replace ![[image.png]] with markdown relative path
    converted = re.sub(r'!\[\[([^\]]+\.(?:png|jpg|jpeg|gif|webp))\]\]', replace_wikilink, content, flags=re.IGNORECASE)
    return converted


def find_image_in_vault(image_name: str) -> Path | None:
    """Search for image in vault Attachments directory (including subdirs)."""
    src = VAULT_ATTACHMENTS / image_name
    if src.exists():
        return src
    # Search subdirectories
    for subdir in VAULT_ATTACHMENTS.iterdir():
        if subdir.is_dir():
            src = subdir / image_name
            if src.exists():
                return src
    return None


def copy_image_to_sfl_attachments(image_name: str) -> bool:
    """Copy image from vault Attachments to SFL_CONTENT/Attachments/."""
    global IMAGES_COPIED
    
    src = find_image_in_vault(image_name)
    if not src:
        print(f"  ⚠️ Image not found in vault: {image_name}")
        return False
    
    # Destination: single root Attachments folder
    SFL_ATTACHMENTS.mkdir(parents=True, exist_ok=True)
    dest = SFL_ATTACHMENTS / image_name
    
    shutil.copy2(src, dest)
    IMAGES_COPIED += 1
    return True


def copy_published_notes():
    """Copy notes with publish: true from vault to content, preserving structure."""
    global FILES_COPIED
    
    for root, dirs, files in os.walk(SFL_VAULT):
        # Skip unpublished directories
        if '.git' in dirs:
            dirs.remove('.git')
        if '.trash' in dirs:
            dirs.remove('.trash')
            
        for fname in files:
            if not fname.endswith('.md'):
                continue
            
            vault_file = Path(root) / fname
            
            # Only copy published notes
            if not has_publish_true(vault_file):
                continue
            
            # Compute relative path from SFL_VAULT
            rel_path = vault_file.relative_to(SFL_VAULT)
            dest_file = SFL_CONTENT / rel_path
            
            # Calculate depth: number of path components from SFL root
            # e.g., "Mechanics/reputation.md" -> depth=1, "Beginners/foo.md" -> depth=1
            # "Sunflower-Land-MOC.md" -> depth=0
            depth = len(rel_path.parts) - 1
            
            # Create parent directories
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Read content and extract image references (from original wikilinks)
            content = vault_file.read_text(encoding='utf-8')
            image_refs = extract_image_refs(content)
            
            # Convert wikilinks to markdown relative paths for publishing
            converted_content = convert_wikilinks_to_markdown(content, depth)
            
            # Write converted content
            dest_file.write_text(converted_content, encoding='utf-8')
            FILES_COPIED += 1
            
            # Copy referenced images to SFL_CONTENT/Attachments/
            for img in image_refs:
                copy_image_to_sfl_attachments(img)
            
            # Show first few to avoid spam
            if FILES_COPIED <= 5 or FILES_COPIED % 20 == 0:
                print(f"  📄 [{FILES_COPIED}] {rel_path}")


def main():
    global PUBLISHED_COUNT
    
    print("=" * 60)
    print("PALACE CONTENT SYNC")
    print("=" * 60)
    
    # Step 1: Count published notes in vault
    print("\n[1/4] Counting published notes in vault...")
    for root, dirs, files in os.walk(SFL_VAULT):
        if '.git' in dirs:
            dirs.remove('.git')
        if '.trash' in dirs:
            dirs.remove('.trash')
        for fname in files:
            if fname.endswith('.md') and has_publish_true(Path(root) / fname):
                PUBLISHED_COUNT += 1
    print(f"  Found {PUBLISHED_COUNT} published notes in vault")
    
    # Step 2: Remove ALL symlinks in content/Sunflower Land/
    print(f"\n[2/4] Removing symlinks in {SFL_CONTENT}...")
    remove_symlinks(SFL_CONTENT)
    print(f"  Removed {SYMLINKS_REMOVED} symlinks")
    
    # Step 3: Remove existing non-symlink files (clean slate)
    print(f"\n[3/4] Cleaning existing files in content (keeping Attachments)...")
    if SFL_CONTENT.exists():
        for item in SFL_CONTENT.iterdir():
            if item.name == '.DS_Store':
                continue
            if item.name == 'index.md':
                # Keep the SFL index if it exists (it's standalone)
                continue
            if item.is_dir():
                shutil.rmtree(item)
                print(f"  🗑️ Removed dir: {item.relative_to(CONTENT)}")
            elif item.is_file():
                item.unlink()
                print(f"  🗑️ Removed file: {item.relative_to(CONTENT)}")
    
    # Step 4: Copy published notes (and their images)
    print(f"\n[4/4] Copying published notes from vault...")
    copy_published_notes()
    
    # Summary
    print(f"\n{'=' * 60}")
    print("SYNC COMPLETE")
    print(f"  Published notes in vault: {PUBLISHED_COUNT}")
    print(f"  Files copied to content/: {FILES_COPIED}")
    print(f"  Images copied: {IMAGES_COPIED}")
    print(f"  Symlinks removed: {SYMLINKS_REMOVED}")
    print(f"  Content size: {sum(f.stat().st_size for f in SFL_CONTENT.rglob('*.md') if f.is_file()) / 1024:.0f} KB")
    print(f"{'=' * 60}")


if __name__ == '__main__':
    main()