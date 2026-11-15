"""Print the Windows-OCR draft of book pages with watermark/footer lines removed.
Usage: python -X utf8 -I _generator/ocr_draft.py <rq|lq|la|ra> FIRST_PAGE LAST_PAGE
The OCR is only a DRAFT: it has wrong letters, drops words, scrambles columns and tables. Always compare with the page
picture (D:/HarperSites/_scratch/forecast-cb/<tag>/pNNN.png) before using any text.
"""
import re, sys, os

BASE = 'D:/HarperSites/_scratch/forecast-cb/'
FIX = [
    (r'%ough', 'Though'), (r'%is\b', 'This'), (r'%e\b', 'The'), (r'%ere\b', 'There'), (r'%ey\b', 'They'),
    (r'%ese\b', 'These'), (r'%en\b', 'Then'), (r'%at\b', 'That'), (r'%us\b', 'Thus'), (r'%rough', 'Through'),
]
# watermark, running footer (publisher name/phone), British Council / IELTS logos, bare page numbers
DROP = re.compile(r'(naugh\s*milk|contact\s*zalo|078\.?\s*426|british\s*council|^\s*ielts\s*$|^\s*\d{1,3}\s*$)', re.I)


def main():
    tag, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    for p in range(a, b + 1):
        f = '%socr-%s/p%03d.txt' % (BASE, tag, p)
        lines = open(f, encoding='utf-8').read().split('\n')
        text = '\n'.join(l for l in lines if not DROP.search(l))
        for pat, rep in FIX:
            text = re.sub(pat, rep, text)
        print('=== page %d (%s/p%03d.png) ===' % (p, tag, p))
        print(text)


if __name__ == '__main__':
    main()
