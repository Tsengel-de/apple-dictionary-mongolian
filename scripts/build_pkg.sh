#!/usr/bin/env bash
# ==============================================================================
# Build Native Apple .pkg Installer for Mongolian Dictionaries
# Part of the "Mongolian Language for All" initiative (tsengel.de)
# ==============================================================================

set -euo pipefail

DIST_DIR="dist"
PKG_ROOT="pkg_root"

mkdir -p "${DIST_DIR}"
rm -rf "${PKG_ROOT}"
mkdir -p "${PKG_ROOT}/Library/Dictionaries"

echo "[*] Staging dictionary bundles for .pkg..."
cp -R "build/Mongolian-English-Altangerel/objects/Mongolian-English-Altangerel.dictionary" "${PKG_ROOT}/Library/Dictionaries/"
cp -R "build/Mongolian-Tsevel-Explanatory/objects/Mongolian-Tsevel-Explanatory.dictionary" "${PKG_ROOT}/Library/Dictionaries/"

echo "[*] Building native macOS Installer Package (.pkg)..."
pkgbuild --root "${PKG_ROOT}" \
  --identifier "de.tsengel.dictionary.mongolian" \
  --version "1.0.0" \
  --install-location "/" \
  "${DIST_DIR}/Mongolian-Dictionaries-macOS.pkg"

rm -rf "${PKG_ROOT}"

echo "[+] Successfully created ${DIST_DIR}/Mongolian-Dictionaries-macOS.pkg"
