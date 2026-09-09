"""Build fictional country/division report variants. Standard library only; no email sending."""
from pathlib import Path
import csv,json,html
ROOT=Path(__file__).resolve().parents[1]
COUNTRIES=['Northland','Westhaven','Southland']
GROUPS={'Rhythm':['Pacing','Monitoring'],'Vascular':['Coronary','Peripheral']}
PERIODS=['Q1 2025','Q2 2025','Q3 2025','Q4 2025']
COLORS={'Rhythm':'#315cc5','Vascular':'#16786c'}
MARKET_COLOR='#a85d24'

def rows():
 result=[]
 for ci,country in enumerate(COUNTRIES):
  for di,(division,groups) in enumerate(GROUPS.items()):
   for gi,group in enumerate(groups):
    for qi,period in enumerate(PERIODS):
     market=1000+ci*210+di*350+gi*180+qi*130
     units=round(market*(.18+ci*.03+gi*.025+qi*.013))
     asp=480+di*160+gi*85-ci*20+qi*(12-ci*4)
     market_asp=445+di*160+gi*85-ci*20-qi*(3+ci*2)
     result.append(dict(country=country,division=division,product_group=group,period=period,market_units=market,company_units=units,revenue_eur=units*asp,market_revenue_eur=market*market_asp))
 return result

def series(data):
 result=[]
 for period in PERIODS:
  r=[x for x in data if x['period']==period];u=sum(x['company_units'] for x in r);m=sum(x['market_units'] for x in r);rev=sum(x['revenue_eur'] for x in r)
  market_rev=sum(x['market_revenue_eur'] for x in r)
  result.append(dict(period=period,share=u/m*100,asp=rev/u,market_asp=market_rev/m,units=u,market=m,revenue=rev,market_revenue=market_rev))
 return result

def chart(values,x,y,width,height,unit,color,benchmark=None):
 all_values=values+(benchmark or [])
 lo=min(all_values)*.9;hi=max(all_values)*1.05
 s=f'<line x1="{x}" y1="{y+height}" x2="{x+width}" y2="{y+height}" stroke="#cad1dc"/>'
 for si,vals in enumerate([values]+([benchmark] if benchmark is not None else [])):
  stroke=color if si==0 else MARKET_COLOR
  dash='' if si==0 else ' stroke-dasharray="9 6"'
  pts=[(x+i*width/3,y+height-(v-lo)/(hi-lo)*height) for i,v in enumerate(vals)]
  path=' '.join(f'{a:.1f},{b:.1f}' for a,b in pts)
  s+=f'<polyline points="{path}" fill="none" stroke="{stroke}" stroke-width="4"{dash}/>'
  for (a,b),v in zip(pts,vals):
   label_y=b-15 if si==0 else b+26
   s+=f'<circle cx="{a}" cy="{b}" r="5" fill="{stroke}"/><text x="{a}" y="{label_y}" text-anchor="middle" font-size="18" fill="{stroke}">{v:.1f}{unit}</text>'
 for i in range(4):
  s+=f'<text x="{x+i*width/3}" y="{y+height+30}" text-anchor="middle" font-size="16">Q{i+1}</text>'
 if benchmark is not None:
  for lx,label,stroke,dash in [(x,'Company',color,''),(x+175,'Market average',MARKET_COLOR,' stroke-dasharray="9 6"')]:
   s+=f'<line x1="{lx}" y1="{y-30}" x2="{lx+30}" y2="{y-30}" stroke="{stroke}" stroke-width="4"{dash}/><text x="{lx+39}" y="{y-24}" font-size="17">{label}</text>'
 return s

def slide(data,country,division,group):
 a=series(data);color=COLORS[division]
 s=f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675"><rect width="1200" height="675" fill="#fff"/><g font-family="Arial,sans-serif" fill="#182331"><text x="60" y="53" font-size="16" fill="{color}">MANAGEMENT REVIEW / SYNTHETIC DEMONSTRATION</text><text x="60" y="108" font-size="35" font-weight="700">{country} · {division}</text><text x="60" y="147" font-size="25">{group} · 2025 quarterly review</text><line x1="60" y1="177" x2="1140" y2="177" stroke="{color}" stroke-width="3"/><text x="70" y="239" font-size="22">Unit market share</text><text x="685" y="239" font-size="22">Average selling price (EUR)</text>'
 s+=chart([r['share'] for r in a],90,310,430,190,'%',color)+chart([r['asp'] for r in a],710,320,370,180,'',color,[r['market_asp'] for r in a])
 s+='<text x="60" y="604" font-size="16" fill="#586171">ASP = revenue / units, calculated separately for company and total market (including company).</text><text x="60" y="637" font-size="15" fill="#586171">Fictional data and routing. New portfolio demonstration; no live Qlik connection.</text></g></svg>'
 return s

