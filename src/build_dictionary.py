#!/usr/bin/env python3
"""
Apple Dictionary Builder for Mongolian (macOS)
==============================================
Builds native Apple Dictionary source packages (.apple) from:
1. Altangerel English-Mongolian Dictionary (25,252 entries)
2. Tsevel Mongolian Explanatory Dictionary (30,626 entries)

Produces DDK-compatible XML, Info.plist, DefaultStyle.css, and Makefile.
Author: Tsengel (tsengel.de | tsengel@tsengel.de)
License: GNU General Public License v3.0 (or later)
"""

import os
import re
import sys
import shutil
import subprocess
import argparse
import html
from pathlib import Path
import lxml.html


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
BUILD_DIR = PROJECT_ROOT / "build"
STYLES_DIR = PROJECT_ROOT / "styles"


PLIST_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
\t<key>CFBundleDevelopmentRegion</key>
\t<string>{dev_region}</string>
\t<key>CFBundleIdentifier</key>
\t<string>{bundle_id}</string>
\t<key>CFBundleDisplayName</key>
\t<string>{display_name}</string>
\t<key>CFBundleName</key>
\t<string>{bundle_name}</string>
\t<key>CFBundleShortVersionString</key>
\t<string>{version}</string>
\t<key>DCSDictionaryCopyright</key>
\t<string>{copyright}</string>
\t<key>DCSDictionaryManufacturerName</key>
\t<string>{author}</string>
\t<key>DCSDictionaryLanguages</key>
\t<array>
\t\t<dict>
\t\t\t<key>DCSDictionaryIndexLanguage</key>
\t\t\t<string>{index_lang}</string>
\t\t\t<key>DCSDictionaryTargetLanguage</key>
\t\t\t<string>{target_lang}</string>
\t\t</dict>
\t</array>
\t<key>DCSDictionaryDefaultPrefs</key>
\t<dict/>
</dict>
</plist>
"""

MAKEFILE_TEMPLATE = """#
# Apple Dictionary Makefile
# Generated automatically by build_dictionary.py
#

DICT_NAME           = "{dict_name}"
DICT_SRC_PATH       = "{dict_src_xml}"
CSS_PATH            = "DefaultStyle.css"
PLIST_PATH          = "Info.plist"

DICT_BUILD_TOOL_DIR ?= /Applications/Utilities/Dictionary Development Kit
DICT_BUILD_TOOL_BIN = $(DICT_BUILD_TOOL_DIR)/bin

DICT_DEV_KIT_OBJ_DIR ?= ./objects
export DICT_DEV_KIT_OBJ_DIR

DESTINATION_FOLDER  = ~/Library/Dictionaries
RM                  = /bin/rm

all:
\t"$(DICT_BUILD_TOOL_BIN)/build_dict.sh" $(DICT_NAME) $(DICT_SRC_PATH) $(CSS_PATH) $(PLIST_PATH)
\t@echo "Build completed: $(DICT_DEV_KIT_OBJ_DIR)/$(DICT_NAME).dictionary"

install:
\t@echo "Installing $(DICT_NAME) into $(DESTINATION_FOLDER)..."
\tmkdir -p $(DESTINATION_FOLDER)
\tditto --noextattr --norsrc $(DICT_DEV_KIT_OBJ_DIR)/$(DICT_NAME).dictionary $(DESTINATION_FOLDER)/$(DICT_NAME).dictionary
\ttouch $(DESTINATION_FOLDER)
\t@echo "Installed. Relaunch Dictionary.app or enable in Dictionary Settings."

