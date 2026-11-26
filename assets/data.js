/* Beijing 2027 Trip Planner — verified source dataset (session 1fa0d691, 2026-11-26).
   Every non-blank price, address, phone, hour, bed/bath detail, amenity, transit leg, and
   social URL is drawn directly from an official page, live Booking.com listing, or oEmbed-verified
   video checked in this repository. Unverified fields remain blank and flagged. */

const META = {
  updated: "2026-11-26",
  session: "1fa0d691 + 1ac7826d",
  targetDates: "2027-02-15 to 2027-02-22 (7 nights, post-Spring Festival; brief's 15–18 Feb 3-night window flagged)",
  springFestival2027: "Sat 6 Feb 2027 (official PRC State Council break Feb 5–13; make-up Sun Feb 14)",
  guideEdition: "MICHELIN Guide Beijing 2027 (released 28 Oct 2026: 33 starred, 32 Bib Gourmand, 42 Selected = 107 total)",
  sources: {
    michelinRelease: "https://www.michelin.com/en/publications/products-and-services/michelin-guide-unveils-the-2027-beijing-tianjin-selection",
    michelinStarred: "https://guide.michelin.com/us/en/beijing-municipality/beijing/restaurants/all-starred",
    michelinBib: "https://guide.michelin.com/us/en/beijing-municipality/beijing/restaurants/bib-gourmand",
    michelinSelected: "https://guide.michelin.com/us/en/beijing-municipality/beijing/restaurants/the-plate-michelin",
    stateCouncil2027: "https://english.www.gov.cn/policies/latestreleases/202611/06/content_WS6aed74dcc6d00ca5f9a0e22e.html",
    beijingGov: "https://english.beijing.gov.cn/",
    palaceMuseum: "https://intl.dpm.org.cn/visit.html",
    nationalMuseum: "https://en.chnmuseum.cn/visit_692/",
    mutianyu: "https://en.mutianyugreatwall.com/",
    visa: "https://travel.state.gov/en/international-travel/travel-advisories/china.html",
    socialIndex: "social-2027/data/social.json",
    transitRef: "https://www.rome2rio.com/s/Wangfujing-Station/Guomao-Beijing-Municipality-China"
  }
};

