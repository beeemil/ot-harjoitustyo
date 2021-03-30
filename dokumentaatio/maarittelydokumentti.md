# Vaatimusmäärittely
---------------------
## Sovelluksen tarkoitus
 * Helpottaa kaukokartoitusaineiston käsittelijän työtä. Sovelluksen tarkoituksena on olla nopea ja helppo tapa saada delineoitua yksittäisten puiden latvukset kaukokartoitusaineistosta.
 * Ohjelma tulee laajalti hyödyntämään pycrown -kirjastoa.
## Käyttöliittymäluonnos
<img src="https://i.imgur.com/Jw6kMRc.png">
Sovelluksessa mahdollisesti myös lokisivu prosessista
## Perusversio
 * Luoda shapefile -muotoinen latvusaineisto pistepilviaineistosta (.las/.laz), jossa yksittäisen puun latvus rajautuu polygoniin.
 ** tällaista aineistoa voi edelleen jalostaa ja hyödyntää tarpeiden mukaan.
 * Riippuen valmiiden koodikirjastojen saatavuudesta tuottaa mahdollisesti myös latvuskorkeusaineiston (CHM) ja maastokorkeusaineiston (DEM).
 * "Plottaa" valmis latvusaineisto käyttöliittymässä, jotta käyttäjä voi nopeasti tulkita tuloksia ja päättää, haluaako hän mahdollisesti ajaa prosessin uudestaan eri parametrein.
## Jatkokehitysideoita