clean:
\t$(RM) -rf $(DICT_DEV_KIT_OBJ_DIR)
"""


def build_tsevel():
    """Builds Tsevel Mongolian Explanatory Dictionary (30,626 entries)."""
    dict_name = "Mongolian-Tsevel-Explanatory"
    out_dir = BUILD_DIR / dict_name
    out_dir.mkdir(parents=True, exist_ok=True)
    
    tsevel_src = DATA_DIR / "tsevel" / "monmon.txt"
    if not tsevel_src.exists():
        print(f"[-] Tsevel source not found at {tsevel_src}")
        return False
        
    print(f"[*] Parsing Tsevel data from {tsevel_src}...")
    with open(tsevel_src, "rb") as f:
        raw = f.read()
    
    parts = raw.split(b"\x00")
    entries = []
    for i in range(0, len(parts) - 1, 2):
        word = parts[i].decode("utf-8", errors="replace").strip()
        defn = parts[i + 1].decode("utf-8", errors="replace").strip()
        if word and defn:
            entries.append((word, defn))
            
    print(f"[+] Loaded {len(entries):,} Tsevel entries.")
    
    # Load traditional Mongolian script mapping if available
    bichig_mapping = {}
    bichig_json_path = DATA_DIR / "bichig_mapping.json"
    if bichig_json_path.exists():
        import json
        with open(bichig_json_path, "r", encoding="utf-8") as f:
            bichig_mapping = json.load(f)
        print(f"[+] Loaded {len(bichig_mapping):,} Traditional Mongolian script mappings.")

    xml_filename = f"{dict_name}.xml"
    xml_path = out_dir / xml_filename
    print(f"[*] Writing Apple Dictionary XML: {xml_path}...")
    
    # Pre-clean definition redundant breaks
    br_cleanup = re.compile(r'(?:<br\s*/?>\s*)+(?:<ol>|<ul>|<li>|</li>|</ol>|</ul>)', re.IGNORECASE)
    
    with open(xml_path, "w", encoding="utf-8") as out:
        out.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        out.write('<d:dictionary xmlns="http://www.w3.org/1999/xhtml" '
                  'xmlns:d="http://www.apple.com/DTDs/DictionaryService-1.0.rng">\n')
        
        for idx, (word, defn) in enumerate(entries):
            entry_id = f"tsevel_{idx + 1}"
            title_esc = html.escape(word, quote=True)
            
            # Build search indexes
            indices = {word}
            
            # Remove Roman or Arabic numerals at end (e.g. 'а i' -> 'а', 'ааг ii' -> 'ааг')
            base_word = re.sub(r'\s+(?:[iIvVxX]+|\d+)$', '', word).strip()
            if base_word and base_word != word:
                indices.add(base_word)
                
            # Split comma separated headwords (e.g. 'морь, морин')
            for part in re.split(r'[,/]', word):
                p_clean = re.sub(r'\s+(?:[iIvVxX]+|\d+)$', '', part.strip()).strip()
                if p_clean:
                    indices.add(p_clean)

            # Check for Traditional Mongolian script
            bichig_data = bichig_mapping.get(base_word) or bichig_mapping.get(word)
            if not bichig_data and ',' in word:
                first_part = word.split(',')[0].strip()
                bichig_data = bichig_mapping.get(first_part)
                
            if bichig_data and bichig_data.get('s'):
                indices.add(bichig_data['s'])
                    
            # Clean and validate definition XHTML with lxml
            try:
                frag = lxml.html.fragment_fromstring(defn, create_parent='div')
                # Render as clean XML
                clean_div = lxml.html.tostring(frag, method='xml', encoding='utf-8').decode('utf-8')
                # Replace root <div> with <div class="definition tsevel-body">
                if clean_div.startswith('<div>'):
                    clean_def = '<div class="definition tsevel-body">' + clean_div[5:]
                elif clean_div.startswith('<div '):
                    clean_def = '<div class="definition tsevel-body">' + clean_div[clean_div.find('>')+1:]
                else:
                    clean_def = f'<div class="definition tsevel-body">{clean_div}</div>'
            except Exception:
                clean_esc = html.escape(defn)
                clean_def = f'<div class="definition tsevel-body"><p>{clean_esc}</p></div>'
            
            out.write(f'<d:entry id="{entry_id}" d:title="{title_esc}">\n')
            for idx_val in sorted(indices):
                val_esc = html.escape(idx_val, quote=True)
                out.write(f'  <d:index d:value="{val_esc}" d:title="{title_esc}"/>\n')
                
            # Header with vertical Traditional Script Ribbon if available
            if bichig_data and bichig_data.get('s'):
                bichig_script = html.escape(bichig_data['s'])
                galig = html.escape(bichig_data.get('g', ''))
                galig_span = f' <span class="galig">({galig})</span>' if galig else ''
                out.write('  <div class="entry-header">\n')
                out.write(f'    <div class="bichig-column">{bichig_script}</div>\n')
                out.write('    <div class="header-content">\n')
                out.write(f'      <h1>{html.escape(word)}{galig_span}</h1>\n')
                out.write('    </div>\n')
                out.write('  </div>\n')
            else:
                out.write(f'  <h1>{html.escape(word)}</h1>\n')
                
            out.write(f'  {clean_def}\n')
            out.write('  <div class="source-badge">Я. Цэвэл — Монгол хэлний тайлбар толь</div>\n')
            out.write('</d:entry>\n')
            
        out.write('</d:dictionary>\n')
        
    print(f"[+] Successfully wrote {xml_path} ({xml_path.stat().st_size / (1024*1024):.1f} MB)")
    
    # Write Info.plist
    plist_path = out_dir / "Info.plist"
    with open(plist_path, "w", encoding="utf-8") as f:
        f.write(PLIST_TEMPLATE.format(
            dev_region="mn",
            bundle_id="org.tsengel.dictionary.Tsevel-Mongolian-Explanatory",
            display_name="Монгол хэлний тайлбар толь (Цэвэл)",
            bundle_name=dict_name,
            version="1.0.0",
            copyright="Cultural Heritage / Public Domain (1966). Digitized and Packaged for Apple macOS by Tsengel (tsengel.de)",
            author="Ya. Tsevel / Tsengel (tsengel.de)",
            index_lang="mn",
            target_lang="mn"
        ))
    print(f"[+] Wrote {plist_path}")
    
    # Copy CSS
    shutil.copy(STYLES_DIR / "Dictionary.css", out_dir / "DefaultStyle.css")
    print(f"[+] Copied DefaultStyle.css")
    
    # Write Makefile
    makefile_path = out_dir / "Makefile"
    with open(makefile_path, "w", encoding="utf-8") as f:
        f.write(MAKEFILE_TEMPLATE.format(dict_name=dict_name, dict_src_xml=xml_filename))
    print(f"[+] Wrote {makefile_path}")
    
    return True


def build_altangerel():
    """Builds Altangerel English-Mongolian Dictionary (25,252 entries)."""
    dict_name = "Mongolian-English-Altangerel"
    out_dir = BUILD_DIR / dict_name
    out_dir.mkdir(parents=True, exist_ok=True)
    
    stardict_ifo = DATA_DIR / "altangerel" / "altangerel.ifo"
    if not stardict_ifo.exists():
        print(f"[-] Altangerel StarDict data not found at {stardict_ifo}")
        return False
        
    # Find pyglossary executable
    pyglossary_bin = shutil.which("pyglossary")
    if not pyglossary_bin:
        venv_bin = Path(sys.executable).parent / "pyglossary"
        if venv_bin.exists():
            pyglossary_bin = str(venv_bin)
        else:
            print("[-] pyglossary binary not found.")
            return False
            
    print(f"[*] Running PyGlossary StarDict -> AppleDict conversion...")
    temp_apple_dir = BUILD_DIR / f"{dict_name}_raw.apple"
    if temp_apple_dir.exists():
        shutil.rmtree(temp_apple_dir)
        
    cmd = [pyglossary_bin, str(stardict_ifo), str(temp_apple_dir), "--write-format=AppleDict"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[-] PyGlossary failed: {res.stderr}")
        return False
        
    # Locate generated xml file
    xml_candidates = list(temp_apple_dir.glob("*.xml"))
    if not xml_candidates:
        print("[-] PyGlossary generated no XML file.")
        return False
        
    raw_xml_path = xml_candidates[0]
    final_xml_filename = f"{dict_name}.xml"
    final_xml_path = out_dir / final_xml_filename
    
    # Load traditional Mongolian script mapping if available
    bichig_mapping = {}
    bichig_json_path = DATA_DIR / "bichig_mapping.json"
    if bichig_json_path.exists():
        import json
        with open(bichig_json_path, "r", encoding="utf-8") as f:
            bichig_mapping = json.load(f)

    print(f"[*] Enhancing XML styling, traditional script & bidirectional indexing from {raw_xml_path.name}...")
    entry_pattern = re.compile(r'<d:entry\s+([^>]+)>(.*?)</d:entry>', re.DOTALL)
    
    with open(raw_xml_path, "r", encoding="utf-8") as fin:
        content = fin.read()

    def process_entry(match):
        attrs = match.group(1)
        body = match.group(2)
        
        title_m = re.search(r'd:title="([^"]+)"', attrs)
        title = title_m.group(1) if title_m else ""
        
        # Split indexes and content
        h1_m = re.search(r'<h1>.*?</h1>', body)
        if not h1_m:
            return match.group(0)
            
        pre_h1 = body[:h1_m.start()]
        h1_tag = body[h1_m.start():h1_m.end()]
        entry_def = body[h1_m.end():]
        
        # Extract primary translation words from initial sentence
        clean_def = re.sub(r'<[^>]+>', ' ', entry_def)
        clean_def = re.sub(r'^[a-z]+\.\s*(?:\([^)]+\)\s*)?', '', clean_def.strip(), flags=re.IGNORECASE)
        clean_def = re.sub(r'^1\.\s*', '', clean_def.strip())
        first_clause = clean_def.split('.')[0]
        
        cyr_words = re.findall(r'[\u0400-\u04FF\u0500-\u052F\-]{2,}', first_clause)
        tags = []
        seen = set()
        for w in cyr_words:
            wc = w.strip('-')
            if wc in bichig_mapping and wc not in seen:
                seen.add(wc)
                tags.append((wc, bichig_mapping[wc]['s'], bichig_mapping[wc].get('g', '')))
                if len(tags) >= 3:
                    break
                    
        # Bidirectional indexes
        extra_indexes = []
        for (cw, s, _) in tags:
            extra_indexes.append(f'  <d:index d:value="{html.escape(cw, quote=True)}" d:title="{html.escape(title, quote=True)}"/>')
            extra_indexes.append(f'  <d:index d:value="{html.escape(s, quote=True)}" d:title="{html.escape(title, quote=True)}"/>')
            
        extra_idx_str = ('\n' + '\n'.join(extra_indexes)) if extra_indexes else ''
        
        # Traditional script badges
        bichig_bar = ''
        if tags:
            spans = []
            for (cw, s, g) in tags:
                g_str = f' ({html.escape(g)})' if g else ''
                spans.append(
                    f'<span class="bichig-tag">'
                    f'<span class="bichig-glyph">{html.escape(s)}</span> '
                    f'<span class="bichig-label">{html.escape(cw)}{g_str}</span>'
                    f'</span>'
                )
            bichig_bar = f'\n  <div class="altangerel-bichig-bar">\n    ' + '\n    '.join(spans) + '\n  </div>'
            
        # Clean up definition tags
        formatted_def = re.sub(r'<font color="blue">([^<]+)</font>', r'<span class="pos">\1</span>', entry_def)
        formatted_def = re.sub(r'<br\s*>', '<br/>', formatted_def, flags=re.IGNORECASE)
        formatted_def = re.sub(r'<br\s*/>', '<br/>', formatted_def, flags=re.IGNORECASE)
        
        return (
            f'<d:entry {attrs}>\n'
            f'{pre_h1.strip()}{extra_idx_str}\n'
            f'  {h1_tag}{bichig_bar}\n'
            f'  <div class="definition altangerel-body">\n    {formatted_def.strip()}\n  </div>\n'
            f'  <div class="source-badge">Altangerel Damdinsuren — English-Mongolian Dictionary</div>\n'
            f'</d:entry>'
        )

    # Process all entries
    enhanced_content = entry_pattern.sub(process_entry, content)
    
    with open(final_xml_path, "w", encoding="utf-8") as fout:
        fout.write(enhanced_content)
            
    print(f"[+] Wrote enhanced {final_xml_path} ({final_xml_path.stat().st_size / (1024*1024):.1f} MB)")
    
    # Clean up temp raw conversion
    shutil.rmtree(temp_apple_dir)
    
    # Write Info.plist
    plist_path = out_dir / "Info.plist"
    with open(plist_path, "w", encoding="utf-8") as f:
        f.write(PLIST_TEMPLATE.format(
            dev_region="en",
            bundle_id="org.tsengel.dictionary.Altangerel-English-Mongolian",
            display_name="English-Mongolian Dictionary (Altangerel)",
            bundle_name=dict_name,
            version="1.0.0",
            copyright="Dr. Altangerel Damdinsuren / Ochirkhuyag.L (MIT License). Packaged for Apple macOS by Tsengel (tsengel.de)",
            author="Altangerel Damdinsuren / Tsengel (tsengel.de)",
            index_lang="en",
            target_lang="mn"
        ))
    print(f"[+] Wrote {plist_path}")
    
    # Copy CSS
    shutil.copy(STYLES_DIR / "Dictionary.css", out_dir / "DefaultStyle.css")
    print(f"[+] Copied DefaultStyle.css")
    
    # Write Makefile
    makefile_path = out_dir / "Makefile"
    with open(makefile_path, "w", encoding="utf-8") as f:
        f.write(MAKEFILE_TEMPLATE.format(dict_name=dict_name, dict_src_xml=final_xml_filename))
    print(f"[+] Wrote {makefile_path}")
    
    return True


def main():
    parser = argparse.ArgumentParser(description="Apple Dictionary Builder for Mongolian (macOS)")
    parser.add_argument("--dict", choices=["altangerel", "tsevel", "all"], default="all",
                        help="Which dictionary to build (default: all)")
    args = parser.parse_args()
    
    print("=" * 65)
    print("Apple Dictionary Builder for Mongolian (macOS) — Tsengel.de")
    print("=" * 65)
    
    success = True
    if args.dict in ("all", "altangerel"):
        if not build_altangerel():
            success = False
            
    if args.dict in ("all", "tsevel"):
        if not build_tsevel():
            success = False
            
    if success:
        print("\n[SUCCESS] Apple Dictionary source packages generated successfully in ./build/")
    else:
        print("\n[FAILURE] One or more dictionaries failed to build.")
        sys.exit(1)


if __name__ == "__main__":
    main()
