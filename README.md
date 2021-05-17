## Solidabis koodihaaste
Tässä reposta löytyvät koodit solidabiksen [koodihaasteeseen.](https://koodihaaste.solidabis.com/#/) 

### Teknologiakuvaus:
Web-sovellus on koodattu pythonilla käyttäen Flask mikroverkkokehys, joka mahdollistaa python web-sovellusten koodauksen. 
Tekninen ratkaisu autonkulutuksen arviontiin on koodattu pythonilla ilman erityisiä kirjastoja.
Web-käyttöliittymä on ns. lomakepohjainen ratkaisu, joka hyödyntään bootstrappiä. Lomakkeella käyttäjä valitsee haluamansa automallin, matkan ja kaksi tarkasteltavaa nopeutta.
Lomakkeen submittoinnin jälkeen avautuu toinen html sivusto, joka näyttää vertailutulokset.

Lisäksi halusin mielenkiinnosta lisätä myös hieman graafisia elementtejä tulosten esitykseen ja sekä arvion kustannuksista, joten lisäsin lomakkeen loppuun pylväsdiagrammin, joka kertoo kustannuksen käytetyille polttoainemäärille eri polttoainetyypeillä. Tiedot polttoaineiden hinnoista haetaan  "https://www.polttoaine.net/index.php?t=PK-Seutu" sivustolta. Grafiikka on esitetty käyttäen plotly javascript kirjastoa. 

Ohjelmisto on koodattu Visual code ohjelmointiympäristösssä Windows käyttöjärjestelmässä, mutta webserveri käyttää Gunicorn Python WSGI HTTP  UNIX serveriä.

### Ratkaisun kuvaus:
- ```car_data.py ``` sisältää python dictionaryn, jossa autojen kulutustiedot ja nimet sijaitsevat. 
- ```util.py ``` sisältää kulutuksen laskemiseen vaadittavan ratkaisun funktiona sekä vertailufunktio kahden eri nopeuden välille.  
- ```petrol_price.py ``` sisältää funktion, joka hakee "https://www.polttoaine.net/index.php?t=PK-Seutu" sivustolta polttoaineiden keskihinnat. 
- ```app/main.py``` sisältää flask app:in main funktion ja ```app/templates``` sisältää html-koodit.

### Ohjeet ohjelmiston pystysttämiseen ja käynnistämiseen:
Ohjelmisto on koodattu conda ympäristössä ja vaadittavat ohjelmistopaketit löytyvät: ```requirements.txt ``` tiedostosta. Käytin ratkaisussa python 3.7 versiota mutta   Herokuapp käyttää uusinta python versiota.   ```wspi.py``` käynnistää web-serverin flask-app:lle.  
  
  
Sovellus löytyy myös heroku palvelusta:
https://autoilumittari.herokuapp.com/
