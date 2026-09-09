import unittest,sys,json
from pathlib import Path
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'demo'))
from build import rows,series
class ReportChecks(unittest.TestCase):
 def setUp(self):
  self.data=rows();self.m=json.loads((R/'reports/manifest.json').read_text())
 def test_country_division_isolation(self):
  slides={s['id']:s for s in self.m['slides']}
  for p in self.m['packages']:
   self.assertEqual(len(set(p['slide_ids'])),len(p['slide_ids']))
   for sid in p['slide_ids']:
    s=slides[sid];self.assertEqual(s['division'],p['division'])
    if p['country']!='All':self.assertEqual(s['country'],p['country'])
 def test_weighted_ratios_reconcile(self):
  totals=series(self.data)
  for t in totals:
   r=[r for r in self.data if r['period']==t['period']]
   self.assertAlmostEqual(t['asp'],sum(x['revenue_eur'] for x in r)/sum(x['company_units'] for x in r))
   self.assertAlmostEqual(t['market_asp'],sum(x['market_revenue_eur'] for x in r)/sum(x['market_units'] for x in r))
   self.assertAlmostEqual(t['share'],100*sum(x['company_units'] for x in r)/sum(x['market_units'] for x in r))
 def test_market_benchmark_scope_and_rendering(self):
  for s in self.m['slides']:
   scoped=[r for r in self.data if (r['country'],r['division'],r['product_group'])==(s['country'],s['division'],s['group'])]
   for point,row in zip(s['series'],scoped):
    self.assertAlmostEqual(point['market_asp'],row['market_revenue_eur']/row['market_units'])
    self.assertGreater(row['market_revenue_eur'],row['revenue_eur'])
   svg=(R/'reports'/f'{s["id"]}.svg').read_text()
   self.assertIn('Market average',svg)
   for point in s['series']:
    self.assertIn(f">{point['market_asp']:.1f}</text>",svg)
 def test_scope_complete(self):
  self.assertEqual(len(self.m['slides']),12);self.assertEqual(len(self.m['packages']),8)
  self.assertEqual(sum(len(p['slide_ids']) for p in self.m['packages']),24)
  for p in self.m['packages']:
   expected=6 if p['country']=='All' else 2;self.assertEqual(len(p['slide_ids']),expected)
 def test_only_fictional_routes(self):
  for p in self.m['packages']:
   self.assertTrue(all(a.endswith('@example.invalid') for a in p['recipients']))
 def test_generated_charts_match_source(self):
  for s in self.m['slides']:
   data=[r for r in self.data if (r['country'],r['division'],r['product_group'])==(s['country'],s['division'],s['group'])]
   self.assertEqual(s['series'],series(data));self.assertTrue((R/'reports'/f'{s["id"]}.svg').is_file())
if __name__=='__main__':unittest.main()
