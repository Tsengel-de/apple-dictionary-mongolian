#!/usr/bin/env bash
# ==============================================================================
# Build Native macOS DMG Installer for Mongolian Dictionaries
# Part of the "Mongolian Language for All" initiative (tsengel.de)
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
DIST_DIR="${REPO_ROOT}/dist"
DMG_STAGE="${REPO_ROOT}/dmg_stage"

mkdir -p "${DIST_DIR}"
rm -rf "${DMG_STAGE}"
mkdir -p "${DMG_STAGE}"

echo "[*] Staging dictionary bundles..."
cp -R "${REPO_ROOT}/build/Mongolian-English-Altangerel/objects/Mongolian-English-Altangerel.dictionary" "${DMG_STAGE}/"
cp -R "${REPO_ROOT}/build/Mongolian-Tsevel-Explanatory/objects/Mongolian-Tsevel-Explanatory.dictionary" "${DMG_STAGE}/"

echo "[*] Adding README.txt..."
cat << 'EOF' > "${DMG_STAGE}/README.txt"
Mongolian Dictionaries for macOS
================================
Dual-Script Suite: Altangerel (EN-MN) & Tsevel (MN-MN)
Part of the "Mongolian Language for All" initiative (https://tsengel.de)

EASY INSTALLATION:
------------------
1. Open Finder, press:
     Cmd + Shift + G
   Type:
     ~/Library/Dictionaries
   and press Enter.

   (If the folder does not exist yet, run 'mkdir -p ~/Library/Dictionaries' in Terminal).

2. Drag both .dictionary bundles from this disk into your ~/Library/Dictionaries/ folder.

3. Open Dictionary.app:
   - Press Cmd + , to open Settings
   - Check the boxes for:
       * English-Mongolian Dictionary (Altangerel)
       * Монгол хэлний тайлбар толь (Цэвэл)
   - Drag to arrange your preferred search priority.

HOW TO USE SYSTEM-WIDE:
-----------------------
- Right-Click on any word in Safari/Notes/Mail -> Select Look Up "..."
- Or place cursor over any word and press: Ctrl + Cmd + D
- Or search in Spotlight (Cmd + Space) directly!

Enjoy! 🇲🇳
EOF

echo "[*] Creating DMG image..."
if command -v hdiutil &>/dev/null; then
    hdiutil create -volname "Mongolian Dictionaries" -srcfolder "${DMG_STAGE}" -ov -format UDZO "${DIST_DIR}/Mongolian-Dictionaries-macOS.dmg"
else
    echo "[-] hdiutil not found (running on non-macOS host). Skipping local DMG creation."
fi
rm -rf "${DMG_STAGE}"

echo "[+] Staging completed successfully."
