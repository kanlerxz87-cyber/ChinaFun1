# T4 — MICHELIN restaurants: counts, star vs listed, clusters, cost for two

Session `arena-16153d37` · All MICHELIN data fetched from **guide.michelin.com** on **2026-11-25 UTC**.

## A. Official guide counts for Shanghai (two official pages disagree — see R4)

**Live guide filter** — https://guide.michelin.com/us/en/shanghai-municipality/shanghai/restaurants (fetched 2026-11-25). Page header reads *"Shanghai and surroundings: 1-48 of 153 restaurants"*:

| Distinction | Count (live filter) |
|---|---|
| 3 Stars — Exceptional cuisine | **1** |
| 2 Stars — Excellent cooking | **11** |
| 1 Star — High quality cooking | **38** |
| Bib Gourmand — good quality, good value | **33** |
| Selected Restaurants — good cooking | **70** |
| **Total** | **153** |

Other verified live-filter facts: 35 cuisines represented; "Good for: Date night" = 16 restaurants; "Good for: Solo dining" = 15; price distribution `$`19 / `$$`37 / `$$$`59 / `$$$$`38; days-open counts Mon 35 · Tue 36 · Wed 37 · Thu 37 · Fri 37 · Sat 37 · Sun 37 (i.e. **35 of 153 are open Monday**, 118 are closed Monday); facilities include "In MICHELIN Hotels" filter, wheelchair access 50, great view 17, counter dining 17.

**Official press release** — https://guide.michelin.com/en/article/michelin-guide-ceremony/michelin-guide-shanghai-jiangsu-zhejiang (published 2026-04-09): first regional edition *MICHELIN Guide Shanghai | Jiangsu | Zhejiang 2026*; **409 restaurants** total (156 Shanghai, 111 Jiangsu, 142 Zhejiang); **77 starred** (1 three-star, 14 two-star, 62 one-star); **164 Bib Gourmand**; **168 MICHELIN Selected**; **1 MICHELIN Green Star**; 4 special awards. Shanghai 2026 changes: promoted to two stars — 菁禧荟 (Changning), 唐阁 (T'ang Court), 头灶; first star — Fabula, 三月醉淮扬 (Jing'an), Vivant by Johnny Pham. Taian Table retains three stars.

**R4 (irregularity):** press release says 156 Shanghai restaurants / 12 two-stars; the live guide now shows 153 / 11. Both pages are official. The live guide is treated as current state; the press release as the April-2026 launch snapshot. **2027 edition not yet published** → all star statuses on this site are the **2026 edition** and must be re-verified after the 2027 ceremony before booking.

## B. Price bands — official MICHELIN legend (from the live filter page)

| Symbol | Official meaning |
|---|---|
| `$` | On a budget |
| `$$` | A moderate spend |
| `$$$` | Special occasion |
| `$$$$` | Spare no expense |

Bands are per-person indications published by MICHELIN. **They are not prices**, so no CNY total is derived from them anywhere on this site.

## C. "Has a star" vs "listed in the guide" — the distinction used in every table

| Label used on site | Meaning |
|---|---|
| **3★ / 2★ / 1★ — currently starred** | the star icon and the wording ("Three Stars: Exceptional cuisine", "Two Stars: Excellent cooking", "One Star: High quality cooking") appear on that restaurant's own official MICHELIN page |
| **Listed — no star** | the restaurant appears in the official MICHELIN Guide selection with a cuisine and price band but **no star icon** on the fetched listing. Bib Gourmand vs "Selected" is **not distinguished** in the fetched list text → flagged, not guessed |
| **Star status not confirmed** | entry seen in an official MICHELIN "nearby restaurants" block where the star icon is not rendered in the fetched text (e.g. Lao Zheng Xing) → left unasserted |

## D. Verified MICHELIN clusters (built only from official published addresses)

### Cluster C1 — Huangpu: Bund / East Beijing Rd / Xintiandi
| Restaurant | Status | Official address |
|---|---|---|
| T'ang Court | **2★** | 5F, The Langham Xintiandi, 99 Madang Road |
| Lu Style (Huangpu) | **1★** | district in official name |
| The Yidao (East Beijing Road) | listed | L201A, 2F, Yi Feng Galleria, 99 East Beijing Road |
| Shanghai | listed | 2F, Central Hotel, 555 Jiujiang Road |
| Lao Xing Xian (Huangpu) | listed | district in official name |

