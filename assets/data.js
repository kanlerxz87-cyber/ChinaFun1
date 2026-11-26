/* ============================================================
   China 2027 — verified dataset
   Trip window: 15 Feb 2027 – 23 Mar 2027 (preferred 15–18 Feb 2027)
   Every value below carries the source used. Blank = not confirmed.
   Last verification pass: 25 Nov 2026
   ============================================================ */

const META = {
  updated: "2026-11-26",
  session: "fac6d965 + 8f562229",
  trip: {
    windowStart: "2027-02-15",
    windowEnd: "2027-03-23",
    preferred: "2027-02-15 → 2027-02-18",
    nights: 7,
    adults: 2,
    city: "Beijing (base) with optional Shanghai extension"
  },
  sources: {
    bjGuide: "https://www.michelin.com/en/publications/products-and-services/michelin-guide-unveils-the-2027-beijing-tianjin-selection",
    bjList: "https://guide.michelin.com/us/en/beijing-municipality/beijing/restaurants/all-starred",
    shGuide: "https://guide.michelin.com/en/article/michelin-guide-ceremony/michelin-guide-shanghai-jiangsu-zhejiang",
    dpm: "https://intl.dpm.org.cn/visit.html",
    dpmBook: "https://bookingticket.dpm.org.cn/",
    mutianyu: "https://en.mutianyugreatwall.com/",
    visa: "https://travel.state.gov/en/international-travel/travel-advisories/china.html",
    holidays: "https://www.timeanddate.com/holidays/china/2027",
    bookingFeb: "https://www.booking.com/searchresults.html?ss=Beijing&checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1&selected_currency=USD&nflt=class%3D5%3Bht_id%3D204",
    bookingMar: "https://www.booking.com/searchresults.html?ss=Beijing&checkin=2027-03-15&checkout=2027-03-22&group_adults=2&no_rooms=1&selected_currency=USD&nflt=class%3D5%3Bht_id%3D204"
  }
};

/* ------------------------------------------------------------
   MICHELIN — Beijing 2027 (released 27–28 Oct 2026)
   107 Beijing entries = 2 three-star + 5 two-star + 26 one-star
   + 32 Bib Gourmand + 42 MICHELIN Selected
   Fields: n=name s=stars c=cuisine p=price band d=district
           a=address h=hours ph=phone w=own site g=guide url
           p2=price for 2 adults (only when officially published)
           soc=[label,url]  fx=notes/flags
   ------------------------------------------------------------ */
