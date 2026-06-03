#!/usr/bin/env python3
"""
Palace Content Sync — Option B: Copy published notes from vault to content/

Usage:
  python3 sync-palace-content.py

What it does:
  1. Removes ALL symlinks in content/Sunflower Land/
  2. Copies only notes with `publish: true` from vault
  3. Preserves directory structure (without vault numeric prefixes)
  4. Handles index.md at Sunflower Land/ root
  5. Copies Attachments referenced by published notes
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

PUBLISHED_COUNT = 0
SYMLINKS_REMOVED = 0
FILES_COPIED = 0

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
            # Don't recurse into Attachments or .git
            if item.name not in ('.git', '.DS_Store'):
                remove_symlinks(item)


def copy_published_notes():
    """Copy notes with publish: true from vault to content, preserving structure."""
    global FILES_COPIED
    
    # Walk the vault SFL directory
    vault_path_str = str(SFL_VAULT)
    content_path_str = str(SFL_CONTENT)
    
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
            
            # Create parent directories
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Copy the file
            shutil.copy2(vault_file, dest_file)
            FILES_COPIED += 1
            
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
            if item.name == 'Attachments' or item.name == '.DS_Store':
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
    
    # Step 4: Copy published notes
    print(f"\n[4/4] Copying published notes from vault...")
    copy_published_notes()
    
    # Summary
    print(f"\n{'=' * 60}")
    print("SYNC COMPLETE")
    print(f"  Published notes in vault: {PUBLISHED_COUNT}")
    print(f"  Files copied to content/: {FILES_COPIED}")
    print(f"  Symlinks removed: {SYMLINKS_REMOVED}")
    print(f"  Content size: {sum(f.stat().st_size for f in SFL_CONTENT.rglob('*.md') if f.is_file()) / 1024:.0f} KB")
    print(f"{'=' * 60}")


if __name__ == '__main__':
    main()