/* ---------- 1. MICHELIN STARRED RESTAURANTS (Beijing 2027: 33 total = 2x3*, 5x2*, 26x1*) ---------- */
const MICHELIN = [
  // 3 MICHELIN Stars
  {s:3, n:"Chao Shang Chao (Chaoyang)", c:"Chao Zhou", p:"¥¥¥¥", d:"Chaoyang",
   a:"L406B, 4F, CP Center, 20 Jinhe East Road, Chaoyang, Beijing", ph:"+86 10 8596 2666",
   w:"", h:"", p2:"",
   note:"3 MICHELIN Stars (retained in 2027). Address & phone verified on guide.michelin.com; hours & prices not published. Off-city video tIBbLQB8Ueo excluded (title names Shanghai).",
   soc:[
     {k:"YT review (唐仁杰)", u:"https://www.youtube.com/watch?v=2Dw1Jkh1SQc"},
     {k:"YT review (特廚隋卞)", u:"https://www.youtube.com/watch?v=FjcHEEL0xcs"},
     {k:"YT interview", u:"https://www.youtube.com/watch?v=SQ9JzAqNpjY"},
     {k:"YT 3★ feature", u:"https://www.youtube.com/watch?v=lC4m_VLOdCY"},
     {k:"YT review (Bay Area)", u:"https://www.youtube.com/watch?v=iaZNyyUDnxc"},
     {k:"IG search", u:"https://www.instagram.com/explore/search/keyword/?q=Chao%20Shang%20Chao%20Beijing"}
   ]},
  {s:3, n:"Xin Rong Ji (Xinyuan South Road)", c:"Taizhou", p:"¥¥¥¥", d:"Chaoyang",
   a:"1F, East Tower, Genesis Beijing, 8 Xinyuan South Road, Chaoyang, Beijing", ph:"+86 10 6501 5501",
   w:"https://www.xinrongji.com/", h:"Mon–Sun 11:30–14:00, 17:30–21:00 (MICHELIN)", p2:"",
   note:"3 MICHELIN Stars (retained in 2027). Phone & hours verified on guide.michelin.com; xinrongji.com is group portal with no menu price.",
   soc:[
     {k:"YT review (Ana Loh)", u:"https://www.youtube.com/watch?v=6SvqIT2SW7M"},
     {k:"YT review (无所尉)", u:"https://www.youtube.com/watch?v=I_UAQlELzVA"},
     {k:"YT review (波儿美食)", u:"https://www.youtube.com/watch?v=0dd524iKZPg"},
     {k:"YT dinner vlog", u:"https://www.youtube.com/watch?v=iKhz-w8cPY8"},
     {k:"IG search", u:"https://www.instagram.com/explore/search/keyword/?q=Xin%20Rong%20Ji%20Beijing"}
   ]},

  // 2 MICHELIN Stars
  {s:2, n:"Blackswan", c:"French Contemporary", p:"¥¥¥¥", d:"Shunyi",
   a:"1F, Luohong Art Museum, 89 Capital Airport Road, Shunyi, Beijing", ph:"+86 10 5385 9911",
   w:"https://www.restaurantblackswan.com/", h:"", p2:"",
   note:"2 MICHELIN Stars. Airport-corridor Shunyi (outside ≤1h central subway cluster; road excursion). Phone verified on guide.michelin.com.",
   soc:[
     {k:"YT short", u:"https://www.youtube.com/shorts/XVF1QjeWKRk"},
     {k:"YT venue clip", u:"https://www.youtube.com/watch?v=b2fxK2c0N9g"},
     {k:"IG search", u:"https://www.instagram.com/explore/search/keyword/?q=Blackswan%20Beijing%20restaurant"}
   ]},
  {s:2, n:"Jingji", c:"Beijing Cuisine", p:"¥¥¥¥", d:"Chaoyang",
   a:"2F, The Ritz-Carlton Hotel, 83A Jianguo Road, Chaoyang, Beijing", ph:"+86 10 5969 5698",
   w:"", h:"", p2:"",
   note:"2 MICHELIN Stars. Address & phone verified on guide.michelin.com; hours & official menu price not published.",
   soc:[
     {k:"YT review", u:"https://www.youtube.com/watch?v=9wni9YGzaTg"},
     {k:"YT short review", u:"https://www.youtube.com/shorts/cB-8dFIIl_Y"},
     {k:"IG search", u:"https://www.instagram.com/explore/search/keyword/?q=Jingji%20Beijing%20Michelin"}
   ]},
  {s:2, n:"King's Joy", c:"Vegetarian", p:"¥¥¥¥", d:"Dongcheng",
   a:"2 Wudaoying Hutong, Dongcheng, Beijing", ph:"+86 10 8404 9191",
   w:"https://www.kingsjoy.com/", h:"Mon–Sun 11:00–22:00 (MICHELIN)", p2:"",
   note:"2 MICHELIN Stars in 2027 (older 2024 videos call it 3-star). Beside Yonghe Temple (Line 5).",
   soc:[
     {k:"YT review (UA Eats)", u:"https://www.youtube.com/watch?v=zbi8tSPRDvs"},
     {k:"YT short review", u:"https://www.youtube.com/shorts/dx2MLoc9blA"},
     {k:"YT review (TastyTrip)", u:"https://www.youtube.com/watch?v=FpN8gqBZ1js"},
     {k:"IG search", u:"https://www.instagram.com/explore/search/keyword/?q=Kings%20Joy%20Beijing"}
   ]},
  {s:2, n:"Lamdre", c:"Vegan", p:"¥¥¥¥", d:"Chaoyang",
   a:"Room 04, 1F, Block 14, Courtyard 4, Gongti North Road, Chaoyang, Beijing", ph:"+86 10 8597 8888",
   w:"", h:"", p2:"",
   note:"2 MICHELIN Stars (Vegan cuisine on guide.michelin.com). Earlier interview clip calls it 1-star; hours & official prices not published.",
   soc:[
     {k:"YT (50 Best)", u:"https://www.youtube.com/watch?v=2Rsj9Q81qAE"},
     {k:"YT (50 Best dish)", u:"https://www.youtube.com/watch?v=rj5Erb_3gIo"},
     {k:"YT (TastyTrip)", u:"https://www.youtube.com/watch?v=PiClQQ0s_Bs"},
     {k:"YT chef interview", u:"https://www.youtube.com/watch?v=SkzeReb61qg"},
     {k:"YT review", u:"https://www.youtube.com/watch?v=_FZ0NlVcgFc"},
     {k:"IG search", u:"https://www.instagram.com/explore/search/keyword/?q=Lamdre%20Beijing"}
   ]},
  {s:2, n:"Lu Shang Lu", c:"Shandong", p:"¥¥¥¥", d:"Chaoyang",
   a:"2A01-2A03 / 2A05-2A13, 2F, Sunshine Financial Center, No.1 Tower, 33 Jinghui Street, Chaoyang, Beijing", ph:"+86 10 8718 5556",
   w:"", h:"", p2:"",
   note:"2 MICHELIN Stars, CBD Guomao (~8 min subway from Wangfujing). Note: MICHELIN page Google Map embed is broken/mismatched (v1/undefined / southern Beijing pin 39.73727,116.32824 vs verified CBD street address).",
   soc:[
     {k:"YT review (特廚隋卞)", u:"https://www.youtube.com/watch?v=kk3L2zMwkMw"},
     {k:"YT review (Weiwei)", u:"https://www.youtube.com/watch?v=ZRIA1Vl8sXI"},
     {k:"YT review (弘举)", u:"https://www.youtube.com/watch?v=_eBigft9cmc"},
     {k:"IG search", u:"https://www.instagram.com/explore/search/keyword/?q=Lu%20Shang%20Lu%20Beijing"}
   ]},

  // 1 MICHELIN Star (26 total)
  {s:1, n:"Cai Yi Xuan", c:"Cantonese", p:"¥¥¥", d:"Chaoyang",
   a:"2F, Four Seasons Hotel, 48 Liangmaqiao Road, Chaoyang, Beijing", ph:"+86 10 5695 8520",
   w:"https://www.fourseasons.com/beijing/dining/restaurants/cai_yi_xuan/",
   h:"Daily 11:30–14:00, 17:30–22:00 (Four Seasons site)",
   p2:"CNY 1,688 Set Menu for Two +10% svc +6% tax (CNY 1,958 additive / 1,968 compounded)",
   note:"Hours & Taste of Cai Yi Xuan Set Menu for Two verified on fourseasons.com.",
   soc:[
     {k:"YT search", u:"https://www.youtube.com/results?search_query=Cai+Yi+Xuan+Four+Seasons+Beijing+review"},
     {k:"IG search", u:"https://www.instagram.com/explore/search/keyword/?q=Cai%20Yi%20Xuan%20Beijing"}
   ]},
  {s:1, n:"Chao Shang Chao (Xicheng)", c:"Chao Zhou", p:"¥¥¥", d:"Xicheng",
   a:"Basement Level, Winland IFC, 7 Jinrong Street, Xicheng, Beijing", ph:"+86 10 6609 1266",
   w:"", h:"", p2:"",
   note:"Verified address & phone on guide.michelin.com; hours & menu price not published. Do not confuse with Chaoyang 3★ branch.",
   soc:[
     {k:"YT search", u:"https://www.youtube.com/results?search_query=Chao+Shang+Chao+Xicheng+Beijing"}
   ]},
  {s:1, n:"Chef 1996", c:"Sichuan", p:"¥¥¥", d:"Chaoyang",
   a:"4A Jiangtaiwa, Xinghuo East Road, Chaoyang, Beijing", ph:"+86 135 2150 9321",
   w:"https://www.chef1996.com/",
   h:"Daily 11:00–14:00, 16:30–23:00 (Malay Mail Jun 2026 profile; confirm direct)",
   p2:"",
   note:"Promoted to 1★ in 2027. @chef1996restaurant IG verified directly on Instagram (link back to chef1996.com); hours per Malay Mail Jun 2026 press report.",
   soc:[
     {k:"YT review (弘举)", u:"https://www.youtube.com/watch?v=3YTgh6MEQ8g"},
     {k:"YT review (Weiwei)", u:"https://www.youtube.com/watch?v=2hI8Dh2F2n0"},
     {k:"IG (@chef1996restaurant)", u:"https://www.instagram.com/chef1996restaurant/"}
   ]},
  {s:1, n:"Fu Chun Ju", c:"Cantonese", p:"¥¥¥", d:"Dongcheng",
   a:"3F, The Puxuan Hotel, 1 Wangfujing Street, Dongcheng, Beijing", ph:"+86 10 5280 6418",
   w:"https://thepuxuan.com/en/beijing-wangfujing-luxury-hotel-dining/cantonese-cuisine-fu-chun-ju-restaurant/",
   h:"Mon–Sun 11:30–14:30, 17:30–21:30 (MICHELIN & PuXuan)",
   p2:"À la carte PDF: starters RMB 88–328 · roast pigeon RMB 98 · brisket RMB 498 (+15% svc; no fixed tasting total)",
   note:"Inside The PuXuan Hotel (Wangfujing). Official à la carte PDF & daily hours verified.",
   soc:[
     {k:"YT review (特廚隋卞)", u:"https://www.youtube.com/watch?v=Z8qFZ3jvAEk"},
     {k:"YT review (弘举)", u:"https://www.youtube.com/watch?v=ZULjI-TdQeA"},
     {k:"IG search", u:"https://www.instagram.com/explore/search/keyword/?q=Fu%20Chun%20Ju%20PuXuan%20Beijing"}
   ]},
  {s:1, n:"Furong", c:"Hunanese", p:"¥¥¥", d:"Xicheng",
   a:"1F, The Westin, 9C Jinrong Street, Xicheng, Beijing", ph:"+86 10 6600 7175",
   w:"https://www.xinrongji.com/", h:"", p2:"",
   note:"Xin Rong Ji Group Hunanese flagship on Financial Street (Xicheng). Hours & official menu price not published.",
   soc:[
     {k:"YT review (Lao Wanzi)", u:"https://www.youtube.com/watch?v=EdcvGYIQMuY"},
     {k:"IG search", u:"https://www.instagram.com/explore/search/keyword/?q=Furong%20Beijing%20Michelin"}
   ]},
  {s:1, n:"Gastro Esthetics DaDong", c:"Chinese Contemporary", p:"¥¥¥", d:"Dongcheng",
   a:"1-2F, Nanxincang Business Tower, 22A Dongsi 10th Alley, Dongcheng, Beijing", ph:"+86 51690328",
   w:"https://www.dadongdadong.com/", h:"", p2:"",
   note:"Flagged: MICHELIN prints phone '+86 51690328' without Beijing's '10' city area code. Brand-level DaDong YouTube clips do not specify this branch; hours not published.",
   soc:[
     {k:"YT (特廚隋卞 - brand)", u:"https://www.youtube.com/watch?v=OVH3HABM794"},
     {k:"YT (chef interview)", u:"https://www.youtube.com/watch?v=XRKJqKZfo1I"},
     {k:"IG search", u:"https://www.instagram.com/explore/search/keyword/?q=DaDong%20Nanxincang%20Beijing"}
   ]},
  {s:1, n:"Giada Garden", c:"Italian", p:"¥¥¥¥", d:"Chaoyang",
   a:"3F, China World Hotel, 1 Jianguomenwai Street, Chaoyang, Beijing", ph:"+86 10 6505 7671",
   w:"https://www.shangri-la.com/beijing/chinaworld/dining/restaurants/giada-garden/",
   h:"Mon–Sun 11:30–14:30, 17:30–22:00 (MICHELIN & Shangri-La)",
   p2:"RMB 3,976 for two (RMB 1,988 pp Degustation PDF; +RMB 988 wine pairing; confirm service charge)",
   note:"Guomao CBD (China World Hotel). Hours & Degustation Menu PDF verified (secondary phone +86 10 6505 7682 also listed).",
   soc:[
     {k:"YT search", u:"https://www.youtube.com/results?search_query=Giada+Garden+Beijing+Michelin"}
   ]},
  {s:1, n:"Il Ristorante – Niko Romito", c:"Italian", p:"¥¥¥¥", d:"Chaoyang",
   a:"1F, Bvlgari Hotel, Building 2, Courtyard 8, Xinyuan South Road, Chaoyang, Beijing", ph:"+86 10 8555 8585",
   w:"https://www.bulgarihotels.com/en_US/beijing/dining/il-ristorante-niko-romito",
   h:"Mon–Sat 12:00–14:30 & 18:00–22:00; Sun 12:00–15:00 & 18:00–22:00 (MICHELIN)",
   p2:"",
   note:"Liangmaqiao riverfront. Hours verified on MICHELIN; official Autumn PDF states prices include tax & svc, though numeric totals did not extract.",
   soc:[
     {k:"YT (Bvlgari official)", u:"https://www.youtube.com/watch?v=Y-7NIh7KR-c"},
     {k:"YT short (Bvlgari)", u:"https://www.youtube.com/watch?v=E8Lg79sXpKc"},
     {k:"IG search", u:"https://www.instagram.com/explore/search/keyword/?q=Il%20Ristorante%20Niko%20Romito%20Beijing"}
   ]},
  {s:1, n:"Lei Garden (Jinbao Tower)", c:"Cantonese", p:"¥¥¥", d:"Dongcheng",
   a:"3F, Jinbao Tower, 89 Jinbao Street, Dongcheng, Beijing", ph:"+86 10 8522 1212",
   w:"https://leigarden.hk/", h:"Daily 11:30–15:00, 17:30–22:30 (leigarden.hk)", p2:"",
   note:"Jinbao Street (Dongcheng, walkable from Wangfujing). Hours verified on leigarden.hk/location/china/; menu prices not published.",
   soc:[
     {k:"YT review", u:"https://www.youtube.com/watch?v=2XgVLAuptC8"},
     {k:"IG search", u:"https://www.instagram.com/explore/search/keyword/?q=Lei%20Garden%20Jinbao%20Beijing"}
   ]},
  {s:1, n:"Lu Style (Anding Road)", c:"Shandong", p:"¥¥¥", d:"Chaoyang",
   a:"5F, Uni Elite, Building 6, Courtyard 5, Anding Road, Chaoyang, Beijing", ph:"+86 10 6441 3777",
   w:"", h:"", p2:"",
   note:"Verified address & phone on guide.michelin.com; hours & official menu price not published.",
   soc:[
     {k:"YT search", u:"https://www.youtube.com/results?search_query=Lu+Style+Anding+Road+Beijing+Michelin"}
   ]},
  {s:1, n:"Mansion Cuisine by Jingyan", c:"Beijing Cuisine", p:"¥¥¥¥", d:"Dongcheng",
   a:"22 Jianchang Hutong, Dongcheng, Beijing", ph:"+86 10 8663 2999",
   w:"", h:"", p2:"",
   note:"Dongcheng courtyard mansion. Verified address & phone on guide.michelin.com; YouTube video verified; hours/price not published.",
   soc:[
     {k:"YT review (Mansion Cuisine)", u:"https://www.youtube.com/watch?v=Yok9qkb4bKw"},
     {k:"YT search", u:"https://www.youtube.com/results?search_query=Mansion+Cuisine+by+Jingyan+Beijing"}
   ]},
  {s:1, n:"MO Jasmine", c:"Beijing Cuisine", p:"¥¥¥", d:"Chaoyang",
   a:"L307, 3F, CP Center, 20 Jinhe East Road, Chaoyang, Beijing", ph:"+86 10 8582 1919",
   w:"", h:"", p2:"",
   note:"Guomao CP Center (same complex as Chao Shang Chao). Address/phone verified; hours/price not published.",
   soc:[
     {k:"YT search", u:"https://www.youtube.com/results?search_query=MO+Jasmine+Beijing+Michelin"}
   ]},
  {s:1, n:"Old Tower", c:"Innovative", p:"¥¥¥¥", d:"Chaoyang",
   a:"40A, 4F, Building N4, North, TaiKoo Li Sanlitun, 11 Sanlitun Road, Chaoyang, Beijing", ph:"+86 139 1020 8150",
   w:"https://www.oldtower.cn/",
   h:"Wed–Sun 18:00–22:00 (closed Mon–Tue; Malay Mail Jun 2026 profile)",
   p2:"",
   note:"New 2027 1★ debut (chef Talib Hudda). @oldtower_beijing IG verified directly on Instagram; hours per Malay Mail Jun 2026 profile (note Mon–Tue closure).",
   soc:[
     {k:"IG (@oldtower_beijing)", u:"https://www.instagram.com/oldtower_beijing/"},
     {k:"YT search", u:"https://www.youtube.com/results?search_query=Old+Tower+Beijing+restaurant+Sanlitun"}
   ]},
  {s:1, n:"Poetry·Wine (Dongsanhuan Middle Road)", c:"Beijing Cuisine", p:"¥¥", d:"Chaoyang",
   a:"61 Dongsanhuan Middle Road, Chaoyang, Beijing", ph:"+86 10 8777 4188",
   w:"", h:"", p2:"",
   note:"Value-band (¥¥ on live MICHELIN guide) Beijing starred kitchen in Chaoyang CBD. Hours/price not published.",
   soc:[
     {k:"YT search", u:"https://www.youtube.com/results?search_query=Poetry+Wine+Beijing+Michelin"}
   ]},
  {s:1, n:"Rong Pao", c:"Sichuan", p:"¥¥¥", d:"Chaoyang",
   a:"2F, The Ritz-Carlton Hotel, 83A Jianguo Road, Chaoyang, Beijing", ph:"+86 10 6616 6636",
   w:"", h:"", p2:"",
   note:"Xin Rong Ji Group Sichuan dining room at Ritz-Carlton / China Central Place.",
   soc:[
     {k:"YT review (特廚隋卞)", u:"https://www.youtube.com/watch?v=aa97MuXH0UY"},
     {k:"IG search", u:"https://www.instagram.com/explore/search/keyword/?q=Rong%20Pao%20Beijing"}
   ]},
  {s:1, n:"Seventh Son", c:"Cantonese", p:"¥¥¥", d:"Chaoyang",
   a:"B1 Level, Jiaming Center, 27 Dongsanhuan North Road, Chaoyang, Beijing", ph:"+86 10 8571 6888",
   w:"https://www.seventhson.hk/", h:"", p2:"",
   note:"Address/phone/site verified on guide.michelin.com; Beijing hours/menu prices not published on homepage.",
   soc:[
     {k:"YT search", u:"https://www.youtube.com/results?search_query=Seventh+Son+Beijing+Michelin"}
   ]},
  {s:1, n:"Shanghai Cuisine", c:"Shanghainese", p:"¥¥¥", d:"Chaoyang",
   a:"South side of Pacific Century Place, 2A Gongrentiyuchang North Road, Chaoyang, Beijing", ph:"+86 10 6539 8660",
   w:"", h:"", p2:"",
   note:"Moved from 2★ (2026) to 1★ in 2027. Sanlitun / Workers' Stadium North Rd. Hours/price not published.",
   soc:[
     {k:"YT search", u:"https://www.youtube.com/results?search_query=Shanghai+Cuisine+Beijing+Michelin"}
   ]},
  {s:1, n:"Sheng Yong Xing (Chaoyang)", c:"Beijing Cuisine", p:"¥¥¥", d:"Chaoyang",
   a:"5 Xindong Road, Chaoyang, Beijing", ph:"+86 10 6464 0968",
   w:"", h:"", p2:"",
   note:"Sanlitun/Xindong Rd Peking duck flagship. Verified YouTube video; hours/price not published on MICHELIN.",
   soc:[
     {k:"YT review", u:"https://www.youtube.com/watch?v=jaZr6qWh0s0"},
     {k:"YT search", u:"https://www.youtube.com/results?search_query=Sheng+Yong+Xing+Chaoyang+Beijing"}
   ]},
  {s:1, n:"The Beijing Kitchen (Jianguo Road)", c:"Cantonese", p:"¥¥", d:"Chaoyang",
   a:"D6007, 6F, SKP Beijing, 87 Jianguo Road, Chaoyang, Beijing", ph:"+86 10 6530 7905",
   w:"", h:"", p2:"",
   note:"Value-tier (¥¥ on live MICHELIN guide) 1★ Cantonese at SKP Beijing. Hours/price not published.",
   soc:[
     {k:"YT short (#北京厨房)", u:"https://www.youtube.com/shorts/4zvpjQt2zpw"},
     {k:"IG search", u:"https://www.instagram.com/explore/search/keyword/?q=Beijing%20Kitchen%20SKP"}
   ]},
  {s:1, n:"The Georg", c:"European Contemporary", p:"¥¥¥¥", d:"Dongcheng",
   a:"95 Donghuamen Street, Dongcheng, Beijing", ph:"+86 186 1833 7710",
   w:"", h:"", p2:"",
   note:"Steps from Forbidden City East Gate (Donghuamen). Address/phone verified; hours/price not published.",
   soc:[
     {k:"YT search", u:"https://www.youtube.com/results?search_query=The+Georg+Beijing+Michelin"}
   ]},
  {s:1, n:"The House of Dynasties", c:"Cantonese", p:"¥¥¥", d:"Chaoyang",
   a:"4F, Rosewood Hotel, Jing Guang Centre, Hujialou, 1 Chaoyangmenwai Street, Chaoyang, Beijing", ph:"+86 10 6536 0066",
   w:"https://www.rosewoodhotels.com/en/beijing/dining/the-house-of-dynasties",
   h:"Daily 11:30–14:30, 17:30–22:00 (Rosewood Beijing site)",
   p2:"",
   note:"Inside Rosewood Beijing (Hujialou). Hours verified on Rosewood site; menu prices not published online.",
   soc:[
     {k:"YT search", u:"https://www.youtube.com/results?search_query=The+House+of+Dynasties+Rosewood+Beijing"}
   ]},
  {s:1, n:"Trb Hutong", c:"French Contemporary", p:"¥¥¥¥", d:"Dongcheng",
   a:"23 Shatan North Street, Dongcheng, Beijing", ph:"+86 139 1171 2083",
   w:"https://www.trbhutong.com/", h:"Mon–Sun 11:30–14:30, 17:30–22:00 (trbhutong.com)",
   p2:"¥3,882 total for 2 on Seasonal (¥788 lunch / ¥1,688 seasonal / ¥2,288 signature pp + 15% svc, trbhutong.com/menu)",
   note:"Hours, phone & tasting prices verified on trbhutong.com & guide.michelin.com. Private video Sy0Df7KVfJk removed.",
   soc:[
     {k:"YT search", u:"https://www.youtube.com/results?search_query=TRB+Hutong+Beijing+review"},
     {k:"IG search", u:"https://www.instagram.com/explore/search/keyword/?q=TRB%20Hutong%20Beijing"}
   ]},
  {s:1, n:"Xin Rong Ji (Jianguomenwai Street)", c:"Taizhou", p:"¥¥¥", d:"Chaoyang",
   a:"5F, Tower A, Yintai Centre, 2 Jianguomenwai Street, Chaoyang, Beijing", ph:"+86 10 8517 1789",
   w:"https://www.xinrongji.com/", h:"", p2:"",
   note:"Guomao Yintai Centre branch (¥¥¥ & +86 10 8517 1789 verified on guide.michelin.com). Hours/price not published.",
   soc:[
     {k:"YT search", u:"https://www.youtube.com/results?search_query=Xin+Rong+Ji+Yintai+Beijing"}
   ]},
  {s:1, n:"Xin Rong Ji (Jinrong Street)", c:"Taizhou", p:"¥¥¥", d:"Xicheng",
   a:"B1 Level, International Finance Centre, 11 Jinrong Street, Xicheng, Beijing", ph:"+86 10 6618 0567",
   w:"https://www.xinrongji.com/", h:"Mon–Sun 11:00–14:00, 17:00–21:30 (MICHELIN)", p2:"",
   note:"Financial Street (Xicheng) branch. ¥¥¥ band, phone & hours verified on guide.michelin.com.",
   soc:[
     {k:"YT search", u:"https://www.youtube.com/results?search_query=Xin+Rong+Ji+Financial+Street+Beijing"}
   ]},
  {s:1, n:"Zhiguan Courtyard", c:"Dongbei", p:"¥¥¥", d:"Dongcheng",
   a:"12 Jinyu Hutong, Dongcheng, Beijing", ph:"+86 10 6559 9899",
   w:"", h:"", p2:"",
   note:"Directly opposite Waldorf Astoria in Jinyu Hutong (Wangfujing). No official website on MICHELIN; verified YT review; hours/price not published.",
   soc:[
     {k:"YT review (Zhiguan)", u:"https://www.youtube.com/watch?v=I9xaH24FLnc"},
     {k:"YT search", u:"https://www.youtube.com/results?search_query=Zhiguan+Courtyard+Beijing+Michelin"}
   ]},
  {s:1, n:"Zijin Mansion", c:"Cantonese", p:"¥¥¥", d:"Dongcheng",
   a:"3F, Waldorf Astoria Hotel, 5-15 Jinyu Hutong, Dongcheng, Beijing", ph:"+86 10 8520 8989",
   w:"https://www.hilton.com/en/hotels/bjswawa-waldorf-astoria-beijing/dining/zijin-mansion/",
   h:"", p2:"",
   note:"Inside Waldorf Astoria Beijing (Wangfujing). Hilton dining URL timed out / 500; hours/price unverified.",
   soc:[
     {k:"YT search", u:"https://www.youtube.com/results?search_query=Zijin+Mansion+Waldorf+Astoria+Beijing"}
   ]}
];