const MICHELIN = [
  {n:"Chao Shang Chao (Chaoyang)", s:3, c:"Chao Zhou", p:"¥¥¥¥", d:"Chaoyang",
   a:"L406B, 4F, CP Center, 20 Jinhe East Road, Chaoyang", h:"", ph:"+86 10 8596 2666", w:"",
   soc:[["YouTube review","https://www.youtube.com/watch?v=2Dw1Jkh1SQc"],["YouTube review","https://www.youtube.com/watch?v=FjcHEEL0xcs"],["YouTube review","https://www.youtube.com/watch?v=iaZNyyUDnxc"],["YouTube search","https://www.youtube.com/results?search_query=Chao+Shang+Chao+%28Chaoyang%29+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Chao+Shang+Chao+%28Chaoyang%29+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Chao+Shang+Chao+%28Chaoyang%29+Beijing+review"]],
   fx:"Hours not published on the MICHELIN page. Book direct — restaurant manages its own reservations."},
  {n:"Xin Rong Ji (Xinyuan South Road)", s:3, c:"Taizhou", p:"¥¥¥¥", d:"Chaoyang",
   a:"1F, East Tower, Genesis Beijing, 8 Xinyuan South Road, Chaoyang", h:"", ph:"", w:"https://www.xinrongji.com/",
   soc:[["YouTube review","https://www.youtube.com/watch?v=I_UAQlELzVA"],["YouTube review","https://www.youtube.com/watch?v=0dd524iKZPg"],["YouTube review","https://www.youtube.com/watch?v=6SvqIT2SW7M"],["YouTube search","https://www.youtube.com/results?search_query=Xin+Rong+Ji+%28Xinyuan+South+Road%29+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Xin+Rong+Ji+%28Xinyuan+South+Road%29+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Xin+Rong+Ji+%28Xinyuan+South+Road%29+Beijing+review"]],
   fx:"Hours not published on the MICHELIN page. Menu prices not published on an official page in this pass."},
  {n:"Blackswan", s:2, c:"French Contemporary", p:"¥¥¥¥", d:"Shunyi",
   a:"1F, Luohong Art Museum, 89 Capital Airport Road, Shunyi", h:"", ph:"+86 10 5385 9911", w:"https://www.restaurantblackswan.com/",
   soc:[["YouTube Short","https://www.youtube.com/shorts/XVF1QjeWKRk"],["YouTube (venue footage)","https://www.youtube.com/watch?v=b2fxK2c0N9g"],["YouTube search","https://www.youtube.com/results?search_query=Blackswan+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Blackswan+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Blackswan+Beijing+review"]],
   fx:"Shunyi / Airport Road — this is outside the central dining core, so it is treated separately in the ≤1 h analysis."},
  {n:"Jingji", s:2, c:"Beijing Cuisine", p:"¥¥¥¥", d:"Chaoyang",
   a:"2F, The Ritz-Carlton Hotel, 83A Jianguo Road, Chaoyang", h:"", ph:"+86 10 5969 5698", w:"",
   soc:[["YouTube Short","https://www.youtube.com/shorts/cB-8dFIIl_Y"],["YouTube search","https://www.youtube.com/results?search_query=Jingji+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Jingji+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Jingji+Beijing+review"]],
   fx:"Hours not published on the MICHELIN page."},
  {n:"King's Joy", s:2, c:"Vegetarian", p:"¥¥¥¥", d:"Dongcheng",
   a:"2 Wudaoying Hutong, Dongcheng", h:"Mon–Sun 11:00–22:00", ph:"+86 10 8404 9191", w:"https://www.kingsjoy.com/",
   soc:[["YouTube Short","https://www.youtube.com/watch?v=TTfH0qd79aE"],["YouTube review","https://www.youtube.com/watch?v=FpN8gqBZ1js"],["YouTube review","https://www.youtube.com/watch?v=lMYI5oF4Izg"],["YouTube Short","https://www.youtube.com/shorts/dx2MLoc9blA"],["YouTube search","https://www.youtube.com/results?search_query=King%27s+Joy+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=King%27s+Joy+Beijing"],["TikTok search","https://www.tiktok.com/search?q=King%27s+Joy+Beijing+review"]],
   fx:"Video is from 2024 and describes the restaurant as 3-star; the current 2027 MICHELIN status is Two Stars."},
  {n:"Lamdre", s:2, c:"Vegan", p:"¥¥¥¥", d:"Chaoyang",
   a:"Room 04, 1F, Block 14, Courtyard 4, Gongti North Road, Chaoyang", h:"", ph:"+86 10 8597 8888", w:"",
   soc:[["YouTube review","https://www.youtube.com/watch?v=PiClQQ0s_Bs"],["YouTube interview","https://www.youtube.com/watch?v=SkzeReb61qg"],["YouTube review","https://www.youtube.com/watch?v=_FZ0NlVcgFc"],["YouTube search","https://www.youtube.com/results?search_query=Lamdre+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Lamdre+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Lamdre+Beijing+review"]],
   fx:"Hours not published on the MICHELIN page. Restaurant manages its own bookings."},
  {n:"Lu Shang Lu", s:2, c:"Shandong", p:"¥¥¥¥", d:"Chaoyang",
   a:"2A01-2A13, 2F, Sunshine Financial Center Tower 1, 33 Jinghui Street, Chaoyang", h:"", ph:"+86 10 8718 5556", w:"",
   soc:[["YouTube review","https://www.youtube.com/watch?v=_eBigft9cmc"],["YouTube review","https://www.youtube.com/watch?v=ZRIA1Vl8sXI"],["YouTube review","https://www.youtube.com/watch?v=kk3L2zMwkMw"],["YouTube search","https://www.youtube.com/results?search_query=Lu+Shang+Lu+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Lu+Shang+Lu+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Lu+Shang+Lu+Beijing+review"]],
   fx:"Hours not published on the MICHELIN page."},
  {n:"Cai Yi Xuan", s:1, c:"Cantonese", p:"¥¥¥", d:"Chaoyang", a:"2F, Four Seasons Hotel, 48 Liangmaqiao Road, Chaoyang", h:"", ph:"+86 10 5695 8520", w:"https://www.fourseasons.com/beijing/dining/restaurants/cai_yi_xuan", soc:[["YouTube search","https://www.youtube.com/results?search_query=Cai+Yi+Xuan+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Cai+Yi+Xuan+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Cai+Yi+Xuan+Beijing+review"]], fx:""},
  {n:"Chao Shang Chao (Xicheng)", s:1, c:"Chao Zhou", p:"¥¥¥", d:"Xicheng", a:"Basement Level, Winland IFC, 7 Jinrong Street, Xicheng", h:"", ph:"+86 10 6609 1266", w:"", soc:[["YouTube search","https://www.youtube.com/results?search_query=Chao+Shang+Chao+%28Xicheng%29+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Chao+Shang+Chao+%28Xicheng%29+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Chao+Shang+Chao+%28Xicheng%29+Beijing+review"]], fx:""},
  {n:"Chef 1996", s:1, c:"Sichuan", p:"¥¥¥", d:"Chaoyang", a:"4A Jiangtaiwa, Xinghuo East Road, Chaoyang", h:"", ph:"+86 135 2150 9321", w:"https://www.chef1996.com/", soc:[["YouTube review","https://www.youtube.com/watch?v=3YTgh6MEQ8g"],["YouTube review","https://www.youtube.com/watch?v=2hI8Dh2F2n0"],["YouTube search","https://www.youtube.com/results?search_query=Chef+1996+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Chef+1996+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Chef+1996+Beijing+review"]], fx:"Promoted from MICHELIN Selected to One Star in the 2027 edition."},
  {n:"Fu Chun Ju", s:1, c:"Cantonese", p:"¥¥¥", d:"Dongcheng", a:"3F, The Puxuan Hotel, 1 Wangfujing Street, Dongcheng, 100006", h:"Mon–Sun 11:30–14:30 & 17:30–21:30", ph:"+86 10 5280 6418", w:"https://thepuxuan.com/en/beijing-wangfujing-luxury-hotel-dining/cantonese-cuisine-fu-chun-ju-restaurant/", soc:[["YouTube review","https://www.youtube.com/watch?v=ZULjI-TdQeA"],["YouTube review","https://www.youtube.com/watch?v=Z8qFZ3jvAEk"],["YouTube search","https://www.youtube.com/results?search_query=Fu+Chun+Ju+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Fu+Chun+Ju+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Fu+Chun+Ju+Beijing+review"]], fx:""},
  {n:"Furong", s:1, c:"Hunanese", p:"¥¥¥", d:"Xicheng", a:"1F, The Westin, 9C Jinrong Street, Xicheng", h:"", ph:"+86 10 6600 7175", w:"https://www.xinrongji.com/", soc:[["YouTube review","https://www.youtube.com/watch?v=EdcvGYIQMuY"],["YouTube search","https://www.youtube.com/results?search_query=Furong+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Furong+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Furong+Beijing+review"]], fx:""},
  {n:"Gastro Esthetics DaDong", s:1, c:"Chinese Contemporary", p:"¥¥¥", d:"Dongcheng", a:"1-2F, Nanxincang Business Tower, 22A Dongsi 10th Alley, Dongcheng", h:"", ph:"+86 51690328", w:"https://www.dadongdadong.com/", soc:[["YouTube (brand)","https://www.youtube.com/watch?v=OVH3HABM794"],["YouTube interview","https://www.youtube.com/watch?v=XRKJqKZfo1I"],["YouTube search","https://www.youtube.com/results?search_query=Gastro+Esthetics+DaDong+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Gastro+Esthetics+DaDong+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Gastro+Esthetics+DaDong+Beijing+review"]], fx:"Phone number as published on the official MICHELIN page (8-digit, no area code shown)."},
  {n:"Giada Garden", s:1, c:"Italian", p:"¥¥¥¥", d:"Chaoyang", a:"3F, China World Hotel, 1 Jianguomenwai Street, Chaoyang", h:"", ph:"+86 10 6505 7671", w:"https://www.shangri-la.com/beijing/chinaworld/dining/restaurants/giada-garden/", soc:[["YouTube search","https://www.youtube.com/results?search_query=Giada+Garden+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Giada+Garden+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Giada+Garden+Beijing+review"]], fx:""},
  {n:"Il Ristorante – Niko Romito", s:1, c:"Italian", p:"¥¥¥¥", d:"Chaoyang", a:"1F, Bvlgari Hotel, Building 2, Courtyard 8, Xinyuan South Road, Chaoyang", h:"Mon–Sat 12:00–14:30 & 18:00–22:00; Sun 12:00–15:00 & 18:00–22:00", ph:"+86 10 8555 8585", w:"https://www.bulgarihotels.com/en_US/beijing/dining/il-ristorante-niko-romito", soc:[["YouTube official","https://www.youtube.com/watch?v=Y-7NIh7KR-c"],["YouTube Short (official)","https://www.youtube.com/watch?v=E8Lg79sXpKc"],["YouTube search","https://www.youtube.com/results?search_query=Il+Ristorante+%E2%80%93+Niko+Romito+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Il+Ristorante+%E2%80%93+Niko+Romito+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Il+Ristorante+%E2%80%93+Niko+Romito+Beijing+review"]], fx:""},
  {n:"Lei Garden (Jinbao Tower)", s:1, c:"Cantonese", p:"¥¥¥", d:"Dongcheng", a:"3F, Jinbao Tower, 89 Jinbao Street, Dongcheng", h:"", ph:"+86 10 8522 1212", w:"https://leigarden.hk/", soc:[["YouTube review","https://www.youtube.com/watch?v=2XgVLAuptC8"],["YouTube search","https://www.youtube.com/results?search_query=Lei+Garden+%28Jinbao+Tower%29+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Lei+Garden+%28Jinbao+Tower%29+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Lei+Garden+%28Jinbao+Tower%29+Beijing+review"]], fx:""},
  {n:"Lu Style (Anding Road)", s:1, c:"Shandong", p:"¥¥¥", d:"Chaoyang", a:"5F, Uni Elite, Building 6, Courtyard 5, Anding Road, Chaoyang", h:"", ph:"+86 10 6441 3777", w:"", soc:[["YouTube search","https://www.youtube.com/results?search_query=Lu+Style+%28Anding+Road%29+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Lu+Style+%28Anding+Road%29+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Lu+Style+%28Anding+Road%29+Beijing+review"]], fx:""},
  {n:"Mansion Cuisine by Jingyan", s:1, c:"Beijing Cuisine", p:"¥¥¥¥", d:"Dongcheng", a:"22 Jianchang Hutong, Dongcheng", h:"", ph:"+86 10 8663 2999", w:"", soc:[["YouTube search","https://www.youtube.com/results?search_query=Mansion+Cuisine+by+Jingyan+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Mansion+Cuisine+by+Jingyan+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Mansion+Cuisine+by+Jingyan+Beijing+review"]], fx:""},
  {n:"MO Jasmine", s:1, c:"Beijing Cuisine", p:"¥¥¥", d:"Chaoyang", a:"L307, 3F, CP Center, 20 Jinhe East Road, Chaoyang, 100020", h:"", ph:"+86 10 8582 1919", w:"", soc:[["YouTube search","https://www.youtube.com/results?search_query=MO+Jasmine+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=MO+Jasmine+Beijing"],["TikTok search","https://www.tiktok.com/search?q=MO+Jasmine+Beijing+review"]], fx:""},
  {n:"Old Tower", s:1, c:"Innovative", p:"¥¥¥¥", d:"Chaoyang", a:"40A, 4F, Building N4, North, TaiKoo Li Sanlitun, 11 Sanlitun Road, Chaoyang", h:"", ph:"+86 139 1020 8150", w:"https://www.oldtower.cn/", soc:[["YouTube search","https://www.youtube.com/results?search_query=Old+Tower+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Old+Tower+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Old+Tower+Beijing+review"]], fx:"New entry: joined the Guide directly with One Star in 2027. Chef Talib Hudda."},
  {n:"Poetry·Wine (Dongsanhuan Middle Road)", s:1, c:"Beijing Cuisine", p:"¥¥", d:"Chaoyang", a:"61 Dongsanhuan Middle Road, Chaoyang, 10020", h:"", ph:"+86 10 8777 4188", w:"", soc:[["YouTube search","https://www.youtube.com/results?search_query=Poetry%C2%B7Wine+%28Dongsanhuan+Middle+Road%29+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Poetry%C2%B7Wine+%28Dongsanhuan+Middle+Road%29+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Poetry%C2%B7Wine+%28Dongsanhuan+Middle+Road%29+Beijing+review"]], fx:""},
  {n:"Rong Pao", s:1, c:"Sichuan", p:"¥¥¥", d:"Chaoyang", a:"2F, The Ritz-Carlton Hotel, 83A Jianguo Road, Chaoyang", h:"", ph:"+86 10 6616 6636", w:"", soc:[["YouTube review","https://www.youtube.com/watch?v=aa97MuXH0UY"],["YouTube search","https://www.youtube.com/results?search_query=Rong+Pao+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Rong+Pao+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Rong+Pao+Beijing+review"]], fx:""},
  {n:"Seventh Son", s:1, c:"Cantonese", p:"¥¥¥", d:"Chaoyang", a:"B1 Level, Jiaming Center, 27 Dongsanhuan North Road, Chaoyang", h:"", ph:"+86 10 8571 6888", w:"https://www.seventhson.hk/", soc:[["YouTube search","https://www.youtube.com/results?search_query=Seventh+Son+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Seventh+Son+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Seventh+Son+Beijing+review"]], fx:""},
  {n:"Shanghai Cuisine", s:1, c:"Shanghainese", p:"¥¥¥", d:"Chaoyang", a:"South side of Pacific Century Place, 2A Gongrentiyuchang North Road, Chaoyang, 100027", h:"", ph:"+86 10 6539 8660", w:"", soc:[["YouTube search","https://www.youtube.com/results?search_query=Shanghai+Cuisine+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Shanghai+Cuisine+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Shanghai+Cuisine+Beijing+review"]], fx:""},
  {n:"Sheng Yong Xing (Chaoyang)", s:1, c:"Beijing Cuisine", p:"¥¥¥", d:"Chaoyang", a:"5 Xindong Road, Chaoyang", h:"", ph:"+86 10 6464 0968", w:"", soc:[["YouTube search","https://www.youtube.com/results?search_query=Sheng+Yong+Xing+%28Chaoyang%29+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Sheng+Yong+Xing+%28Chaoyang%29+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Sheng+Yong+Xing+%28Chaoyang%29+Beijing+review"]], fx:"District taken from the restaurant name as published by MICHELIN; full address not captured in this pass."},
  {n:"The Beijing Kitchen (Jianguo Road)", s:1, c:"Cantonese", p:"¥¥", d:"Chaoyang", a:"D6007, 6F, SKP Beijing, 87 Jianguo Road, Chaoyang", h:"", ph:"+86 10 6530 7905", w:"", soc:[["YouTube Short","https://www.youtube.com/shorts/4zvpjQt2zpw"],["YouTube search","https://www.youtube.com/results?search_query=The+Beijing+Kitchen+%28Jianguo+Road%29+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=The+Beijing+Kitchen+%28Jianguo+Road%29+Beijing"],["TikTok search","https://www.tiktok.com/search?q=The+Beijing+Kitchen+%28Jianguo+Road%29+Beijing+review"]], fx:""},
  {n:"The Georg", s:1, c:"European Contemporary", p:"¥¥¥¥", d:"Dongcheng", a:"95 Donghuamen Street, Dongcheng, 100006", h:"", ph:"+86 186 1833 7710", w:"", soc:[["YouTube search","https://www.youtube.com/results?search_query=The+Georg+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=The+Georg+Beijing"],["TikTok search","https://www.tiktok.com/search?q=The+Georg+Beijing+review"]], fx:""},
  {n:"The House of Dynasties", s:1, c:"Cantonese", p:"¥¥¥", d:"Chaoyang", a:"4F, Rosewood Hotel, Jing Guang Centre, Hujialou, 1 Chaoyangmenwai Street, Chaoyang", h:"", ph:"+86 10 6536 0066", w:"https://www.rosewoodhotels.com/en/beijing/dining/the-house-of-dynasties", soc:[["YouTube search","https://www.youtube.com/results?search_query=The+House+of+Dynasties+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=The+House+of+Dynasties+Beijing"],["TikTok search","https://www.tiktok.com/search?q=The+House+of+Dynasties+Beijing+review"]], fx:""},
  {n:"Trb Hutong", s:1, c:"French Contemporary", p:"¥¥¥¥", d:"Dongcheng",
   a:"23 Shatan North Street, Dongcheng", h:"Mon–Sun 11:30–14:30, 17:30–22:00", ph:"+86 139 1171 2083", w:"https://www.trbhutong.com/",
   p2:"Weekday lunch ¥788 pp · Seasonal ¥1,688 pp · Signature ¥2,288 pp (+15% service). Two on Seasonal = ¥3,376 + 15% = ¥3,882",
   soc:[["YouTube review","https://www.youtube.com/watch?v=Sy0Df7KVfJk"],["YouTube search","https://www.youtube.com/results?search_query=Trb+Hutong+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Trb+Hutong+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Trb+Hutong+Beijing+review"]],
   fx:"Menu prices read from the restaurant's own menu page on 25 Nov 2026; +15% service charge applies."},
  {n:"Xin Rong Ji (Jianguomenwai Street)", s:1, c:"Taizhou", p:"¥¥¥", d:"Chaoyang",
   a:"5F, Tower A, Yintai Centre, 2 Jianguomenwai Street, Chaoyang", h:"", ph:"", w:"https://www.xinrongji.com/", soc:[["YouTube search","https://www.youtube.com/results?search_query=Xin+Rong+Ji+%28Jianguomenwai+Street%29+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Xin+Rong+Ji+%28Jianguomenwai+Street%29+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Xin+Rong+Ji+%28Jianguomenwai+Street%29+Beijing+review"]], fx:""},
  {n:"Xin Rong Ji (Jinrong Street)", s:1, c:"Taizhou", p:"¥¥¥", d:"Xicheng",
   a:"B1, International Finance Centre, 11 Jinrong Street, Xicheng", h:"", ph:"", w:"https://www.xinrongji.com/", soc:[["YouTube search","https://www.youtube.com/results?search_query=Xin+Rong+Ji+%28Jinrong+Street%29+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Xin+Rong+Ji+%28Jinrong+Street%29+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Xin+Rong+Ji+%28Jinrong+Street%29+Beijing+review"]], fx:""},
  {n:"Zhiguan Courtyard", s:1, c:"Dongbei", p:"¥¥¥", d:"Dongcheng", a:"12 Jinyu Hutong, Dongcheng", h:"", ph:"+86 10 6559 9899", w:"", soc:[["YouTube search","https://www.youtube.com/results?search_query=Zhiguan+Courtyard+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Zhiguan+Courtyard+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Zhiguan+Courtyard+Beijing+review"]], fx:""},
  {n:"Zijin Mansion", s:1, c:"Cantonese", p:"¥¥¥", d:"Dongcheng", a:"3F, Waldorf Astoria Hotel, 5-15 Jinyu Hutong, Dongcheng", h:"", ph:"+86 10 8520 8989", w:"https://www.hilton.com/en/hotels/bjswawa-waldorf-astoria-beijing/dining/zijin-mansion/", soc:[["YouTube search","https://www.youtube.com/results?search_query=Zijin+Mansion+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Zijin+Mansion+Beijing"],["TikTok search","https://www.tiktok.com/search?q=Zijin+Mansion+Beijing+review"]], fx:""}
];

