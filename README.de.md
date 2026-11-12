# 🇲🇳 Apple-Wörterbücher für Mongolisch (macOS)
### Dual-Script Mongolische Apple Dictionaries (Altangerel & Tsevel)

[![License: GPL-3.0-or-later](https://img.shields.io/badge/License-GPLv3--or--later-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-macOS-lightgrey.svg)](https://apple.com)
[![Initiative](https://img.shields.io/badge/Initiative-Mongolian%20Language%20for%20All-brightgreen.svg)](https://tsengel.de)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Support-ff5e5b?logo=ko-fi&logoColor=white)](https://ko-fi.com/tsengel)
[![Author: Tsengel](https://img.shields.io/badge/Author-Tsengel%20(tsengel.de)-red.svg)](https://tsengel.de)

**Sprachen / Languages / Хэл сонгох:** [🇲🇳 Монгол](README.md) • [🇬🇧 English](README.en.md) • [🇩🇪 Deutsch](README.de.md)

Native Apple Dictionary-Pakete (`.dictionary`) für macOS für blitzschnelle Offline-Wortsuche in allen Apple-Programmen (Safari, Pages, Mail, Vorschau, Terminal, Notizen und Spotlight). Mit vollständiger Unterstützung der **klassischen mongolischen Schrift (ᠮᠣᠩᠭᠣᠯ ᠪᠢᠴᠢᠭ - Hudum)** und **lateinischer Transliteration (Galig)**.

Teil der Open-Source-Initiative **„Mongolische Sprache für alle“** von [Tsengel](https://tsengel.de).

---

## Wörterbuch vs. Maschinelle Übersetzung

Viele Benutzer verwechseln ein systemweites **Wörterbuch** mit einem **Übersetzungsprogramm** (wie Google Translate / DeepL):

| Merkmal | Systemwörterbuch (Dieses Projekt) | Maschinelle Übersetzung (Google / DeepL) |
| :--- | :--- | :--- |
| **Zweck** | Fundierte Wortbedeutungen, Grammatik, Sprichwörter, Redewendungen und Etymologie | Übersetzung ganzer Sätze und Absätze |
| **Internet erforderlich?** | **Nein (100% Offline)** — direkt lokal auf Ihrem Mac installiert | **Ja** — erfordert permanente Serververbindung |
| **Geschwindigkeit** | **Sofort (0,001 Sek.)** beim Anklicken | 1–3 Sekunden Netzwerklatenz |
| **macOS-Integration** | **Nahtlos integriert**: Rechtsklick-Nachschlagen, Spotlight, Lexikon.app | Separater Browser-Tab oder Drittanbieter-Webseite |

---

## Enthaltene Wörterbücher

| Wörterbuch | Autor / Quelle | Einträge | Typ | Bundle-ID |
| :--- | :--- | :---: | :---: | :--- |
| **Englisch-Mongolisches Wörterbuch** | Dr. Ch. Altangerel Damdinsuren | **25.252** | Zweisprachig (EN &rarr; MN) | `org.tsengel.dictionary.Altangerel-English-Mongolian` |
| **Mongolisches Erklärungswörterbuch** | Akad. Ya. Tsevel | **30.626** | Einsprachig (MN &rarr; MN) | `org.tsengel.dictionary.Tsevel-Mongolian-Explanatory` |
| **Klassische Schrift & Galig** | Mongolische Schrift (`ᠮᠣᠩᠭᠣᠯ`) & Lateinisches Galig | Mehrschriftig | Kyrillisch + Hudum-Schrift | Direkt in jedem Kopfeintrag |
| **Gesamteinträge & Erklärungen** | | **55.878+** | | |

---

## Hauptmerkmale

- **Dual-Script-Darstellung (Kyrillisch + Klassische Mongolische Schrift)**:
  - Jeder Eintrag zeigt die klassische vertikale mongolische Schrift (`ᠮᠣᠷᠢ`) neben dem Standardkyrillischen (`морь`) und der wissenschaftlichen lateinischen Transliteration (*mori*).
  - Bidirektionale Suche in Englisch, Kyrillisch und klassischer mongolischer Schrift.
- **Modernes Retina-Design & San Francisco Typografie**:
  - Maßgeschneidertes CSS, optimiert für Apple Retina-Displays und Apple Systemschriften.
  - Wortart-Badges (`n.`, `v.`, `adj.`, `suff.`).
  - Eigene Formatierung für Beispielsätze, Sprichwörter und Redewendungen (*зүйр цэцэн үг*).
- **Dunkelmodus mit hohem Kontrast (High-Contrast Dark Mode)**:
  - Passt sich automatisch dem macOS-Erscheinungsbild an (`prefers-color-scheme: dark`) und garantiert kristallklare Lesbarkeit auf dunklem Hintergrund.
- **100% Sicher & Datenschutzkonform**:
  - Keine externen Netzwerkaufrufe, keine Telemetrie, keine Analyse. Läuft vollständig lokal auf Ihrem Mac.

---

## Schnelle Installation

### Methode 1: Natives DMG-Image (Empfohlen — Drag & Drop)
1. Laden Sie **`Mongolian-Dictionaries-macOS.dmg`** aus den [GitHub Releases](https://github.com/Tsengel-de/apple-dictionary-mongolian/releases) herunter und öffnen Sie es per Doppelklick.
2. Stellen Sie sicher, dass der Zielordner auf Ihrem Mac existiert (auf neuen Macs mit Apple Silicon M1/M2/M3/M4 bzw. macOS Sonoma/Sequoia existiert dieser Ordner standardmäßig noch nicht). Führen Sie einmalig im Terminal aus:
   ```bash
   mkdir -p ~/Library/Dictionaries
   ```
   *(Oder im Finder: `Cmd + Shift + G` drücken, `~/Library` eingeben und einen neuen Ordner namens `Dictionaries` anlegen)*.
3. Ziehen Sie beide `.dictionary`-Pakete per Drag & Drop in den Ordner **`~/Library/Dictionaries/`** (oder auf die Verknüpfung im DMG).

### Methode 2: ZIP-Archive
1. Laden Sie `Mongolian-English-Altangerel.dictionary.zip` und `Mongolian-Tsevel-Explanatory.dictionary.zip` herunter.
2. Entpacken Sie die Archive.
3. Kopieren Sie die extrahierten `.dictionary`-Ordner in `~/Library/Dictionaries/`:
   ```bash
   mkdir -p ~/Library/Dictionaries
   cp -R Mongolian-*.dictionary ~/Library/Dictionaries/
   ```

### Aktivierung in der Lexikon-App (Dictionary.app):
1. Starten Sie **Lexikon.app** (Dictionary.app) über Spotlight oder den Programme-Ordner.
2. Öffnen Sie die Einstellungen mit **`Cmd + ,`**.
3. Aktivieren Sie die beiden mongolischen Wörterbücher durch Anhaken:
   - ☑️ **English-Mongolian Dictionary (Altangerel)**
   - ☑️ **Монгол хэлний тайлбар толь (Цэвэл)**
4. Ziehen Sie die Wörterbücher in der Liste an die gewünschte Position für die Suchpriorität.

---

## Verwendung unter macOS

Sobald aktiviert, stehen Ihnen die Wörterbücher systemweit in allen Mac-Apps zur Verfügung (Safari, Pages, Notizen, Mail, Vorschau, Terminal, TextEdit):

### 1. Nachschlagen per Rechtsklick (Empfohlen)
1. Markieren Sie ein beliebiges Wort in Safari oder einer anderen App.
2. Klicken Sie mit der **rechten Maustaste (Rechtsklick)** und wählen Sie **„... nachschlagen“**.
3. Ein Popover-Fenster öffnet sich sofort! Klicken Sie unten im Fenster auf **English-Mongolian** oder **Цэвэл**, um zwischen den Wörterbüchern zu wechseln.

### 2. Globaler Tastatur-Kurzbefehl
- Platzieren Sie den Mauszeiger über einem Wort und drücken Sie:
  ```text
  Ctrl + Cmd + D
  ```
  Das macOS-Wörterbuchfenster öffnet sich augenblicklich.

### 3. Trackpad-Geste (Optional)
- Bewegen Sie den Zeiger über ein Wort und **tippen Sie mit 3 Fingern** (oder **kräftig drücken / Force Click**, einstellbar unter *Systemeinstellungen $\rightarrow$ Trackpad $\rightarrow$ Zeigen und Klicken $\rightarrow$ Nachschlagen & Datendetektoren*).

### 4. Apple Spotlight-Suche (`Cmd + Leertaste`)
- Drücken Sie `Cmd + Leertaste`, tippen Sie ein englisches, kyrillisches oder klassisch mongolisches Wort ein (z. B. `морь`, `computer`, `ᠬᠦᠰᠡᠯ`), und die Definition erscheint direkt in den Spotlight-Ergebnissen.

---

## Aus dem Quellcode erstellen (Building from Source)

### Voraussetzungen:
- Python 3.10+
- Node.js 18+ (für die klassische mongolische Schriftkonvertierung)
- Apple Dictionary Development Kit (DDK) und Xcode Command Line Tools.

### Schritte:
```bash
git clone https://github.com/Tsengel-de/apple-dictionary-mongolian.git
cd apple-dictionary-mongolian

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python3 src/build_dictionary.py --dict all

make -C build/Mongolian-English-Altangerel all
make -C build/Mongolian-Tsevel-Explanatory all
bash scripts/build_dmg.sh
```

---

## Unterstützung (Support & Spenden)

Wenn dieses Projekt für Sie nützlich ist, können Sie die Weiterentwicklung und Infrastruktur gerne unterstützen:

[![Ko-fi](https://img.shields.io/badge/Ko--fi-Unterstützen-ff5e5b?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/tsengel)

---

## Lizenz & Danksagung

- **Quellwörterbücher**:
  - *Englisch-Mongolisches Wörterbuch* von Dr. Ch. Altangerel Damdinsuren.
  - *Mongolisches Erklärungswörterbuch* von Akad. Ya. Tsevel.
- **Klassische mongolische Schrift**: Unterstützt durch `@gege-mn/gege-converter`.
- **Software & Styles**: Lizenziert unter der [GNU General Public License v3.0 (GPLv3)](LICENSE). Dual-Licensing-Vorbehalt durch Tsengel (tsengel@tsengel.de | [tsengel.de](https://tsengel.de)).

*Möge die mongolische Sprache und Schrift im digitalen Zeitalter weiter erblühen! 🇲🇳*