const GUIDE_SLUG = {
  "Chao Shang Chao (Chaoyang)": "chao-shang-chao",
  "Xin Rong Ji (Xinyuan South Road)": "xin-rong-ji-xinyuan-south-road",
  "Blackswan": "blackswan",
  "Jingji": "jingji",
  "King's Joy": "king-s-joy",
  "Lamdre": "lamdre",
  "Lu Shang Lu": "lu-shang-lu",
  "Cai Yi Xuan": "cai-yi-xuan",
  "Chao Shang Chao (Xicheng)": "chao-shang-chao-xicheng",
  "Chef 1996": "chef-1996",
  "Fu Chun Ju": "fu-chun-ju",
  "Furong": "furong",
  "Gastro Esthetics DaDong": "gastro-esthetics-dadong",
  "Giada Garden": "giada-garden",
  "Il Ristorante – Niko Romito": "il-ristorante-niko-romito-1186723",
  "Lei Garden (Jinbao Tower)": "lei-garden-jinbao-tower",
  "Lu Style (Anding Road)": "lu-style",
  "Mansion Cuisine by Jingyan": "mansion-cuisine-by-jingyan",
  "MO Jasmine": "mo-jasmine",
  "Old Tower": "old-tower",
  "Poetry·Wine (Dongsanhuan Middle Road)": "poetry%E2%80%A7wine",
  "Rong Pao": "rong-pao",
  "Seventh Son": "seventh-son-1186794",
  "Shanghai Cuisine": "shanghai-cuisine",
  "Sheng Yong Xing (Chaoyang)": "sheng-yong-xing-chaoyang",
  "The Beijing Kitchen (Jianguo Road)": "the-beijing-kitchen",
  "The Georg": "the-georg",
  "The House of Dynasties": "the-house-of-dynasties",
  "Trb Hutong": "trb-hutong",
  "Xin Rong Ji (Jianguomenwai Street)": "xin-rong-ji-jianguomenwai-street",
  "Xin Rong Ji (Jinrong Street)": "xin-rong-ji-jinrong-street",
  "Zhiguan Courtyard": "zhiguan",
  "Zijin Mansion": "zijin-mansion"
};

