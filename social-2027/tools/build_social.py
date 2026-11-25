#!/usr/bin/env python3
"""Write social.json from links fetched and read on 2026-11-25.

Every row below was opened with fetch_page in this session; the title/creator/date
are copied from the fetched page. Search-result URLs are recorded separately as
rejected, never as reviews. Nothing here is inferred from a URL string.
"""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "social-2027/data/social.json"

# venue_id, platform, url, title, creator, published, kind, official, note
V = [
("BJ-R01","YouTube","https://www.youtube.com/watch?v=_fOMeu8jdCA","Tour of a 3-Michelin-Star Kitchen in China's Capital","The Drunken Sommelier Food Show","2026-01-10","kitchen tour",False,"Description names Chef Cheung's Chao Shang Chao in Beijing; not a diner review."),
("BJ-R02","YouTube","https://www.youtube.com/watch?v=6SvqIT2SW7M","Must Visit 3-Michelin Stars Restaurant ’Xin Rong Ji’ in Beijing.","Ana Loh","2025-02-04","review",False,"Description says the chain's Beijing location holds three stars; no specific branch named."),
("BJ-R04","YouTube Short","https://www.youtube.com/shorts/cB-8dFIIl_Y","I Tried a 2-Michelin-Star Royal Feast in Beijing | Jingji Restaurant Review","Bei Aiba","2026-08-31","review",False,"Description gives Jingji, 2F Ritz-Carlton, 83A Jianguo Road, Chaoyang."),
("BJ-R05","YouTube","https://www.youtube.com/watch?v=TTfH0qd79aE","King's Joy - Michelin 3-star vegetarian restaurant #beijing #michelin #food","Epicurean Escapes","2024-04-06","short clip",False,"Description gives 2 Wudaoying Hutong, Dongcheng, Beijing. Upload says 3-star; the 2027 guide in this repo says Two Stars — older video, flag."),
("BJ-R05","Instagram","https://www.instagram.com/kingsjoy_official/","King’s Joy 京兆尹 (@kingsjoy_official)","King’s Joy 京兆尹","","official account",True,"Bio: Michelin two stars, rsvp@kingsjoy.com, +86(10)8404 9191, No.2 Wudaoying Hutong; links to kingsjoy.com. Fetched 2026-11-25."),
("BJ-R06","YouTube","https://www.youtube.com/watch?v=PiClQQ0s_Bs","Lamdre Beijing Brings Vegetarian Cuisine to New Heights 植物系料理之路，北京蘭齋將蔬食推向新高度","TastyTrip","2024-02-29","restaurant feature",False,"Description: Lamdre, plant-based restaurant in Sanlitun, Chef Dai Jun."),
("BJ-R06","YouTube","https://www.youtube.com/watch?v=2Rsj9Q81qAE","Inside Asia's Hottest New Restaurant: Lamdre in Beijing","The 50","2024-03-04","restaurant feature",False,"Official channel of the 50 Best brand; description names owner Zhao Jia and chef Dai Jun."),
("BJ-R29","Video (CNN)","https://edition.cnn.com/videos/travel-play/2018/06/22/trb-hutong-beijing-china.cnn","Beijing’s beautiful TRB Hutong restaurant","CNN / Black Buddha","2018-06-22","video feature",False,"CNN video page. Not YouTube/TikTok/Instagram: included as a supplementary video link, expressly labelled."),
("BJ-A01","YouTube","https://www.youtube.com/watch?v=yHYT3_xpOSU","BEIJING 4K: Exploring the 9,999 Room Palace | Forbidden City Walk","Pathfinder CN","2026-03-13","walking tour",False,"Description: filmed at The Forbidden City (Palace Museum), Beijing."),
("BJ-A01","YouTube","https://www.youtube.com/watch?v=d972yZ8bcx4","The Forbidden City: China’s Legendary Imperial Palace | 4K Walking Tour","Ambient Explorers","2025-03-08","walking tour",False,"Video transcript walks the Forbidden City."),
("BJ-A01","YouTube","https://www.youtube.com/watch?v=Lr-jVXDSyY0","Beijing China - Forbidden City | 4K HDR Walking Tour","LADmob","2025-08-22","walking tour",False,"Description names Forbidden City, Beijing."),
("BJ-A02","YouTube","https://www.youtube.com/watch?v=z49wo_Zki4U","Unbelievable Toboggan Ride Down the Great Wall of China 4K","Yao Hui","2025-07-23","activity POV",False,"Description names the Mutianyu section and the toboggan."),
("BJ-A02","YouTube","https://www.youtube.com/watch?v=kU9huPVdVlM","The Ultimate Way to Leave the Great Wall of China | Great Wall Toboggan Ride","ActionKid","2026-06-27","activity POV",False,"Transcript: 'Mutianyu section' and slideway ticket booth."),
("BJ-A02","YouTube","https://www.youtube.com/watch?v=D9gdGqZ0Pc0","Exploring the Great Wall of China | Mutianyu East Side & Toboggan Ride","ActionKid","2026-06-30","activity POV",False,"Description names Mutianyu East Section."),
("DOC-R01","YouTube","https://www.youtube.com/watch?v=JNpZw1f49TY","Taian Table Shanghai, China Review | The Best Meal I’ve Ever Had","Oli Eatz","2026-09-30","review",False,"Description gives the Zhenning Road address and a 10-course menu price. Price is a creator's report, NOT an official price."),
("DOC-R01","YouTube","https://www.youtube.com/watch?v=9FbSPG4We0M","I Went to CHINA for This Restaurant - Taian Table (Shanghai)","Alexander The Guest","2023-09-04","review",False,"Description names Taian Table and chef Stefan Stiller."),
("DOC-R01","YouTube","https://www.youtube.com/watch?v=RYsEUZJSrN8","IN-DEPTH REVIEW Of Shanghai's ONLY 3 MICHELIN-STAR Restaurant","Alexander On The Road","2026-07-16","review",False,"Description names Taian Table; transcript shows menu 48 prices quoted by restaurant staff (creator recording, not official menu)."),
("DOC-R01","YouTube Short","https://www.youtube.com/shorts/1Z01UZSP8-w","How many times did you have scrambled eggs in a 3 Michelin-starred restaurant?","Alexander The Guest","2026-07","short clip",False,"Short description: 'This restaurant is Shanghai’s only 3 Michelin star restaurant, Taian Table.'"),
("DOC-R02","YouTube Short","https://www.youtube.com/shorts/1S18-k4lDO4","Chef Nicolo Rotella's Summer Menu - 2 Michelin Star Restaurant 8½ Otto e Mezzo BOMBANA Shanghai","All4Chefs","2024-07-12","chef feature",False,"Title and description name the Shanghai restaurant."),
("DOC-R02","YouTube Short","https://www.youtube.com/shorts/1o1ReTjMkP0","Behind the doors at Otto e Mezzo Bombana Shanghai","All4Chefs","2024-05-13","chef feature",False,"Fetched short title names the Shanghai restaurant."),
("DOC-R02","YouTube Short","https://www.youtube.com/shorts/WCAnMndg-1s","The Favs Shanghai Edition: 8 1/2 Otto e Mezzo Bombana Shanghai — Nicoló","","","short clip",False,"Fetched title names the Shanghai restaurant; no uploader/date exposed by the fetch."),
("DOC-R04","YouTube","https://www.youtube.com/watch?v=XqRipEUwYOs","Canton 8 Shanghai, China Review | Most Affordable 2 Michelin Star Restaurant?","Oli Eatz","2026-10-02","review",False,"Description gives 63 Runan Street, Huangpu and item prices (creator-reported, not official)."),
("DOC-R04","YouTube","https://www.youtube.com/watch?v=MerTf4Wl8Gg","I Tried to the World’s Cheapest 2-Star Michelin Restaurant in The World","Christian Grossi","2026-01-31","review",False,"Description names Canton 8 in Shanghai; price in description is creator-reported."),
("DOC-R04","YouTube","https://www.youtube.com/watch?v=5i4wIJx8Bgo","Maître Kenneth Boon presents the world's cheapest 2 Michelin Star Restaurant Canton 8 in Shanghai","wbpstarscom","2018-10-14","restaurant feature",False,"Title and transcript name Canton 8 Shanghai."),
("DOC-R05","YouTube","https://www.youtube.com/watch?v=gaJsg5lnCvE","My 27th Birthday Dinner at DA VITTORIO, Shanghai","pookpcn","2023-05-07","review",False,"Thai-language review; title and transcript name Da Vittorio Shanghai."),
("DOC-R05","YouTube","https://www.youtube.com/watch?v=ctWXi7a-S0E","#Experience food & wine pairing with Meiyu #DAVITTORIO #SHANGHAI","Meiyu's Wine Pairing","2023-10-19","event feature",False,"Description: Da Vittorio, Two Michelin Star restaurant in Shanghai."),
("DOC-R05","YouTube Short","https://www.youtube.com/shorts/GknYBT4BBhw","TRYING TWO MICHELIN STAR in Shanghai: DA VITTORIO","asdfgvalerie","2023-04-17","short clip",False,"Short description names Da Vittorio in Shanghai."),
("DOC-R06","YouTube","https://www.youtube.com/watch?v=RcjG3JuE-y0","Fu He Hui Shanghai, China Review | Is a 2 Michelin Star Vegetarian Tasting Menu Worth It?","Oli Eatz","2026-10-15","review",False,"Description gives 1037 Yuyuan Road and creator-reported menu price (not official)."),
("DOC-R06","YouTube","https://www.youtube.com/watch?v=RS18ML_iRW0","Fu He Hui Shanghai | 2 Michelin Stars & World’s 50 Best Vegetarian Fine Dining","SongieWorld","2026-10-20","restaurant feature",False,"Description names Fu He Hui and its awards as claimed by the creator."),
("DOC-R06","YouTube","https://www.youtube.com/watch?v=i_2WMZhuL04","Shanghai's Black Pearl Guide: Is Asia's Top 50 Veg Restaurant Worth It?","Bingjie Lin","2025-09-06","multi-restaurant review",False,"Chapters list Fu He Hui at 0:25; three other restaurants are also reviewed."),
("DOC-R06","YouTube Short","https://www.youtube.com/shorts/7APfxnHcnMw","$200 For Michelin Star Vegetables, Worth It? (Fu He Hui)","Clement Leung","2026-05-05","short clip",False,"Description gives Fu He Hui, 1037 Yuyuan Road and a creator-reported 988 RMB price."),
("DOC-R07","YouTube","https://www.youtube.com/watch?v=XTPzS4m9ggQ","This Dim Sum Experience is The Real Imperial Treasure","Black Buddha","2016-07-12","review",False,"Description: 'Shanghai's treasure trove of Chinese classics… Imperial Treasure.'"),
("DOC-A01","YouTube","https://www.youtube.com/watch?v=YqK30WIIvuU","Shanghai The Bund Night Walk 4K | ROCKBUND | Yuyuan Mall | Suzhou Creek","Tour Walking","2026-09-25","walking tour",False,"Chapters start at 'The Bund | Nanjing Road Intersection'."),
("DOC-A01","YouTube","https://www.youtube.com/watch?v=JzqsCnefpWk","4K CHINA Walking Shanghai at Night | From Nanjing Road to The Bund","World Wanderings: 4K Walking Tours","2026-01-02","walking tour",False,"Description features 'The Bund Waterfront' at 1:35:00."),
("DOC-A02","YouTube","https://www.youtube.com/watch?v=5rbE9xE15to","Why You MUST Visit Yu Garden in Shanghai | A Local's Guide","Travel Shanghai Like a Local","2026-10-14","walking tour",False,"Description and transcript focus on Yu Garden itself."),
("DOC-A02","YouTube","https://www.youtube.com/watch?v=Ay96PAha8uQ","Is Visiting Yu Garden in Shanghai REALLY Worth It?","Jimmy Visits World","2025-04-07","review",False,"Description names Yu Garden (Yuyuan Garden), Shanghai."),
("DOC-A02","YouTube","https://www.youtube.com/watch?v=K1sloREQ6bI","The Fabulous YU GARDEN SHANGHAI | Watch this before you go","Paul Ifrim","2023-02-04","review",False,"Description and transcript name Yu Garden in Huangpu."),
("DOC-A02","YouTube","https://www.youtube.com/watch?v=f7ErJ2COBH4","Shanghai - Walking Tour Yu Garden Yuyuan at Night","Walking Expedition","2024-01-30","walking tour",False,"Description names Yu Garden (Yuyuan), filmed November 2023."),
("DOC-A02","YouTube","https://www.youtube.com/watch?v=Und9LL4DX2M","Visiting Shanghai Yu Garden, China","More Bumps Ahead","2020-12-03","review",False,"Description names Yu Garden in central Shanghai."),
("DOC-A03","YouTube","https://www.youtube.com/watch?v=kp04RPUOJ_c","Shanghai Tower - Highest Observation Deck - 118th Floor","WanderFit with Kazi","2019-09-06","activity POV",False,"Title names the Shanghai Tower 118F observation deck."),
("DOC-A03","YouTube","https://www.youtube.com/watch?v=ujsLgyOJYeo","Inside the SHANGHAI TOWER: High-Speed Elevator & 118th Floor Views!","TRAVEL AROUND THE WORLD","2026-05-10","activity POV",False,"Description names the 118th floor, 546 m."),
("DOC-A03","YouTube Short","https://www.youtube.com/shorts/qb1sZXiQML4","55 seconds to the 118th floor, Shanghai Observation Deck","TourChina","2024-09-25","short clip",False,"Title names the Shanghai observation deck at 118F."),
("DOC-A04","YouTube","https://www.youtube.com/watch?v=WH24eys8xd4","Shanghai Museum: Where Arts Shine | 上海博物馆2026新版宣传片","The Shanghai Museum","2026-01-30","official channel",True,"Uploaded by the museum's own YouTube channel; description names the Shanghai Museum."),
("DOC-A04","YouTube","https://www.youtube.com/@theshanghaimuseum","The Shanghai Museum","The Shanghai Museum","","official channel",True,"Channel page fetched; playlists include 'Treasures in Shanghai Museum' and 'The Shanghai Museum East'."),
("DOC-A04","YouTube","https://www.youtube.com/watch?v=bqU3WbL6xac","Shanghai Museum East Branch reopens","Shanghai Let's Meet","2024-06-26","news feature",False,"About the Museum East branch specifically; the plans list both branches."),
]
REJECTED = [
("BJ-R01","YouTube search URL","https://www.youtube.com/results?search_query=Chao+Shang+Chao+Beijing+michelin","Result page returned a 401 banner; a different direct video was mined from the results and verified instead."),
("BJ-R03","YouTube search URL","https://www.youtube.com/results?search_query=Blackswan+restaurant+Beijing+Luohong+Art+Museum","Result page only; no video on it names Blackswan restaurant. No direct review verified."),
("BJ-R04","YouTube search URL","https://www.youtube.com/results?search_query=Jingji+restaurant+Ritz+Carlton+Beijing+michelin","Result page only; direct short mined from the results and verified instead."),
("BJ-R06","YouTube search URL","https://www.youtube.com/results?search_query=Lamdre+Beijing+vegan+michelin","Result page only; two direct videos mined and verified instead."),
("BJ-R07","YouTube search URL","https://www.youtube.com/results?search_query=Lu+Shang+Lu+Beijing+Shandong+michelin","Result page only; none of the visible results names Lu Shang Lu. No direct review verified."),
("DOC-A01","YouTube search URL","https://www.youtube.com/results?search_query=the+bund+shanghai+walking+tour","Result page only; two direct walks mined and verified instead."),
]
payload = {
 "checked": "2026-11-25", "session": "c2067093",
 "method": "Each URL was fetched; title, uploader and date copied from the fetched page. Search-result URLs are rejected. Creator-reported prices are never treated as official prices.",
 "verified": [dict(venue_id=v[0],platform=v[1],url=v[2],title=v[3],creator=v[4],published=v[5],kind=v[6],official_account=v[7],note=v[8]) for v in V],
 "rejected": [dict(venue_id=r[0],platform=r[1],url=r[2],reason=r[3]) for r in REJECTED],
}
OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n")
print("verified",len(V),"rejected",len(REJECTED))
