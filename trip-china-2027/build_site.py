import json, os, html, datetime
from pathlib import Path

BASE = Path('/home/user/ChinaFun1/trip-china-2027')
DATA = BASE/'data'; ASSETS = BASE/'assets'; NOTES = BASE/'notes'
for d in [DATA,ASSETS,NOTES]: d.mkdir(parents=True, exist_ok=True)
TODAY='2026-11-25'
BRANCH='arena/5470d254-chinafun1'

# ---------------------- VERIFIED DATA ----------------------
# MICHELIN: verified from https://guide.michelin.com/en/cn/beijing-municipality/beijing/restaurants/all-starred
# fetched 2026-11-25. 33 starred restaurants total (2x3,5x2,26x1). 
MICHELIN_SOURCE='https://guide.michelin.com/en/cn/beijing-municipality/beijing/restaurants/all-starred'
MICHELIN_RELEASE='https://www.michelin.com/en/publications/products-and-services/michelin-guide-unveils-the-2027-beijing-tianjin-selection'
RESTAURANTS=[
  # 3 stars
  {"name":"Chao Shang Chao (Chaoyang)","stars":3,"cuisine":"Chao Zhou","price_band":"¥¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/chao-shang-chao","status":"MICHELIN 3 Stars","source":MICHELIN_SOURCE},
  {"name":"Xin Rong Ji (Xinyuan South Road)","stars":3,"cuisine":"Taizhou","price_band":"¥¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/xin-rong-ji-xinyuan-south-road","status":"MICHELIN 3 Stars","source":MICHELIN_SOURCE},
  # 2 stars
  {"name":"Black Swan","stars":2,"cuisine":"French Contemporary","price_band":"¥¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/blackswan","status":"MICHELIN 2 Stars","source":MICHELIN_SOURCE},
  {"name":"Jingji","stars":2,"cuisine":"Beijing Cuisine","price_band":"¥¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/jingji","status":"MICHELIN 2 Stars","source":MICHELIN_SOURCE},
  {"name":"King's Joy","stars":2,"cuisine":"Vegetarian","price_band":"¥¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/king-s-joy","status":"MICHELIN 2 Stars","source":MICHELIN_SOURCE},
  {"name":"Lamdre","stars":2,"cuisine":"Vegan","price_band":"¥¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/lamdre","status":"MICHELIN 2 Stars","source":MICHELIN_SOURCE},
  {"name":"Lu Shang Lu","stars":2,"cuisine":"Shandong","price_band":"¥¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/lu-shang-lu","status":"MICHELIN 2 Stars","source":MICHELIN_SOURCE},
  # 1 star
  {"name":"Cai Yi Xuan","stars":1,"cuisine":"Cantonese","price_band":"¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/cai-yi-xuan","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Chao Shang Chao (Xicheng)","stars":1,"cuisine":"Chao Zhou","price_band":"¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/chao-shang-chao-xicheng","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Chef 1996","stars":1,"cuisine":"Sichuan","price_band":"¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/chef-1996","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Fu Chun Ju","stars":1,"cuisine":"Cantonese","price_band":"¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/fu-chun-ju","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Furong","stars":1,"cuisine":"Hunanese","price_band":"¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/furong","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Gastro Esthetics DaDong","stars":1,"cuisine":"Chinese Contemporary","price_band":"¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/gastro-esthetics-dadong","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Giada Garden","stars":1,"cuisine":"Italian","price_band":"¥¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/giada-garden","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Il Ristorante - Niko Romito","stars":1,"cuisine":"Italian","price_band":"¥¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/il-ristorante-niko-romito-1186723","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Lei Garden (Jinbao Tower)","stars":1,"cuisine":"Cantonese","price_band":"¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/lei-garden-jinbao-tower","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Lu Style (Anding Road)","stars":1,"cuisine":"Shandong","price_band":"¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/lu-style","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Mansion Cuisine by Jingyan","stars":1,"cuisine":"Beijing Cuisine","price_band":"¥¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/mansion-cuisine-by-jingyan","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"MO Jasmine","stars":1,"cuisine":"Beijing Cuisine","price_band":"¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/mo-jasmine","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Old Tower","stars":1,"cuisine":"Innovative","price_band":"¥¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/old-tower","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Poetry‧Wine (Dongsanhuan Middle Road)","stars":1,"cuisine":"Beijing Cuisine","price_band":"¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/poetry%E2%80%A7wine","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Rong Pao","stars":1,"cuisine":"Sichuan","price_band":"¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/rong-pao","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Seventh Son","stars":1,"cuisine":"Cantonese","price_band":"¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/seventh-son-1186794","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Shanghai Cuisine","stars":1,"cuisine":"Shanghainese","price_band":"¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/shanghai-cuisine","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Sheng Yong Xing (Chaoyang)","stars":1,"cuisine":"Beijing Cuisine","price_band":"¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/sheng-yong-xing-chaoyang","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"The Beijing Kitchen (Jianguo Road)","stars":1,"cuisine":"Cantonese","price_band":"¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/the-beijing-kitchen","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"The Georg","stars":1,"cuisine":"European Contemporary","price_band":"¥¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/the-georg","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"The House of Dynasties","stars":1,"cuisine":"Cantonese","price_band":"¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/the-house-of-dynasties","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Trb Hutong","stars":1,"cuisine":"French Contemporary","price_band":"¥¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/trb-hutong","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Xin Rong Ji (Jianguomenwai Street)","stars":1,"cuisine":"Taizhou","price_band":"¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/xin-rong-ji-jianguomenwai-street","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Xin Rong Ji (Jinrong Street)","stars":1,"cuisine":"Taizhou","price_band":"¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/xin-rong-ji-jinrong-street","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Zhiguan Courtyard","stars":1,"cuisine":"Dongbei","price_band":"¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/zhiguan","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
  {"name":"Zijin Mansion","stars":1,"cuisine":"Cantonese","price_band":"¥¥¥","district":"","area":"","hours":"","days_open":"","closed":"","price_for_two":"","official_site":"","social_youtube":"","social_instagram":"","social_tiktok":"","guide_url":"https://guide.michelin.com/en/beijing-municipality/beijing/restaurant/zijin-mansion","status":"MICHELIN 1 Star","source":MICHELIN_SOURCE},
]
# NOTE: hours/days_open/closed/price_for_two/district/official_site/social links left blank unless verified.
# They are flagged in flagged.html.

BOOKING_SEARCH='https://www.booking.com/searchresults.html?ss=Beijing&checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1&selected_currency=USD&nflt=class%3D5%3Bht_id%3D204'
BOOKING_MAR='https://www.booking.com/searchresults.html?ss=Beijing&checkin=2027-03-15&checkout=2027-03-22&group_adults=2&no_rooms=1&selected_currency=USD&nflt=class%3D5%3Bht_id%3D204'
BOOKING_FEB22='https://www.booking.com/searchresults.html?ss=Beijing&checkin=2027-02-22&checkout=2027-03-01&group_adults=2&no_rooms=1&selected_currency=USD&nflt=class%3D5%3Bht_id%3D204'

# Hotels: only entries with verifiable data from Booking.com search results fetched 2026-11-25.
# Prices are OTA "from" rates shown by Booking for 7 nights, 2 adults, 1 room, USD, taxes/fees as displayed by Booking.
# Bed/bath compliance: requirement is private bathroom + queen bed or equivalent or bigger.
HOTELS=[
  {"name":"New World Beijing Hotel","rating":"5-star (property listing)","district":"Dongcheng (Qianmen)","area":"Qianmen / Dongcheng","total_7n_public_usd":1177,"total_7n_member_usd":901,"nightly_from_usd":117,"room":"Superior Room King","beds":"1 king bed","private_bath":"Yes (standard room; verify on booking page)","breakfast":"","free_cancel":"Yes","prepay":"No prepayment needed","score":"9.1","reviews":1542,"checkin":"2027-02-15","checkout":"2027-02-22","compliant":"Yes (king bed)","transit_note":"Central Dongcheng; near Qianmen/Chongwenmen subway access (verify exact walking time).","source":BOOKING_SEARCH,"source_note":"Booking.com search results fetched 2026-11-25; member price shown as sign-in rate."},
  {"name":"Sunworld Dynasty Hotel Beijing Wangfujing","rating":"5-star (property listing)","district":"Dongcheng (Wangfujing)","area":"Wangfujing / Dongcheng","total_7n_public_usd":836,"total_7n_member_usd":697,"nightly_from_usd":90,"room":"Superior Room Twin Beds","beds":"2 twin beds","private_bath":"Yes (standard room; verify on booking page)","breakfast":"","free_cancel":"Yes","prepay":"","score":"9.1","reviews":4217,"checkin":"2027-02-15","checkout":"2027-02-22","compliant":"NO - 2 twin beds (fails queen/king requirement). Shown for transparency; exclude from compliant ranking.","transit_note":"Wangfujing; central Dongcheng.","source":BOOKING_SEARCH,"source_note":"Booking.com fetched 2026-11-25; displayed room is twin beds - non-compliant."},
  {"name":"Waldorf Astoria Beijing","rating":"5-star (property listing)","district":"Dongcheng (Wangfujing)","area":"Wangfujing / Dongcheng","total_7n_public_usd":2246,"total_7n_member_usd":None,"nightly_from_usd":292,"room":"Deluxe King Room","beds":"1 king bed","private_bath":"Yes (standard room; verify on booking page)","breakfast":"","free_cancel":"","prepay":"","score":"9.2","reviews":474,"checkin":"2027-02-15","checkout":"2027-02-22","compliant":"Yes (king bed)","transit_note":"Wangfujing; central Dongcheng.","source":BOOKING_SEARCH,"source_note":"Booking.com fetched 2026-11-25."},
  {"name":"Hilton Beijing Wangfujing","rating":"5-star (property listing)","district":"Dongcheng (Wangfujing)","area":"Wangfujing / Dongcheng","total_7n_public_usd":1244,"total_7n_member_usd":None,"nightly_from_usd":162,"room":"Deluxe King Room Plus","beds":"1 king bed","private_bath":"Yes (standard room; verify on booking page)","breakfast":"","free_cancel":"Yes","prepay":"No prepayment needed","score":"8.7","reviews":904,"checkin":"2027-02-15","checkout":"2027-02-22","compliant":"Yes (king bed)","transit_note":"Wangfujing; central Dongcheng.","source":BOOKING_SEARCH,"source_note":"Booking.com fetched 2026-11-25."},
  {"name":"The Peninsula Beijing","rating":"5-star (property listing)","district":"Dongcheng (Wangfujing)","area":"Wangfujing / Dongcheng","total_7n_public_usd":2744,"total_7n_member_usd":None,"nightly_from_usd":356,"room":"Superior King Suite","beds":"1 king bed","private_bath":"Yes (suite; verify on booking page)","breakfast":"","free_cancel":"Yes","prepay":"No prepayment needed","score":"9.5","reviews":596,"checkin":"2027-02-15","checkout":"2027-02-22","compliant":"Yes (king bed)","transit_note":"Wangfujing; central Dongcheng.","source":BOOKING_SEARCH,"source_note":"Booking.com fetched 2026-11-25; displayed room is a suite."},
  {"name":"Happy Dragon Courtyard Hotel (Nearby Forbidden City)","rating":"5-star (property listing)","district":"Dongcheng","area":"Near Forbidden City / Dongcheng","total_7n_public_usd":1075,"total_7n_member_usd":None,"nightly_from_usd":132,"room":"King Room with Garden View","beds":"1 queen bed","private_bath":"Yes (verify on booking page)","breakfast":"Included (as displayed)","free_cancel":"Yes","prepay":"","score":"9.8","reviews":727,"checkin":"2027-02-15","checkout":"2027-02-22","compliant":"Yes (queen bed)","transit_note":"Near Forbidden City; Dongcheng. Verify exact subway/bus access.","source":BOOKING_SEARCH,"source_note":"Booking.com fetched 2026-11-25; Black Friday deal price shown."},
  {"name":"Prime Hotel Beijing Wangfujing","rating":"5-star (property listing)","district":"Dongcheng (Wangfujing)","area":"Wangfujing / Dongcheng","total_7n_public_usd":1029,"total_7n_member_usd":None,"nightly_from_usd":133,"room":"Deluxe Twin Room","beds":"2 full beds","private_bath":"Yes (standard room; verify on booking page)","breakfast":"","free_cancel":"Yes","prepay":"","score":"8.9","reviews":1511,"checkin":"2027-02-15","checkout":"2027-02-22","compliant":"NO - 2 full beds (full < queen; fails requirement). Shown for transparency.","transit_note":"Wangfujing; central Dongcheng.","source":BOOKING_SEARCH,"source_note":"Booking.com fetched 2026-11-25; displayed room is 2 full beds - non-compliant."},
  {"name":"East Sacred Hotel (Wangfujing)","rating":"5-star (property listing)","district":"Dongcheng (Wangfujing)","area":"Wangfujing / Dongcheng","total_7n_public_usd":554,"total_7n_member_usd":None,"nightly_from_usd":79,"room":"Superior Twin Room","beds":"2 twin beds","private_bath":"Yes (verify on booking page)","breakfast":"Included (as displayed)","free_cancel":"Yes","prepay":"No prepayment needed","score":"8.4","reviews":2183,"checkin":"2027-02-15","checkout":"2027-02-22","compliant":"NO - 2 twin beds (fails queen/king requirement). Shown for transparency.","transit_note":"Wangfujing; central Dongcheng.","source":BOOKING_SEARCH,"source_note":"Booking.com fetched 2026-11-25; displayed room is twin beds - non-compliant."},
]

PRICE_WINDOWS=[
  {"window":"15–22 Feb 2027 (7 nights, preferred start)","checkin":"2027-02-15","checkout":"2027-02-22","example":"New World Beijing Hotel: $1,177 public / $901 member (king)","source":BOOKING_SEARCH,"note":"Fetched 2026-11-25. Rates are dynamic."},
  {"window":"22 Feb–1 Mar 2027 (7 nights)","checkin":"2027-02-22","checkout":"2027-03-01","example":"Waldorf Astoria Beijing: $2,246 (Deluxe King Room)","source":BOOKING_FEB22,"note":"Fetched 2026-11-25. Limited sample; compare on Booking for full picture."},
  {"window":"15–22 Mar 2027 (7 nights)","checkin":"2027-03-15","checkout":"2027-03-22","example":"Sunworld Dynasty (twin, non-compliant room shown): $933 public / $778 member","source":BOOKING_MAR,"note":"Fetched 2026-11-25. Sample only; not a compliant-room comparison."},
]

ACTIVITIES=[
  {"name":"The Palace Museum (Forbidden City)","category":"Museum / Heritage","area":"Dongcheng, central Beijing","hours":"Apr 1–Oct 31: 08:30–17:00 (last entry 16:00). Nov 1–Mar 31: 08:30–16:30 (last entry 15:30).","days_open":"Tue–Sun; closed Mondays (except national holidays). Closed eve of Chinese New Year.","closed_notes":"May close on irregular basis; check official notice.","ticket_price":"High season (Apr 1–Oct 31): CNY 60. Low season (Nov 1–Mar 31): CNY 40. Treasure Gallery CNY 10; Clock Gallery CNY 10.","cost_for_two":"Low season base: CNY 80 (2 × CNY 40). Add galleries if selected.","official_site":"https://intl.dpm.org.cn/","source_url":"https://intl.dpm.org.cn/visit.html","social_youtube":"","social_instagram":"","social_tiktok":"","booking":"https://bookingticket.dpm.org.cn/","notes":"Daily visitor cap 40,000; advance online booking required; no same-day ticket sales stated on official visit page. Passport number required for foreign visitors in online booking (per visit page)."},
  {"name":"Mutianyu Great Wall","category":"Outdoor / Heritage","area":"Huairou District (outside central Beijing)","hours":"08:00–17:30 (ticket sales end 16:30; ticket check-in 08:00–17:00). Off-season business hours stated for Nov 16–Mar 15.","days_open":"Open daily per official site notice; verify specific date before travel.","closed_notes":"Off-season hours Nov 16–Mar 15; check official notices for weather/volume warnings.","ticket_price":"","cost_for_two":"","official_site":"https://en.mutianyugreatwall.com/","source_url":"https://en.mutianyugreatwall.com/","social_youtube":"","social_instagram":"https://www.instagram.com/mutianyu_greatwall_official/","social_tiktok":"","booking":"https://en.mutianyugreatwall.com/reservation-center/tickets","notes":"Ticket price not captured from official page during this session - leave blank and flag. Travel time from central Beijing can exceed 1 hour; verify transit before scheduling."},
  {"name":"Temple of Heaven (Tiantan Park)","category":"Park / Heritage","area":"Dongcheng, Beijing","hours":"","days_open":"","closed_notes":"","ticket_price":"","cost_for_two":"","official_site":"","source_url":"","social_youtube":"","social_instagram":"","social_tiktok":"","booking":"","notes":"Not verified in this session. All fields blank pending official source verification."},
  {"name":"Summer Palace","category":"Park / Heritage","area":"Haidian, Beijing","hours":"","days_open":"","closed_notes":"","ticket_price":"","cost_for_two":"","official_site":"","source_url":"","social_youtube":"","social_instagram":"","social_tiktok":"","booking":"","notes":"Not verified in this session. All fields blank pending official source verification."},
  {"name":"National Museum of China","category":"Museum","area":"Dongcheng (Tiananmen Square)","hours":"","days_open":"","closed_notes":"","ticket_price":"","cost_for_two":"","official_site":"","source_url":"","social_youtube":"","social_instagram":"","social_tiktok":"","booking":"","notes":"Not verified in this session. All fields blank pending official source verification."},
]

# Patch verified TRB Hutong details from official site https://www.trbhutong.com/findus (fetched 2026-11-25)
for r in RESTAURANTS:
    if r['name']=='Trb Hutong':
        r['district']='Dongcheng'
        r['area']='Shatan North Street / near National Art Museum'
        r['hours']='11:30 AM – 2:30 PM; 5:30 PM – 10:00 PM'
        r['days_open']='Mon–Sun (daily)'
        r['closed']='None stated on official find-us page'
        r['official_site']='https://www.trbhutong.com/'
        r['source']='https://www.trbhutong.com/findus'
        r['price_for_two']=''
        r['notes']='Address/phone/hours verified from official find-us page. Menu price for two not captured in this session - leave blank.'

def esc(x):
    return html.escape('' if x is None else str(x), quote=True)

def link(url, label=None):
    if not url: return '<span class="muted">—</span>'
    label = label or url
    return f'<a href="{esc(url)}" target="_blank" rel="noopener">{esc(label)}</a>'

def cell(val, src=None, flagged=False):
    if val is None or str(val).strip()=='':
        flag = ' <span class="flag">unverified</span>' if flagged else ' <span class="muted">—</span>'
        src_html = f'<div class="src">{link(src,"source")}</div>' if src else ''
        return f'<td class="blank">{flag}{src_html}</td>'
    src_html = f'<div class="src">{link(src,"source")}</div>' if src else ''
    return f'<td>{esc(val)}{src_html}</td>'

def stars_badge(n):
    return '★'*n + f' <span class="muted">({n})</span>'

NAV=[
  ('index.html','Executive Summary'),
  ('hotels.html','Hotels'),
  ('restaurants.html','MICHELIN Restaurants'),
  ('activities.html','Activities'),
  ('itinerary.html','Itinerary'),
  ('questions.html','Questions'),
  ('suggestions.html','Suggestions'),
  ('flagged.html','Flagged / Verification'),
  ('sources.html','Sources'),
]

def page(title, active, body, description=''):
    nav=''
    for href,label in NAV:
        cls=' class="active"' if href==active else ''
        nav += f'<a{cls} href="{href}">{esc(label)}</a>'
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)} · China Trip 2027</title>
  <meta name="description" content="{esc(description or title)}">
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="topbar">
  <div class="wrap topbar-inner">
    <div class="brand">
      <div class="brand-title">China Trip 2027</div>
      <div class="brand-sub">Beijing · 2 adults · 7 nights · verified-source planner</div>
    </div>
    <button class="menu-btn" aria-label="Open menu" onclick="document.body.classList.toggle('menu-open')">Menu</button>
    <nav class="nav" aria-label="Primary">{nav}</nav>
  </div>