/* ---------- 1B. NON-STARRED MICHELIN GUIDE BEIJING 2027 (32 Bib Gourmand + 42 Selected = 74) ---------- */
const MICHELIN_LISTED = [
  // 32 Bib Gourmand (good quality, good value cooking — NOT starred)
  {tier:"Bib Gourmand", n:"Mingyuan Restaurant", c:"Beijing Cuisine", p:"¥¥", slug:"mingyuan-restaurant"},
  {tier:"Bib Gourmand", n:"Bao Du Jin Sheng Long (Dongcheng)", c:"Hotpot", p:"¥¥", slug:"bao-du-jin-sheng-long"},
  {tier:"Bib Gourmand", n:"Tong He Ju (Yuetan South Street)", c:"Shandong", p:"¥¥", slug:"tong-he-ju-yuetan-south-street"},
  {tier:"Bib Gourmand", n:"Yibin", c:"Sichuan", p:"¥", slug:"yibin"},
  {tier:"Bib Gourmand", n:"Yu Hua Tai (Xicheng)", c:"Huaiyang", p:"¥¥", slug:"yu-hua-tai-xicheng"},
  {tier:"Bib Gourmand", n:"Man Heng Ji", c:"Hotpot", p:"¥¥", slug:"niujie-halal-man-heng-ji"},
  {tier:"Bib Gourmand", n:"Jingyi (Liulichang East Street)", c:"Hubei", p:"¥", slug:"jingyi"},
  {tier:"Bib Gourmand", n:"Chen Ji Lu Zhu Xiao Chang", c:"Small eats", p:"¥", slug:"chen-ji-lu-zhu-xiao-chang"},
  {tier:"Bib Gourmand", n:"Pang Mei Noodles (Xiang'er Hutong)", c:"Noodles", p:"¥", slug:"pang-mei-noodles"},
  {tier:"Bib Gourmand", n:"Bao Bao Hao", c:"Cantonese", p:"¥¥", slug:"bao-bao-hao"},
  {tier:"Bib Gourmand", n:"No. 69 Fangzhuanchang Zhajiangmian (Fangzhuanchang Hutong)", c:"Noodles", p:"¥", slug:"no-69-fangzhuanchang-zhajiangmian"},
  {tier:"Bib Gourmand", n:"Pan Zhi Hua Yin Xiang", c:"Sichuan", p:"¥¥", slug:"pan-zhi-hua-yin-xiang"},
  {tier:"Bib Gourmand", n:"Lao Chuan Ban (Dongcheng)", c:"Sichuan", p:"¥¥", slug:"lao-chuan-ban"},
  {tier:"Bib Gourmand", n:"Zhong", c:"Huaiyang", p:"¥¥", slug:"zhong"},
  {tier:"Bib Gourmand", n:"Fujian Yu Shan Tang", c:"Fujian", p:"¥¥", slug:"fujian-yu-shan-tang"},
  {tier:"Bib Gourmand", n:"Rong Cuisine (Baiziwan South Er Road)", c:"Taizhou", p:"¥¥", slug:"rong-cuisine-baiziwan-south-er-road"},
  {tier:"Bib Gourmand", n:"Bao Yuan", c:"Dumplings", p:"¥", slug:"bao-yuan"},
  {tier:"Bib Gourmand", n:"Wan Hong Lu Yang Tang Shao Bing Dian", c:"Small eats", p:"¥", slug:"wan-hong-lu-yang-tang-shao-bing-dian"},
  {tier:"Bib Gourmand", n:"Hong Fan Qie (Yuyuantan South Road)", c:"Hubei", p:"¥¥", slug:"hong-fan-qie-yuyuantan-south-road"},
  {tier:"Bib Gourmand", n:"Xiang Lin Tian Xia", c:"Hunanese", p:"¥¥", slug:"xiang-lin-tian-xia"},
  {tier:"Bib Gourmand", n:"Jing Hua Lou", c:"Beijing Cuisine", p:"¥¥", slug:"jing-hua-lou"},
  {tier:"Bib Gourmand", n:"My Soup", c:"Cantonese", p:"¥¥", slug:"my-soup"},
  {tier:"Bib Gourmand", n:"Tianchumiaoxiang Vegetarian (Chaoyang)", c:"Vegetarian", p:"¥", slug:"tianchumiaoxiang-vegetarian-chaoyang"},
  {tier:"Bib Gourmand", n:"Xiang Bin Xuan (Huayuan Road)", c:"Hunanese", p:"¥¥", slug:"xiang-bin-xuan-huayuan-road"},
  {tier:"Bib Gourmand", n:"Qiantang Garden (Shuangyushu North Road)", c:"Ningbo", p:"¥¥", slug:"qiantang-garden"},
  {tier:"Bib Gourmand", n:"Hua Sheng Feng (Dongsanhuan South Road)", c:"Zhejiang", p:"¥¥", slug:"hua-sheng-feng-dongsanhuan-south-road"},
  {tier:"Bib Gourmand", n:"Zhe Xian Xiao Chu (Chaoyang)", c:"Taizhou", p:"¥¥", slug:"zhe-xian-xiao-chu-chaoyang"},
  {tier:"Bib Gourmand", n:"Fujian Cuisine (Dongsanhuan North Road)", c:"Fujian", p:"¥¥", slug:"fujian-cuisine-dongsanhuan-north-road"},
  {tier:"Bib Gourmand", n:"Louyau", c:"Cantonese", p:"¥¥", slug:"louyau"},
  {tier:"Bib Gourmand", n:"Fragrant Kitchen (Chaoyang)", c:"Shandong", p:"¥¥", slug:"fragrant-kitchen-chaoyang"},
  {tier:"Bib Gourmand", n:"Tan", c:"Sichuan", p:"¥¥", slug:"tan-1218718"},
  {tier:"Bib Gourmand", n:"Liu Ma Ma Dumplings (Chaoyang)", c:"Dumplings", p:"¥", slug:"liu-ma-ma-dumplings-chaoyang"},

  // 42 MICHELIN Selected (Guide-recommended, NOT starred)
  {tier:"MICHELIN Selected", n:"Yan Garden by Chef Fei", c:"Chao Zhou", p:"¥¥¥¥", slug:"yan-garden-by-chef-fei"},
  {tier:"MICHELIN Selected", n:"Rive Gauche", c:"French Contemporary", p:"¥¥¥", slug:"rive-gauche-1186760"},
  {tier:"MICHELIN Selected", n:"Qu Lang Yuan", c:"Innovative", p:"¥¥¥", slug:"curvy-corridor-courtyard"},
  {tier:"MICHELIN Selected", n:"1949 - Duck de Chine", c:"Cantonese", p:"¥¥¥", slug:"1949-duck-de-chine"},
  {tier:"MICHELIN Selected", n:"Tong Chun Yuan", c:"Jiangzhe", p:"¥¥", slug:"tong-chun-yuan"},
  {tier:"MICHELIN Selected", n:"Fortune Long Beijing Bean Sauce Noodles (East Xinglong Street)", c:"Beijing Cuisine", p:"¥", slug:"fortune-long-beijing-bean-sauce-noodles-east-xinglong-street"},
  {tier:"MICHELIN Selected", n:"Granary", c:"Huaiyang", p:"¥¥¥", slug:"granary"},
  {tier:"MICHELIN Selected", n:"Brasserie 1893", c:"French Contemporary", p:"¥¥¥", slug:"brasserie-1893"},
  {tier:"MICHELIN Selected", n:"Under Clouds Green", c:"Vegetarian", p:"¥¥¥", slug:"under-clouds-green"},
  {tier:"MICHELIN Selected", n:"Hong 0871", c:"Yunnanese", p:"¥¥", slug:"hong-0871-1203720"},
  {tier:"MICHELIN Selected", n:"Huaiyang Fu (Dongcheng)", c:"Huaiyang", p:"¥¥", slug:"huaiyang-fu"},
  {tier:"MICHELIN Selected", n:"Monsieur Dior by Anne-Sophie Pic", c:"French Contemporary", p:"¥¥¥¥", slug:"monsieur-dior-by-anne-sophie-pic"},
  {tier:"MICHELIN Selected", n:"Everlasting Happiness", c:"Hunanese", p:"¥¥¥", slug:"everlasting-happiness"},
  {tier:"MICHELIN Selected", n:"Yu De Fu", c:"Hotpot", p:"¥¥", slug:"yu-de-fu"},
  {tier:"MICHELIN Selected", n:"In Love", c:"Hunanese", p:"¥¥¥", slug:"in-love-gongti-east-road"},
  {tier:"MICHELIN Selected", n:"Ji Chuan", c:"Sichuan", p:"¥¥", slug:"ji-chuan"},
  {tier:"MICHELIN Selected", n:"Mio", c:"Italian", p:"¥¥¥", slug:"mio"},
  {tier:"MICHELIN Selected", n:"Maison Flo", c:"French", p:"¥¥¥", slug:"maison-flo"},
  {tier:"MICHELIN Selected", n:"L. Bodhi (Guanghua Road)", c:"Vegetarian", p:"¥¥¥¥", slug:"l-bodhi-guanghua-road"},
  {tier:"MICHELIN Selected", n:"Jing Cai Xuan", c:"Cantonese", p:"¥¥¥", slug:"exquisite-bocuse"},
  {tier:"MICHELIN Selected", n:"Meng Du Hui", c:"Hui Cuisine", p:"¥¥", slug:"meng-du-hui"},
  {tier:"MICHELIN Selected", n:"Jia (Chaoyang)", c:"Cantonese", p:"¥¥¥", slug:"jia"},
  {tier:"MICHELIN Selected", n:"Fujian Restaurant", c:"Fujian", p:"¥¥¥", slug:"fujian-restaurant"},
  {tier:"MICHELIN Selected", n:"Héritage East", c:"Chinese Contemporary", p:"¥¥¥", slug:"heritage-east"},
  {tier:"MICHELIN Selected", n:"Fu Man Yuan (Xinyuanli)", c:"Beijing Cuisine", p:"¥¥", slug:"fu-man-yuan-xinyuanli"},
  {tier:"MICHELIN Selected", n:"Xiang Shang Xiang (Jinhe East Road)", c:"Hunanese", p:"¥¥¥", slug:"xiang-shang-xiang-jinhe-east-road"},
  {tier:"MICHELIN Selected", n:"Bistro Strong (Chaoyanggongyuan Road)", c:"Meats and Grills", p:"¥¥", slug:"bistro-strong"},
  {tier:"MICHELIN Selected", n:"Beef & Dumplings (Chaoyang)", c:"Dumplings", p:"¥", slug:"beef-dumplings"},
  {tier:"MICHELIN Selected", n:"Country Kitchen", c:"Beijing Cuisine", p:"¥¥¥", slug:"country-kitchen"},
  {tier:"MICHELIN Selected", n:"Qiao Dong Bei (Dongcheng)", c:"Dongbei", p:"¥¥", slug:"qiao-dong-bei"},
  {tier:"MICHELIN Selected", n:"Wolfgang's Steakhouse (Gongrentiyuchang North Road)", c:"Steakhouse", p:"¥¥¥¥", slug:"wolfgang-s-steakhouse"},
  {tier:"MICHELIN Selected", n:"Qian Li", c:"Taizhou", p:"¥¥", slug:"qian-li"},
  {tier:"MICHELIN Selected", n:"Huai Xiang Guo Se", c:"Huaiyang", p:"¥¥¥", slug:"huai-xiang-guo-se"},
  {tier:"MICHELIN Selected", n:"Ding Sheng Xin", c:"Shanghainese", p:"¥¥", slug:"ding-sheng-xin"},
  {tier:"MICHELIN Selected", n:"La Chansonnière", c:"French Contemporary", p:"¥¥¥¥", slug:"la-chansonniere"},
  {tier:"MICHELIN Selected", n:"Bad Ass Lamb Hot Pot (Maizidian West Street)", c:"Hotpot", p:"¥¥", slug:"bad-ass-lamb-hot-pot-maizidian-west-street"},
  {tier:"MICHELIN Selected", n:"Amico BJ", c:"European Contemporary", p:"¥¥¥", slug:"amico-bj"},
  {tier:"MICHELIN Selected", n:"Les Morilles", c:"French Contemporary", p:"¥¥¥", slug:"les-morilles"},
  {tier:"MICHELIN Selected", n:"Baiweiyuan Dumpling", c:"Dumplings", p:"¥", slug:"baiweiyuan-dumpling"},
  {tier:"MICHELIN Selected", n:"Char (South Sanlitun Road)", c:"Steakhouse", p:"¥¥¥", slug:"char-south-sanlitun-road"},
  {tier:"MICHELIN Selected", n:"La Roba", c:"Yunnanese", p:"¥¥", slug:"la-roba"},
  {tier:"MICHELIN Selected", n:"Yue Jie (Qi Yang Road)", c:"Cantonese", p:"¥¥¥", slug:"yue-jie-qi-yang-road"}
];

