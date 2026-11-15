"""Checks data/listening.json: every test has 4 sections with questions 1-10, 11-20, 21-30, 31-40 exactly once, every question
has a key, gaps match, choices are valid, transcripts are present, the audio file exists.
Usage: python -X utf8 -I _generator/check_listening.py data/listening.json [test number]"""
import json, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d = json.load(open(sys.argv[1], encoding='utf-8'))
only = int(sys.argv[2]) if len(sys.argv) > 2 else None
bad = []


def walk_gaps(blocks, out):
    for b in blocks:
        if b['type'] == 'table':
            for row in b['rows']:
                for cell in row:
                    walk_gaps(cell, out)
        else:
            for r in b.get('runs', []):
                if 'gap' in r and r.get('part') != 2:
                    out.append(r['gap'])


for t in d['tests']:
    if only and t['test'] != only:
        continue
    where = 'Test %d' % t['test']
    if not os.path.exists(os.path.join(ROOT, t['audio'])):
        bad.append('%s: audio file %s missing' % (where, t['audio']))
    if [s['n'] for s in t['sections']] != [1, 2, 3, 4]:
        bad.append('%s: sections are %s, not 1-4' % (where, [s['n'] for s in t['sections']]))
    allnums = []
    for s in t['sections']:
        w = '%s Section %d' % (where, s['n'])
        nums = []
        chars = sum(len(''.join(r.get('t', '') for r in b['runs'])) for b in s['transcript'])
        if chars < 2500:
            bad.append('%s: transcript looks too short (%d characters)' % (w, chars))
        for g in s['groups']:
            nums += g['numbers']
            if g['type'] == 'multi':
                k = g['key']
                if len(k['accept']) != g['choose']:
                    bad.append('%s %s: multi choose mismatch' % (w, g['title']))
                letters = [o['key'] for o in g['options']]
                for a in k['accept']:
                    if a not in letters:
                        bad.append('%s %s: answer %s not an option' % (w, g['title'], a))
                continue
            if g['type'] in ('gap', 'bank'):
                gaps = []
                walk_gaps(g['content'], gaps)
                if sorted(gaps) != sorted(g['numbers']):
                    bad.append('%s %s: gaps in the text %s != numbers %s' % (w, g['title'], sorted(gaps), g['numbers']))
            for n in g['numbers']:
                k = s['key'].get(str(n))
                if not k or not k['answer'] or not str(k['answer']).strip():
                    bad.append('%s Q%d: no answer' % (w, n))
                    continue
                if g['type'] in ('tfng', 'ynng') and k['answer'] not in g['choices']:
                    bad.append('%s Q%d: answer %r not in %s' % (w, n, k['answer'], g['choices']))
                if g['type'] in ('match', 'grid', 'headings', 'bank'):
                    letters = [o['key'] for o in g['options']['list']] if g.get('options') else g['letters']
                    if k['answer'] not in letters:
                        bad.append('%s Q%d: answer %r not among %s' % (w, n, k['answer'], letters))
                if g['type'] == 'mcq':
                    q = [x for x in g['questions'] if x['n'] == n][0]
                    if k['answer'] not in [o['key'] for o in q['options']]:
                        bad.append('%s Q%d: answer %r not an option' % (w, n, k['answer']))
            if g['type'] in ('tfng', 'ynng', 'short', 'mcq', 'match', 'grid', 'headings'):
                have = [q['n'] for q in g['questions']]
                if have != g['numbers']:
                    bad.append('%s %s: items %s != range' % (w, g['title'], have))
        want = list(range(10 * (s['n'] - 1) + 1, 10 * s['n'] + 1))
        if sorted(nums) != want:
            bad.append('%s: questions %s are not exactly %d-%d' % (w, sorted(nums), want[0], want[-1]))
        allnums += nums
    if sorted(allnums) != list(range(1, 41)):
        bad.append('%s: questions are not exactly 1-40' % where)
for line in bad:
    print('PROBLEM:', line)
print('OK' if not bad else '%d problems' % len(bad))
sys.exit(1 if bad else 0)
