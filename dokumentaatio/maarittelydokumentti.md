# Vaatimusmäärittely
---------------------
## Sovelluksen tarkoitus
 * Helpottaa kaukokartoitusaineiston käsittelijän työtä. Sovelluksen tarkoituksena on olla nopea ja helppo tapa saada delineoitua yksittäisten puiden latvukset kaukokartoitusaineistosta.
 * Ohjelma tulee laajalti hyödyntämään pycrown -kirjastoa.
## Käyttöliittymäluonnos
![Käyttöliittymäluonnos] (https://imgur.com/a/4NA01e6)
Sovelluksessa mahdollisesti myö lokisivu prosessista
## Perusversio
 * Luoda shapefile -muotoinen latvusaineisto pistepilviaineistosta (.las/.laz), jossa yksittäisen puun latvus rajautuu polygoniin.
 ** tällaista aineistoa voi edelleen jalostaa ja hyödyntää tarpeiden mukaan.
 * Riippuen valmiiden koodikirjastojen saatavuudesta tuottaa mahdollisesti myös latvuskorkeusaineiston (CHM) ja maastokorkeusaineiston (DEM).
 * "Plottaa" valmis latvusaineisto käyttöliittymässä, jotta käyttäjä voi nopeasti tulkita tuloksia ja päättää, haluaako hän mahdollisesti ajaa prosessin uudestaan eri parametrein.
## Jatkokehitysideoita