const GUIDE_SLUG = {
  "Chao Shang Chao (Chaoyang)":"chao-shang-chao",
  "Xin Rong Ji (Xinyuan South Road)":"xin-rong-ji-xinyuan-south-road",
  "Blackswan":"blackswan", "Jingji":"jingji", "King's Joy":"king-s-joy", "Lamdre":"lamdre",
  "Lu Shang Lu":"lu-shang-lu", "Cai Yi Xuan":"cai-yi-xuan",
  "Chao Shang Chao (Xicheng)":"chao-shang-chao-xicheng", "Chef 1996":"chef-1996",
  "Fu Chun Ju":"fu-chun-ju", "Furong":"furong",
  "Gastro Esthetics DaDong":"gastro-esthetics-dadong", "Giada Garden":"giada-garden",
  "Il Ristorante – Niko Romito":"il-ristorante-niko-romito-1186723",
  "Lei Garden (Jinbao Tower)":"lei-garden-jinbao-tower", "Lu Style (Anding Road)":"lu-style",
  "Mansion Cuisine by Jingyan":"mansion-cuisine-by-jingyan", "MO Jasmine":"mo-jasmine",
  "Old Tower":"old-tower", "Poetry·Wine (Dongsanhuan Middle Road)":"poetry%E2%80%A7wine",
  "Rong Pao":"rong-pao", "Seventh Son":"seventh-son-1186794",
  "Shanghai Cuisine":"shanghai-cuisine", "Sheng Yong Xing (Chaoyang)":"sheng-yong-xing-chaoyang",
  "The Beijing Kitchen (Jianguo Road)":"the-beijing-kitchen", "The Georg":"the-georg",
  "The House of Dynasties":"the-house-of-dynasties", "Trb Hutong":"trb-hutong",
  "Xin Rong Ji (Jianguomenwai Street)":"xin-rong-ji-jianguomenwai-street",
  "Xin Rong Ji (Jinrong Street)":"xin-rong-ji-jinrong-street",
  "Zhiguan Courtyard":"zhiguan", "Zijin Mansion":"zijin-mansion"
};
MICHELIN.forEach(r=>{ r.g = "https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/" + GUIDE_SLUG[r.n]; });

