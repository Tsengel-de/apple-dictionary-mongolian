#!/usr/bin/env bash
# ==============================================================================
# Build Native macOS DMG Installer for Mongolian Dictionaries
# Part of the "Mongolian Language for All" initiative (tsengel.de)
# ==============================================================================

set -euo pipefail

DIST_DIR="dist"
DMG_STAGE="dmg_stage"

mkdir -p "${DIST_DIR}"
rm -rf "${DMG_STAGE}"
mkdir -p "${DMG_STAGE}"

echo "[*] Staging dictionary bundles..."
cp -R "build/Mongolian-English-Altangerel/objects/Mongolian-English-Altangerel.dictionary" "${DMG_STAGE}/"
cp -R "build/Mongolian-Tsevel-Explanatory/objects/Mongolian-Tsevel-Explanatory.dictionary" "${DMG_STAGE}/"

echo "[*] Creating symlink to Dictionaries for Drag & Drop..."
ln -s /Library/Dictionaries "${DMG_STAGE}/Dictionaries"

echo "[*] Creating DMG image..."
hdiutil create -volname "Mongolian Dictionaries" -srcfolder "${DMG_STAGE}" -ov -format UDZO "${DIST_DIR}/Mongolian-Dictionaries-macOS.dmg"
rm -rf "${DMG_STAGE}"

echo "[+] Successfully created ${DIST_DIR}/Mongolian-Dictionaries-macOS.dmg"

