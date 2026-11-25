/* ============================================================
   China 2027 — verified dataset
   Trip window: 15 Feb 2027 – 23 Mar 2027 (preferred 15–18 Feb 2027)
   Every value below carries the source used. Blank = not confirmed.
   Last verification pass: 25 Nov 2026
   ============================================================ */

const META = {
  updated: "2026-11-25",
  session: "fac6d965",
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
   soc:[["YouTube search","https://www.youtube.com/results?search_query=Chao+Shang+Chao+Beijing+michelin"]],
   fx:"Hours not published on the MICHELIN page. Book direct — restaurant manages its own reservations."},
  {n:"Xin Rong Ji (Xinyuan South Road)", s:3, c:"Taizhou", p:"¥¥¥¥", d:"Chaoyang",
   a:"1F, East Tower, Genesis Beijing, 8 Xinyuan South Road, Chaoyang", h:"", ph:"", w:"https://www.xinrongji.com/",
   soc:[["YouTube","https://www.youtube.com/watch?v=6SvqIT2SW7M"]],
   fx:"Hours not published on the MICHELIN page. Menu prices not published on an official page in this pass."},
  {n:"Blackswan", s:2, c:"French Contemporary", p:"¥¥¥¥", d:"Shunyi",
   a:"1F, Luohong Art Museum, 89 Capital Airport Road, Shunyi", h:"", ph:"+86 10 5385 9911", w:"https://www.restaurantblackswan.com/",
   soc:[["YouTube search","https://www.youtube.com/results?search_query=Blackswan+restaurant+Beijing+Luohong+Art+Museum"]],
   fx:"Shunyi / Airport Road — this is outside the central dining core, so it is treated separately in the ≤1 h analysis."},
  {n:"Jingji", s:2, c:"Beijing Cuisine", p:"¥¥¥¥", d:"Chaoyang",
   a:"2F, The Ritz-Carlton Hotel, 83A Jianguo Road, Chaoyang", h:"", ph:"+86 10 5969 5698", w:"",
   soc:[["YouTube search","https://www.youtube.com/results?search_query=Jingji+restaurant+Ritz+Carlton+Beijing+michelin"]],
   fx:"Hours not published on the MICHELIN page."},
  {n:"King's Joy", s:2, c:"Vegetarian", p:"¥¥¥¥", d:"Dongcheng",
   a:"2 Wudaoying Hutong, Dongcheng", h:"Mon–Sun 11:00–22:00", ph:"+86 10 8404 9191", w:"https://www.kingsjoy.com/",
   soc:[["YouTube","https://www.youtube.com/watch?v=TTfH0qd79aE"]],
   fx:"Video is from 2024 and describes the restaurant as 3-star; the current 2027 MICHELIN status is Two Stars."},
  {n:"Lamdre", s:2, c:"Vegan", p:"¥¥¥¥", d:"Chaoyang",
   a:"Room 04, 1F, Block 14, Courtyard 4, Gongti North Road, Chaoyang", h:"", ph:"+86 10 8597 8888", w:"",
   soc:[["YouTube search","https://www.youtube.com/results?search_query=Lamdre+Beijing+vegan+michelin"]],
   fx:"Hours not published on the MICHELIN page. Restaurant manages its own bookings."},
  {n:"Lu Shang Lu", s:2, c:"Shandong", p:"¥¥¥¥", d:"Chaoyang",
   a:"2A01-2A13, 2F, Sunshine Financial Center Tower 1, 33 Jinghui Street, Chaoyang", h:"", ph:"+86 10 8718 5556", w:"",
   soc:[["YouTube search","https://www.youtube.com/results?search_query=Lu+Shang+Lu+Beijing+Shandong+michelin"]],
   fx:"Hours not published on the MICHELIN page."},
  {n:"Cai Yi Xuan", s:1, c:"Cantonese", p:"¥¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:""},
  {n:"Chao Shang Chao (Xicheng)", s:1, c:"Chao Zhou", p:"¥¥¥", d:"Xicheng", a:"", h:"", ph:"", w:"", soc:[], fx:""},
  {n:"Chef 1996", s:1, c:"Sichuan", p:"¥¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:"Promoted from MICHELIN Selected to One Star in the 2027 edition."},
  {n:"Fu Chun Ju", s:1, c:"Cantonese", p:"¥¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:""},
  {n:"Furong", s:1, c:"Hunanese", p:"¥¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:""},
  {n:"Gastro Esthetics DaDong", s:1, c:"Chinese Contemporary", p:"¥¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:""},
  {n:"Giada Garden", s:1, c:"Italian", p:"¥¥¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:""},
  {n:"Il Ristorante – Niko Romito", s:1, c:"Italian", p:"¥¥¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:""},
  {n:"Lei Garden (Jinbao Tower)", s:1, c:"Cantonese", p:"¥¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:""},
  {n:"Lu Style (Anding Road)", s:1, c:"Shandong", p:"¥¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:""},
  {n:"Mansion Cuisine by Jingyan", s:1, c:"Beijing Cuisine", p:"¥¥¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:""},
  {n:"MO Jasmine", s:1, c:"Beijing Cuisine", p:"¥¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:""},
  {n:"Old Tower", s:1, c:"Innovative", p:"¥¥¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:"New entry: joined the Guide directly with One Star in 2027. Chef Talib Hudda."},
  {n:"Poetry·Wine (Dongsanhuan Middle Road)", s:1, c:"Beijing Cuisine", p:"¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:""},
  {n:"Rong Pao", s:1, c:"Sichuan", p:"¥¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:""},
  {n:"Seventh Son", s:1, c:"Cantonese", p:"¥¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:""},
  {n:"Shanghai Cuisine", s:1, c:"Shanghainese", p:"¥¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:""},
  {n:"Sheng Yong Xing (Chaoyang)", s:1, c:"Beijing Cuisine", p:"¥¥¥", d:"Chaoyang", a:"", h:"", ph:"", w:"", soc:[], fx:"District taken from the restaurant name as published by MICHELIN; full address not captured in this pass."},
  {n:"The Beijing Kitchen (Jianguo Road)", s:1, c:"Cantonese", p:"¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:""},
  {n:"The Georg", s:1, c:"European Contemporary", p:"¥¥¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:""},
  {n:"The House of Dynasties", s:1, c:"Cantonese", p:"¥¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:""},
  {n:"Trb Hutong", s:1, c:"French Contemporary", p:"¥¥¥¥", d:"Dongcheng",
   a:"23 Shatan North Street, Dongcheng", h:"Mon–Sun 11:30–14:30, 17:30–22:00", ph:"+86 139 1171 2083", w:"https://www.trbhutong.com/",
   p2:"Weekday lunch ¥788 pp · Seasonal ¥1,688 pp · Signature ¥2,288 pp (+15% service). Two on Seasonal = ¥3,376 + 15% = ¥3,882",
   soc:[["CNN video","https://edition.cnn.com/videos/travel-play/2018/06/22/trb-hutong-beijing-china.cnn"]],
   fx:"Menu prices read from the restaurant's own menu page on 25 Nov 2026; +15% service charge applies."},
  {n:"Xin Rong Ji (Jianguomenwai Street)", s:1, c:"Taizhou", p:"¥¥¥", d:"Chaoyang",
   a:"5F, Tower A, Yintai Centre, 2 Jianguomenwai Street, Chaoyang", h:"", ph:"", w:"https://www.xinrongji.com/", soc:[], fx:""},
  {n:"Xin Rong Ji (Jinrong Street)", s:1, c:"Taizhou", p:"¥¥¥", d:"Xicheng",
   a:"B1, International Finance Centre, 11 Jinrong Street, Xicheng", h:"", ph:"", w:"https://www.xinrongji.com/", soc:[], fx:""},
  {n:"Zhiguan Courtyard", s:1, c:"Dongbei", p:"¥¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:""},
  {n:"Zijin Mansion", s:1, c:"Cantonese", p:"¥¥¥", d:"", a:"", h:"", ph:"", w:"", soc:[], fx:""}
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
const DISTRICT_STARS = {Chaoyang:6, Dongcheng:2, Xicheng:1, Shunyi:1};

/* ------------------------------------------------------------
   ACTIVITIES
   v = verified against the official site in this pass
   ------------------------------------------------------------ */
const ACTIVITIES = [
  {n:"Palace Museum (Forbidden City)", area:"Dongcheng", h:"Tue–Sun 8:30–16:30, last entry 15:30 (1 Nov–31 Mar). Closed Mondays, except national holidays and Chinese New Year's Eve.",
   price:"¥40 low season (1 Nov–31 Mar) · Treasure Gallery +¥10 · Gallery of Clocks +¥10", v:true,
   off:"https://intl.dpm.org.cn/visit.html", book:"https://bookingticket.dpm.org.cn/",
   soc:[["YouTube","https://www.youtube.com/watch?v=yHYT3_xpOSU"],["YouTube","https://www.youtube.com/watch?v=d972yZ8bcx4"],["YouTube","https://www.youtube.com/watch?v=Lr-jVXDSyY0"]],
   fx:"No same-day tickets. Daily cap 40,000. Passport number required for foreign visitors."},
  {n:"Mutianyu Great Wall", area:"Huairou (day trip)", h:"Off-season 16 Nov–15 Mar: 8:00–17:30, ticket sales end 16:30, check-in 8:00–17:00.",
   price:"", v:true, off:"https://en.mutianyugreatwall.com/", book:"https://en.mutianyugreatwall.com/reservation-center/tickets",
   soc:[["YouTube","https://www.youtube.com/watch?v=z49wo_Zki4U"],["YouTube","https://www.youtube.com/watch?v=kU9huPVdVlM"],["YouTube","https://www.youtube.com/watch?v=D9gdGqZ0Pc0"]],
   fx:"Ticket and cable-car prices were not published on the English page read in this pass — check the booking page."},
  {n:"Temple of Heaven Park", area:"Dongcheng", h:"", price:"", v:false, off:"", book:"", soc:[], fx:"Hours and ticket price not yet verified against an official page."},
  {n:"Summer Palace (Yiheyuan)", area:"Haidian", h:"", price:"", v:false, off:"", book:"", soc:[], fx:"Not yet verified against an official page. It is a 60-minute-plus trip from the Wangfujing hotels — verify before scheduling."},
  {n:"Tiananmen Square", area:"Dongcheng", h:"", price:"", v:false, off:"", book:"", soc:[], fx:"Advance real-name reservation is reported to be required; not verified in this pass."},
  {n:"Yonghe Temple (Lama Temple)", area:"Dongcheng", h:"", price:"", v:false, off:"", book:"", soc:[], fx:"Not yet verified. Adjacent to King's Joy (2★), so it pairs naturally with lunch."},
  {n:"798 Art Zone", area:"Chaoyang", h:"", price:"", v:false, off:"", book:"", soc:[], fx:"Not yet verified against an official page."},
  {n:"Nanluoguxiang / hutong walk", area:"Dongcheng", h:"", price:"", v:false, off:"", book:"", soc:[], fx:"Public street, no ticket. Not an official source item."},
  {n:"National Museum of China", area:"Dongcheng", h:"", price:"", v:false, off:"", book:"", soc:[], fx:"Free admission is reported but not verified in this pass; reservation rules need checking."},
  {n:"Jingshan Park (Prospect Hill)", area:"Xicheng", h:"", price:"", v:false, off:"", book:"", soc:[], fx:"Best rooftop view of the Forbidden City; hours not verified in this pass."}
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
