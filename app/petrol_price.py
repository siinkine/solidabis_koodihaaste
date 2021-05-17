from urllib.request import Request, urlopen

def get_scraped_avg_prices():
    '''This function gets the average prices of petrol from polttoaine.net webpage. It returns a dictionary for petrols and diesel '''

    url = "https://www.polttoaine.net/index.php?t=PK-Seutu"
    req = Request(url, headers={'User-Agent': 'Chrome'})
    page = urlopen(req)

    html_bytes = page.read()
    html = html_bytes.decode('latin-1')

    res = html[15000:2*10000]  #crop to the main results (quick and dirty)
    ind = res.find("Keskihinnat")
    res2 = res[ind:ind+200]

    inds = [i for i in range(len(res2)) if res2.startswith('Hinnat', i)] #find prices

    names = ['v95E10', 'v98E', 'Di']
    hinta = []
    for c, ind in enumerate(inds):
        hinta.append(float(res2[ind+8:ind+13]))
    
    res = {names[i]: hinta[i] for i in range(len(names))}

    return res


if __name__ == '__main__':
    res = get_scraped_avg_prices()
    print(res)