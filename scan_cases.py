#!/usr/bin/env python3
import os, re, sys
from collections import Counter

cases_dir = "/Users/csmyz/Documents/maizicheng/wit-wiki/cases"
files = sorted([f for f in os.listdir(cases_dir) if f.endswith('.md')])

# Simple YAML frontmatter parser (avoid external deps)
def parse_frontmatter(content):
    fm = {}
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not m:
        return fm
    text = m.group(1)
    for line in text.split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        # Handle key: value
        match = re.match(r'^(\w+)\s*:\s*(.*)', line)
        if match:
            key = match.group(1)
            val = match.group(2).strip()
            # Strip quotes
            if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                val = val[1:-1]
            # Handle YAML list [a, b, c]
            if val.startswith('[') and val.endswith(']'):
                inner = val[1:-1]
                val = [v.strip().strip('"').strip("'") for v in inner.split(',')]
                val = [v for v in val if v]
            fm[key] = val
    return fm

strategy_keywords = [
    '定位', '差异化', '品牌资产', '传播', '引爆', '破圈', '心智', '占位',
    '故事', '内容营销', '社交媒体', 'KOL', '私域', 'IP', '跨界',
    '事件营销', '话题', '视觉锤', '符号', '仪式感', '情感共鸣',
    '价值主张', '用户洞察', '场景', '文化母体', '超级符号',
    '流量', '转化', '闭环', '裂变', '社群', '人设', '标签',
    '策略', '洞察', '创意', '执行', '效果', '复盘', '方法论',
    '品牌年轻化', '品牌升级', '品牌重塑', 'IP打造', '内容策略',
    '传播策略', '营销策略', '数字营销', '全案', '整合营销',
    '客户画像', '目标人群', '传播渠道', '媒体策略', '投放',
    '文案', '视觉', '短视频', '直播', '种草', '品效合一',
    '用户增长', '增长黑客', '心智占领', '价值感', '品牌力',
]
kw_re = re.compile('|'.join(re.escape(k) for k in strategy_keywords))

records = []
missing_count = Counter()
year_dist = Counter()
client_dist = Counter()
industry_dist = Counter()
methodology_dist = Counter()
all_body_kw = Counter()
dl_has = 0
dl_missing = 0

for fname in files:
    fpath = os.path.join(cases_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    fm = parse_frontmatter(content)
    
    def getf(key):
        v = fm.get(key, 'MISSING')
        if not v:
            v = 'MISSING'
        return v

    for field in ['date','client','industry','methodology','title','keywords','decision_logic']:
        if field not in fm or not fm[field]:
            missing_count[field] += 1

    date_v = getf('date')
    client_v = getf('client')
    industry_v = getf('industry')
    meth_v = getf('methodology')
    title_v = getf('title')
    kw_fm_v = getf('keywords')
    dl_v = getf('decision_logic')

    # Year
    if date_v != 'MISSING':
        year = str(date_v)[:4]
    else:
        year = 'MISSING'
    year_dist[year] += 1

    # Client
    client_str = str(client_v)
    client_dist[client_str] += 1

    # Industry
    industry_str = str(industry_v)
    industry_dist[industry_str] += 1

    # Methodology
    if isinstance(meth_v, list):
        meth_str = ', '.join(meth_v)
        for m in meth_v:
            methodology_dist[m] += 1
    else:
        meth_str = str(meth_v)
        methodology_dist[meth_str] += 1

    # Decision logic
    if dl_v != 'MISSING':
        dl_has += 1
        dl_flag = 'YES'
    else:
        dl_missing += 1
        dl_flag = 'NO'

    # Body keywords
    fm_end = re.match(r'^---\s*\n.*?\n---\s*\n', content, re.DOTALL)
    body = content[fm_end.end():] if fm_end else content
    found = kw_re.findall(body)
    body_kw = Counter(found)
    all_body_kw.update(body_kw)

    records.append({
        'file': fname,
        'year': year,
        'client': client_str,
        'industry': industry_str,
        'methodology': meth_str,
        'title': title_v if title_v != 'MISSING' else 'MISSING',
        'dl': dl_flag,
        'body_kw': body_kw,
    })

# ====== PRINT RESULTS ======
out = []

out.append("=" * 80)
out.append("WIT-WIKI CASES ANALYSIS SUMMARY")
out.append("=" * 80)
out.append(f"\nTotal .md files: {len(files)}")

out.append("\n--- A. Year Distribution ---")
for y in sorted(year_dist.keys()):
    bar = '█' * year_dist[y]
    out.append(f"  {y}: {year_dist[y]:>3} {bar}")

out.append("\n--- B. Client Distribution ---")
for c, cnt in client_dist.most_common(40):
    out.append(f"  {c}: {cnt}")

out.append("\n--- C. Industry Distribution ---")
for ind, cnt in industry_dist.most_common():
    out.append(f"  {ind}: {cnt}")

out.append("\n--- D. Methodology Keywords Frequency ---")
for m, cnt in methodology_dist.most_common(40):
    out.append(f"  {m}: {cnt}")

out.append("\n--- E. Missing Fields ---")
for f, cnt in missing_count.most_common():
    out.append(f"  {f}: {cnt} files missing")

out.append(f"\n--- F. Decision Logic ---")
out.append(f"  Complete: {dl_has}")
out.append(f"  Missing:  {dl_missing}")

out.append("\n--- G. Top Strategy Keywords in Body Text ---")
for kw, cnt in all_body_kw.most_common(30):
    out.append(f"  {kw}: {cnt}")

out.append("\n" + "=" * 80)
out.append("PER-FILE TABLE")
out.append("=" * 80)
out.append(f"{'#':>3}  {'Year':<5} {'Client':<16} {'Industry':<16} {'Methodology':<30} {'DL':<3} {'File'}")
out.append("-" * 140)
for i, r in enumerate(records, 1):
    meth_short = r['methodology'][:28]
    fname_short = r['file'][:55]
    client_short = r['client'][:14]
    ind_short = r['industry'][:14]
    out.append(f"{i:>3}  {r['year']:<5} {client_short:<16} {ind_short:<16} {meth_short:<30} {r['dl']:<3} {fname_short}")

result = '\n'.join(out)
print(result)

# Also write to file
with open('/Users/csmyz/Documents/maizicheng/wit-wiki/cases_analysis_output.txt', 'w', encoding='utf-8') as f:
    f.write(result)
