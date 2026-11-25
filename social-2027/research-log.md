# Research log — session `773e75a3`, 25 Nov 2026 (UTC)

All searches below were run on **YouTube's own search pages**, read through a text proxy because the sandbox
cannot open YouTube directly from the shell. The search page itself is first-party YouTube and supplied the
video IDs, titles and channel names. Each retained ID was then checked against YouTube's official oEmbed
endpoint; the exact endpoint is stored beside every row in `social.json` and rendered as “oEmbed proof” in
`videos.html`.

## Restaurant discovery queries

| Venue | First-party YouTube query | Outcome |
|---|---|---|
| Chao Shang Chao (Chaoyang) | [潮上潮 北京 米其林 三星](https://www.youtube.com/results?search_query=%E6%BD%AE%E4%B8%8A%E6%BD%AE%20%E5%8C%97%E4%BA%AC%20%E7%B1%B3%E5%85%B6%E6%9E%97%20%E4%B8%89%E6%98%9F) | 3 venue-named reviews verified |
| Xin Rong Ji (Xinyuan South Road) | [新荣记 新源南路 北京 米其林](https://www.youtube.com/results?search_query=%E6%96%B0%E8%8D%A3%E8%AE%B0%20%E6%96%B0%E6%BA%90%E5%8D%97%E8%B7%AF%20%E5%8C%97%E4%BA%AC%20%E7%B1%B3%E5%85%B6%E6%9E%97) | 3 branch-specific videos verified |
| Blackswan | [Blackswan Beijing restaurant Michelin](https://www.youtube.com/results?search_query=Blackswan%20Beijing%20restaurant%20Michelin) | 2 venue-named videos; both are short/venue footage, not a full review |
| Jingji | [Jingji Beijing Ritz Carlton Michelin restaurant](https://www.youtube.com/results?search_query=Jingji%20Beijing%20Ritz%20Carlton%20Michelin%20restaurant) | 1 named Short; Peninsula “Jing” results rejected as a different restaurant |
| King's Joy | [京兆尹 King's Joy 北京 米其林](https://www.youtube.com/results?search_query=%E4%BA%AC%E5%85%86%E5%B0%B9%20King%27s%20Joy%20%E5%8C%97%E4%BA%AC%20%E7%B1%B3%E5%85%B6%E6%9E%97) | 4 verified; older 3-star titles retained with a status note |
| Lamdre | [兰斋 Lamdre 北京 米其林](https://www.youtube.com/results?search_query=%E5%85%B0%E6%96%8B%20Lamdre%20%E5%8C%97%E4%BA%AC%20%E7%B1%B3%E5%85%B6%E6%9E%97) | 3 verified (review, chef interview, short) |
| Lu Shang Lu | [鲁上鲁 北京 米其林](https://www.youtube.com/results?search_query=%E9%B2%81%E4%B8%8A%E9%B2%81%20%E5%8C%97%E4%BA%AC%20%E7%B1%B3%E5%85%B6%E6%9E%97) | 3 venue-named reviews verified |
| Fu Chun Ju | [富春居 北京 米其林](https://www.youtube.com/results?search_query=%E5%AF%8C%E6%98%A5%E5%B1%85%20%E5%8C%97%E4%BA%AC%20%E7%B1%B3%E5%85%B6%E6%9E%97) | 2 verified |
| Furong | [芙蓉 北京 米其林 餐厅](https://www.youtube.com/results?search_query=%E8%8A%99%E8%93%89%20%E5%8C%97%E4%BA%AC%20%E7%B1%B3%E5%85%B6%E6%9E%97%20%E9%A4%90%E5%8E%85) | 1 explicit Beijing Furong video; Chengdu “Fu Rong Huang” results rejected |
| Gastro Esthetics DaDong | [大董 北京 米其林 餐厅](https://www.youtube.com/results?search_query=%E5%A4%A7%E8%91%A3%20%E5%8C%97%E4%BA%AC%20%E7%B1%B3%E5%85%B6%E6%9E%97%20%E9%A4%90%E5%8E%85) | 2 DaDong-brand videos; exact guide branch not named in titles |
| Giada Garden | [Giada Garden Beijing Michelin review](https://www.youtube.com/results?search_query=Giada%20Garden%20Beijing%20Michelin%20review) | No venue-specific result; blank |
| Il Ristorante – Niko Romito | [Il Ristorante Niko Romito Beijing review](https://www.youtube.com/results?search_query=Il%20Ristorante%20Niko%20Romito%20Beijing%20review) | 2 videos from the official Bvlgari Hotels channel; Tokyo/Dubai results rejected |
| Lei Garden (Jinbao Tower) | [利苑 北京 金宝汇 米其林](https://www.youtube.com/results?search_query=%E5%88%A9%E8%8B%91%20%E5%8C%97%E4%BA%AC%20%E9%87%91%E5%AE%9D%E6%B1%87%20%E7%B1%B3%E5%85%B6%E6%9E%97) | 1 Beijing one-star video; Guangzhou/HK/Shanghai results rejected |
| Lu Style (Anding Road) | [Lu Style Beijing Michelin Anding Road](https://www.youtube.com/results?search_query=Lu%20Style%20Beijing%20Michelin%20Anding%20Road) | No venue-specific result; blank |
| Mansion Cuisine by Jingyan | [京艳 Mansion Cuisine by Jingyan Beijing](https://www.youtube.com/results?search_query=%E4%BA%AC%E8%89%B3%20Mansion%20Cuisine%20by%20Jingyan%20Beijing) | No venue-specific result; blank |
| MO Jasmine | [MO Jasmine Beijing Mandarin Oriental restaurant](https://www.youtube.com/results?search_query=MO%20Jasmine%20Beijing%20Mandarin%20Oriental%20restaurant) | Hotel and other-outlet videos only; blank |
| Old Tower | [Old Tower Beijing Michelin restaurant 2027](https://www.youtube.com/results?search_query=Old%20Tower%20Beijing%20Michelin%20restaurant%202027) | Guide gala and general lists only; blank |
| Rong Pao | [荣袍 北京 米其林](https://www.youtube.com/results?search_query=%E8%8D%A3%E8%A2%8D%20%E5%8C%97%E4%BA%AC%20%E7%B1%B3%E5%85%B6%E6%9E%97) | 1 explicit 北京荣袍 review |
| Seventh Son | [Seventh Son Beijing Michelin restaurant](https://www.youtube.com/results?search_query=Seventh%20Son%20Beijing%20Michelin%20restaurant) | No venue-specific result; blank |
| The Beijing Kitchen | [北京厨房 米其林 餐厅](https://www.youtube.com/results?search_query=%E5%8C%97%E4%BA%AC%E5%8E%A8%E6%88%BF%20%E7%B1%B3%E5%85%B6%E6%9E%97%20%E9%A4%90%E5%8E%85) | 1 short tagged #北京厨房 at SKP |
| The Georg | [The Georg Beijing restaurant review](https://www.youtube.com/results?search_query=The%20Georg%20Beijing%20restaurant%20review) | No venue-specific result; blank |
| Trb Hutong | [TRB Hutong Beijing restaurant review](https://www.youtube.com/results?search_query=TRB%20Hutong%20Beijing%20restaurant%20review) | Videos were for unrelated hutong BBQ; blank. A CNN video is linked in the root plan, not counted as a social link here |
| Chef 1996 | [Chef 1996 北京 米其林 川菜](https://www.youtube.com/results?search_query=Chef%201996%20%E5%8C%97%E4%BA%AC%20%E7%B1%B3%E5%85%B6%E6%9E%97%20%E5%B7%9D%E8%8F%9C) | 2 venue-named reviews |

No separate queries were run for Cai Yi Xuan, Chao Shang Chao (Xicheng), Shanghai Cuisine, Sheng Yong Xing,
The House of Dynasties, Zhiguan Courtyard or Zijin Mansion: the first broad query for each name family either
returned only other cities/branches or no venue-named result. They are flagged as unverified rather than
repeating a search that would produce the same ambiguity.

## Activity discovery queries

| Activity | First-party YouTube query | Outcome |
|---|---|---|
| Palace Museum | [故宫博物院 北京 参观 攻略](https://www.youtube.com/results?search_query=%E6%95%85%E5%AE%AB%E5%8D%9A%E7%89%A9%E9%99%A2%20%E5%8C%97%E4%BA%AC%20%E5%8F%82%E8%A7%82%20%E6%94%BB%E7%95%A5) | 5 links (3 carried over from the root plan and re-verified, 2 new) |
| Mutianyu Great Wall | [慕田峪长城 缆车 攻略](https://www.youtube.com/results?search_query=%E6%85%95%E7%94%B0%E5%B3%AA%E9%95%BF%E5%9F%8E%20%E7%BC%86%E8%BD%A6%20%E6%94%BB%E7%95%A5) | 3 root-plan links re-verified; all explicitly Mutianyu |
| Temple of Heaven | [Temple of Heaven Beijing visit guide](https://www.youtube.com/results?search_query=Temple%20of%20Heaven%20Beijing%20visit%20guide) | 2 visitor guides verified |
| Summer Palace | [颐和园 北京 游玩 攻略](https://www.youtube.com/results?search_query=%E9%A2%90%E5%92%8C%E5%9B%AD%20%E5%8C%97%E4%BA%AC%20%E6%B8%B8%E7%8E%A9%20%E6%94%BB%E7%95%A5) | 3 verified |
| Tiananmen Square | [天安门广场 预约 参观](https://www.youtube.com/results?search_query=%E5%A4%A9%E5%AE%89%E9%97%A8%E5%B9%BF%E5%9C%BA%20%E9%A2%84%E7%BA%A6%20%E5%8F%82%E8%A7%82) | 2 reservation guides verified |
| Yonghe Temple | [雍和宫 北京 参观 攻略](https://www.youtube.com/results?search_query=%E9%9B%8D%E5%92%8C%E5%AE%AB%20%E5%8C%97%E4%BA%AC%20%E5%8F%82%E8%A7%82%20%E6%94%BB%E7%95%A5) | 2 verified |
| 798 Art Zone | [798艺术区 北京 逛](https://www.youtube.com/results?search_query=798%E8%89%BA%E6%9C%AF%E5%8C%BA%20%E5%8C%97%E4%BA%AC%20%E9%80%9B) | 2 verified |
| Nanluoguxiang | [南锣鼓巷 北京 胡同](https://www.youtube.com/results?search_query=%E5%8D%97%E9%94%A3%E9%BC%93%E5%B7%B7%20%E5%8C%97%E4%BA%AC%20%E8%83%A1%E5%90%8C) | 2 verified |
| National Museum of China | [中国国家博物馆 参观 攻略](https://www.youtube.com/results?search_query=%E4%B8%AD%E5%9B%BD%E5%9B%BD%E5%AE%B6%E5%8D%9A%E7%89%A9%E9%A6%86%20%E5%8F%82%E8%A7%82%20%E6%94%BB%E7%95%A5) | 3 verified |
| Jingshan Park | [景山公园 故宫 全景 北京](https://www.youtube.com/results?search_query=%E6%99%AF%E5%B1%B1%E5%85%AC%E5%9B%AD%20%E6%95%85%E5%AE%AB%20%E5%85%A8%E6%99%AF%20%E5%8C%97%E4%BA%AC) | 3 verified |

## Official pages fetched for hours and status

| Page | Result |
|---|---|
| [MICHELIN Beijing all-starred](https://guide.michelin.com/us/en/beijing-municipality/beijing/restaurants/all-starred) | Live filter: 3★ 2 · 2★ 5 · 1★ 26 · Bib 32 · Selected 42; “Days open” facet counts only 8 entries per weekday |
| [MICHELIN Lamdre entry](https://guide.michelin.com/us/en/beijing-municipality/beijing/restaurant/lamdre) | Address, cuisine, ¥¥¥¥, two-star icons; no opening-hours block |
| [Palace Museum visit page](https://intl.dpm.org.cn/visit.html) | Lower-season hours and Monday closure already captured by the root plan; reused, not re-derived here |
| [Mutianyu official site](https://en.mutianyugreatwall.com/) | Off-season window already captured by the root plan; reused |
| [National Museum of China](https://www.chnmuseum.cn/) | Home page fetched; no visit-hours statement in captured content → blank |
| [Temple of Heaven park site](https://www.tiantanpark.com/) | Fetch failed → blank |
| [798 Art Zone](https://www.798art.org/) | Fetch failed → blank |
| [Yonghe Temple](https://www.yonghegong.cn/) | HTTP 403 → blank |

## Deliberate non-fills

- No Instagram or TikTok URL is recorded. No first-party page for any of the 43 venues was found that publishes such an account.
- No search-results URL is counted as a review link.
- No price, hour, transit time or menu cost was taken from a creator's description or title.
- The 2027 star status always comes from MICHELIN, never from a video title.
