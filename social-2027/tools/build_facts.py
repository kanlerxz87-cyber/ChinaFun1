#!/usr/bin/env python3
"""Hours/cost facts, each copied from a page fetched this session (2026-11-25).
Blank cells are generated for every other venue by the site generator.
"""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "social-2027/data"

HOURS = [
 # venue, days_open, hours, exceptions, source, evidence
 ("BJ-R05","Mon–Sun","11:00–22:00","No closure or exception stated on the fetched MICHELIN page.","https://guide.michelin.com/us/en/beijing-municipality/beijing/restaurant/king-s-joy","MICHELIN page, opening-hours block: Monday–Sunday 11 AM–10 PM."),
 ("BJ-R29","Mon–Sun","11:30–14:30; 17:30–22:00","No exception stated on the operator page.","https://www.trbhutong.com/findus","Operator page: 'Open Monday through Sunday 11:30 AM - 2:30 PM, 5:30 PM – 10:00 PM'."),
 ("BJ-A01","Tue–Sun (closed Mon)","1 Nov–31 Mar: 08:30–16:30, last entry 15:30. 1 Apr–31 Oct: 08:30–17:00, last entry 16:00.","Monday closed except national traditional holidays; closed on Chinese New Year's Eve; 'does not sell tickets on the day of your visit'; 40,000 daily cap; passport number required for foreign visitors; may close irregularly.","https://intl.dpm.org.cn/visit.html","Official 'Opening Hours' and 'Tickets' tables on the Palace Museum visit page."),
 ("BJ-A02","Daily (off-season timetable applies 16 Nov–15 Mar)","08:00–17:30; ticket sales end 16:30; check-in 08:00–17:00.","Operator states off-season hours from 16 Nov to 15 Mar of the next year. Visitor-volume warnings are posted on the operator notice page.","https://en.mutianyugreatwall.com/","Official 'Opening Hours' block and 'Notes' line."),
 ("DOC-R02","Mon–Wed; Thu–Sun","Mon–Wed 18:00–21:00 (no lunch). Thu–Sun 12:00–13:30 and 18:00–21:00.","No closure stated; no exception stated.","https://guide.michelin.com/en/shanghai-municipality/shanghai/restaurant/8-%C2%BD-otto-e-mezzo-bombana","MICHELIN page opening-hours block lists all seven days separately."),
 ("DOC-R05","Tue–Sun; closed Mon","12:00–13:30; 18:00–21:30","Monday shown as 'closed' on the MICHELIN page.","https://guide.michelin.com/en/shanghai-municipality/shanghai/restaurant/da-vittorio-570570","MICHELIN page opening-hours block: Monday 'closed', Tuesday–Sunday two services."),
 ("DOC-R06","Mon–Sun","11:00–13:00; 17:30–21:00","No closure stated on the fetched MICHELIN page.","https://guide.michelin.com/us/en/shanghai-municipality/shanghai/restaurant/fu-he-hui","MICHELIN page opening-hours block lists the same sessions for all seven days."),
 ("DOC-R12","Mon–Sun for lunch and dinner, but off on Monday","Lunch 11:30–14:00; dinner 17:30–21:00","Operator states 'Off on Monday' on the same page. Reserved tables held only 15 minutes past booking; smart casual attire.","https://www.langhamhotels.com/en/the-langham/shanghai/dine/tang-court/","Official Langham restaurant page, HOURS and IMPORTANT NOTE sections."),
 ("DOC-R13","Mon–Sun","11:30–14:30; 18:00–22:30","No closure or exception stated on the fetched MICHELIN page.","https://guide.michelin.com/en/shanghai-municipality/shanghai/restaurant/yi-long-court","MICHELIN page opening-hours block lists identical sessions for all seven days."),
 ("DOC-A02","Tue–Sun (closed Mon)","09:00–16:30; last entry 16:00","Closed every Monday except national statutory holidays; during Spring Festival hours follow a separate announcement. Off-season ticket applies 1 Dec–31 Mar.","https://www.yugarden.com.cn/page/articleview/message.html","Official 参观信息 page: 开放时间 and 每周一闭园 lines."),
 ("DOC-A04","Tue–Sun (closed Mon)","Day session 09:00–17:00 (last entry 15:00); day & evening session 09:00–21:00 (last entry 19:00)","Closed Mondays except national holidays. During 'On Top of the World Tree' (9 Jul 2026–14 Nov 2027) this branch hosts no other exhibitions; permanent collections are at Museum East. Evening sessions follow the museum's official WeChat channel. Advance booking via WeChat Mini Program; overseas visitors may book through trip.com.","https://www.shanghaimuseum.net/mu/frontend/pg/en/service/visit-west","Official visit page: 'Admission' and 'Guidelines' sections; guidelines effective 30 Jun 2026."),
 ("VER-A02","Wed–Mon (closed Tue)","10:00–18:00; last entry 17:00","Closed Tuesdays except national holidays. Individual visitors need no reservation; The Curio-City and Digital Gallery still require reservations via the museum WeChat account.","https://www.shanghaimuseum.net/mu/frontend/pg/m/en/service/visit-east","Official Museum East visit page: 'Admission' and 'Guidelines'."),
]
COSTS = [
 # venue, total for two, basis, source, evidence, status
 ("BJ-R29","¥1,812.40 / ¥3,882.40 / ¥5,262.40","2 × ¥788 weekday lunch / 2 × ¥1,688 seasonal / 2 × ¥2,288 signature, each +15% service charge. Calculated from the operator menu; not a quoted total for two.","https://www.trbhutong.com/menu","Operator menu prints ¥788 / ¥1,688 / ¥2,288 per person and 'A 15% Service Charge Will Be Added'.","calculated from official prices"),
 ("BJ-A01","¥80 for two (base)","2 × ¥40 low-season ticket (1 Nov–31 Mar); optional galleries +¥10 each per person, so +¥20 for two if both are added. Calculated from the official tariff; no 'couple ticket' exists.","https://intl.dpm.org.cn/visit.html","Official Tickets table: ¥40 low season, ¥10 Treasure Gallery, ¥10 Gallery of Clocks.","calculated from official prices"),
 ("DOC-R12","¥888 (Classic Dim Sum Lunch Set for Two) or ¥2,288 (All Day Set Menu for Two)","Official set-menu PDF labels both as 'FOR TWO' and states prices are inclusive of service charge and taxes.","https://www.langhamhotels.com/content/dam/langhamhotels/tlshx-pdfs/tang-court/2026/seasonal-set-menu-selection-2026.pdf","PDF headings: 'CLASSIC DIM SUM LUNCH SET FOR TWO ¥888', 'ALL DAY SET MENU FOR TWO ¥2,288'.","official total for two"),
 ("DOC-A02","¥60 for two","2 × ¥30 off-season adult ticket (1 Dec–31 Mar), which covers all trip dates. Calculated from the official tariff.","https://www.yugarden.com.cn/page/articleview/message.html","Official 豫园票价: 淡季（12月1日至3月31日）成人每位30元.","calculated from official prices"),
]
def dump(name, keys, rows):
    out=[dict(zip(keys,r)) for r in rows]
    (D/name).write_text(json.dumps({"checked":"2026-11-25","session":"c2067093","count":len(out),"rows":out},ensure_ascii=False,indent=2)+"\n")
dump("hours.json",["venue_id","days_open","hours","exceptions","source_url","evidence"],HOURS)
dump("costs.json",["venue_id","total_for_two","basis","source_url","evidence","status"],COSTS)
print("hours",len(HOURS),"costs",len(COSTS))