def build():
 data=rows();(ROOT/'reports').mkdir(exist_ok=True)
 with (ROOT/'data/synthetic-market.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=data[0],lineterminator="\n");w.writeheader();w.writerows(data)
 scopes=[];slides=[]
 for country in COUNTRIES:
  for division,groups in GROUPS.items():
   for group in groups:
    subset=[r for r in data if (r['country'],r['division'],r['product_group'])==(country,division,group)]
    key=f'{country}-{division}-{group}'.lower();svg=slide(subset,country,division,group);(ROOT/'reports'/f'{key}.svg').write_text(svg)
    slides.append(dict(id=key,country=country,division=division,group=group,series=series(subset)))
   scopes.append(dict(id=f'{country}-{division}'.lower(),country=country,division=division,recipients=[f'{country.lower()}.{division.lower()}@example.invalid'],slide_ids=[s['id'] for s in slides if s['country']==country and s['division']==division]))
 for division in GROUPS:
  scopes.append(dict(id=f'regional-{division}'.lower(),country='All',division=division,recipients=[f'regional.{division.lower()}@example.invalid'],slide_ids=[s['id'] for s in slides if s['division']==division]))
 (ROOT/'data/distribution-plan.json').write_text(json.dumps(scopes,indent=2)+'\n')
 (ROOT/'reports/manifest.json').write_text(json.dumps(dict(synthetic=True,slides=slides,packages=scopes),indent=2)+'\n')
 style='body{font:18px/1.6 system-ui;max-width:1250px;margin:35px auto;padding:0 24px;color:#182331;background:#fafbfc}a{color:#315cc5}img{width:100%;height:auto;border:1px solid #ccd4df;margin:22px 0}h1{font-size:38px}nav{margin:20px 0}@media print{nav{display:none}img{break-after:page;border:0}body{margin:0;padding:0}}'
 for scope in scopes:
  imgs=''.join(f'<img src="{sid}.svg" alt="{sid.replace("-"," ")} market share and company versus market average selling price">' for sid in scope['slide_ids'])
  page=f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{scope["id"]} report</title><style>{style}</style><nav><a href="index.html">All report packages</a></nav><h1>{scope["country"]} · {scope["division"]}</h1><p>Fictional report package. Routing: {html.escape(", ".join(scope["recipients"]))}. No email is sent.</p>{imgs}</html>'
  (ROOT/'reports'/f'{scope["id"]}.html').write_text(page)
 links=''.join(f'<li><a href="{s["id"]}.html">{s["country"]} / {s["division"]}</a> — {len(s["slide_ids"])} slides</li>' for s in scopes)
 (ROOT/'reports/index.html').write_text(f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Country and division reporting</title><style>{style}</style><h1>One template. Distinct reporting views.</h1><p>12 unique slides, 8 scoped packages, 24 slide placements. Fictional data; generated locally without Qlik or an email connection.</p><ul>{links}</ul><p>Country packages contain only that country and division. Regional packages span countries within one division. Routing illustrates recipient selection; it is not a live authorisation control.</p></html>')
 # Stack diagram uses the same generated slide contents and header scopes, not invented screenshot imagery.
 cards=[slides[0],slides[6],slides[11]];svg='<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="1180" viewBox="0 0 1400 1180"><rect width="1400" height="1180" fill="#edf1f8"/><g font-family="Arial,sans-serif" fill="#182331"><text x="65" y="76" font-size="35" font-weight="700">One template. Distinct country and product views.</text><text x="65" y="119" font-size="23">12 unique slides · 8 scoped packages · all data fictional</text></g>'
 for i,s in enumerate(cards):
  y=200+i*140;x=65+i*65;subset=[r for r in data if (r['country'],r['division'],r['product_group'])==(s['country'],s['division'],s['group'])]
  inner=slide(subset,s['country'],s['division'],s['group']);inner=inner.replace('width="1200" height="675"','width="1120" height="630"',1)
  svg+=f'<g transform="translate({x} {y})"><rect x="-2" y="-2" width="1124" height="634" fill="#c8d1de"/>{inner}</g>'
 svg+='</svg>';(ROOT/'assets/report-stack.svg').write_text(svg)
 print(f'Generated {len(slides)} unique slides and {len(scopes)} packages; 24 slide placements.')
if __name__=='__main__':build()