/* ---------- 2. HOTELS (12 Beijing properties: Budget/Mid-range, Boutique Courtyard & 5★ Luxury) ---------- */
/* Live 7-night pricing for 2 adults, 15–22 Feb 2027 (verified 2026-11-26) + Mar 1–8 / Mar 15–22 comparison */
const DISTRICT_STARS = { Chaoyang: 20, Dongcheng: 9, Xicheng: 3, Shunyi: 1 }; // 33 / 33 verified

const HOTELS = [
  {n:"Beijing XinQiao Hotel (Novotel XinQiao)", d:"Dongcheng", area:"Chongwenmen (Lines 2/5 interchange)",
   tier:"4★ Mid-range", rating:"8.2",
   usd:568, listUsd:668, bf:0, bfUsd:751, cancel:"Free cancellation (before 12 Feb 2027)",
   room:"Standard Double Room with Indoor Window", bed:"1 queen bed", kingOk:true,
   bath:"Attached private bathroom confirmed (Booking.com)",
   amenities:"Fitness center, tennis court, natural hot spring water, 6 restaurants, bar, free WiFi, 24h room service",
   mar1:511, mar15:null, bestWindow:"Feb 15–22 ($568 queen free-cancel vs $511 Twin room; earlier Nov 26 Partner Offer $485)",
   transitStars:32, transitActs:9,
   transitNote:"Subway Lines 2 & 5 at door: ~20m to Chaoyang CBD★, ~15m to Wangfujing★, ~10m to Temple of Heaven, ~51m to Summer Palace",
   u:"https://www.booking.com/hotel/cn/novotelxinqiao.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1",
   note:"Live Booking check shows $568 ($751 w/ breakfast) for 1 queen bed w/ free cancellation (10% svc incl, 6% VAT excl); $511 quote is a 2-twin room (earlier Partner Offer $485)."},

  {n:"Holiday Inn Express Beijing Temple of Heaven", d:"Xicheng / Temple of Heaven border", area:"No. 36 Nanwei Road, Xicheng (Tian Qiao Metro)",
   tier:"3–4★ Value (IHG)", rating:"8.3",
   usd:536, listUsd:596, bf:1, bfUsd:536, cancel:"Free cancellation · no prepayment (Genius Rate)",
   room:"1 Queen Standard Air Purifier", bed:"1 queen bed", kingOk:true,
   bath:"Private bathroom confirmed (Booking.com)",
   amenities:"Breakfast included, fitness center, coin launderette, free parking, free WiFi, 24h front desk",
   mar1:536, mar15:505, bestWindow:"Feb 15–22 ($536 Genius / $596 list; earlier Nov 26 snapshot $499) vs $505 Mar 15–22",
   transitStars:32, transitActs:9,
   transitNote:"Walk to Temple of Heaven; Line 8/5 ~18m to Wangfujing, ~28m to Guomao CBD★, ~55m to Summer Palace",
   u:"https://www.booking.com/hotel/cn/holiday-inn-express-beijing-temple-of-heaven.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1",
   note:"Best refundable value: $536 Genius ($596 public; $499 earlier snapshot) for 7 nights WITH breakfast, 1 queen bed, and free cancellation (10% svc incl, 6% VAT excl)."},

  {n:"Sunworld Hotel Wangfujing", d:"Dongcheng", area:"Wangfujing / Dengshikou (Line 5)",
   tier:"4★ Mid-range", rating:"8.4",
   usd:502, listUsd:773, bf:0, bfUsd:571, cancel:"Free cancellation (Black Friday Deal)",
   room:"Superior King Room (select 1 king or 1 twin)", bed:"1 king bed (request/confirm at booking)", kingOk:true,
   bath:"Attached private bathroom confirmed (Booking.com)",
   amenities:"Fitness center, spa, restaurant, bar, free WiFi, 24h front desk (breakfast +$13/p/nt)",
   mar1:581, mar15:590, bestWindow:"Feb 15–22 ($502 Black Friday Deal vs $581 Mar 1–8 / $590 Mar 15–22)",
   transitStars:32, transitActs:9,
   transitNote:"Wangfujing Line 1/5 hub: 8m to Guomao CBD★, 12m to Yonghe Temple, 26m to Temple of Heaven, 51m to Summer Palace, 54m to 798",
   u:"https://www.booking.com/hotel/cn/bei-jing-tian-lun-song-he-da-fan-dian.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1",
   note:"$502 Black Friday Deal (10% svc incl, 6% VAT excl; $571 w/ bfast). Room lists 'Select your bed (if available): 1 twin / 1 king' — confirm king in writing. ($469 Annex Double has full bed only.)"},

  {n:"NUO Hotel Beijing", d:"Chaoyang", area:"Jiuxianqiao / 798 Art District",
   tier:"5★ Luxury", rating:"9.2",
   usd:943, listUsd:943, bf:1, bfUsd:943, cancel:"Free cancellation · no prepayment",
   room:"Deluxe King Room", bed:"1 king bed", kingOk:true,
   bath:"Private bathroom with bathtub confirmed (Booking.com)",
   amenities:"Breakfast included, 25m heated indoor pool, NUO Spa, fitness center, 6 restaurants, tea house, bike rental, free WiFi",
   mar1:943, mar15:null, bestWindow:"Flat ($943 in both Feb 15–22 and Mar 1–8; 10% svc incl, 6% VAT excl)",
   transitStars:28, transitActs:8,
   transitNote:"10-min walk to 798 Art Zone & ~15m to Chef 1996★; ~35m to Dongcheng; Summer Palace >1h by subway",
   u:"https://www.booking.com/hotel/cn/nuo-jin-jiu-dian-nuo-beijing.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1",
   note:"Lowest-priced 5-star king with breakfast ($943) & indoor pool (10% svc incl, 6% VAT excl); NE Chaoyang next to 798."},

  {n:"Peking Yard Boutique Hotel", d:"Dongcheng", area:"Zhangzizhonglu / Nanluoguxiang Hutongs",
   tier:"4★ Courtyard Boutique", rating:"8.9",
   usd:1105, listUsd:1163, bf:1, bfUsd:1105, cancel:"$1,105 non-refundable / $1,163 free cancellation ($995/$1,047 Genius)",
   room:"Economy Double Room", bed:"1 queen bed", kingOk:true,
   bath:"Attached private bathroom confirmed (Booking.com)",
   amenities:"Breakfast included, traditional hutong courtyard, sun terrace, restaurant, bar, library, bicycle rental, laundry, free WiFi",
   mar1:1664, mar15:null, bestWindow:"Feb 15–22 ($1,105/$1,163 public vs $1,664 min in Mar 1–8; entry rooms sold out in March)",
   transitStars:32, transitActs:9,
   transitNote:"Line 5 Zhangzizhonglu: walk to King's Joy/Nanluoguxiang, ~15m to Wangfujing/Guomao★, ~51m to Summer Palace",
   u:"https://www.booking.com/hotel/cn/peking-yard-hostel.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1",
   note:"Traditional hutong courtyard (Booking 8.9/10, 9.4 location) with 1 queen bed, private bath, breakfast & 15% service included."},

  {n:"The Orchid Hotel", d:"Dongcheng", area:"Gulou / Drum Tower Hutongs",
   tier:"4★ Design Boutique", rating:"9.4",
   usd:1194, listUsd:1327, bf:1, bfUsd:1194, cancel:"Free cancellation · no prepayment",
   room:"Garden Room", bed:"1 queen bed", kingOk:true,
   bath:"Attached private bathroom confirmed (Booking.com)",
   amenities:"Breakfast included, rooftop terrace, 3 restaurants (Toast), bar, free bicycles, airport shuttle, free WiFi",
   mar1:1025, mar15:null, bestWindow:"Feb 15–22 ($1,194 Genius / $1,327 public for Queen Garden Room; $923/$1,025 Courtyard Room is 1 full bed)",
   transitStars:32, transitActs:9,
   transitNote:"Line 8 Shichahai: walk to Gulou/Nanluoguxiang, ~25m to Guomao★, ~45m to Summer Palace",
   u:"https://www.booking.com/hotel/cn/the-orchid.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1",
   note:"9.4-rated boutique hotel in Baochao Hutong; Garden Room (1 queen bed, 15% svc incl) is $1,194 Genius / $1,327 public. Note Courtyard Room ($1,025) has 1 full bed only."},

  {n:"Four Seasons Hotel Beijing", d:"Chaoyang", area:"Liangmaqiao / Diplomatic Quarter",
   tier:"5★ Luxury", rating:"9.0",
   usd:1751, listUsd:1945, bf:0, bfUsd:2118, cancel:"$1,751 non-refundable / $1,945 free cancellation",
   room:"Deluxe King Room with City View", bed:"1 king bed (1 queen listed on Booking widget)", kingOk:true,
   bath:"One full marble bathroom confirmed (fourseasons.com & Booking.com)",
   amenities:"Heated indoor pool, sauna, hot tub, spa, 24h fitness center, Cai Yi Xuan (1★) & Mio (Selected) on site, free WiFi",
   mar1:1914, mar15:1950, bestWindow:"Feb 15–22 ($1,751 non-ref / $1,945 ref vs $1,914 Mar 1–8)",
   transitStars:32, transitActs:8,
   transitNote:"Line 10 Liangmaqiao: walk to Xin Rong Ji (3★) & Il Ristorante (1★); ~25m to Dongcheng; Summer Palace ~58m subway / >1h door-to-door",
   u:"https://www.booking.com/hotel/cn/bei-jing-si-ji.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1",
   note:"Lowest-priced ultra-luxury 5-star in Beijing ($1,751 non-ref / $1,945 ref; 10% svc incl, 6.6% VAT excl); marble bath verified on fourseasons.com; houses 1★ Cai Yi Xuan."},

  {n:"Waldorf Astoria Beijing", d:"Dongcheng", area:"Wangfujing / Jinyu Hutong",
   tier:"5★ Luxury", rating:"9.2",
   usd:2243, listUsd:2582, bf:0, bfUsd:2612, cancel:"$2,243 non-refundable / $2,582 free cancellation",
   room:"Deluxe King Room", bed:"1 king bed", kingOk:true,
   bath:"Private marble bathroom w/ double vanities & bathtub (Booking.com & Hilton)",
   amenities:"Heated indoor pool, whirlpool, steam room, spa, fitness center, Peacock Alley, Zijin Mansion (1★) & Brasserie 1893 on site, WiFi",
   mar1:2243, mar15:null, bestWindow:"Feb 15–22 ($2,243 non-ref / $2,582 ref) · $2,556 ref Mar 1–8",
   transitStars:32, transitActs:9,
   transitNote:"Prime Wangfujing hub: 8m Line 1 to Guomao CBD★, walk to Forbidden City & Zijin Mansion/Zhiguan★, 51m to Summer Palace, 54m to 798",
   u:"https://www.booking.com/hotel/cn/waldorf-astoria-beijing.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1",
   note:"Best 5-star central hub for ≤1h transit to BOTH all 9 central sights AND 32/33 starred kitchens (10% svc incl, 6% VAT excl); houses 1★ Zijin Mansion."},

  {n:"Park Hyatt Beijing", d:"Chaoyang", area:"Guomao / China World CBD",
   tier:"5★ Luxury", rating:"8.8",
   usd:2297, listUsd:2552, bf:0, bfUsd:2784, cancel:"$2,297 non-refundable / $2,552 free cancellation ($2,784 w/ bfast)",
   room:"King Room", bed:"1 king bed", kingOk:true,
   bath:"Private bathroom with bath & shower confirmed (Booking.com)",
   amenities:"25m indoor lap pool, hot tub, sauna, Tian Chi Spa, fitness center, 3 restaurants (China Grill), bar, free WiFi",
   mar1:2589, mar15:null, bestWindow:"Feb 15–22 ($2,297 non-ref / $2,552 ref vs $2,589/$2,876 Mar 1–8)",
   transitStars:32, transitActs:8,
   transitNote:"Direct Guomao subway: walk to 6+ CBD★ kitchens; 8m to Wangfujing; Summer Palace ~58m subway / 1h07m bus+metro (>1h door-to-door)",
   u:"https://www.booking.com/hotel/cn/park-hyatt-beijing.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1",
   note:"Right inside Chaoyang's CBD Michelin cluster ($2,297 non-ref / $2,552 ref live Feb check, 10% svc incl, 6% VAT excl; prior snapshot $2,610)."},

  {n:"The PuXuan Hotel and Spa", d:"Dongcheng", area:"Wangfujing / National Art Museum",
   tier:"5★ Luxury", rating:"9.3",
   usd:3114, listUsd:3114, bf:0, bfUsd:3346, cancel:"Free cancellation · no prepayment",
   room:"Grand Room (538 sq ft)", bed:"1 queen bed", kingOk:true,
   bath:"Attached private bathroom confirmed (Booking.com)",
   amenities:"UR Spa, sauna, 24h fitness center, terrace, garden, Fu Chun Ju (1★) & Rive Gauche (Selected) on site, 10% F&B discount, free WiFi",
   mar1:2803, mar15:null, bestWindow:"Mar 1–8 ($2,803 Genius vs $3,114 list in Feb; 16.6% service incl)",
   transitStars:32, transitActs:9,
   transitNote:"Walk to Forbidden City, Trb Hutong & National Art Museum; 8m to Guomao CBD★; 51m to Summer Palace",
   u:"https://www.booking.com/hotel/cn/pu-xuan-jiu-dian-bei-jing.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1",
   note:"Wangfujing architectural luxury hotel (16.6% service charge included); houses 1★ Fu Chun Ju. Note Booking lists 1 queen bed in Grand Room."},

  {n:"Rosewood Beijing", d:"Chaoyang", area:"Hujialou / Chaoyang CBD",
   tier:"5★ Luxury", rating:"8.8",
   usd:3115, listUsd:3115, bf:0, bfUsd:3577, cancel:"Free cancellation · no prepayment (Partner Offer Twin $2,752 non-ref)",
   room:"Deluxe King Room (484 sq ft)", bed:"1 queen bed (per Booking listing)", kingOk:true,
   bath:"Private bathroom with bath or shower confirmed (Booking.com)",
   amenities:"Indoor pool, Sense Spa, yoga studio, fitness center, 7 dining venues incl. The House of Dynasties (1★), free WiFi",
   mar1:3115, mar15:null, bestWindow:"Flat ($3,115 in both Feb 15–22 and Mar 1–8; 10% svc incl, 6% VAT excl)",
   transitStars:32, transitActs:8,
   transitNote:"Line 10/6 Hujialou: 1 stop to Guomao CBD★; ~25m to Dongcheng; Summer Palace ~58m+ (~1h+ door-to-door)",
   u:"https://www.booking.com/hotel/cn/beijing-rosewood.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1",
   note:"Houses 1★ The House of Dynasties. Flat $3,115 rate across Feb and Mar (10% svc incl, 6% VAT excl)."},

  {n:"Courtyard 7 Hotel", d:"Dongcheng", area:"Nanluoguxiang / Qiangulouyuan Hutong",
   tier:"4★ Courtyard Boutique", rating:"8.7",
   usd:null, listUsd:null, bf:0, bfUsd:null, cancel:"Live Feb 2027 Booking.com listing unavailable (redirects to search)",
   room:"Standard Double / Superior Queen (unverified for Feb 2027)", bed:"1 queen / 1 king options (third-party)", kingOk:true,
   bath:"Private bathroom confirmed (20-room property; third-party listings)",
   amenities:"20-room traditional courtyard, restaurant, 24h reception, free WiFi in public areas, free parking",
   mar1:null, mar15:null, bestWindow:"Not live-priced on Booking.com; third-party indicative ~$50–$94/nt (~$350–$658/wk)",
   transitStars:32, transitActs:9,
   transitNote:"Nanluoguxiang Line 6/8: central hutong hub (~20m to Wangfujing/Guomao★, ~51m to Summer Palace)",
   u:"https://www.letsbookhotel.com/en/china/beijing/hotel/courtyard-7.aspx",
   oop:true,
   note:"FLAGGED UNVERIFIED: Booking.com courtyard7.html redirects to city search for Feb 15–22, 2027. Confirm direct availability before counting."}
];

