from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
from datetime import date

ROOT = Path(__file__).resolve().parent.parent
PAGES = ['index.html', 'hotels.html', 'restaurants.html', 'activities.html', 'plan.html', 'review.html']
class Checker(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.rows=[]; self.row=None; self.inside_tbody=False; self.title=False
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag=='title': self.title=True
        if tag=='tbody': self.inside_tbody=True
        if tag=='tr' and self.inside_tbody: self.row=[]
        if tag in ('a','link') and attrs.get('href'):
            self.links.append(attrs['href'])
            if self.row is not None and tag=='a': self.row.append(attrs['href'])
    def handle_endtag(self,tag):
        if tag=='tr' and self.row is not None: self.rows.append(self.row); self.row=None
        if tag=='tbody': self.inside_tbody=False

errors=[]
official=('guide.michelin.com','www.gov.cn','www.hyatt.com','www.fourseasons.com','sh.taian-table.cn','www.shanghaimuseum.net','intl.dpm.org.cn','cs.mfa.gov.cn')
for file in PAGES:
    parser=Checker(); parser.feed((ROOT/file).read_text(encoding='utf8'))
    if not parser.title: errors.append(f'{file}: missing title')
    for url in parser.links:
        p=urlparse(url)
        if not p.scheme and not (ROOT / (p.path or file)).exists(): errors.append(f'{file}: missing local link {url}')
    for n,row in enumerate(parser.rows,1):
        if not any(urlparse(url).hostname in official for url in row): errors.append(f'{file} row {n}: no official source link')
assert (date(2027,2,22)-date(2027,2,15)).days == 7
assert (date(2027,3,1)-date(2027,2,15)).days == 14
assert (date(2027,3,23)-date(2027,3,16)).days == 7
if errors: raise SystemExit('\n'.join(errors))
print(f'OK: {len(PAGES)} pages, local links, source per table row and date arithmetic')