</header>
<main class="wrap">
{body}
</main>
<footer class="wrap footer">
  <p>Built by session <code>5470d254</code> on branch <code>{esc(BRANCH)}</code>. Last updated {TODAY}. Unverified values are left blank and flagged; nothing here is invented.</p>
</footer>
<script src="assets/app.js"></script>
</body>
</html>'''

# Write CSS
(ASSETS/'style.css').write_text(r'''
:root{--bg:#f6f7fb;--card:#fff;--text:#182230;--muted:#5f6b7a;--line:#dbe3ee;--accent:#0b5fff;--accent2:#0a7a5a;--warn:#b45309;--bad:#b91c1c;--good:#166534;--shadow:0 1px 2px rgba(16,24,40,.04),0 4px 16px rgba(16,24,40,.04);--radius:14px;--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;--sans:Inter,system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:var(--sans);color:var(--text);background:var(--bg);line-height:1.5}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:1180px;margin:0 auto;padding:0 16px}
.topbar{position:sticky;top:0;z-index:30;background:rgba(246,247,251,.95);backdrop-filter:saturate(140%) blur(8px);border-bottom:1px solid var(--line)}
.topbar-inner{display:flex;gap:16px;align-items:center;justify-content:space-between;padding:14px 16px}
.brand-title{font-weight:750;font-size:1.1rem;letter-spacing:-.02em}.brand-sub{font-size:.85rem;color:var(--muted)}
.menu-btn{display:none;border:1px solid var(--line);background:#fff;padding:8px 12px;border-radius:10px;font:inherit}
.nav{display:flex;gap:6px;flex-wrap:wrap;justify-content:flex-end}.nav a{padding:8px 10px;border-radius:10px;color:#243041;font-size:.92rem}.nav a:hover{background:#eaf1ff;text-decoration:none}.nav a.active{background:#dfeaff;color:#073ea8;font-weight:600}
main{padding:24px 16px 40px}.hero{background:linear-gradient(135deg,#0b5fff 0%,#1d8fff 55%,#53b5ff 100%);color:#fff;padding:28px;border-radius:20px;box-shadow:var(--shadow);margin-bottom:20px}
.hero h1{margin:0 0 8px;font-size:clamp(1.5rem,4vw,2.3rem);line-height:1.15;letter-spacing:-.03em}.hero p{margin:0;max-width:75ch;opacity:.96}
.hero-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:18px}.stat{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.18);border-radius:12px;padding:12px}.stat .k{font-size:.75rem;text-transform:uppercase;letter-spacing:.04em;opacity:.88}.stat .v{font-size:1rem;font-weight:650;margin-top:4px}
.grid{display:grid;grid-template-columns:repeat(12,1fr);gap:16px;margin:18px 0}.card{grid-column:span 12;background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:18px;box-shadow:var(--shadow)}
.card h2{margin:0 0 10px;font-size:1.2rem;letter-spacing:-.02em}.card h3{margin:18px 0 8px;font-size:1rem}.card p,.card li{color:#243041}.muted{color:var(--muted)}
.pill{display:inline-flex;align-items:center;gap:6px;padding:4px 10px;border-radius:999px;font-size:.78rem;font-weight:600;border:1px solid transparent;white-space:nowrap}
.pill.good{background:#ecfdf3;color:#166534;border-color:#b7ebc6}.pill.warn{background:#fff7ed;color:#9a3412;border-color:#fed7aa}.pill.bad{background:#fef2f2;color:#991b1b;border-color:#fecaca}.pill.info{background:#eff6ff;color:#1d4ed8;border-color:#bfdbfe}
.table-wrap{overflow:auto;-webkit-overflow-scrolling:touch;border:1px solid var(--line);border-radius:12px;background:#fff}
table{width:100%;border-collapse:separate;border-spacing:0;min-width:760px;font-size:.92rem}
th,td{padding:10px 12px;vertical-align:top;text-align:left;border-bottom:1px solid #e8edf3}th{position:sticky;top:0;background:#f8fafc;font-size:.78rem;text-transform:uppercase;letter-spacing:.04em;color:#475569;z-index:1}
tr:last-child td{border-bottom:none}
td .src{margin-top:4px;font-size:.75rem;color:var(--muted);word-break:break-word}
td.blank{color:var(--muted);background:#fcfcfd}
.flag{display:inline-block;font-size:.72rem;padding:2px 7px;border-radius:999px;background:#fff7ed;color:#9a3412;border:1px solid #fed7aa;font-weight:600}
code,kbd{font-family:var(--mono);font-size:.88em;background:#f1f5f9;padding:.12em .35em;border-radius:5px}
ul.check{padding-left:1.2rem} .check li{margin:.35rem 0}
.callout{padding:12px 14px;border-radius:12px;border:1px solid var(--line);background:#f8fafc;margin:12px 0}
.callout.warn{background:#fff7ed;border-color:#fed7aa}.callout.bad{background:#fef2f2;border-color:#fecaca}.callout.good{background:#f0fdf4;border-color:#bbf7d0}
.small{font-size:.88rem;color:var(--muted)}
.footer{padding:24px 16px 40px;color:var(--muted);font-size:.88rem}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.kv{display:grid;grid-template-columns:minmax(140px,220px) 1fr;gap:8px 14px}.kv div:nth-child(odd){color:var(--muted);font-size:.88rem}
@media (max-width:900px){.hero-grid{grid-template-columns:repeat(2,1fr)}.two-col{grid-template-columns:1fr}}
@media (max-width:760px){.menu-btn{display:inline-block}.nav{display:none;position:absolute;left:16px;right:16px;top:calc(100% + 2px);background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px;box-shadow:var(--shadow);flex-direction:column;align-items:stretch}.menu-open .nav{display:flex}.nav a{padding:10px 12px}.topbar-inner{position:relative}.hero{padding:22px}.kv{grid-template-columns:1fr}}
@media print{.topbar,.menu-btn{position:static;backdrop-filter:none}.nav{display:none}body{background:#fff}.card,.hero{box-shadow:none}}
''', encoding='utf-8')

(ASSETS/'app.js').write_text('''// Minimal JS: close mobile menu on outside click
document.addEventListener('click', (e) => {
  if (!document.body.classList.contains('menu-open')) return;
  const top = document.querySelector('.topbar');
  if (top && !top.contains(e.target)) document.body.classList.remove('menu-open');
});
''', encoding='utf-8')

# Data exports
(DATA/'restaurants.json').write_text(json.dumps(RESTAURANTS, ensure_ascii=False, indent=2), encoding='utf-8')
(DATA/'hotels.json').write_text(json.dumps(HOTELS, ensure_ascii=False, indent=2), encoding='utf-8')
(DATA/'activities.json').write_text(json.dumps(ACTIVITIES, ensure_ascii=False, indent=2), encoding='utf-8')
(DATA/'price_windows.json').write_text(json.dumps(PRICE_WINDOWS, ensure_ascii=False, indent=2), encoding='utf-8')

# ---------- Hotels page ----------
hotel_rows=''
for h in sorted(HOTELS, key=lambda x: (0 if x['compliant'].startswith('Yes') else 1, x['total_7n_public_usd'])):
    compliant = h['compliant'].startswith('Yes')
    badge = '<span class="pill good">Compliant</span>' if compliant else '<span class="pill bad">Non-compliant</span>'
    price = f"US${h['total_7n_public_usd']:,} public" + (f" / US${h['total_7n_member_usd']:,} member" if h.get('total_7n_member_usd') else "")
    hotel_rows += f'''<tr>
      <td><strong>{esc(h['name'])}</strong><div class="src">{badge}</div></td>
      <td>{esc(h['area'])}<div class="src">{esc(h['district'])}</div></td>
      <td>{esc(price)}<div class="src">{esc(h['checkin'])} → {esc(h['checkout'])} · 2 adults · 1 room</div><div class="src">{link(h['source'],'Booking search (fetched '+TODAY+')')}</div></td>
      <td>{esc(h['beds'])}<div class="src">Private bath: {esc(h['private_bath'])}</div></td>
      <td>{esc(h['room'])}<div class="src">Breakfast: {esc(h['breakfast'] or 'Not shown / verify')}</div></td>
      <td>{esc(h['score'])} ({esc(h['reviews'])} reviews)<div class="src">Free cancel: {esc(h['free_cancel'] or 'See source')}</div></td>
      <td>{esc(h['transit_note'])}<div class="src"><span class="flag">modelled / verify</span></div></td>
    </tr>'''

window_rows=''
for w in PRICE_WINDOWS:
    window_rows += f'''<tr>
      <td>{esc(w['window'])}</td>
      <td>{esc(w['checkin'])} → {esc(w['checkout'])}</td>
      <td>{esc(w['example'])}</td>
      <td>{esc(w['note'])}<div class="src">{link(w['source'],'Booking search')}</div></td>
    </tr>'''

hotels_body=f'''
<section class="hero"><h1>Hotels — verified pricing & compliance</h1><p>7-night stay for 2 adults, Beijing, check-in 15 Feb 2027 / check-out 22 Feb 2027 (primary window). Only rooms with <strong>private bathroom</strong> and <strong>queen/king-equivalent or larger bed</strong> qualify. Prices are Booking.com OTA rates observed on {TODAY}; they are dynamic and not a locked contract.</p></section>
<div class="grid">
  <div class="card">
    <h2>Compliance rule (applied to every row)</h2>
    <div class="callout warn"><strong>Required:</strong> private bathroom + queen bed or equivalent/bigger for 2 adults. Rooms shown as twin/full in the captured Booking result are marked <span class="pill bad">Non-compliant</span> and excluded from the compliant ranking. Always re-check the exact room name and bed type before booking.</div>
    <h2>Hotel comparison (primary window 15–22 Feb 2027)</h2>
    <div class="table-wrap"><table>
      <thead><tr><th>Hotel</th><th>Area / location</th><th>Total 7-night price (2 adults)</th><th>Bed / bathroom</th><th>Room / meals</th><th>Review score</th><th>Transit note (≤1h target)</th></tr></thead>
      <tbody>{hotel_rows}</tbody>
    </table></div>
    <p class="small">Source for prices: <a href="{esc(BOOKING_SEARCH)}" target="_blank" rel="noopener">Booking.com search results</a> (5-star hotels, Beijing, 2027-02-15→2027-02-22, 2 adults, 1 room, USD). Fetched {TODAY}. Booking displays dynamic rates; member rates require sign-in.</p>
  </div>
  <div class="card">
    <h2>Cheapest upcoming time to book / date-window comparison</h2>
    <p>Limited comparison based on Booking.com searches fetched {TODAY}. This is <strong>not</strong> a full price-history tracker; rates change. The preferred window (15–18 Feb) is only 3 nights — inconsistent with a 1–2 week stay — so 7-night windows starting 15 Feb, 22 Feb, and 15 Mar were sampled.</p>
    <div class="table-wrap"><table>
      <thead><tr><th>Window</th><th>Dates</th><th>Observed sample</th><th>Notes / source</th></tr></thead>
      <tbody>{window_rows}</tbody>
    </table></div>
    <div class="callout warn"><strong>Decision caution:</strong> "Cheapest time to book" cannot be proven from a single-day snapshot. A weekly price tracker is listed in Suggestions. Do not treat these samples as a guaranteed minimum.</div>
  </div>
  <div class="card">
    <h2>MICHELIN-cluster proximity ranking (modelled, not routed)</h2>
    <p>The brief asks for hotels ranked by number/density of MICHELIN restaurants within 1 hour by subway/bus. <strong>No live routing API was verified in this session.</strong> Therefore no fabricated minute-by-minute transit claims are made. Instead, this section gives a transparent, modelled proximity view using hotel district and the known concentration of starred restaurants in central Beijing (Dongcheng/Xicheng/Chaoyang/CBD).</p>
    <div class="callout bad"><strong>Not verified:</strong> Actual door-to-door subway/bus times. Use Amap/Google Maps/Baidu Maps at the exact departure time before relying on the ≤1 hour rule. See Flagged items F-003.</div>
    <div class="table-wrap"><table>
      <thead><tr><th>Hotel</th><th>Area</th><th>MICHELIN cluster access (modelled)</th><th>Evidence / caveat</th></tr></thead>
      <tbody>
        <tr><td>New World Beijing Hotel</td><td>Qianmen/Dongcheng</td><td><span class="pill good">High (modelled)</span> Central Dongcheng; likely convenient to Wangfujing/Dongcheng/CBD clusters by subway.</td><td class="small">Modelled from district; no routed time. <a href="{esc(BOOKING_SEARCH)}" target="_blank" rel="noopener">Booking source</a></td></tr>
        <tr><td>Waldorf Astoria Beijing</td><td>Wangfujing/Dongcheng</td><td><span class="pill good">High (modelled)</span> Wangfujing core; strong access to central starred restaurants.</td><td class="small">Modelled; not routed. <a href="{esc(BOOKING_SEARCH)}" target="_blank" rel="noopener">Booking source</a></td></tr>
        <tr><td>Hilton Beijing Wangfujing</td><td>Wangfujing/Dongcheng</td><td><span class="pill good">High (modelled)</span> Wangfujing core.</td><td class="small">Modelled; not routed. <a href="{esc(BOOKING_SEARCH)}" target="_blank" rel="noopener">Booking source</a></td></tr>
        <tr><td>The Peninsula Beijing</td><td>Wangfujing/Dongcheng</td><td><span class="pill good">High (modelled)</span> Wangfujing core.</td><td class="small">Modelled; not routed. <a href="{esc(BOOKING_SEARCH)}" target="_blank" rel="noopener">Booking source</a></td></tr>
        <tr><td>Happy Dragon Courtyard Hotel</td><td>Near Forbidden City/Dongcheng</td><td><span class="pill good">High (modelled)</span> Very central; may trade luxury amenities for location/value.</td><td class="small">Modelled; not routed. <a href="{esc(BOOKING_SEARCH)}" target="_blank" rel="noopener">Booking source</a></td></tr>
      </tbody>
    </table></div>
  </div>
</div>
'''
(BASE/'hotels.html').write_text(page('Hotels','hotels.html',hotels_body,'Verified hotel pricing and compliance for Beijing Feb 15–22 2027.'), encoding='utf-8')

# ---------- Restaurants page ----------
rest_rows=''
for r in RESTAURANTS:
    social=[]
    if r.get('social_youtube'): social.append(link(r['social_youtube'],'YouTube'))
    if r.get('social_instagram'): social.append(link(r['social_instagram'],'Instagram'))
    if r.get('social_tiktok'): social.append(link(r['social_tiktok'],'TikTok'))
    social_html=' · '.join(social) if social else '<span class="muted">—</span> <span class="flag">not verified</span>'
    hours = r['hours'] or ''
    days = r['days_open'] or ''
    closed = r['closed'] or ''
    price2 = r['price_for_two'] or ''
    official = link(r['official_site'],'Official site') if r['official_site'] else '<span class="muted">—</span> <span class="flag">not verified</span>'
    rest_rows += f'''<tr>
      <td><strong>{esc(r['name'])}</strong><div class="src">{esc(r['status'])}</div></td>
      <td>{stars_badge(r['stars'])}</td>
      <td>{esc(r['cuisine'])}</td>
      <td>{esc(r['price_band'])}<div class="src">MICHELIN price band</div></td>
      <td>{esc(price2) if price2 else '<span class="muted">—</span> <span class="flag">unverified</span>'}<div class="src">Est./exact for 2 adults</div></td>
      <td>{esc(hours) if hours else '<span class="muted">—</span> <span class="flag">unverified</span>'}</td>
      <td>{esc(days) if days else '<span class="muted">—</span> <span class="flag">unverified</span>'}{('<div class="src">Closed: '+esc(closed)+'</div>') if closed else ''}</td>
      <td>{official}<div class="src">{link(r['guide_url'],'MICHELIN Guide')}</div></td>
      <td>{social_html}</td>
    </tr>'''

restaurants_body=f'''
<section class="hero"><h1>MICHELIN Restaurants — Beijing 2027</h1><p>All 33 starred restaurants from the MICHELIN Guide Beijing 2027 selection, verified against the official MICHELIN Guide listing. Starred restaurants are explicitly labeled; no "selected/listed" venue is presented as starred.</p></section>
<div class="grid">
  <div class="card">
    <h2>Verified counts (official MICHELIN 2027 release)</h2>
    <div class="hero-grid" style="margin-top:0">
      <div class="stat" style="background:#eff6ff;color:#1e3a8a;border-color:#bfdbfe"><div class="k">Total starred</div><div class="v">33</div></div>
      <div class="stat" style="background:#eff6ff;color:#1e3a8a;border-color:#bfdbfe"><div class="k">3 Stars</div><div class="v">2</div></div>
      <div class="stat" style="background:#eff6ff;color:#1e3a8a;border-color:#bfdbfe"><div class="k">2 Stars</div><div class="v">5</div></div>
      <div class="stat" style="background:#eff6ff;color:#1e3a8a;border-color:#bfdbfe"><div class="k">1 Star</div><div class="v">26</div></div>
    </div>
    <p class="small" style="margin-top:12px">Sources: <a href="{esc(MICHELIN_SOURCE)}" target="_blank" rel="noopener">MICHELIN Guide Beijing all starred</a> · <a href="{esc(MICHELIN_RELEASE)}" target="_blank" rel="noopener">MICHELIN 2027 Beijing & Tianjin release</a>. Fetched {TODAY}.</p>
    <div class="callout warn"><strong>Data gaps (honest):</strong> For most restaurants, hours/days/closed/price-for-two/official site/social links were <strong>not verified</strong> in this session. Those cells are blank and flagged. Do not infer. The MICHELIN Guide page is the official source for star status, cuisine, and price band.</div>
  </div>
  <div class="card">
    <h2>All starred restaurants (33)</h2>
    <div class="table-wrap"><table>
      <thead><tr><th>Restaurant</th><th>Stars</th><th>Cuisine</th><th>MICHELIN price band</th><th>Cost for 2 adults</th><th>Hours</th><th>Days open / closed</th><th>Links</th><th>Social (YouTube/IG/TikTok)</th></tr></thead>
      <tbody>{rest_rows}</tbody>
    </table></div>
  </div>
</div>
'''
(BASE/'restaurants.html').write_text(page('MICHELIN Restaurants','restaurants.html',restaurants_body,'All 33 MICHELIN-starred Beijing 2027 restaurants with verified source links.'), encoding='utf-8')

# ---------- Activities page ----------
act_rows=''
for a in ACTIVITIES:
    if not a.get('source_url') and not a.get('official_site'):
        continue  # exclude unverified candidates from main table; they go to flagged
    social=[]
    for k,label in [('social_youtube','YouTube'),('social_instagram','Instagram'),('social_tiktok','TikTok')]:
        if a.get(k): social.append(link(a[k],label))
    social_html=' · '.join(social) if social else '<span class="muted">—</span> <span class="flag">not verified</span>'
    act_rows += f'''<tr>
      <td><strong>{esc(a['name'])}</strong><div class="src">{esc(a['category'])}</div></td>
      <td>{esc(a['area'])}</td>
      <td>{esc(a['hours']) if a['hours'] else '<span class="muted">—</span> <span class="flag">unverified</span>'}</td>
      <td>{esc(a['days_open']) if a['days_open'] else '<span class="muted">—</span> <span class="flag">unverified</span>'}<div class="src">{('Closed: '+esc(a['closed_notes'])) if a['closed_notes'] else ''}</div></td>
      <td>{esc(a['ticket_price']) if a['ticket_price'] else '<span class="muted">—</span> <span class="flag">unverified</span>'}<div class="src">2 adults: {esc(a['cost_for_two']) if a['cost_for_two'] else '—'}</div></td>
      <td>{link(a['official_site'],'Official site') if a['official_site'] else '<span class="muted">—</span>'}<div class="src">{link(a['source_url'],'Source page')}</div>{('<div class="src">'+link(a['booking'],'Booking/tickets')+'</div>') if a.get('booking') else ''}</td>
      <td>{social_html}</td>
    </tr>'''

activities_body=f'''
<section class="hero"><h1>Activities — verified hours, tickets, links</h1><p>Only activities with at least one official/verifiable source checked in this session are included in the main table. Unverified candidates are listed in Flagged. No hours or prices are guessed.</p></section>
<div class="grid">
  <div class="card">
    <div class="callout warn"><strong>1-hour travel rule:</strong> Mutianyu Great Wall is outside central Beijing and may exceed the 1-hour subway/bus preference from a central hotel. Verify door-to-door travel time before scheduling. Palace Museum is central and generally compatible with a central-hotel base.</div>
    <h2>Verified activities</h2>
    <div class="table-wrap"><table>
      <thead><tr><th>Activity</th><th>Area</th><th>Hours</th><th>Days open / closed</th><th>Ticket / cost for 2</th><th>Official / source / booking</th><th>Social (YouTube/IG/TikTok)</th></tr></thead>
      <tbody>{act_rows}</tbody>
    </table></div>
  </div>
  <div class="card">
    <h2>Unverified candidates (not in main table)</h2>
    <p>Temple of Heaven, Summer Palace, and National Museum of China were identified as common candidates but were <strong>not verified</strong> in this session. They are intentionally excluded from the verified table. See <a href="flagged.html">Flagged / Verification</a>.</p>
  </div>
</div>
'''
(BASE/'activities.html').write_text(page('Activities','activities.html',activities_body,'Verified Beijing activities with official hours, tickets, and social links.'), encoding='utf-8')

# ---------- Itinerary ----------
# 2027-02-15 is a Monday (verified by datetime)
import datetime as _dt
d0=_dt.date(2027,2,15)
days=[(d0+_dt.timedelta(days=i)) for i in range(7)]
def dow(d): return d.strftime('%a')
def fmt(d): return d.strftime('%a %d %b %Y')

it_rows=''
for i,d in enumerate(days,1):
    note=''
    plan=''
    if dow(d)=='Mon':
        plan='Arrival / settle in; avoid Palace Museum (closed Mondays except national holidays). Optional hutong walk / Wangfujing area. Book MICHELIN dinner in advance.'
        note='Palace Museum closed Monday (official visit page).'
    elif dow(d)=='Tue':
        plan='Palace Museum (morning, advance booking required; low-season 08:30–16:30, last entry 15:30). Evening MICHELIN dinner near central Beijing.'
        note='Palace Museum open Tue–Sun; verify ticket availability.'
    elif dow(d)=='Wed':
        plan='Central Beijing activity (verify hours) + MICHELIN lunch/dinner. Keep within ~1h transit of hotel.'
        note='Choose verified-open venues.'
    elif dow(d)=='Thu':
        plan='Flexible day: Temple of Heaven / National Museum candidate ONLY if verified before booking. Alternative: shopping, hutongs, verified museum.'
        note='Unverified candidates flagged.'
    elif dow(d)=='Fri':
        plan='MICHELIN-focused day. Reserve starred restaurant; confirm opening day/hours directly.'
        note='Most restaurant hours unverified in this session.'
    elif dow(d)=='Sat':
        plan='Day trip candidate: Mutianyu Great Wall (verify weather, transport, ticket; travel may exceed 1h).'
        note='Mutianyu hours verified; ticket price not verified here.'
    elif dow(d)=='Sun':
        plan='Buffer / departure prep / final MICHELIN meal. Confirm checkout and airport transfer.'
        note=''
    note_html = esc(note) if note else '<span class="muted">—</span>'
    it_rows += f'<tr><td>Day {i}</td><td>{esc(fmt(d))}</td><td>{esc(plan)}</td><td>{note_html}<div class="src"><a href="activities.html">Activities</a> · <a href="restaurants.html">Restaurants</a></div></td></tr>'

itinerary_body=f'''
<section class="hero"><h1>7-night itinerary (draft, verification-first)</h1><p>Proposed 7-night plan starting {fmt(days[0])} through checkout {fmt(days[-1]+_dt.timedelta(days=1))}. This is a planning scaffold — activities/restaurants with unverified hours are marked as verify-before-booking.</p></section>
<div class="grid">
  <div class="card">
    <div class="callout warn"><strong>Date note:</strong> The brief's preferred window 15–18 Feb 2027 is 3 nights, which conflicts with a 1–2 week trip. This plan uses 7 nights starting 15 Feb 2027 (checkout 22 Feb 2027) and flags the conflict. <strong>15 Feb 2027 is a Monday</strong> — Palace Museum is closed Mondays per official visit page.</div>
    <div class="table-wrap"><table>
      <thead><tr><th>Day</th><th>Date</th><th>Plan</th><th>Verification note / source</th></tr></thead>
      <tbody>{it_rows}</tbody>
    </table></div>
  </div>
</div>
'''
(BASE/'itinerary.html').write_text(page('Itinerary','itinerary.html',itinerary_body,'7-night Beijing itinerary draft with verification notes.'), encoding='utf-8')

# ---------- Questions ----------
questions=[
  ("Q1","Destination confirmed as Beijing?","The brief says 'Trip Planning China' without naming a city. This session chose Beijing because the MICHELIN Guide Beijing 2027 is officially published. Confirm city choice before booking.","High","User decision; compare Beijing vs Shanghai plans already in repo."),
  ("Q2","Preferred dates: 3 nights or 7 nights?","Brief states preferred 15–18 Feb 2027 (3 nights) but also asks for 1–2 weeks. This plan prices 7 nights 15–22 Feb 2027.","High","Confirm exact travel dates and trip length."),
  ("Q3","Hotel bed type on final booking page?","Some Booking-displayed rooms were twin/full. Requirement is queen/king or equivalent/bigger. Non-compliant rooms are excluded from ranking.","High","Open the hotel's room selection page and confirm bed type before paying."),
  ("Q4","Actual door-to-door transit times (≤1 hour)?","No routing API was verified. Hotel-MICHELIN proximity is modelled by district only.","High","Use Amap/Google Maps transit directions for exact departure times."),
  ("Q5","Restaurant opening days/hours for specific dates?","Only TRB Hutong hours verified from official site in this session; 32/33 restaurants have unverified hours.","High","Check each restaurant's official site/MICHELIN page/phone before reserving."),
  ("Q6","Exact menu price for 2 adults?","MICHELIN shows price bands (¥¥–¥¥¥¥), not a fixed dinner-for-two total for most venues.","Medium","Check official menu PDFs or call restaurants; record per-person/set-menu price."),
  ("Q7","Mutianyu ticket price and transport cost?","Official Mutianyu site confirms hours but ticket price was not captured in this session.","Medium","Check https://en.mutianyugreatwall.com/reservation-center/tickets and transport options."),
  ("Q8","Which MICHELIN restaurants are within 1h of chosen hotel?","Requires verified routing and restaurant addresses. Only district-level model available.","High","Build a hotel×restaurant transit matrix after geocoding verified addresses."),
  ("Q9","Visa/entry requirements for travelers' passports?","Not verified for the travelers' specific nationalities in this session.","High","Check official embassy/consulate and government travel advisory for traveler nationality."),
  ("Q10","Are Booking.com OTA prices final?","Prices were captured 2026-11-25 and are dynamic; taxes/fees/service charges may differ at checkout.","Medium","Re-check total price on Booking and hotel's official site before booking."),
]
q_rows=''.join(f"<tr><td>{esc(i)}</td><td><strong>{esc(q)}</strong></td><td>{esc(why)}</td><td>{esc(impact)}</td><td>{esc(how)}</td></tr>" for i,q,why,impact,how in questions)
questions_body=f'''
<section class="hero"><h1>Open questions & missing information</h1><p>Decisions that cannot be responsibly made without additional verified information. No question below is answered by guessing.</p></section>
<div class="grid"><div class="card">
  <div class="table-wrap"><table>
    <thead><tr><th>ID</th><th>Question</th><th>Why it matters</th><th>Impact</th><th>How to resolve</th></tr></thead>
    <tbody>{q_rows}</tbody>
  </table></div>
</div></div>
'''
(BASE/'questions.html').write_text(page('Questions','questions.html',questions_body,'Open questions and missing information before booking.'), encoding='utf-8')

# ---------- Suggestions ----------
suggestions=[
  ("S1","Build a verified hotel × restaurant transit matrix","High","Use Amap/Google Maps Directions API or manual verified checks to compute subway/bus time from each compliant hotel to each starred restaurant. Publish only verified times.","Improves the core ranking requirement; replaces modelled proximity.","Do not implement until routing source is verified and reproducible."),
  ("S2","Capture restaurant hours/days/menus from official sources","High","For each MICHELIN restaurant, open official site or verified listing and record hours, closed days, menu price for two. Leave blank if not published.","Makes dining planning reliable.","Use official restaurant sites / MICHELIN detail pages; do not scrape paywalled/unverifiable sources."),
  ("S3","Add weekly price tracker","Medium","Record 7-night total for compliant king/queen rooms weekly in a CSV with timestamp and source URL.","Answers 'cheapest time to book' with evidence instead of snapshot.","Track same room type; include taxes/fees notes."),
  ("S4","Verify social media links for every venue","Medium","Find official/verified YouTube, Instagram, TikTok accounts or review videos for each restaurant/activity; label as official vs third-party.","Satisfies social-link requirement with provenance.","Do not guess handles; verify via official website links or verified profiles."),
  ("S5","Add visa/entry advisory section per nationality","High","Add a table for traveler nationality with official embassy/consulate source links. Do not generalize.","Prevents entry issues.","Only use official government sources."),
  ("S6","Add airport transfer and transit card guidance","Low","Document PEK/PKX to hotel options with official sources and estimated costs from official operators.","Improves arrival planning.","Verify current prices from official operator pages."),
]
s_rows=''.join(f"<tr><td>{esc(i)}</td><td><strong>{esc(t)}</strong></td><td>{esc(p)}</td><td>{esc(desc)}</td><td>{esc(impact)}</td><td>{esc(caveat)}</td></tr>" for i,t,p,desc,impact,caveat in suggestions)
suggestions_body=f'''
<section class="hero"><h1>Suggestions (review before implementing)</h1><p>Improvement ideas only. Nothing here is implemented automatically. Each suggestion includes impact and caveat.</p></section>
<div class="grid"><div class="card">
  <div class="table-wrap"><table>
    <thead><tr><th>ID</th><th>Suggestion</th><th>Priority</th><th>Description</th><th>Expected impact</th><th>Caveat / before implementing</th></tr></thead>
    <tbody>{s_rows}</tbody>
  </table></div>
</div></div>
'''
(BASE/'suggestions.html').write_text(page('Suggestions','suggestions.html',suggestions_body,'Suggestions for improving the trip planner.'), encoding='utf-8')

# ---------- Flagged ----------
flagged_items=[
  ("F-001","Hotel prices are OTA snapshots","Booking.com prices were fetched 2026-11-25 for 15–22 Feb 2027. They are dynamic, may change, and may exclude/add taxes/fees at checkout. Member prices require sign-in.","Use Booking search URL per row; re-verify before booking.","Hotels"),
  ("F-002","Non-compliant room types displayed","Sunworld Dynasty (twin beds), Prime Hotel (2 full beds), East Sacred Hotel (twin beds) were shown in Booking results but do not meet queen/king requirement. They are excluded from compliant ranking.","Booking search URL; room name shown in table.","Hotels"),
  ("F-003","Transit times not routed","The ≤1 hour subway/bus rule was not verified with a routing engine. Hotel-MICHELIN proximity is modelled by district only.","No official routing source captured; flag remains open.","Hotels / Ranking"),
  ("F-004","Restaurant hours/days/price-for-two mostly unverified","Only TRB Hutong has verified hours/address from official site in this session. 32/33 restaurants have blank hours/days/closed/price-for-two.","MICHELIN guide URLs are official for star/cuisine/band; other fields blank.","Restaurants"),
  ("F-005","Social media links incomplete","Requirement asks for YouTube/TikTok/Instagram for every restaurant/activity. Most are unverified. Mutianyu Instagram found from official web presence; others need verification.","Only verified links included; blanks flagged.","Restaurants / Activities"),
  ("F-006","Preferred window conflict","Brief prefers 15–18 Feb 2027 (3 nights) but also asks for 1–2 weeks. Plan uses 7 nights starting 15 Feb 2027.","Flagged in itinerary and questions.","Itinerary"),
  ("F-007","Mutianyu ticket price not captured","Official site confirms hours/booking path but ticket price was not captured in this session.","https://en.mutianyugreatwall.com/","Activities"),
  ("F-008","Unverified activity candidates excluded","Temple of Heaven, Summer Palace, National Museum of China not verified in this session; excluded from main table.","No official source captured in-session.","Activities"),
  ("F-009","Booking.com 5-star label is platform rating","Property star rating on Booking may not equal an official tourism star classification; treated as platform listing metadata.","Booking search results.","Hotels"),
]
f_rows=''.join(f"<tr><td>{esc(i)}</td><td><strong>{esc(t)}</strong></td><td>{esc(d)}</td><td>{esc(src)}</td><td>{esc(scope)}</td></tr>" for i,t,d,src,scope in flagged_items)

flagged_body=f'''
<section class="hero"><h1>Flagged items & verification log</h1><p>Every blank/unverified value is intentional. This page lists irregularities, data gaps, and verification status. No value was inferred to fill a gap.</p></section>
<div class="grid">
  <div class="card">
    <h2>Verification summary</h2>
    <div class="kv">
      <div>MICHELIN 33 starred restaurants</div><div><span class="pill good">Verified</span> Names, stars, cuisine, price band, guide URLs verified against official MICHELIN Guide listing fetched {TODAY}.</div>
      <div>MICHELIN 2027 release counts</div><div><span class="pill good">Verified</span> 107 Beijing restaurants; 2/5/26 stars; 32 Bib Gourmand; 42 Selected. Source: <a href="{esc(MICHELIN_RELEASE)}" target="_blank" rel="noopener">michelin.com release</a>.</div>
      <div>Palace Museum hours/tickets</div><div><span class="pill good">Verified</span> From <a href="https://intl.dpm.org.cn/visit.html" target="_blank" rel="noopener">intl.dpm.org.cn/visit.html</a>.</div>
      <div>Mutianyu hours</div><div><span class="pill good">Verified</span> From <a href="https://en.mutianyugreatwall.com/" target="_blank" rel="noopener">en.mutianyugreatwall.com</a>. Ticket price not captured.</div>
      <div>Hotel prices</div><div><span class="pill warn">OTA snapshot</span> Booking.com search results fetched {TODAY}; dynamic rates.</div>
      <div>Restaurant hours/price-for-two/social</div><div><span class="pill bad">Mostly unverified</span> Only TRB Hutong hours/address verified from official site.</div>
      <div>Transit ≤1 hour</div><div><span class="pill bad">Not routed</span> Modelled by district only; no fabricated times.</div>
    </div>
  </div>
  <div class="card">
    <h2>Flagged irregularities / gaps</h2>
    <div class="table-wrap"><table>
      <thead><tr><th>ID</th><th>Issue</th><th>Detail</th><th>Source / evidence</th><th>Scope</th></tr></thead>
      <tbody>{f_rows}</tbody>
    </table></div>
  </div>
  <div class="card">
    <h2>Repo review (session 5470d254)</h2>
    <ul class="check">
      <li><strong>Observed:</strong> Repository contains multiple prior session outputs (Beijing root by fac6d965; Shanghai docs/ by 68e13071; shanghai-2027/ by 3b27db6c; shanghai-verified-2027/ by 16153d37). Existing COORDINATION.md and README.md document conflicts and resolutions.</li>
      <li><strong>Observed:</strong> Root site files are owned by prior sessions. This session does not modify them.</li>
      <li><strong>Observed:</strong> <code>.gitignore</code> exists; <code>__pycache__</code> patterns present in prior notes/history - I will avoid committing pycache.</li>
      <li><strong>Risk:</strong> Multiple overlapping plans can confuse users; README should clearly distinguish them. This session extends README additively.</li>
      <li><strong>Risk:</strong> Prior plans contain modelled transit/pricing snapshots; users may mistake them for current verified facts. All snapshots should be timestamped.</li>
    </ul>
  </div>
</div>
'''
(BASE/'flagged.html').write_text(page('Flagged / Verification','flagged.html',flagged_body,'Verification log, flagged gaps, and repo review.'), encoding='utf-8')

# ---------- Sources ----------
sources=[
  ("MICHELIN Guide - Beijing all starred restaurants","Official restaurant list (stars, cuisine, price band, URLs)","https://guide.michelin.com/en/cn/beijing-municipality/beijing/restaurants/all-starred","Fetched 2026-11-25"),
  ("MICHELIN 2027 Beijing & Tianjin selection release","Official counts and new stars","https://www.michelin.com/en/publications/products-and-services/michelin-guide-unveils-the-2027-beijing-tianjin-selection","Fetched 2026-11-25"),
  ("Palace Museum (intl.dpm.org.cn) - Visit","Opening hours, tickets, booking, closure rules","https://intl.dpm.org.cn/visit.html","Fetched 2026-11-25"),
  ("Mutianyu Great Wall official site","Opening hours, booking path, notices","https://en.mutianyugreatwall.com/","Fetched 2026-11-25"),
  ("TRB Hutong official find-us page","Address, hours, phone","https://www.trbhutong.com/findus","Fetched 2026-11-25"),
  ("Booking.com Beijing 5-star search (15–22 Feb 2027)","Hotel prices/room/bed/cancellation snapshot","https://www.booking.com/searchresults.html?ss=Beijing&checkin=2027-02-15&checkout=2027-02-22&group_adults=2&no_rooms=1&selected_currency=USD&nflt=class%3D5%3Bht_id%3D204","Fetched 2026-11-25"),
  ("Booking.com Beijing 5-star search (22 Feb–1 Mar 2027)","Date-window comparison sample","https://www.booking.com/searchresults.html?ss=Beijing&checkin=2027-02-22&checkout=2027-03-01&group_adults=2&no_rooms=1&selected_currency=USD&nflt=class%3D5%3Bht_id%3D204","Fetched 2026-11-25"),
  ("Booking.com Beijing 5-star search (15–22 Mar 2027)","Date-window comparison sample","https://www.booking.com/searchresults.html?ss=Beijing&checkin=2027-03-15&checkout=2027-03-22&group_adults=2&no_rooms=1&selected_currency=USD&nflt=class%3D5%3Bht_id%3D204","Fetched 2026-11-25"),
]
src_rows=''.join(f"<tr><td><strong>{esc(n)}</strong></td><td>{esc(u)}</td><td>{link(url,url)}</td><td>{esc(d)}</td></tr>" for n,u,url,d in sources)
sources_body=f'''
<section class="hero"><h1>Sources</h1><p>Primary sources used in this session. Every data row in this plan should trace back to one of these sources or be flagged as unverified.</p></section>
<div class="grid"><div class="card">
  <div class="table-wrap"><table>
    <thead><tr><th>Source</th><th>What it supports</th><th>URL</th><th>Fetch / note</th></tr></thead>
    <tbody>{src_rows}</tbody>
  </table></div>
</div></div>
'''
(BASE/'sources.html').write_text(page('Sources','sources.html',sources_body,'Source register for trip-china-2027.'), encoding='utf-8')

# ---------- Index ----------
compliant=[h for h in HOTELS if h['compliant'].startswith('Yes')]
compliant_sorted=sorted(compliant, key=lambda x:x['total_7n_public_usd'])
top=compliant_sorted[0] if compliant_sorted else None
index_body=f'''
<section class="hero">
  <h1>Beijing Trip Planner — 7 nights, 2 adults</h1>
  <p>Source-verified planning dashboard for 15–22 Feb 2027 (preferred start 15 Feb 2027). Built with a strict rule: if a value is not confirmed by an official/verifiable source, it is left blank and flagged.</p>
  <div class="hero-grid">
    <div class="stat"><div class="k">Primary window</div><div class="v">15–22 Feb 2027</div></div>
    <div class="stat"><div class="k">Travelers</div><div class="v">2 adults · 1 room</div></div>
    <div class="stat"><div class="k">MICHELIN starred</div><div class="v">33 (2027 Beijing)</div></div>
    <div class="stat"><div class="k">Compliant hotels priced</div><div class="v">{len(compliant)} verified rows</div></div>
  </div>
</section>
<div class="grid">
  <div class="card">
    <h2>Executive summary</h2>
    <div class="callout good"><strong>Recommended starting point (based on verified snapshot):</strong> {esc(top['name']) if top else 'No compliant hotel verified'} — {('US$'+format(top['total_7n_public_usd'],',')+' public total for 7 nights, '+esc(top['beds'])+', '+esc(top['area'])) if top else ''}. <span class="small">Booking.com snapshot {TODAY}; re-verify before booking.</span></div>
    <ul class="check">
      <li><strong>Destination:</strong> Beijing (chosen because MICHELIN Guide Beijing 2027 is officially published; confirm before booking). Shanghai plans also exist in this repo.</li>
      <li><strong>Dates:</strong> 7 nights, check-in 2027-02-15, check-out 2027-02-22. Preferred brief window 15–18 Feb is only 3 nights — flagged as a conflict.</li>
      <li><strong>Hotel rule:</strong> private bathroom + queen bed or equivalent/bigger. Non-compliant displayed rooms are excluded.</li>
      <li><strong>MICHELIN:</strong> 33 starred restaurants in Beijing 2027 (2×3★, 5×2★, 26×1★). Official MICHELIN guide links included for every row.</li>
      <li><strong>Transit rule:</strong> ≤1 hour by subway/bus to MICHELIN clusters is <strong>not routed/verified</strong> in this session; district-level model only, flagged.</li>
      <li><strong>Honesty rule:</strong> blanks = unverified. No fabricated hours, prices, social links, or transit times.</li>
    </ul>
  </div>
  <div class="card two-col">
    <div>
      <h2>Key verified facts</h2>
      <div class="kv">
        <div>Palace Museum</div><div>Tue–Sun; closed Mon. Low season 08:30–16:30, last entry 15:30; CNY 40. <a href="https://intl.dpm.org.cn/visit.html" target="_blank" rel="noopener">Official</a></div>
        <div>Mutianyu Great Wall</div><div>08:00–17:30; ticket sales end 16:30; off-season Nov 16–Mar 15. Ticket price unverified. <a href="https://en.mutianyugreatwall.com/" target="_blank" rel="noopener">Official</a></div>
        <div>TRB Hutong</div><div>Daily 11:30–14:30, 17:30–22:00. <a href="https://www.trbhutong.com/findus" target="_blank" rel="noopener">Official</a></div>
        <div>15 Feb 2027</div><div>Monday — Palace Museum closed; plan arrival/light activities.</div>
      </div>
    </div>
    <div>
      <h2>What still needs verification</h2>
      <ul class="check">
        <li>Restaurant hours/days/price-for-two for 32/33 starred venues.</li>
        <li>Social media links for most venues.</li>
        <li>Door-to-door subway/bus travel times.</li>
        <li>Live hotel re-price before booking.</li>
        <li>Mutianyu ticket price and transport.</li>
      </ul>
      <p><a href="flagged.html">See all flagged items →</a></p>
    </div>
  </div>
  <div class="card">
    <h2>Pages</h2>
    <div class="table-wrap"><table>
      <thead><tr><th>Page</th><th>Purpose</th></tr></thead>
      <tbody>
        <tr><td><a href="hotels.html">Hotels</a></td><td>Compliant hotel comparison, 7-night totals, date-window samples, modelled cluster ranking.</td></tr>
        <tr><td><a href="restaurants.html">MICHELIN Restaurants</a></td><td>All 33 starred Beijing 2027 restaurants with official guide links and flagged gaps.</td></tr>
        <tr><td><a href="activities.html">Activities</a></td><td>Verified activities with hours/tickets/official/social links.</td></tr>
        <tr><td><a href="itinerary.html">Itinerary</a></td><td>7-night draft respecting closures and verification constraints.</td></tr>
        <tr><td><a href="questions.html">Questions</a></td><td>Decisions that need user input or verified follow-up.</td></tr>
        <tr><td><a href="suggestions.html">Suggestions</a></td><td>Improvements to review before implementing.</td></tr>
        <tr><td><a href="flagged.html">Flagged / Verification</a></td><td>Verification log, gaps, irregularities, repo review.</td></tr>
        <tr><td><a href="sources.html">Sources</a></td><td>Source register.</td></tr>
      </tbody>
    </table></div>
  </div>
</div>
'''
(BASE/'index.html').write_text(page('Executive Summary','index.html',index_body,'Beijing 7-night trip planner for 2 adults with verified sources.'), encoding='utf-8')

print('built', len(list(BASE.glob('*.html'))), 'html files')