/* ---------- 3. BEIJING ACTIVITIES (10 / 10 verified via official municipal & attraction pages) ---------- */
const ACTIVITIES = [
  {n:"Palace Museum (Forbidden City)", d:"Dongcheng",
   hours:"Tue–Sun 08:30–16:30, last entry 15:30 (low season 1 Nov–31 Mar)",
   closed:"Mondays (except statutory holidays & Chinese New Year's Eve)",
   price:"¥40/person low season (1 Nov–31 Mar; Treasure Gallery +¥10, Clock Gallery +¥10); ¥60 high season", p2:"¥80 base total (2 × ¥40)",
   book:"Real-name ticket via official portal (bookingticket.dpm.org.cn) 7 days ahead at 20:00; 40,000/day cap; NO same-day tickets",
   transit:"Walk or 1 stop Line 1 from Wangfujing; ~20 min from Guomao CBD",
   u:"https://intl.dpm.org.cn/visit.html",
   status:"verified",
   soc:[
     {k:"YT 4K walk", u:"https://www.youtube.com/watch?v=yHYT3_xpOSU"},
     {k:"YT walk", u:"https://www.youtube.com/watch?v=d972yZ8bcx4"},
     {k:"YT 4K HDR", u:"https://www.youtube.com/watch?v=Lr-jVXDSyY0"},
     {k:"YT ticket guide", u:"https://www.youtube.com/watch?v=I33X1PrHRQg"}
   ]},

  {n:"Mutianyu Great Wall", d:"Huairou (day excursion)",
   hours:"Off-season 16 Nov–15 Mar: 08:00–17:30 (ticket sales stop 16:30, check-in 08:00–17:00)",
   closed:"Open daily (weather permitting)",
   price:"CNY 45 adult on Beijing Gov ticketing page (official 1-day PDF: basic RMB 40 / postcard RMB 45 + shuttle RMB 15 + cable car RMB 140 RT; ~RMB 180–200 pkg)", p2:"CNY 90 base entry (or ~CNY 360–400 for 2 w/ shuttle + cable car)",
   book:"Passport/ID required; en.mutianyugreatwall.com/reservation-center/tickets or concierge transfer",
   transit:"Outside 1h central transit (~70 km north; ~90 min road trip from central Beijing)",
   u:"https://en.mutianyugreatwall.com/",
   status:"verified",
   soc:[
     {k:"YT planning guide", u:"https://www.youtube.com/watch?v=3HJkn0BRHlk"},
     {k:"YT Mutianyu tour", u:"https://www.youtube.com/watch?v=D9gdGqZ0Pc0"},
     {k:"YT toboggan", u:"https://www.youtube.com/watch?v=z49wo_Zki4U"}
   ]},

  {n:"Temple of Heaven Park", d:"Dongcheng",
   hours:"Low season 1 Nov–31 Mar: Park 06:30–22:00 (last entry 21:00); Hall of Prayer/Echo Wall/Circular Mound 08:00–17:00 (last entry 16:30)",
   closed:"Inner buildings closed Mondays (except statutory holidays); outer park open daily",
   price:"CNY 10 park entry / CNY 28 combined ticket (low season 1 Nov–31 Mar; note Mar 2026 summary displays high-season CNY 15/34)", p2:"CNY 56 combo for 2 (or CNY 20 park only)",
   book:"Online booking via Temple of Heaven WeChat w/ passport or gate purchase",
   transit:"Subway Line 5 direct to Tiantandongmen (~25–30 min from Wangfujing; ~30 min from Guomao)",
   u:"https://english.beijing.gov.cn/specials/parktours/guidevisitors/templeofheaven/",
   status:"verified",
   soc:[
     {k:"YT visitor guide", u:"https://www.youtube.com/watch?v=nXqpgrJeCmI"},
     {k:"YT top sites", u:"https://www.youtube.com/watch?v=vij3lliVLLA"},
     {k:"IG Top 10 Beijing", u:"https://www.instagram.com/p/Cq2w9ssgcDW/"}
   ]},

  {n:"Summer Palace (Yiheyuan)", d:"Haidian",
   hours:"Off-season 1 Nov–31 Mar: Park 06:30–19:00 (last entry 18:00); inner courtyards 08:30–17:00 (last entry 16:30)",
   closed:"Inner courtyards closed Mondays (except statutory holidays); park grounds open daily",
   price:"CNY 20 park entry / CNY 50 combined through-ticket (off-season 1 Nov–31 Mar)", p2:"CNY 100 through-ticket for 2 (or CNY 40 park only)",
   book:"On-site gate cash/Visa/Mastercard accepted per 12345 FAQ, or official Summer Palace WeChat w/ passport",
   transit:"51 min subway from Wangfujing via Xidan Line 4 (Rome2rio); 58 min subway / 1h 07m bus+subway from Guomao (~1h+ door-to-door)",
   u:"https://english.beijing.gov.cn/travellinginbeijing/parks/202603/t20260320_4562531.html",
   status:"verified",
   soc:[
     {k:"YT walkthrough", u:"https://www.youtube.com/watch?v=ItLhW3AWPps"},
     {k:"YT deep guide", u:"https://www.youtube.com/watch?v=inAImsumpsw"},
     {k:"YT visitor guide", u:"https://www.youtube.com/watch?v=nFfDvCWrvHk"}
   ]},

  {n:"Tian'anmen Square", d:"Dongcheng",
   hours:"Daily 05:00–22:00 (time-slotted: flag raising, morning, afternoon, flag lowering); Rostrum 08:30–17:00 (closed Mon)",
   closed:"Open daily (Rostrum closed Mondays)",
   price:"Free square entry (mandatory real-name reservation); Tian'anmen Rostrum CNY 15", p2:"Free (¥0) / ¥30 with Rostrum",
   book:"Reserve via WeChat/Alipay Jingtong mini-program, OR same-day morning/afternoon Square access included w/ confirmed National Museum / Mao Hall ticket per 12345 FAQ",
   transit:"Line 1 Tian'anmen East/West: 1 stop from Wangfujing, ~12 min from Guomao",
   u:"https://english.beijing.gov.cn/travellinginbeijing/attractions/202603/t20260325_4566110.html",
   status:"verified",
   soc:[
     {k:"YT booking guide", u:"https://www.youtube.com/watch?v=OHSW0wAjej0"},
     {k:"YT combo guide", u:"https://www.youtube.com/watch?v=97gG9qekGzs"}
   ]},

  {n:"Yonghe Temple (Lama Temple)", d:"Dongcheng",
   hours:"Off-season 1 Nov–31 Mar: 09:00–16:30 (ticket sales stop 16:00; verify Lantern Festival hours Feb 20)",
   closed:"Open daily (40,000 daily visitor cap)",
   price:"CNY 25/person (half-price CNY 12)", p2:"CNY 50 total (2 × CNY 25)",
   book:"Real-name booking via Yonghe Temple WeChat up to 10 days ahead; bring original passport (hotline +86 10 84191906)",
   transit:"Subway Line 2/5 Yonghegong Station (~15–20 min from Wangfujing; steps from King's Joy 2★)",
   u:"https://english.beijing.gov.cn/specials/240tour/index.html",
   status:"verified",
   soc:[
     {k:"YT temple guide", u:"https://www.youtube.com/watch?v=AtMDwwnVgg4"},
     {k:"YT street walk", u:"https://www.youtube.com/watch?v=QzV_64K2tSM"}
   ]},

  {n:"798·751 Art Zone", d:"Chaoyang",
   hours:"Zone open all day; most galleries & museums ~10:00–18:00",
   closed:"Most indoor galleries/museums closed Mondays (avoid Mon)",
   price:"Free zone entry (special exhibitions ticketed via WeChat Mini Programs or on-site)", p2:"Free (¥0) zone entry",
   book:"No advance ticket needed for zone grounds; exhibition tickets on-site/WeChat (info +86 10 59789114)",
   transit:"10-min walk from NUO Hotel; 54 min subway from Wangfujing via Dawanglu Line 14 (Rome2rio)",
   u:"https://english.beijing.gov.cn/travellinginbeijing/attractions/202603/t20260323_4563864.html",
   status:"verified",
   soc:[
     {k:"YT guide", u:"https://www.youtube.com/watch?v=aHyqscDqykA"},
     {k:"YT walking tour", u:"https://www.youtube.com/watch?v=crrMxi9W8-c"}
   ]},

  {n:"Nanluoguxiang / Hutong Walk", d:"Dongcheng",
   hours:"Pedestrian street open all day; shops/cafes set own hours (~10:00–22:00)",
   closed:"Open daily",
   price:"Free (¥0) public pedestrian hutong", p2:"Free (¥0)",
   book:"No ticket required; pair with adjacent Bell/Drum Towers or Shichahai",
   transit:"Subway Line 6/8 Nanluoguxiang (~15 min from Wangfujing; ~28 min from Guomao)",
   u:"https://english.beijing.gov.cn/specials/240tour/index.html",
   status:"verified",
   soc:[
     {k:"YT walk", u:"https://www.youtube.com/watch?v=V2fD-zCd37Y"},
     {k:"YT local food route", u:"https://www.youtube.com/watch?v=gp4OIjcfUMw"}
   ]},

  {n:"National Museum of China", d:"Dongcheng",
   hours:"Tue–Sun 09:00–17:00 (last admission 16:00)",
   closed:"Mondays (except national public holidays)",
   price:"Free (¥0) general admission", p2:"Free (¥0)",
   book:"International portal (pcticket.chnmuseum.cn/museum-en/) accepts email + passport for up to 5 visitors; grants same-day morning/afternoon Square access",
   transit:"Line 1 Tian'anmen East: 1 stop from Wangfujing, ~12 min from Guomao",
   u:"https://en.chnmuseum.cn/visit_692/",
   status:"verified",
   soc:[
     {k:"YT full guide", u:"https://www.youtube.com/watch?v=NEFKE6SUFdQ"},
     {k:"YT treasures", u:"https://www.youtube.com/watch?v=R6v62W2Hn2I"},
     {k:"YT entry short", u:"https://www.youtube.com/shorts/qXNZ0AvK37w"}
   ]},

  {n:"Jingshan Park (Prospect Hill)", d:"Xicheng / Dongcheng border",
   hours:"Low season 1 Nov–31 Mar: 06:30–20:00 (last admission 19:30)",
   closed:"Open daily (Pavilion of Everlasting Spring panoramic overlook)",
   price:"CNY 2/person regular (CNY 10 during special exhibition periods)", p2:"CNY 4 regular (CNY 20 during exhibitions)",
   book:"Buy ticket at park gates or up to 7 days ahead via WeChat 'Visiting Beijing Parks' (010-64038098)",
   transit:"Walk 5 min north from Palace Museum exit; ~18 min from Wangfujing; ~25 min from Guomao",
   u:"https://english.beijing.gov.cn/travellinginbeijing/parks/202603/t20260320_4562541.html",
   status:"verified",
   soc:[
     {k:"YT 2 RMB viewpoint", u:"https://www.youtube.com/watch?v=VF0SZNKKvGg"},
     {k:"YT short", u:"https://www.youtube.com/shorts/8TU0pBUqxIY"},
     {k:"TikTok Beijing", u:"https://www.tiktok.com/@wadeandtaylor/video/7429005950222257454"}
   ]}
];

