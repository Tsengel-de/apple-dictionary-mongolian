# Apple Dictionaries for Mongolian (macOS)

[![License: GPL-3.0-or-later](https://img.shields.io/badge/License-GPLv3--or--later-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-macOS-lightgrey.svg)](https://apple.com)
[![Initiative](https://img.shields.io/badge/Initiative-Mongolian%20Language%20for%20All-brightgreen.svg)](https://tsengel.de)

Native Apple Dictionary bundles (`.dictionary`) designed for macOS, providing instant offline lookups across all Apple applications (Safari, Pages, Mail, Preview, Terminal, Notes, and Spotlight).

Part of the **Mongolian Language for All** open-source initiative by [Tsengel](https://tsengel.de).

---

## What is this? (Dictionary vs. Translator)

Many users confuse a **Dictionary** with a **Machine Translator**:

| Feature | System Dictionary (This Project) | Machine Translator (Google Translate / NLLB) |
| :--- | :--- | :--- |
| **Purpose** | In-depth meaning, grammar, proverbs, idioms, and usage of words | Translating full sentences and paragraphs from one language to another |
| **Internet Required?** | **No (100% Offline)** — installed directly on your Mac | **Yes** — requires an active internet connection to cloud AI servers |
| **Speed** | **Instant (0.001s)** popover window on selection | 1–3 seconds network latency |
| **macOS Integration** | **Native Deep Integration**: Force-Click, 3-finger Trackpad tap, Spotlight | Separate browser tab or third-party web app |

---

## Real-World Usage on macOS

### 1. Three-Finger Tap / Force Click (Look Up)
When browsing a webpage in Safari, reading a PDF, or reviewing code:
1. Move your cursor over any word (e.g., `horse` or `морь`).
2. **Tap with three fingers on your Trackpad** (or **Force Click**).
3. An elegant popover window appears immediately at your cursor showing the exact translation or explanatory definition without ever leaving your app.

### 2. Spotlight Search (`Cmd + Space`)
1. Press `Cmd + Space` anywhere on your desktop.
2. Type an English or Mongolian word (e.g., `нохой` or `algorithm`).
3. The dictionary definition appears directly in Spotlight search results. Press `Enter` to open it in full view.

### 3. Dedicated Dictionary App (`Dictionary.app`)
Open macOS built-in **Dictionary.app** to browse, search, and bookmark entries like a traditional encyclopedic book.

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
  - Searchable in both Cyrillic and Traditional Mongolian script.
- **Modern San Francisco Typography & Styling**:
  - Customized CSS optimized for Apple Retina displays and macOS San Francisco / PingHei typography.
  - Grammatical part-of-speech badges (`n.`, `v.`, `adj.`, `suff.`).
  - Distinct styling for example sentences, Mongolian idioms, and proverbs (*зүйр цэцэн үг*).
- **Dark Mode Support**:
  - Automatic theme switching matching macOS system appearance (`prefers-color-scheme`).
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
- Node.js 18+ (for script enrichment)
- `pip install pyglossary lxml beautifulsoup4`
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
   This generates the Apple DDK input sources in:
   - `build/Mongolian-English-Altangerel/`
   - `build/Mongolian-Tsevel-Explanatory/`

3. **Compile `.dictionary` bundles (on macOS)**:
   ```bash
   make -C build/Mongolian-English-Altangerel all
   make -C build/Mongolian-Tsevel-Explanatory all
   ```

4. **Install directly into user library**:
   ```bash
   make -C build/Mongolian-English-Altangerel install
   make -C build/Mongolian-Tsevel-Explanatory install
   ```

---

## Credits & Acknowledgements

- **Dr. Altangerel Damdinsuren**: Author of the English-Mongolian Dictionary, open-sourced for the Mongolian people.
- **Academician Ya. Tsevel**: Author of the foundational "Монгол хэлний товч тайлбар толь" (1966, Institute of Language and Literature, Mongolian Academy of Sciences).
- **Ochirkhuyag.L ([@ochko](https://github.com/ochko))**: Digitization and StarDict conversion work.
- **Tsengel ([tsengel.de](https://tsengel.de))**: System architecture, Apple DDK packaging, dark mode styling, and ongoing maintenance.

---

## License

This project is licensed under the **GNU General Public License v3.0 (or later)**. See the [LICENSE](LICENSE) file for complete details.

### Commercial Licensing
For commercial redistribution or custom proprietary integration licensing, contact:
`tsengel@tsengel.de` | [tsengel.de](https://tsengel.de)