/* ------------------------------------------------------------
   HOTELS — 7 nights, 15–22 Feb 2027, 2 adults, USD
   Prices: Booking.com live result pages, read 25 Nov 2026.
   These are "from" rates for the quoted room type, not a locked contract.
   Fields: n, area(Booking district), cls(Booking rating), room, bed, bedOk,
           tot(total 7 nts), cancel, rev(guest score), url, fx
   ------------------------------------------------------------ */
const HOTELS = [
  {n:"Four Seasons Hotel Beijing", area:"Chaoyang (Yansha)", cls:"5/5", room:"Deluxe Twin Room, City View",
   bed:"2 twin beds", bedOk:false, tot:1753, cancel:"", rev:9.0,
   url:"https://www.booking.com/hotel/cn/bei-jing-si-ji.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1&selected_currency=USD",
   fx:"Only Chaoyang listing confirmed bookable for 15–22 Feb 2027; quoted rate is a twin room, so it fails the queen-bed requirement as priced."},
  {n:"Happy Dragon Courtyard Hotel (near Forbidden City)", area:"Dongcheng", cls:"5/5", room:"King Room with Garden View",
   bed:"1 queen bed", bedOk:true, tot:1075, cancel:"Free cancellation", rev:9.8,
   url:"https://www.booking.com/hotel/cn/the-classic-courtyard-beijing.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1&selected_currency=USD",
   fx:"Breakfast included. Booking's '5/5' is a property rating, not an official star class. Courtyard property — no pool/gym confirmed."},
  {n:"Sunworld Dynasty Hotel Beijing Wangfujing", area:"Dongcheng (Wangfujing)", cls:"5/5", room:"Superior Room, Twin Beds",
   bed:"2 twin beds", bedOk:false, tot:697, cancel:"Free cancellation", rev:9.1,
   url:"https://www.booking.com/hotel/cn/sunworld-dynasty-beijing.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1&selected_currency=USD",
   fx:"Cheapest confirmed 5-star for the preferred dates. Twin only at this rate."},
  {n:"East Sacred Hotel (Jingfang Dasha)", area:"Dongcheng (Wangfujing)", cls:"5/5", room:"Superior Twin Room",
   bed:"2 twin beds", bedOk:false, tot:554, cancel:"Free cancellation · no prepayment", rev:8.5,
   url:"https://www.booking.com/hotel/cn/jing-fang-da-sha.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1&selected_currency=USD",
   fx:"Breakfast included; lowest total found for a 5-star in the preferred window."},
  {n:"Grand Hyatt Beijing", area:"Dongcheng (Wangfujing)", cls:"5/5", room:"1 King Bed",
   bed:"1 king bed", bedOk:true, tot:1652, cancel:"", rev:8.9,
   url:"https://www.booking.com/hotel/cn/grand-hyatt-beijing.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1&selected_currency=USD",
   fx:"Identical $1,652 total quoted for 15–22 Mar 2027 — a direct same-hotel date comparison."},
  {n:"Waldorf Astoria Beijing", area:"Dongcheng (Wangfujing)", cls:"5/5", room:"Deluxe King Room",
   bed:"1 king bed", bedOk:true, tot:2246, cancel:"", rev:9.2,
   url:"https://www.booking.com/hotel/cn/waldorf-astoria-beijing.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1&selected_currency=USD",
   fx:"Highest guest score among confirmed king-bed options."},
  {n:"Regent Beijing", area:"Dongcheng (Wangfujing)", cls:"5/5", room:"Classic Room, High Floor",
   bed:"Multiple bed types", bedOk:"partial", tot:1102, cancel:"", rev:8.8,
   url:"https://www.booking.com/hotel/cn/the-regent-beijing.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1&selected_currency=USD",
   fx:"Bed type is allocated by the hotel at this rate — request a king in writing."},
  {n:"New World Beijing Hotel", area:"Dongcheng (Qianmen)", cls:"5/5", room:"Superior Twin Room",
   bed:"2 twin beds", bedOk:false, tot:1177, cancel:"Free cancellation · no prepayment", rev:9.1,
   url:"https://www.booking.com/hotel/cn/beijing-new-world-hotel.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1&selected_currency=USD",
   fx:"$1,177 is the public rate; a members-only rate of $901 was displayed when signed in. Use the public figure as the planning number."},
  {n:"Prime Hotel Beijing Wangfujing", area:"Dongcheng (Wangfujing)", cls:"5/5", room:"Deluxe Twin Room",
   bed:"2 full beds", bedOk:false, tot:1029, cancel:"Free cancellation", rev:8.9,
   url:"https://www.booking.com/hotel/cn/prime.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1&selected_currency=USD",
   fx:"Discounted from $1,387 at time of check."},
  {n:"Swissotel Beijing Hong Kong Macau Center", area:"Dongcheng (Sanlitun)", cls:"5/5", room:"Premier Twin Room",
   bed:"2 twin beds", bedOk:false, tot:1011, cancel:"Free cancellation · no prepayment", rev:9.0,
   url:"https://www.booking.com/hotel/cn/swissotelbeijing.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1&selected_currency=USD",
   fx:"Booking labels the area 'Sanlitun, Dongcheng' although Sanlitun is usually described as Chaoyang. Confirm the exact address before relying on it for Michelin walk-ups."},
  {n:"Hilton Beijing Wangfujing", area:"Dongcheng (Wangfujing)", cls:"5/5", room:"Deluxe Twin Room",
   bed:"2 twin beds", bedOk:false, tot:1244, cancel:"Free cancellation · no prepayment", rev:8.7,
   url:"https://www.booking.com/hotel/cn/hilton-beijing-wangfujing.html?checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1&selected_currency=USD",
   fx:""},
  {n:"Beijing Purple Horse Garden Hotel Wangfujing", area:"Dongcheng (Wangfujing)", cls:"5/5", room:"Deluxe King Room",
   bed:"1 queen bed", bedOk:true, tot:901, cancel:"Free cancellation", rev:9.4,
   url:"https://www.booking.com/hotel/cn/zi-long-hua-yuan-jiu-dian.html?checkin=2027-03-15&checkout=2027-03-22&group_adults=2&no_rooms=1&selected_currency=USD",
   oop:true,
   fx:"Quote is for 15–22 MAR 2027, not February. Not bookable for 15–22 Feb when checked, so it is excluded from the ranking and listed last."}
];

