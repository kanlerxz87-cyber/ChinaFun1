#!/usr/bin/env python3
"""Static generator for the social-2027 sub-site. Standard library only.

Data:  ../data/venues.json, ../data/social.json, ../data/content.json
Output: ../index.html and the seven subpages in the same folder.
"""
from __future__ import annotations

import html
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT

PAGES = [
    ("index.html", "Overview", "Executive summary, coverage and method"),
    ("restaurants.html", "Restaurants", "33 Beijing starred restaurants and their verified videos"),
    ("activities.html", "Activities", "10 activities, hours, official links and videos"),
    ("videos.html", "Video index", "All verified video links with first-party proof"),
    ("questions.html", "Questions", "What must be answered before a decision"),
    ("suggestions.html", "Suggestions", "Improvement paths awaiting review"),
    ("flagged.html", "Flagged", "Blanks, irregularities and limits"),
    ("sources.html", "Sources", "Every source used, with what it proved"),
]

NAV = [(f, label) for f, label, _ in PAGES]


def h(value):
    return html.escape(str(value or ""), quote=True)


def load(name):
    with (DATA / name).open(encoding="utf-8") as fh:
        return json.load(fh)


def link(url, label=None, cls=""):
    if not url:
        return '<span class="blank">blank — unverified</span>'
    text = label or url.replace("https://", "").replace("http://", "")
    class_attr = ' class="{}"'.format(h(cls)) if cls else ""
    return '<a href="{}" target="_blank" rel="noopener noreferrer"{}>{}</a>'.format(
        h(url), class_attr, h(text))


def ext_link(url, label):
    return f'<a href="{h(url)}" target="_blank" rel="noopener noreferrer">{h(label)} ↗</a>'


def table(headers, rows, caption="", cls=""):
    """rows: list of list of html strings. Last column is expected to hold sources."""
    body = "".join(
        "<tr>" + "".join(f'<td data-label="{h(headers[i])}">{cell}</td>' for i, cell in enumerate(row)) + "</tr>"
        for row in rows
    )
    head = "".join(f"<th scope=\"col\">{h(x)}</th>" for x in headers)
    cap = f"<caption>{h(caption)}</caption>" if caption else ""
    return (
        f'<div class="table-wrap {h(cls)}"><table><thead><tr>{head}</tr></thead>'
        f"<tbody>{body}</tbody>{cap}</table></div>"
    )


def chips(videos):
    if not videos:
        return '<span class="chip chip-none">No verified link</span>'
    out = []
    for v in videos:
        label = "Short" if "Short" in v["platform"] else "Video"
        out.append(f'<a class="chip" href="{h(v["url"])}" target="_blank" rel="noopener noreferrer">{h(label)} · {h(v["id"])}</a>')
    return " ".join(out)


def source_cell(official, extra=None, verify=None):
    parts = []
    if official:
        parts.append(ext_link(official, "Official page"))
    if extra:
        parts.append(ext_link(extra, "Operator site"))
    if verify:
        parts.append(ext_link(verify, "YouTube proof"))
    if not parts:
        return '<span class="blank">no official source located</span>'
    return "<br>".join(parts)


def shell(title, subtitle, body, active, extra_head=""):
    nav_parts = []
    for filename, label in NAV:
        class_attr = ' class="on"' if filename == active else ""
        nav_parts.append('<a href="{}"{}>{}</a>'.format(h(filename), class_attr, h(label)))
    nav = "".join(nav_parts)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{h(subtitle)}">
<title>{h(title)} · ChinaFun1 social register</title>
<link rel="stylesheet" href="assets/style.css">
{extra_head}
</head>
<body>
<header class="site-head">
  <a class="brand" href="index.html">ChinaFun1 <span>/ social register</span></a>
  <button id="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">Menu</button>
  <nav id="site-nav">{nav}</nav>
</header>
<main>
  <div class="page-head"><h1>{h(title)}</h1><p>{h(subtitle)}</p></div>
  {body}