Hotels sitting inside this cluster: The Peninsula Shanghai (No.32 The Bund) · Waldorf Astoria Shanghai on the Bund (No.2 Zhong Shan Dong Yi Rd) · The Langham Shanghai Xintiandi (99 Madang Rd — contains T'ang Court) · Radisson Collection Hyland and Atour Light (People's Square / West Nanjing Rd).

### Cluster C2 — Zhenning Road corridor (Jing'an ↔ Changning)
| Restaurant | Status | Official address |
|---|---|---|
| Taian Table | **3★** (region's only three-star; MICHELIN Green Star per official guide listing) | No.161, Lane 465, Zhenning Road, Changning |
| Fu 1088 | **1★** | 375 Zhenning Road, Jing'an |

**Finding:** the region's only three-star restaurant and a one-star are on the **same street**. Official press release adds 菁禧荟 (Amazing Chinese Cuisine, Changning, 2★) and 三月醉淮扬 (Jing'an, 1★) to this corridor's district pair. No hotel in this corridor was priced in this session → **highest-value open research gap** (see `questions.html`).

### Cluster C3 — Middle Huaihai Road / iapm (Xuhui)
| Restaurant | Status | Official address |
|---|---|---|
| Lei Garden (Xuhui) | **1★** | Shop 401, **4F, iapm**, 999 Middle Huaihai Road |
| Da Dong (Xuhui) | **1★** | Shop 602, **6F, iapm**, 999 Middle Huaihai Road |
| Ren He Guan (Xuhui) | **1★** | 407 Zhaojiabang Road |

**Finding:** two one-star restaurants in the **same building** (iapm mall) — one visit covers both, and both are `$$`/`$$$`, the most affordable starred options verified in this session.

### Outlier (excluded from cluster ranking)
Zhou She (Minhang) — 1★ — Hongqiao Lihpao Plaza, Lane 318 Suhong Road. Near Hongqiao transport hub, far from the three clusters above.

## E. Cost for a couple (2 adults) — verified totals only

| Restaurant | Verified total for 2 adults | Basis | Source |
|---|---|---|---|
| **T'ang Court (2★)** | **¥888** — Classic Dim Sum Lunch Set for Two | official set-menu PDF; "All prices are in Chinese Yuan and inclusive of service charge and taxes" | https://www.langhamhotels.com/content/dam/langhamhotels/tlshx-pdfs/tang-court/2026/seasonal-set-menu-selection-2026.pdf |
| **T'ang Court (2★)** | **¥2,288** — All Day Set Menu for Two | same PDF, same inclusive-of-service-and-tax statement | same |
| Taian Table (3★) | **BLANK — flagged** | official Menu No.55 PDF publishes add-on prices (Pied de Cochon ¥388, NZ King Salmon ¥218, Coconut Gelato ¥188) and states the 10-course degustation is "fixed and mandatory", but the degustation price is not in the fetched document | https://sh.taian-table.cn/wp-content/uploads/2026/10/Menu-No.55.pdf |
| All other entries | **BLANK — flagged** | only the official MICHELIN `$`–`$$$$` band is published; no numeric menu located | each restaurant's guide.michelin.com page |

Also verified for T'ang Court (same PDF set): Set Menu for Four ¥3,388 · Set Menu for Six ¥6,688. Seating: à la carte 24 guests, private dining rooms 91 guests. Reservations via https://www.diningcity.cn/en/shanghai/tang_court_the_langham_xintiandi or (8621) 2330 2430; tables held 15 minutes; smart casual attire.

**Range presentation rule applied:** where an exact official price exists it is shown as an exact total (T'ang Court). Where none exists the cell is left blank and flagged — **no estimate is invented**, per the verification rule in the brief.

## F. Booking-channel facts (official)

- Taian Table: the official MICHELIN page states *"This establishment manages its own bookings. Please contact the restaurant directly to book a table."* → no OpenTable/Resy path. Official site: https://sh.taian-table.cn/ · phone +86 173 0160 5350.
- Ren He Guan: same "manages its own bookings" notice; phone +86 21 6403 0731.
- T'ang Court: official MICHELIN page links a reserve widget and the hotel's own site; hotel publishes the DiningCity reservation link.
- MICHELIN Guide global booking partnerships are OpenTable and Resy (official guide footer): https://guide.michelin.com/us/en/booking-partnership-between-the-michelin-guide-and-open-table · https://guide.michelin.com/us/en/booking-partnership-between-the-michelin-guide-and-resy