/* ---------- 4. TEN DECISION-GATE QUESTIONS BEFORE BOOKING ---------- */
const QUESTIONS = [
  {id:1, title:"Do both travellers already have valid passports (>6 months past Feb 2027) and Chinese visas?",
   blocks:"Everything. US passport holders need a Chinese visa in advance unless transiting ≤240h to a third country.",
   have:"Visa policy checked on travel.state.gov (Level 2, issued 2026-10-19); 240-hour visa-free transit does NOT cover a simple US–Beijing–US round trip.",
   missing:"Passport expiry dates & whether 10-year L visas are already issued.",
   action:"Check both passports this week; submit visa applications at least 8 weeks before departure."},

  {id:2, title:"Fixed travel week: 15–22 February 2027 (recommended) vs early March?",
   blocks:"All hotel holds and flight purchases (plus resolving the brief's 15–18 Feb 3-night vs 1–2 week conflict).",
   have:"Spring Festival 2027 is Sat 6 Feb (break 5–13 Feb; make-up Sun 14 Feb per secondary calendars). Across 11 live-priced hotels, Feb 15–22 is cheaper or flat at 8 properties (Sunworld $502, HI Express $536 live/$499 prior, XinQiao $568 queen, Peking Yard $1,105, Four Seasons $1,751, Waldorf $2,243, Park Hyatt $2,297, NUO $943, Rosewood $3,115), while Mar 1–8 drops at PuXuan ($2,803) and Orchid Courtyard ($1,025 full bed).",
   missing:"Airfare pricing for Feb 15–22 vs Mar 1–8 and final Lantern Festival (Sat 20 Feb) crowd tolerance.",
   action:"Lock Feb 15–22 with a refundable hotel rate today (Sunworld $502, HI Express $536, XinQiao $568, or Waldorf $2,582)."},

  {id:3, title:"What is the hotel budget tier (Value ~$500–$570 vs Boutique ~$1,160 vs 5★ Luxury ~$1,750–$3,115)?",
   blocks:"Hotel selection.",
   have:"All 11 bookable Booking.com properties verified for 1-queen/1-king bed + private/attached bath for 15–22 Feb 2027 ($502–$3,115 before 6%/6.6% checkout VAT where noted). Courtyard 7 flagged unbookable on Booking.com.",
   missing:"Your target 7-night lodging ceiling and final king-bed confirmation on Sunworld's selectable room.",
   action:"Choose Value (Sunworld $502 king request / HI Express $536 w/ breakfast / XinQiao $568 queen), Courtyard (Peking Yard $1,163 ref), or 5★ Luxury (Four Seasons $1,945 ref / Waldorf $2,582 ref)."},

  {id:4, title:"District base: Wangfujing / Dongcheng (all 9 city sights ≤1h) vs Chaoyang CBD (walk to top Michelin cluster)?",
   blocks:"Hotel shortlist.",
   have:"Verified 33/33 starred addresses (Chaoyang 20, Dongcheng 9, Xicheng 3, Shunyi 1) AND Rome2rio subway times: Wangfujing -> Guomao CBD★ is 8 min on Line 1, Wangfujing -> 798 is 54 min, and Wangfujing -> Summer Palace is 51 min. From Guomao CBD, Summer Palace is 58 min subway / 1h 07m bus+metro (~1h+ door-to-door).",
   missing:"Live Amap door-to-door checks (including station walking) for your specific finalists.",
   action:"Pick Dongcheng (Wangfujing/Jinyu Hutong/Chongwenmen) to keep ALL 9 city sights AND 32/33 starred restaurants under 1 hour."},

  {id:5, title:"Refundable rate vs non-refundable discount?",
   blocks:"Checkout method.",
   have:"Free-cancellation 1-queen/king rates are live at Sunworld ($502), HI Express ($536), XinQiao ($568), NUO ($943), Peking Yard ($1,163), Orchid ($1,194), Four Seasons ($1,945), Park Hyatt ($2,552), Waldorf ($2,582), PuXuan ($3,114), Rosewood ($3,115).",
   missing:"Visa confirmation before committing non-refundable cash.",
   action:"Book refundable today; switch to non-refundable only after visas and flights are ticketed."},

  {id:6, title:"Dining ceiling per meal for 2 adults?",
   blocks:"Starred restaurant reservations.",
   have:"Official published menus for 4 of 33 starred kitchens: Fu Chun Ju (à la carte PDF ¥88–¥498 + 15% svc), Cai Yi Xuan (¥1,688 + 10% svc + 6% tax = ¥1,958–1,968 for 2), Trb Hutong (¥3,882 tasting for 2), Giada Garden (¥3,976 degustation for 2). Remaining 29 carry ¥¥–¥¥¥¥ bands only.",
   missing:"Personal dining budget and whether to mix 1–2 splurge dinners with Bib Gourmand (32) / Selected (42) meals.",
   action:"Set a per-dinner cap and call shortlisted 2★/3★ venues for exact 2027 menu quotes."},

  {id:7, title:"Which 4–6 starred dinners + Bib Gourmand lunches go into the 7-night plan?",
   blocks:"Booking sequence & day-of-week routing.",
   have:"Verified hours for 13 starred kitchens (11 official MICHELIN/restaurant sites incl. Xin Rong Ji Xinyuan/Jinrong, King's Joy, Fu Chun Ju, Giada Garden, Il Ristorante, Cai Yi Xuan, House of Dynasties, Trb Hutong, Lei Garden + 2 Malay Mail press profiles for Chef 1996 & Old Tower). Note Old Tower closes Mon–Tue.",
   missing:"Opening hours for the other 20 starred kitchens (esp. Lantern Festival Sat 20 Feb).",
   action:"Anchor Mon 15 Feb with Yonghe Temple + Nanluoguxiang + King's Joy / Fu Chun Ju (all open Mon) and save Old Tower for Wed–Sun."},

  {id:8, title:"Mutianyu Great Wall transport: private driver vs rail/bus?",
   blocks:"Day 3 excursion.",
   have:"Off-season hours 08:00–17:30, CNY 45 entry (Beijing Gov), and Mutianyu PDF bundle prices (RMB 40–45 wall + RMB 15 shuttle + RMB 140 cable car RT; ~90m road trip each way).",
   missing:"Exact door-to-door private driver/tour quote and Feb 2027 live cart checkout.",
   action:"Reserve a hotel-concierge car or verified day tour once hotel is locked."},

  {id:9, title:"Palace Museum, National Museum & Tian'anmen Square booking alarms?",
   blocks:"Days 2 & 7 entry.",
   have:"All three require advance real-name reservations with original passport (Palace Museum 7 days ahead at 20:00, NO walk-up tickets; National Museum English site accepts email + passport and grants same-day morning/afternoon Tian'anmen Square access).",
   missing:"Traveller passport numbers & WeChat Pay / Alipay setup.",
   action:"Set calendar reminders 7–10 days before arrival and bind foreign cards to Alipay & WeChat Pay."},

  {id:10, title:"Beijing-only (7 nights) or Beijing + Shanghai extension?",
   blocks:"Cross-city rail/flight routing.",
   have:"Complete verified Shanghai companion planners already live in docs/, shanghai-2027/, and shanghai-verified-2027/ (see All Plans hub).",
   missing:"Confirmation that Feb 15–22 stays 100% Beijing.",
   action:"Use the All Plans / Shanghai links in the top bar if you want to split the trip."}
];
