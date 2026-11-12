# Apple Dictionaries for Mongolian (macOS)

[![License: GPL-3.0-or-later](https://img.shields.io/badge/License-GPLv3--or--later-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-macOS-lightgrey.svg)](https://apple.com)
[![Initiative](https://img.shields.io/badge/Initiative-Mongolian%20Language%20for%20All-brightgreen.svg)](https://tsengel.de)

Native Apple Dictionary bundles (`.dictionary`) designed for macOS, providing instant offline lookups across all Apple applications (Safari, Pages, Mail, Preview, Terminal, and Spotlight).

Part of the **Mongolian Language for All** open-source initiative by [Tsengel](https://tsengel.de).

---

## Included Dictionaries

| Dictionary | Source / Author | Entries | Type | Bundle ID |
| :--- | :--- | :---: | :---: | :--- |
| **English-Mongolian Dictionary** | Dr. Altangerel Damdinsuren | **25,252** | Bilingual (EN &rarr; MN) | `org.tsengel.dictionary.Altangerel-English-Mongolian` |
| **Mongolian Explanatory Dictionary** | Academician Ya. Tsevel | **30,626** | Monolingual (MN &rarr; MN) | `org.tsengel.dictionary.Tsevel-Mongolian-Explanatory` |
| **Total Headwords & Definitions** | | **55,878** | | |

---

## Features

- **Native macOS Deep Integration**:
  - **Three-Finger Tap / Force Click**: Highlight any word in Safari, PDF reader, or Notes to get instant definitions in a popover window.
  - **Spotlight Search**: Press `Cmd + Space` and search Mongolian or English words directly from the macOS desktop without opening any app.
  - **Look Up (`Cmd + Ctrl + D`)**: Global keyboard shortcut lookup across macOS.
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

### Step 1: Download
Download the precompiled `.dictionary.zip` packages from the latest [GitHub Releases](https://github.com/Tsengel-de/apple-dictionary-mongolian/releases):
- `Mongolian-English-Altangerel.dictionary.zip`
- `Mongolian-Tsevel-Explanatory.dictionary.zip`

### Step 2: Copy to Dictionary Folder
1. Unzip the downloaded archives to extract the `.dictionary` bundles:
   - `Mongolian-English-Altangerel.dictionary`
   - `Mongolian-Tsevel-Explanatory.dictionary`
2. Open **Finder**, press `Cmd + Shift + G`, paste:
   ```bash
   ~/Library/Dictionaries/
   ```
   and press Enter.
3. Drag and drop the `.dictionary` folders into `~/Library/Dictionaries/`.

### Step 3: Enable in Dictionary.app
1. Launch **Dictionary.app** (via Spotlight or Applications folder).
2. Open Settings (`Cmd + ,`).
3. Scroll through the list and check the boxes next to:
   - **English-Mongolian Dictionary (Altangerel)**
   - **Монгол хэлний тайлбар толь (Цэвэл)**
4. Drag them to your preferred priority order.

---

## Building from Source

### Prerequisites
- Python 3.10+
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
   pip install pyglossary lxml beautifulsoup4
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

## Repository Structure

```
apple-dictionary-mongolian/
├── .github/
│   └── workflows/
│       └── build-dictionary.yml    # GitHub Actions automated CI/CD for macOS
├── data/
│   ├── altangerel/                 # Dr. Altangerel StarDict source dataset
│   └── tsevel/                     # Ya. Tsevel explanatory dataset
├── src/
│   └── build_dictionary.py         # Converter & XML validator
├── styles/
│   └── Dictionary.css              # Apple Dictionary Retina & Dark Mode styling
├── build/                          # Generated DDK packages
├── LICENSE                         # GNU General Public License v3.0
└── README.md                       # Documentation
```

---

## Credits & Acknowledgements

- **Dr. Altangerel Damdinsuren**: Author of the English-Mongolian Dictionary, open-sourced for the Mongolian people.
- **Academician Ya. Tsevel**: Author of the foundational "Монгол хэлний товч тайлбар толь" (1966, Institute of Language and Literature, Mongolian Academy of Sciences).
- **Ochirkhuyag.L ([@ochko](https://github.com/ochko))**: Digitization and StarDict conversion work.
- **Tsengel ([tsengel.de](https://tsengel.de))**: System integration, Apple DDK packaging, dark mode styling, and ongoing maintenance.

---

## License

This project is licensed under the **GNU General Public License v3.0 (or later)**. See the [LICENSE](LICENSE) file for complete details.

### Commercial Licensing
For commercial redistribution or custom proprietary integration licensing, contact:
`tsengel@tsengel.de` | [tsengel.de](https://tsengel.de)
