"""Cut a picture out of a book page: python -X utf8 -I _generator/crop.py <rq|lq|la|ra> PAGE x0 y0 x1 y1 NAME
x0..y1 are fractions (0-1) of the page. Writes img/<NAME>.png (max width 1000 px). Use NAME like t3-p2-diagram.
Use [[img:NAME]] in an authoring file to show it."""
import sys, os
from PIL import Image

BASE = 'D:/HarperSites/_scratch/forecast-cb/'
tag, page, x0, y0, x1, y1, name = sys.argv[1], int(sys.argv[2]), *map(float, sys.argv[3:7]), sys.argv[7]
im = Image.open('%s%s/p%03d.png' % (BASE, tag, page)).convert('RGB')
w, h = im.size
crop = im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
if crop.width > 1000:
    crop = crop.resize((1000, round(crop.height * 1000 / crop.width)), Image.LANCZOS)
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'img')
os.makedirs(out, exist_ok=True)
crop.save(os.path.join(out, name + '.png'), optimize=True)
print(os.path.join(out, name + '.png'), crop.size)
