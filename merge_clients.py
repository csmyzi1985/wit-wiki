import os, re
from collections import Counter

cases_dir = "/Users/csmyz/Documents/maizicheng/wit-wiki/cases"
files = sorted([f for f in os.listdir(cases_dir) if f.endswith('.md')])

def parse_fm(content):
    fm = {}
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not m: return fm
    for line in m.group(1).split('\n'):
        line = line.strip()
        if not line: continue
        match = re.match(r'^(\w+)\s*:\s*(.*)', line)
        if match:
            key = match.group(1)
            val = match.group(2).strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            fm[key] = val
    return fm

major_client = Counter()
for f in files:
    with open(os.path.join(cases_dir, f), 'r', encoding='utf-8') as fh:
        fm = parse_fm(fh.read())
    c = fm.get('client', 'MISSING')
    if '万科' in str(c):
        major_client['万科系（含各城市公司）'] += 1
    elif '保利' in str(c):
        major_client['保利'] += 1
    elif '华润' in str(c):
        major_client['华润'] += 1
    elif '美的' in str(c):
        major_client['美的地产'] += 1
    elif '龙湖' in str(c):
        major_client['龙湖'] += 1
    elif '碧桂园' in str(c):
        major_client['碧桂园'] += 1
    elif '招商' in str(c):
        major_client['招商蛇口'] += 1
    elif '越秀' in str(c):
        major_client['越秀'] += 1
    elif '绿城' in str(c):
        major_client['绿城'] += 1
    elif '嘀嗒' in str(c):
        major_client['嘀嗒拼车'] += 1
    elif '壳牌' in str(c) or '延长' in str(c):
        major_client['延长壳牌'] += 1
    elif '高新' in str(c):
        major_client['咸阳高新区'] += 1
    else:
        major_client['其他'] += 1

print('=== 合并后的主要客户分布 ===')
for c, cnt in major_client.most_common():
    pct = cnt/150*100
    print(f'  {c}: {cnt} ({pct:.1f}%)')
