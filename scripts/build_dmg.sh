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

echo "[*] Creating 1-click Install.command..."
cat << 'EOF' > "${DMG_STAGE}/Install.command"
#!/usr/bin/env bash
DIR="$(cd "$(dirname "$0")" && pwd)"
DEST="$HOME/Library/Dictionaries"
mkdir -p "$DEST"
echo "Installing Mongolian Dictionaries into $DEST..."
cp -R "$DIR"/Mongolian-*.dictionary "$DEST/"
xattr -dr com.apple.quarantine "$DEST"/Mongolian-*.dictionary 2>/dev/null || true
touch "$DEST"
osascript -e 'display dialog "🇲🇳 Монгол толь бичгүүд амжилттай суулаа!\n\nDictionary.app-аа нээгээд Cmd + , (Settings) дотроос идэвхжүүлж ашиглана уу." with title "Mongolian Dictionaries for macOS" buttons {"Ойлголоо"} default button 1 with icon note' 2>/dev/null || echo "Done!"
EOF
chmod +x "${DMG_STAGE}/Install.command"

echo "[*] Creating README.txt..."
cat << 'EOF' > "${DMG_STAGE}/README.txt"
Mongolian Dictionaries for macOS
================================
Part of the "Mongolian Language for All" initiative (tsengel.de)

EASY INSTALLATION:
1. Double-click "Install.command" to install automatically.
   OR: Drag both .dictionary folders into ~/Library/Dictionaries/.
2. Launch Dictionary.app, press Cmd + , (Settings), and enable:
   - English-Mongolian Dictionary (Altangerel)
   - Монгол хэлний тайлбар толь (Цэвэл)
EOF

echo "[*] Creating symlink to Dictionaries..."
ln -s /Library/Dictionaries "${DMG_STAGE}/Drop Dictionaries Here"

echo "[*] Creating DMG image..."
hdiutil create -volname "Mongolian Dictionaries" -srcfolder "${DMG_STAGE}" -ov -format UDZO "${DIST_DIR}/Mongolian-Dictionaries-macOS.dmg"
rm -rf "${DMG_STAGE}"

echo "[+] Successfully created ${DIST_DIR}/Mongolian-Dictionaries-macOS.dmg"