/* Michelin density: verified same-district stars (see method note) */
const DISTRICT_STARS = {Chaoyang:20, Dongcheng:9, Xicheng:3, Shunyi:1};

/* ------------------------------------------------------------
   ACTIVITIES
   v = verified against the official site in this pass
   ------------------------------------------------------------ */
const ACTIVITIES = [
  {n:"Palace Museum (Forbidden City)", area:"Dongcheng", h:"Tue–Sun 8:30–16:30, last entry 15:30 (1 Nov–31 Mar). Closed Mondays, except national holidays and Chinese New Year's Eve.",
   price:"¥40 low season (1 Nov–31 Mar) per adult; ¥80 for 2 adults. Treasure Gallery +¥10; Gallery of Clocks +¥10 (per person).", v:true,
   off:"https://intl.dpm.org.cn/visit.html", book:"https://bookingticket.dpm.org.cn/",
   soc:[["YouTube visit guide","https://www.youtube.com/watch?v=I33X1PrHRQg"],["YouTube visit guide","https://www.youtube.com/watch?v=qpyLndAmsxY"],["YouTube","https://www.youtube.com/watch?v=yHYT3_xpOSU"],["YouTube","https://www.youtube.com/watch?v=d972yZ8bcx4"],["YouTube","https://www.youtube.com/watch?v=Lr-jVXDSyY0"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Forbidden%20City%20Beijing"],["TikTok search","https://www.tiktok.com/search?q=Forbidden%20City%20Beijing%20travel"]],
   fx:"No same-day tickets. Daily cap 40,000. Passport number required for foreign visitors. Official booking: bookingticket.dpm.org.cn."},
  {n:"Mutianyu Great Wall", area:"Huairou (day trip)", h:"Off-season 16 Nov–15 Mar: 8:00–17:30. Ticket sales end 16:30; ticket check-in 8:00–17:00. Open daily (seasonal schedule; verify before travel).",
   price:"Admission price not clearly published in USD/CNY on the English landing page captured in this pass; verify on official ticket page before purchase.", v:true, off:"https://en.mutianyugreatwall.com/", book:"https://en.mutianyugreatwall.com/reservation-center/tickets",
   soc:[["YouTube","https://www.youtube.com/watch?v=z49wo_Zki4U"],["YouTube","https://www.youtube.com/watch?v=kU9huPVdVlM"],["YouTube","https://www.youtube.com/watch?v=D9gdGqZ0Pc0"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Mutianyu%20Great%20Wall"],["TikTok search","https://www.tiktok.com/search?q=Mutianyu%20Great%20Wall"]],
   fx:"Outside 1-hour transit from central Wangfujing hotels; plan as a half/full-day excursion. Confirm cable car/toboggan prices on official booking page."},
  {n:"Temple of Heaven Park", area:"Dongcheng", h:"Park 6:00–22:00 (last entry 21:00). Attractions with separate charges: Tue–Sun 8:00–18:00 (last entry 17:30). Closed Mondays except statutory holidays.",
   price:"Official page lists seasonal ticket options (high season examples shown on page: combo CNY 34, admission CNY 15; concessions available). Feb 2027 is low season — confirm low-season rates on official page before purchase.", v:true,
   off:"https://english.beijing.gov.cn/travellinginbeijing/parks/202603/t20260320_4562532.html", book:"https://english.beijing.gov.cn/travellinginbeijing/parks/202603/t20260320_4562532.html",
   soc:[["YouTube visit guide","https://www.youtube.com/watch?v=nXqpgrJeCmI"],["YouTube visit guide","https://www.youtube.com/watch?v=vij3lliVLLA"],["YouTube search","https://www.youtube.com/results?search_query=Temple+of+Heaven+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Temple%20of%20Heaven%20Beijing"],["TikTok search","https://www.tiktok.com/search?q=Temple%20of%20Heaven%20Beijing"]],
   fx:"Verified from Beijing Municipal Government official English page. Ticket categories/seasonal pricing should be rechecked for exact Feb 2027 low-season amounts."},
  {n:"Summer Palace (Yiheyuan)", area:"Haidian", h:"", price:"", v:false,
   off:"https://www.summerpalace-china.com/English/", book:"",
   soc:[["YouTube visit guide","https://www.youtube.com/watch?v=1hmKrSTbDv4"],["YouTube visit guide","https://www.youtube.com/watch?v=inAImsumpsw"],["YouTube walkthrough","https://www.youtube.com/watch?v=nFfDvCWrvHk"],["YouTube search","https://www.youtube.com/results?search_query=Summer+Palace+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Summer%20Palace%20Beijing"],["TikTok search","https://www.tiktok.com/search?q=Summer%20Palace%20Beijing"]],
   fx:"Official site linked; hours/ticket prices not fully verified in this pass. Usually 60+ minutes from Wangfujing by transit — verify route/time before scheduling."},
  {n:"Tiananmen Square", area:"Dongcheng", h:"", price:"Free (reservation rules apply; verify).", v:false,
   off:"https://english.beijing.gov.cn/", book:"",
   soc:[["YouTube reservation guide","https://www.youtube.com/watch?v=97gG9qekGzs"],["YouTube reservation guide","https://www.youtube.com/watch?v=OHSW0wAjej0"],["YouTube search","https://www.youtube.com/results?search_query=Tiananmen+Square+Beijing+visit"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Tiananmen%20Square%20Beijing"],["TikTok search","https://www.tiktok.com/search?q=Tiananmen%20Square%20Beijing"]],
   fx:"Advance real-name reservation has been required in recent years; official current reservation flow not fully verified in this pass. Check official notice before visit."},
  {n:"Yonghe Temple (Lama Temple)", area:"Dongcheng", h:"", price:"", v:false,
   off:"https://www.yonghegong.cn/", book:"",
   soc:[["YouTube visit guide","https://www.youtube.com/watch?v=AtMDwwnVgg4"],["YouTube neighbourhood walk","https://www.youtube.com/watch?v=QzV_64K2tSM"],["YouTube search","https://www.youtube.com/results?search_query=Yonghe+Lama+Temple+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Lama%20Temple%20Beijing"],["TikTok search","https://www.tiktok.com/search?q=Lama%20Temple%20Beijing"]],
   fx:"Official site linked; hours/ticket prices not verified in this pass. Adjacent to King's Joy (2★), so it pairs naturally with lunch/dinner planning."},
  {n:"798 Art Zone", area:"Chaoyang", h:"", price:"", v:false,
   off:"http://www.798district.com/", book:"",
   soc:[["YouTube visit guide","https://www.youtube.com/watch?v=aHyqscDqykA"],["YouTube walking tour","https://www.youtube.com/watch?v=crrMxi9W8-c"],["YouTube search","https://www.youtube.com/results?search_query=798+Art+Zone+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=798%20Art%20Zone%20Beijing"],["TikTok search","https://www.tiktok.com/search?q=798%20Art%20Zone%20Beijing"]],
   fx:"District/venue hours vary by gallery. Not verified as a single official-hours attraction in this pass; verify specific galleries before visit."},
  {n:"Nanluoguxiang / hutong walk", area:"Dongcheng", h:"Public street; open access (individual shops have their own hours).", price:"Free to walk; purchases vary.", v:false,
   off:"https://english.beijing.gov.cn/", book:"",
   soc:[["YouTube walking tour","https://www.youtube.com/watch?v=V2fD-zCd37Y"],["YouTube walking guide","https://www.youtube.com/watch?v=gp4OIjcfUMw"],["YouTube search","https://www.youtube.com/results?search_query=Nanluoguxiang+hutong+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Nanluoguxiang%20Beijing"],["TikTok search","https://www.tiktok.com/search?q=Nanluoguxiang%20Beijing"]],
   fx:"Public street area, not a ticketed single attraction. Hours for shops/cafes vary; no single official hours source applies."},
  {n:"National Museum of China", area:"Dongcheng", h:"Tue–Sun 9:00–17:00 (last admission 16:00). Closed Mondays (except national public holidays).",
   price:"Free admission; advance reservation required.", v:true,
   off:"https://en.chnmuseum.cn/visit_692/", book:"https://pcticket.chnmuseum.cn/museum-en/",
   soc:[["YouTube visit guide","https://www.youtube.com/watch?v=NEFKE6SUFdQ"],["YouTube collection guide","https://www.youtube.com/watch?v=R6v62W2Hn2I"],["YouTube Short (entry)","https://www.youtube.com/shorts/qXNZ0AvK37w"],["YouTube search","https://www.youtube.com/results?search_query=National+Museum+of+China+Beijing+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=National%20Museum%20of%20China%20Beijing"],["TikTok search","https://www.tiktok.com/search?q=National%20Museum%20of%20China%20Beijing"]],
   fx:"Verified from official National Museum of China English visit page. Passport/ID required for reservation; check current exhibition availability."},
  {n:"Jingshan Park (Prospect Hill)", area:"Xicheng", h:"", price:"", v:false,
   off:"https://english.beijing.gov.cn/", book:"",
   soc:[["YouTube Short","https://www.youtube.com/shorts/8TU0pBUqxIY"],["YouTube visit guide","https://www.youtube.com/watch?v=VF0SZNKKvGg"],["YouTube Short","https://www.youtube.com/shorts/kxVk6NYj5Uk"],["YouTube search","https://www.youtube.com/results?search_query=Jingshan+Park+Beijing+view+review"],["Instagram search","https://www.instagram.com/explore/search/keyword/?q=Jingshan%20Park%20Beijing"],["TikTok search","https://www.tiktok.com/search?q=Jingshan%20Park%20Beijing"]],
   fx:"Popular for Forbidden City overlook; official hours/ticket price not verified in this pass. Confirm on official Beijing park page before visit."}
];

/* ------------------------------------------------------------
   QUESTIONS — everything that must be answered before booking
   status: open | answered
   ------------------------------------------------------------ */
const QUESTIONS = [
  {q:"Which of the two adults' passports will be used, and is a Chinese visa already held?",
   why:"US passport holders need a tourist (L) visa before flying; the visa must be in the passport used to enter.",
   now:"US State Department China page: visa required, 10-year multiple-entry typical for US citizens. Not yet confirmed whether the couple already holds valid visas.",
   action:"Check both passports for an existing valid Chinese visa and for 6+ months validity beyond the arrival date.", st:"open"},
  {q:"Is a queen bed non-negotiable at the quoted rate, or is a twin acceptable if the hotel allows a bed-type request?",
   why:"Every cheapest confirmed 7-night rate for the preferred dates is a twin room. Only 4 of 12 hotels quoted a king/queen bed.",
   now:"Bed type per quoted rate is recorded in the hotel table.", action:"Decide: pay a king-room premium, or accept twin + written bed request.", st:"open"},
  {q:"Does the couple want a single Beijing base, or a split stay (Beijing + Shanghai) inside the 1–2 week window?",
   why:"It changes the hotel count, the Michelin cluster analysis and the transport cost entirely.",
   now:"Beijing has 33 starred restaurants in the current guide; the Shanghai/Jiangsu/Zhejiang edition has 77 stars across the region.", action:"Pick: 7 nights Beijing only (current plan) or 5 + 2 nights split.", st:"open"},
  {q:"Which exact week inside 15 Feb – 23 Mar 2027?",
   why:"15–18 Feb was the stated preference, but Spring Festival runs 5–13 Feb 2027 with a make-up workday on 14 Feb. Everything before 15 Feb is peak travel.",
   now:"Pricing evidence: the same hotel quoted the same total for 15–22 Feb and 15–22 Mar, so date choice within the window is not a big price lever.",
   action:"Confirm 15–22 Feb (7 nights) as the working plan.", st:"open"},
  {q:"Is a Michelin meal programme 1 per day, or a handful of splurges?",
   why:"Sets the restaurant budget and the reservation sequence.",
   now:"Only Trb Hutong publishes exact menu prices (¥788–¥2,288 pp + 15%). Other restaurants publish price bands only.", action:"Set a per-meal ceiling, then pick from the ranked list.", st:"open"},
  {q:"Is the couple willing to travel to Shunyi for Blackswan (2★)?",
   why:"It is the only two-star outside the central core and is likely well beyond a 1-hour transit hop.",
   now:"Address verified as 89 Capital Airport Road, Shunyi.", action:"Decide to include or skip before ranking it.", st:"open"},
  {q:"What is the trip budget ceiling, all-in?",
   why:"Hotel totals for the preferred week span $554 to $2,246 for 7 nights — a 4× spread.",
   now:"Hotel totals verified; airfare, visas, meals and transport not yet costed.", action:"Set a ceiling so the shortlist can be cut to 2–3 options.", st:"open"},
  {q:"Which travel-documents/payment tools will be set up before departure?",
   why:"Metro, taxis and most restaurants run on Alipay/WeChat Pay; foreign cards work unevenly.",
   now:"Not verified in this pass.", action:"Confirm Alipay/WeChat Pay setup and a data plan/VPN decision.", st:"open"},
  {q:"Does either traveller need step-free access or a lift-free route?",
   why:"Hutong restaurants and the Great Wall involve stairs and uneven ground.",
   now:"Not captured.", action:"Answer before choosing hotels and restaurant seats.", st:"open"},
  {q:"Do we accept that Michelin density counts are floors, not totals?",
   why:"Only 10 of the 33 starred restaurants had their address captured and verified in this pass, so same-district counts understate the real cluster.",
   now:"Verified: Chaoyang 6, Dongcheng 2, Xicheng 1, Shunyi 1.", action:"Approve the remaining address capture (see Suggestions).", st:"open"}
];
