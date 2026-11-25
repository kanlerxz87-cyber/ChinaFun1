#!/usr/bin/env python3
"""Structural checks for the generated site: links, tags, row coverage."""
import re
from html.parser import HTMLParser
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "social-2027"

class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.stack=[]; self.bad=[]; self.rows=0; self.cells=0
    def handle_starttag(self, tag, attrs):
        d=dict(attrs)
        if tag=='a': self.links.append(d.get('href',''))
        if tag=='tr': self.rows+=1
        if tag=='td': self.cells+=1
        if tag not in ('meta','link','br','img','input','hr','source'): self.stack.append(tag)
    def handle_endtag(self, tag):
        if not self.stack: self.bad.append('extra '+tag); return
        if self.stack[-1]==tag: self.stack.pop()
        else: self.bad.append('mismatch '+tag+' vs '+self.stack[-1])

pages=sorted(BASE.glob('*.html'))
errors=[]
for p in pages:
    parser=P(); parser.feed(p.read_text())
    for href in parser.links:
        if not href or href.startswith(('http:','https:','mailto:','#')): continue
        target=(BASE/href.split('#')[0]).resolve()
        if not target.exists():
            errors.append(f'{p.name}: broken local link {href}')
    if parser.bad or parser.stack: errors.append(f'{p.name}: tag errors {parser.bad[:3]} leftover {parser.stack[:3]}')
    text=p.read_text()
    for token in (r'\bundefined\b', r'\bnan\b', r'\[object'):
        if re.search(token, text, re.I): errors.append(f'{p.name}: suspicious token {token}')
    if '<title>' not in text or 'name="viewport"' not in text: errors.append(f'{p.name}: missing title/viewport')
    if re.search(r'\{e\(|\{n_|\{\w+\}', text): errors.append(f'{p.name}: unresolved template token in HTML')
    if '<nav id="nav">' in text and 'Overview</a>' not in text: errors.append(f'{p.name}: nav labels missing')
    print(f'{p.name:28s} rows={parser.rows:3d} links={len(parser.links):3d}')

# every restaurant/activity row must carry at least one outbound source link
import json
inv=json.loads((BASE/'data/inventory.json').read_text())['venues']
for fname, city, kind in (('beijing-restaurants.html','Beijing','restaurant'),
                          ('shanghai-restaurants.html','Shanghai','restaurant'),
                          ('activities.html',None,'activity')):
    text=(BASE/fname).read_text()
    for v in inv:
        if v['kind']!=kind: continue
        if city and v['city']!=city: continue
        m=re.search(r'<tr id="'+re.escape(v['id'])+r'">(.*?)</tr>', text, re.S)
        if not m: errors.append(f'{fname}: missing row {v["id"]}'); continue
        if ('rel="noopener noreferrer"' not in m.group(1) and
                'No official source found' not in m.group(1)):
            errors.append(f'{fname}: row {v["id"]} has no outbound link and no flag')

print('\nERRORS',len(errors))
for e in errors: print(' -',e)
raise SystemExit(1 if errors else 0)
