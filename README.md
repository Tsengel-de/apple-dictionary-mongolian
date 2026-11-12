# 🇲🇳 macOS-д Зориулсан Apple Монгол Толь Бичгийн Багц
### Dual-Script Mongolian Apple Dictionaries (Altangerel & Tsevel)

[![License: GPL-3.0-or-later](https://img.shields.io/badge/License-GPLv3--or--later-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-macOS-lightgrey.svg)](https://apple.com)
[![Initiative](https://img.shields.io/badge/Initiative-Mongolian%20Language%20for%20All-brightgreen.svg)](https://tsengel.de)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Support-ff5e5b?logo=ko-fi&logoColor=white)](https://ko-fi.com/tsengel)
[![Author: Tsengel](https://img.shields.io/badge/Author-Tsengel%20(tsengel.de)-red.svg)](https://tsengel.de)

**Хэл сонгох / Languages / Sprachen:** [🇲🇳 Монгол](README.md) • [🇬🇧 English](README.en.md) • [🇩🇪 Deutsch](README.de.md)

> **"Эх хэлнийхээ үгийн баялгийг технологийн дэвшилтэй уялдуулж, хүн бүрд хүртээмжтэй болгох нь бидний зорилго юм."**  
> macOS үйлдлийн системд зориулсан Apple-ийн албан ёсны стандартын `.dictionary` толь бичгийн багц. Системийн түвшинд гүн суурилан, ямар ч програм дээр (Safari, Pages, Mail, Preview, Terminal, Notes) интернэтгүйгээр үгийн утга, орчуулгыг хормын төдийд харах боломжтой.

Энэхүү төсөл нь [Цэнгэл (tsengel.de)](https://tsengel.de)-ийн **"Бүх Нийтийн Монгол Хэл"** (Mongolian Language for All) нээлттэй санаачилгын нэг хэсэг юм.

---

## Толь Бичиг гэж юу вэ? (Толь Бичиг vs. Орчуулагч)

Олон хэрэглэгчид **Толь бичиг (Dictionary)** болон **Машин орчуулагч (Google Translate / DeepL)** хоёрыг андуурдаг:

| Шинж чанар | Системийн Толь Бичиг (Энэ төсөл) | Машин Орчуулагч (Google Translate / AI) |
| :--- | :--- | :--- |
| **Зорилго** | Үгийн гүн тайлбар, зөв бичгийн дүрэм, зүйр цэцэн үг, хэлц, язгуур утга | Бүтэн өгүүлбэр, текстийг нэг хэлнээс нөгөөд шууд буулгах |
| **Интернэт шаардах эсэх** | **Үгүй (100% Offline)** — Mac дотор шууд сууж ажиллана | **Тийм** — үүлэн серверийн холболт заавал шаардана |
| **Хурд** | **Агшин зуур (0.001 секунд)** — хулгана очиход л гарна | 1–3 секундийн сүлжээний хүлээгдэл |
| **macOS холболт** | **Apple-ийн системийн цөмтэй нэгдсэн**: Right-Click, Spotlight, Dictionary.app | Хөтчийн тусдаа таб эсвэл гуравдагч веб апп |

---

## Багтсан Толь Бичгүүд

| Толь бичиг | Зохиогч / Эх сурвалж | Үгийн тоо | Төрөл | Багцын ID |
| :--- | :--- | :---: | :---: | :--- |
| **Англи-Монгол Толь Бичиг** | Д-р Ч. Алтангэрэл Дамдинсүрэн | **25,252** | Хоёр хэлний (EN &rarr; MN) | `org.tsengel.dictionary.Altangerel-English-Mongolian` |
| **Монгол Хэлний Тайлбар Толь** | Академич Я. Цэвэл | **30,626** | Нэг хэлний тайлбар (MN &rarr; MN) | `org.tsengel.dictionary.Tsevel-Mongolian-Explanatory` |
| **Хос бичиг & Латин галиг** | Худам Монгол бичиг (`ᠮᠣᠩᠭᠣᠯ`) & Сонгодог галиг | Хос бичигтэй | Кирилл + Худам Бичиг | Толгой үг бүрд суулгасан |
| **Нийт үг ба тайлбарын тоо** | | **55,878+** | | |

---

## Онцлог Давуу Талууд

- **Хос Бичгийн Хослол (Кирилл + Худам Монгол Бичиг)**:
  - Толгой үг бүр босоо Худам монгол бичиг (`ᠮᠣᠷᠢ`), стандарт кирилл бичиг (`морь`) болон сонгодог латин галигтайгаа (*mori*) зэрэгцэн харагдана.
  - Англи, кирилл болон худам монгол бичгийн алинаар нь ч хоёр урсгалаар хайх боломжтой (Bidirectional Indexing).
- **Орчин Үеийн Apple Retina Дизайн**:
  - macOS San Francisco фонт болон Retina дэлгэцэнд зориулсан цэвэр CSS загвар.
  - Үгийн аймгийн тэмдэглэгээ (`n.`, `v.`, `adj.`, `suff.`).
  - Жишээ өгүүлбэр, монгол ардын зүйр цэцэн үг, өвөрмөц хэлцийг тодруулсан онцгой загвар.
- **Өдөр & Шөнийн Горим (High-Contrast Dark Mode)**:
  - macOS-ийн өнгөний тохиргоог автоматаар мэдэрч, Dark Mode дээр тод цагаан текстээр өндөр тодосгогчтойгоор уншигдана.
- **100% Аюулгүй, Хувийн Нууцлал Хадгалагдсан**:
  - Ямар нэгэн сүлжээний холболт, хэрэглэгчийн өгөгдөл цуглуулах хэрэгсэл байхгүй. Компьютерт бүрэн офлайн ажиллана.

---

## Хялбар Суулгах Заавар

### Арга 1: Apple Native `.dmg` Дискээр Суулгах (Зөвлөмж — Drag & Drop)
1. Хамгийн сүүлийн [GitHub Releases](https://github.com/Tsengel-de/apple-dictionary-mongolian/releases)-ээс **`Mongolian-Dictionaries-macOS.dmg`** файлыг татаж аваад 2 товшиж нээнэ.
2. Mac дээр тань очих хавтас байгаа эсэхийг баталгаажуулна. (Шинэ Apple Silicon M1/M2/M3/M4 болон macOS Sonoma/Sequoia дээр энэ хавтас анхнаасаа байдаггүй тул Terminal дээр ганцхан удаа дараах тушаалыг ажиллуулна):
   ```bash
   mkdir -p ~/Library/Dictionaries
   ```
   *(Эсвэл Finder дээр `Cmd + Shift + G` дараад `~/Library` гэж бичиж ороод `Dictionaries` нэртэй шинэ хавтас үүсгэж болно)*.
3. DMG доторх хоёр `.dictionary` багцыг **`~/Library/Dictionaries/`** хавтас руу чирж хуулна.

### Арга 2: Бие Даасан `.zip` Архиваар Суулгах
1. `Mongolian-English-Altangerel.dictionary.zip` болон `Mongolian-Tsevel-Explanatory.dictionary.zip` файлуудыг татаж авна.
2. Архивыг задлаад гарч ирсэн хоёр `.dictionary` хавтсыг `~/Library/Dictionaries/` руу хуулна:
   ```bash
   mkdir -p ~/Library/Dictionaries
   cp -R Mongolian-*.dictionary ~/Library/Dictionaries/
   ```

### Толь бичгээ Dictionary.app дотроос идэвхжүүлэх:
1. Mac дээрээ **Dictionary.app**-ийг нээнэ (Spotlight эсвэл Applications дотроос).
2. Тохиргоо цэсийг нээнэ: **`Cmd + ,`**.
3. Жагсаалтаас дараах хоёр толийг чагталж идэвхжүүлнэ:
   - ☑️ **English-Mongolian Dictionary (Altangerel)**
   - ☑️ **Монгол хэлний тайлбар толь (Цэвэл)**
4. Хүсвэл жагсаалт дотор нь чирж дээш доош байрлуулан эрэмбэлж болно.

---

## macOS Дээр Хэрхэн Хялбар Ашиглах вэ?

Идэвхжүүлсний дараа таны Mac-ийн бүх програм дээр шууд ажиллана:

### 1. Хулганы Баруун Товчоор Хайх (Look Up — Хамгийн шилдэг арга)
1. Safari, Pages, Notes, Mail эсвэл ямар ч програм дээр үгээ сонгоно (эсвэл заагчаа аваачна).
2. **Хулганы баруун товч (Right-Click)** дараад **Look Up "..."** сонгоно.
3. Тухайн үгийн хажууд бяцхан цонх үсрэн гарч ирнэ. Доод талын жагсаалтаас **English-Mongolian** эсвэл **Цэвэл** дээр дарж хос бичигтэй тайлбарыг харна.

### 2. Гарын Түргэн Товчлол (Global Keyboard Shortcut)
- Дурын үгэн дээр заагчаа тавиад дараах товчлуурыг зэрэг дарна:
  ```text
  Ctrl + Cmd + D
  ```
  Толь бичгийн цонх шууд дэлгэгдэнэ.

### 3. Trackpad Товшилт (Сонголттой)
- Хэрэв хүсвэл Trackpad дээрээ үгэн дээр 3 хуруугаараа зөөлөн товшиж (Tap with 3 fingers) эсвэл чанга дарж (Force Click) хайж болно (*System Settings $\rightarrow$ Trackpad $\rightarrow$ Point & Click дотроос тохируулна*).

### 4. Apple Spotlight Хайлт (`Cmd + Space`)
- `Cmd + Space` дараад дурын англи, кирилл эсвэл худам монгол үг (жишээ нь: `морь`, `computer`, `ᠬᠦᠰᠡᠯ`) шивэхэд Spotlight дотор толь бичгийн үр дүн шууд гарч ирнэ.

---

## Эх Кодоос Угсрах (Building from Source)

### Шаардлагатай багажууд:
- Python 3.10+
- Node.js 18+ (Худам монгол бичгийн хөрвүүлэгчид)
- Apple Dictionary Development Kit (DDK) болон Xcode Command Line Tools.

### Угсрах алхмууд:
```bash
git clone https://github.com/Tsengel-de/apple-dictionary-mongolian.git
cd apple-dictionary-mongolian

# Python сангууд суулгах
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Apple Dictionary XML болон хөрвүүлэлтийг бэлтгэх
python3 src/build_dictionary.py --dict all

# macOS дээр компиляци хийж DMG үүсгэх
make -C build/Mongolian-English-Altangerel all
make -C build/Mongolian-Tsevel-Explanatory all
bash scripts/build_dmg.sh
```

---

## Төслийг Дэмжих (Support & Donation)

Хэрэв энэхүү толь бичиг танд тус болж байгаа бол төслийн хөгжүүлэлт болон дэд бүтцийн зардлыг дэмжих боломжтой:

[![Ko-fi](https://img.shields.io/badge/Ko--fi-Дэмжих-ff5e5b?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/tsengel)

---

## Зохиогчийн Эрх ба Талархал

- **Эх Толь Бичгүүд**:
  - *Англи-Монгол Толь Бичиг* — Доктор Ч. Алтангэрэл Дамдинсүрэн.
  - *Монгол Хэлний Тайлбар Толь* — Академич Ядамжавын Цэвэл.
- **Худам Бичгийн Хөрвүүлэгч**: `@gege-mn/gege-converter` санг ашиглав.
- **Програм Хангамж ба Загвар**: [GNU General Public License v3.0 (GPLv3)](LICENSE) лицензтэй. Зохиогч: Цэнгэл (tsengel@tsengel.de | [tsengel.de](https://tsengel.de)).

*Монгол хэл, бичиг маань дижитал ертөнцөд мөнхөд гялалзах болтугай! 🇲🇳*
