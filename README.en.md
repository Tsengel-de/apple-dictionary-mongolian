# Apple Dictionaries for Mongolian (macOS)

[![License: GPL-3.0-or-later](https://img.shields.io/badge/License-GPLv3--or--later-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-macOS-lightgrey.svg)](https://apple.com)
[![Initiative](https://img.shields.io/badge/Initiative-Mongolian%20Language%20for%20All-brightgreen.svg)](https://tsengel.de)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Support-ff5e5b?logo=ko-fi&logoColor=white)](https://ko-fi.com/tsengel)
[![Author: Tsengel](https://img.shields.io/badge/Author-Tsengel%20(tsengel.de)-red.svg)](https://tsengel.de)

**Languages / Хэл сонгох / Sprachen:** [🇲🇳 Монгол](README.md) • [🇬🇧 English](README.en.md) • [🇩🇪 Deutsch](README.de.md)

Native Apple Dictionary bundles (`.dictionary`) designed for macOS, providing instant offline lookups across all Apple applications (Safari, Pages, Mail, Preview, Terminal, Notes, and Spotlight). Featuring full **Traditional Mongolian Script (ᠮᠣᠩᠭᠣᠯ ᠪᠢᠴᠢᠭ)** and **Classical Latin Galig**.

Part of the **"Mongolian Language for All"** open-source initiative by [Tsengel](https://tsengel.de).

---

## What is this? (Dictionary vs. Machine Translator)

Many users confuse a **Dictionary** with a **Machine Translator**:

| Feature | System Dictionary (This Project) | Machine Translator (Google Translate / NLLB) |
| :--- | :--- | :--- |
| **Purpose** | In-depth word meanings, grammar, proverbs, idioms, and nuances | Translating full sentences and paragraphs between languages |
| **Internet Required?** | **No (100% Offline)** — installed directly on your Mac | **Yes** — requires an active internet connection to cloud AI servers |
| **Speed** | **Instant (0.001s)** popover window on selection | 1–3 seconds network latency |
| **macOS Integration** | **Native Deep Integration**: Right-Click Look Up, Spotlight, Dictionary.app | Separate browser tab or third-party web app |

---

## Included Dictionaries

| Dictionary | Source / Author | Entries | Type | Bundle ID |
| :--- | :--- | :---: | :---: | :--- |
| **English-Mongolian Dictionary** | Dr. Altangerel Damdinsuren | **25,252** | Bilingual (EN &rarr; MN) | `org.tsengel.dictionary.Altangerel-English-Mongolian` |
| **Mongolian Explanatory Dictionary** | Academician Ya. Tsevel | **30,626** | Monolingual (MN &rarr; MN) | `org.tsengel.dictionary.Tsevel-Mongolian-Explanatory` |
| **Dual Script & Galig** | Traditional Script (`ᠮᠣᠩᠭᠣᠯ`) & Classical Latin | Multi-script | Cyrillic + Hudum Bichig | Embedded in Header |
| **Total Headwords & Definitions** | | **55,878+** | | |

---

## Features

- **Dual-Script Presentation (Cyrillic + Traditional Mongolian Script)**:
  - Headwords feature vertical Traditional Script (`ᠮᠣᠷᠢ`) alongside standard Cyrillic (`морь`) and Classical Latin transliteration (*mori*).
  - Searchable in English, Cyrillic, and Traditional Mongolian script.
- **Modern Typography & Styling**:
  - Customized CSS optimized for Apple Retina displays and macOS typography.
  - Grammatical part-of-speech badges (`n.`, `v.`, `adj.`, `suff.`).
  - Distinct styling for example sentences, idioms, and proverbs (*зүйр цэцэн үг*).
- **Dark Mode Support (High Contrast)**:
  - High-contrast color scheme switching dynamically with macOS system appearance (`prefers-color-scheme: dark`).
- **100% Offline & Private**:
  - Zero external network requests, zero telemetry, zero analytics. Runs completely on-device.

---

## Quick Installation

### Method 1: Native Disk Image `.dmg` (Recommended — Drag & Drop)
1. Download **`Mongolian-Dictionaries-macOS.dmg`** from [GitHub Releases](https://github.com/Tsengel-de/apple-dictionary-mongolian/releases) and double-click to mount it.
2. Ensure the destination folder exists on your Mac. If your Mac does not have a `Dictionaries` folder yet (standard on fresh macOS Sonoma / Sequoia / Apple Silicon), run this once in Terminal:
   ```bash
   mkdir -p ~/Library/Dictionaries
   ```
   *(Or in Finder: press `Cmd + Shift + G`, enter `~/Library`, and create a new folder named `Dictionaries`)*.
3. Drag both `.dictionary` bundles into `~/Library/Dictionaries/` (or the `Dictionaries` shortcut in the DMG).

### Method 2: Standalone `.zip` Archives
1. Download `Mongolian-English-Altangerel.dictionary.zip` and `Mongolian-Tsevel-Explanatory.dictionary.zip`.
2. Extract the archives.
3. Copy the extracted `.dictionary` folders into `~/Library/Dictionaries/`:
   ```bash
   mkdir -p ~/Library/Dictionaries
   cp -R Mongolian-*.dictionary ~/Library/Dictionaries/
   ```

### Step 3: Enable in Dictionary.app
1. Launch **Dictionary.app** (via Spotlight or Applications folder).
2. Open Settings (`Cmd + ,`).
3. Scroll through the list and check the boxes next to:
   - **English-Mongolian Dictionary (Altangerel)**
   - **Монгол хэлний тайлбар толь (Цэвэл)**
4. Drag them to your preferred priority order.

---

## How to Use Everywhere on macOS

Once enabled, your Mongolian dictionaries work system-wide across all Mac applications (Safari, Pages, Notes, Mail, Books, Terminal, TextEdit):

### 1. Instant Look Up via Right-Click (Recommended)
1. Select or hover over any word in Safari or any app.
2. **Right-click** and select **Look Up "..."**.
3. A popup window appears instantly! At the bottom of the popup, click on **English-Mongolian (Altangerel)** or **Цэвэл** to view the dual-script definitions.

### 2. Global Keyboard Shortcut
- Place your cursor over any word and press:
  ```text
  Ctrl + Cmd + D
  ```
  The native Apple Dictionary popup will open immediately.

### 3. Trackpad Look Up (Optional)
- Hover over any word and **Tap with 3 fingers** (or **Force Click with 1 finger** if configured in *System Settings $\rightarrow$ Trackpad $\rightarrow$ Point & Click $\rightarrow$ Look up & data detectors*).

### 4. macOS Spotlight Integration
- Press `Cmd + Space` (Spotlight), type any English, Cyrillic, or Traditional Mongolian word (e.g., `морь` or `ᠬᠦᠰᠡᠯ`), and preview definitions directly in Spotlight without opening any app.

---

## Building from Source

### Prerequisites
- Python 3.10+
- Node.js 18+ (for Traditional script generation)
- `pip install -r requirements.txt`
- macOS with Xcode Command Line Tools and Apple Dictionary Development Kit (DDK).

### Build Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Tsengel-de/apple-dictionary-mongolian.git
   cd apple-dictionary-mongolian
   ```

2. **Generate Apple Dictionary XML and assets**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python3 src/build_dictionary.py --dict all
   ```

3. **Compile `.dictionary` bundles & DMG (on macOS)**:
   ```bash
   make -C build/Mongolian-English-Altangerel all
   make -C build/Mongolian-Tsevel-Explanatory all
   bash scripts/build_dmg.sh
   ```

---

## Support & Donation

If you find this project helpful, you can support its ongoing maintenance and infrastructure:

[![Ko-fi](https://img.shields.io/badge/Ko--fi-Support-ff5e5b?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/tsengel)

---

## License & Attribution

- **Source Dictionaries**:
  - *English-Mongolian Dictionary* by Dr. Ch. Altangerel Damdinsuren.
  - *Mongolian Explanatory Dictionary* by Academician Ya. Tsevel.
- **Traditional Script Mapping Engine**: Powered by `@gege-mn/gege-converter`.
- **Software & Styles**: Licensed under the [GNU General Public License v3.0 (GPLv3)](LICENSE). Dual-licensing reservation by Tsengel (tsengel@tsengel.de | [tsengel.de](https://tsengel.de)).

