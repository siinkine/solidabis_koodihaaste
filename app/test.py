from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MyHTMLParser()



from urllib.request import Request, urlopen

url = "https://www.polttoaine.net/index.php?t=PK-Seutu"

req = Request(url, headers={'User-Agent': 'Chrome'})
page = urlopen(req)
html_bytes = page.read()
html = html_bytes.decode('latin-1')


parser.feed(html[10000:2*10000])



res = html[15000:2*10000]
ind = res.find("Keskihinnat")
res2 = res[ind:ind+200]


inds = [i for i in range(len(res2)) if res2.startswith('Hinnat', i)]

float(res2[inds[0]+8:inds[0]+13])

names = ['95E10', '98E', 'Di']
hinta = []
for c, ind in enumerate(inds):
    hinta.append(float(res2[ind+8:ind+13]))
    
res = {names[i]: hinta[i] for i in range(len(names))}


import pdb; pdb.set_trace()