</main>
<footer>
  <p>Session <code>773e75a3</code> · checked 25 Nov 2026 · every social URL confirmed via YouTube's own oEmbed endpoint · blank means not verified.</p>
  <p><a href="flagged.html">Flagged items</a> · <a href="sources.html">Source register</a> · <a href="../index.html">Back to repo-root plan</a></p>
</footer>
<script src="assets/app.js" defer></script>
</body>
</html>
"""


def main():
    venues_doc = load("venues.json")
    social = load("social.json")
    content = load("content.json")
    venues = venues_doc["venues"]
    by_id = {v["id"]: v for v in venues}
    by_venue = defaultdict(list)
    for v in social["videos"]:
        by_venue[v["venue"]].append(v)

    # ---- index -----------------------------------------------------------
    c = content["coverage"]
    cards = "".join(
        f'<div class="card"><strong>{h(value)}</strong><span>{h(label)}</span></div>'
        for label, value in [
            ("Venues in scope", len(venues)),
            ("Verified video links", c["social_links"]),
            ("Restaurants with links", f'{c["restaurants_with_links"]} / {c["restaurants_total"]}'),
            ("Activities with links", f'{c["activities_with_links"]} / {c["activities_total"]}'),
            ("Hours confirmed", f'{c["hours_confirmed_restaurants"] + c["hours_confirmed_activities"]} / {len(venues)}'),
            ("Platforms verified", "YouTube only"),
        ]
    )
    summary = "".join(f"<li>{h(x)}</li>" for x in content["executive_summary"])
    top = defaultdict(int)
    for v in social["videos"]:
        top[v["venue"]] += 1
    top_rows = []
    for vid, count in sorted(top.items(), key=lambda kv: -kv[1])[:8]:
        vn = by_id[vid]
        top_rows.append([
            h(vn["name"]), h(vn["stars"] or "Activity"), str(count),
            " ".join(f'<a class="chip" href="{h(v["url"])}" target="_blank" rel="noopener noreferrer">{h(v["id"])}</a>' for v in by_venue[vid]),
            source_cell(vn["official"], vn["other"]),
        ])
    index_body = f"""
    <section class="cards">{cards}</section>
    <section class="panel"><h2>Executive summary</h2><ol class="summary">{summary}</ol></section>
    <section class="panel"><h2>Where the verified reviews are</h2>
      {table(["Venue", "Guide status", "Links", "Video IDs", "Official source"], top_rows, "Top eight by number of verified links.")}
    </section>
    <section class="panel"><h2>How a link became “verified”</h2>
      <ol><li>Find candidate videos on {ext_link('https://www.youtube.com/results?search_query=%E6%BD%AE%E4%B8%8A%E6%BD%AE', 'YouTube search (example query)')} — one query per venue, logged in <a href="research-log.md">research-log.md</a>.</li>
      <li>Fetch {ext_link('https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=TTfH0qd79aE&format=json', 'YouTube oEmbed (example)')} for the exact video ID; it returns the canonical title and channel.</li>
      <li>Store the link only if the returned title names the venue. Otherwise leave the cell blank and flag it.</li></ol>
      <p class="note">{h(social['method']['limitations'])}</p>
    </section>
    <section class="panel"><h2>Decision rule</h2><p>Read <a href="questions.html">Questions</a> before choosing a hotel or date. Read <a href="suggestions.html">Suggestions</a> before changing any existing plan. Nothing in this sub-site edits another session's files.</p></section>
    """
    write("index.html", shell("Overview", "A source-checked social-video register for the Beijing trip plan", index_body, "index.html"))

    # ---- restaurants -----------------------------------------------------
    rows = []
    for v in venues:
        if v["type"] != "Restaurant":
            continue
        links = by_venue[v["id"]]
        verify = links[0]["verify"] if links else None
        rows.append([
            f'<strong>{h(v["name"])}</strong><br><span class="muted">{h(v["cuisine"])} · {h(v["district"] or "district blank")}</span>',
            h(v["stars"]), h(v["band"]),
            h(v["hours"]) if v["hours"] else '<span class="blank">blank — unverified</span>',
            chips(links),
            f'<span class="muted">{h(v["flag"])}</span>',
            source_cell(v["official"], v["other"], verify),
        ])
    rbody = f"""
    <section class="panel"><h2>All 33 Beijing 2027 starred restaurants</h2>
      <p class="note">Star status and price band come from the MICHELIN 2027 selection. Social links are third-party videos unless marked “official”. Blank hours are not inferred from reviews.</p>
      {table(["Restaurant", "Guide status", "Band", "Open / exceptions", "Social links (verified)", "Review notes", "Official source"], rows, "Click a video chip to open it; “YouTube proof” opens the exact first-party oEmbed response.")}
    </section>
    """
    write("restaurants.html", shell("Restaurants", "MICHELIN-starred Beijing venues with verified social-video links", rbody, "restaurants.html"))

    # ---- activities ------------------------------------------------------
    arows = []
    for v in venues:
        if v["type"] != "Activity":
            continue
        links = by_venue[v["id"]]
        arows.append([
            f'<strong>{h(v["name"])}</strong><br><span class="muted">{h(v["district"])}</span>',
            h(v["hours"]) if v["hours"] else '<span class="blank">blank — unverified</span>',
            h(v["exceptions"]) if v["exceptions"] else '<span class="blank">no exceptions confirmed</span>',
            chips(links),
            f'<span class="muted">{h(v["flag"])}</span>',
            source_cell(v["official"], v["other"], links[0]["verify"] if links else None),
        ])
    abody = f"""
    <section class="panel"><h2>All 10 activities</h2>
      {table(["Activity", "Open", "Exceptions", "Social links (verified)", "Review notes", "Official source"], arows, "Hours appear only where an official operator page was verified.")}
    </section>
    <section class="panel"><h2>Video coverage by activity</h2><p>Every activity has at least one verified link. The Palace Museum has five, including walking tours and a reservation guide; creator ticket prices are never used as official prices.</p></section>
    """
    write("activities.html", shell("Activities", "Beijing activities with verified social-video links and official hours where available", abody, "activities.html"))

    # ---- video index -----------------------------------------------------
    vrows = []
    for v in social["videos"]:
        vn = by_id[v["venue"]]
        vrows.append([
            h(v["id"]),
            f'<strong>{h(vn["name"])}</strong><br><span class="muted">{h(vn["stars"] or "Activity")}</span>',
            h(v["platform"]),
            h(v["title"]),
            h(v["channel"]),
            h(v["kind"]),
            f'<span class="{"pill-official" if v["source"] == "Official brand channel" else "pill-third"}">{h(v["source"])}</span>',
            f'{ext_link(v["url"], "Watch")}<br>{ext_link(v["verify"], "oEmbed proof")}<br>{ext_link(vn["official"] or vn["other"] or venues_doc["meta"]["guide_list"], "Venue source")}',
        ])
    vbody = f"""
    <section class="panel"><h2>{len(vrows)} verified links</h2>
      <p class="note">{h(social['method']['verification'])}</p>
      <label class="filter-label" for="video-filter">Filter the table</label><input id="video-filter" class="filter" data-filter-table="video-table" type="search" placeholder="Try a venue, channel or video ID">
      {table(["ID", "Venue", "Platform", "Published title (as returned by YouTube)", "Channel", "Kind", "Provenance", "Links / proof"], vrows, "Every row links to the video, its first-party proof and a venue source.", "video-table")}
    </section>
    """
    write("videos.html", shell("Video index", "Every social link, its published title and the first-party proof behind it", vbody, "videos.html"))

    # ---- questions -------------------------------------------------------
    qrows = []
    for q in content["questions"]:
        qrows.append([
            "<strong>" + h(q["id"]) + "</strong>", h(q["q"]), h(q["known"]),
            h(q["missing"]), h(q["resolve"]),
            ext_link(q["source"], "Official source") + "<br>" + ext_link("research-log.md", "Research log"),
        ])
    qbody = f"""
    <section class="panel"><h2>{len(qrows)} open questions</h2>
      <p class="note">Each row separates what is known from what is not. Nothing below is assumed or filled in.</p>
      {table(["#", "Question", "Known", "Missing", "How to resolve", "Official source / log"], qrows)}
    </section>
    """
    write("questions.html", shell("Questions", "What must be answered before a booking decision is reasonable", qbody, "questions.html"))

    # ---- suggestions -----------------------------------------------------
    srows = []
    for s in content["suggestions"]:
        srows.append([
            "<strong>" + h(s["id"]) + "</strong>", h(s["title"]), h(s["problem"]),
            h(s["proposal"]), h(s["path"]), h(s["status"]),
            ext_link(s["source"], "Official source") + "<br>" + ext_link("flagged.html", "Related flags"),
        ])
    sbody = f"""
    <section class="panel"><h2>{len(srows)} proposals — none implemented</h2>
      {table(["#", "Suggestion", "Problem", "Proposal", "Path", "Status", "Official source / review"], srows, "Path A = low effort · Path B = needs an external check · Path C = presentation only.")}
    </section>
    <section class="panel"><h2>Recommended order</h2><ol><li>Decide city and dates (Q1, Q2) — this is the gate for everything else.</li><li>Apply Path A to close hours and social-account gaps (S1, S2, S3).</li><li>Only then spend effort on routing and price tracking (S4, S5).</li></ol></section>
    """
    write("suggestions.html", shell("Suggestions", "Improvement paths for review — no change has been applied", sbody, "suggestions.html"))

    # ---- flagged ---------------------------------------------------------
    frows = []
    for f in content["flags"]:
        frows.append([
            "<strong>" + h(f["id"]) + "</strong>", h(f["title"]), h(f["detail"]),
            h(f["impact"]),
            ext_link(f["source"], "Official source") + "<br>" + ext_link("research-log.md", "Research log"),
        ])
    blanks = [v for v in venues if not v["hours"]]
    brows = [[h(v["id"]), h(v["name"]), "Opening hours", "blank — unverified", source_cell(v["official"], v["other"], by_venue[v["id"]][0]["verify"] if by_venue[v["id"]] else None)] for v in blanks]
    fbody = f"""
    <section class="panel"><h2>Irregularities</h2>
      {table(["#", "Issue", "What was found", "Effect", "Official source / log"], frows)}
    </section>
    <section class="panel"><h2>Blank register — {len(brows)} venue rows</h2>
      <p class="note">These cells are deliberately empty. A blank is never filled from a video description, a search snippet or a pattern-guessed URL.</p>
      {table(["ID", "Venue", "Field", "Value", "Official source"], brows)}
    </section>
    """
    write("flagged.html", shell("Flagged", "Unverified values, failed fetches and irregularities", fbody, "flagged.html"))

    # ---- sources ---------------------------------------------------------
    srcrows = [[h(s["id"]), h(s["name"]), ext_link(s["url"], s["url"].replace("https://", "")), h(s["used_for"])] for s in content["sources"]]
    body = f"""
    <section class="panel"><h2>Source register</h2>
      {table(["#", "Source", "URL", "What it proved"], srcrows)}
    </section>
    <section class="panel"><h2>Verification statement</h2>
      <p>Every video row on the <a href="videos.html">video index</a> carries a link to the exact YouTube oEmbed response used to verify it. Every venue row on the restaurant and activity pages carries a link to an official guide or operator page (or an explicit “no official source located” marker where no page could be fetched). Values without a first-party source are blank and listed on <a href="flagged.html">Flagged</a>.</p>
    </section>
    """
    write("sources.html", shell("Sources", "Official sources and the exact claims each one supports", body, "sources.html"))

    print(f"Generated {len(PAGES)} pages in {OUT}")


def write(name, text):
    (OUT / name).write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
