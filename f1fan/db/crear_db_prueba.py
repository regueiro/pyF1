#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Crear una BBDD con datos de temporadas para usar en las pruebas.
"""

import sys
import datetime
from model import Facade


if sys.argv[1]:
    Facade.establecer_directorio_bd(sys.argv[1])
else:
    Facade.establecer_directorio_bd(".")

#
# Temporada 2010
#
inicio =  datetime.date(2010, 3, 12)
fin = datetime.date(2010, 11, 14)
temporada = Facade.nueva_temporada("Temporada 2010", "t_2010")
temporada.establecer_datos({'inicio': inicio, 'fin': fin, 'n_pilotos_parrilla': 24, 'n_pilotos_gp': 24, 'tabla_puntos': [25,18,15,12,10,8,6,4,1]})

nombre = "2010 FORMULA 1 GULF AIR BAHRAIN GRAND PRIX"
lugar = "Sakhir"
inicio = datetime.date(2010, 3, 12)
fin = datetime.date(2010, 3, 14)
n_vueltas = 49
gp01 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vueltas)

nombre = "2010 FORMULA 1 QANTAS AUSTRALIAN GRAND PRIX"
lugar = "Melbourne"
inicio = datetime.date(2010, 3, 26)
fin = datetime.date(2010, 3, 28)
n_vuletas = 58
gp02 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vuletas)

nombre = "2010 FORMULA 1 PETRONAS MALAYSIAN GRAND PRIX"
lugar = "Kuala Lumpur"
inicio = datetime.date(2010, 4, 2)
fin = datetime.date(2010, 4, 4)
n_vuletas = 56
gp03 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vuletas)

nombre = "2010 FORMULA 1 CHINESE GRAND PRIX"
lugar = "Shanghai"
inicio = datetime.date(2010, 4, 16)
fin = datetime.date(2010, 4, 18)
n_vuletas = 56
gp04 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vuletas)

nombre = "FORMULA 1 GRAN PREMIO DE ESPANA TELEFÓNICA 2010"
lugar = "Catalunya"
inicio = datetime.date(2010, 5, 7)
fin = datetime.date(2010, 5, 9)
n_vuletas = 66
gp05 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vuletas)

nombre = "FORMULA 1 GRAND PRIX DE MONACO 2010"
lugar = "Monte Carlo"
inicio = datetime.date(2010, 5, 13)
fin = datetime.date(2010, 5, 16)
n_vuletas = 78
gp06 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vuletas)

nombre = "2010 FORMULA 1 TURKISH GRAND PRIX"
lugar = "Istanbul"
inicio = datetime.date(2010, 5, 28)
fin = datetime.date(2010, 5, 30)
n_vuletas = 58
gp07 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vuletas)

nombre = "FORMULA 1 GRAND PRIX DU CANADA 2010"
lugar = "Montreal"
inicio = datetime.date(2010, 6, 11)
fin = datetime.date(2010, 6, 13)
n_vuletas = 70
gp08 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vuletas)

nombre = "2010 FORMULA 1 TELEFÓNICA GRAND PRIX OF EUROPE"
lugar = "Valencia"
inicio = datetime.date(2010, 6, 25)
fin = datetime.date(2010, 6, 27)
n_vuletas = 57
gp09 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vuletas)

nombre = "2010 FORMULA 1 SANTANDER BRITISH GRAND PRIX"
lugar = "Silverstone"
inicio = datetime.date(2010, 7, 9)
fin = datetime.date(2010, 7, 11)
n_vuletas = 60
gp10 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vuletas)

nombre = "FORMULA 1 GROSSER PREIS SANTANDER VON DEUTSCHLAND 2010"
lugar = "Hockenheim"
inicio = datetime.date(2010, 7, 23)
fin = datetime.date(2010, 7, 25)
n_vuletas = 67
gp11 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vuletas)

nombre = "FORMULA 1 MAGYAR NAGYDIJ 2010"
lugar = "Budapest"
inicio = datetime.date(2010, 7, 30)
fin = datetime.date(2010, 8, 1)
n_vuletas = 70
gp12 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vuletas)

nombre = "2010 FORMULA 1 BELGIAN GRAND PRIX"
lugar = "Spa-Francorchamps"
inicio = datetime.date(2010, 8, 27)
fin = datetime.date(2010, 8, 29)
n_vuletas = 44
gp13 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vuletas)

nombre = "FORMULA 1 GRAN PREMIO SANTANDER D'ITALIA 2010"
lugar = "Monza"
inicio = datetime.date(2010, 9, 10)
fin = datetime.date(2010, 9, 12)
n_vuletas = 53
gp14 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vuletas)

nombre = "2010 FORMULA 1 SINGTEL SINGAPORE GRAND PRIX"
lugar = "Singapore"
inicio = datetime.date(2010, 9, 24)
fin = datetime.date(2010, 9, 26)
n_vuletas = 61
gp15 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vuletas)

nombre = "2010 FORMULA 1 JAPANESE GRAND PRIX"
lugar = "Suzuka"
inicio = datetime.date(2010, 10, 8)
fin = datetime.date(2010, 10, 10)
n_vuletas = 53
gp16 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vuletas)

nombre = "2010 FORMULA 1 KOREAN GRAND PRIX"
lugar = "Yeongam"
inicio = datetime.date(2010, 10, 22)
fin = datetime.date(2010, 10, 24)
n_vuletas = 55
gp17 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vuletas)

nombre = "FORMULA 1 GRANDE PREMIO DO BRASIL 2010"
lugar = "Sao Paulo"
inicio = datetime.date(2010, 11, 5)
fin = datetime.date(2010, 11, 7)
n_vuletas = 71
gp18 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vuletas)

nombre = "2010 FORMULA 1 ETIHAD AIRWAYS ABU DHABI GRAND PRIX"
lugar = "Yas Marina Circuit"
inicio = datetime.date(2010, 11, 12)
fin = datetime.date(2010, 11, 14)
n_vuletas = 55
gp19 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vuletas)

for gp in [gp01, gp02, gp03, gp04, gp05, gp06, gp07, gp08, gp09, gp10, gp11, gp12, gp13, gp14, gp15, gp16, gp17, gp18, gp19]:
    temporada.anadir_GP(gp)


vettel = Facade.nuevo_piloto("Sebastian Vettel")
massa = Facade.nuevo_piloto("Felipe Massa")
alonso = Facade.nuevo_piloto("Fernando Alonso")
hamilton = Facade.nuevo_piloto("Lewis Hamilton")
rosberg = Facade.nuevo_piloto("Nico Rosberg")
webber = Facade.nuevo_piloto("Mark Webber")
schumacher = Facade.nuevo_piloto("Michael Schumacher")
button = Facade.nuevo_piloto("Jenson Button")
kubica = Facade.nuevo_piloto("Robert Kubica")
sutil = Facade.nuevo_piloto("Adrian Sutil")
barrichello = Facade.nuevo_piloto("Rubens Barrichello")
liuzzi = Facade.nuevo_piloto("Vitantonio Liuzzi")
hulkenberg = Facade.nuevo_piloto("Nico Hulkenberg")
delarosa = Facade.nuevo_piloto("Pedro De la Rosa")
buemi = Facade.nuevo_piloto("Sebastien Buemi")
kobayashi = Facade.nuevo_piloto("Kamui Kobayashi")
petrov = Facade.nuevo_piloto("Vitaly Petrov")
alguersuari = Facade.nuevo_piloto("Jaime Alguersuari")
glock = Facade.nuevo_piloto("Timo Glock")
trulli = Facade.nuevo_piloto("Jarno Trulli")
kovalainen = Facade.nuevo_piloto("Heikki Kovalainen")
digrassi = Facade.nuevo_piloto("Lucas di Grassi")
senna = Facade.nuevo_piloto("Bruno Senna")
chandhok = Facade.nuevo_piloto("Karun Chandhok")

for piloto in [ vettel, massa, alonso, hamilton, rosberg, webber, schumacher, button, kubica, sutil, barrichello, liuzzi, hulkenberg, delarosa, buemi, kobayashi, petrov, alguersuari, glock, trulli, kovalainen, digrassi, senna, chandhok ]:
    temporada.anadir_piloto(piloto)

redbull= Facade.nuevo_equipo("Red Bull")
ferrari = Facade.nuevo_equipo("Ferrari")
mclaren = Facade.nuevo_equipo("McLaren")
renault = Facade.nuevo_equipo("Renault")
mercedes = Facade.nuevo_equipo("Mercedes GP")
forceindia = Facade.nuevo_equipo("Force India")
williams = Facade.nuevo_equipo("Williams")
sauber = Facade.nuevo_equipo("Sauber")
tororosso = Facade.nuevo_equipo("Toro Rosso")
virgin = Facade.nuevo_equipo("Virgin Racing")
lotus = Facade.nuevo_equipo("Lotus F1 Racing")
hispania = Facade.nuevo_equipo("Hispania Racing F1 Team")

for equipo in [ redbull, ferrari, mclaren, renault, mercedes, forceindia, williams, sauber, tororosso, virgin, lotus, hispania]:
    temporada.anadir_equipo(equipo)


fecha = datetime.date(2010,1,1)
vettel.fichar_por_equipo(redbull, fecha)
massa.fichar_por_equipo(ferrari, fecha)
alonso.fichar_por_equipo(ferrari, fecha)
hamilton.fichar_por_equipo(mclaren, fecha)
rosberg.fichar_por_equipo(mercedes, fecha)
webber.fichar_por_equipo(redbull, fecha)
schumacher.fichar_por_equipo(mercedes, fecha)
button.fichar_por_equipo(mclaren, fecha)
kubica.fichar_por_equipo(renault, fecha)
sutil.fichar_por_equipo(forceindia, fecha)
barrichello.fichar_por_equipo(williams, fecha)
liuzzi.fichar_por_equipo(forceindia, fecha)
hulkenberg.fichar_por_equipo(williams, fecha)
delarosa.fichar_por_equipo(sauber, fecha)
buemi.fichar_por_equipo(tororosso, fecha)
kobayashi.fichar_por_equipo(sauber, fecha)
petrov.fichar_por_equipo(renault, fecha)
alguersuari.fichar_por_equipo(tororosso, fecha)
glock.fichar_por_equipo(virgin, fecha)
trulli.fichar_por_equipo(lotus, fecha)
kovalainen.fichar_por_equipo(lotus, fecha)
digrassi.fichar_por_equipo(virgin, fecha)
senna.fichar_por_equipo(hispania, fecha)
chandhok.fichar_por_equipo(hispania, fecha)


gp01.establecer_parrilla([ vettel, massa, alonso, hamilton, rosberg, webber, schumacher, button, kubica, sutil, barrichello, liuzzi, hulkenberg, delarosa, buemi, kobayashi, petrov, alguersuari, glock, trulli, kovalainen, digrassi, senna, chandhok ])
gp01.establecer_resultado([alonso, massa, hamilton, vettel, rosberg, schumacher, button, webber, liuzzi, barrichello, kubica, sutil, alguersuari, hulkenberg, kovalainen, buemi, trulli, delarosa, senna, glock, petrov, kobayashi, digrassi, chandhok], 49) 

gp02.establecer_parrilla([ kubica, massa, sutil, hamilton, rosberg, webber, schumacher, button, alonso, vettel, barrichello, liuzzi, hulkenberg, delarosa, buemi, kobayashi, petrov, alguersuari, glock, trulli, kovalainen, digrassi, senna, chandhok ])
gp02.establecer_resultado([alonso, massa, hamilton, vettel, rosberg, schumacher, button, webber, liuzzi, barrichello, kubica, sutil, alguersuari, hulkenberg, kovalainen, buemi, trulli, delarosa, senna, glock, petrov, kobayashi, digrassi, chandhok], 49)

gp03.establecer_parrilla([ rosberg, vettel, massa, hamilton, alonso, webber, schumacher, button, kubica, sutil, barrichello, liuzzi, hulkenberg, delarosa, buemi, kobayashi, petrov, alguersuari, glock, trulli, kovalainen, digrassi, senna, chandhok ])


trulli.fichar_por_equipo(virgin, datetime.date(2010, 3, 19))
digrassi.fichar_por_equipo(lotus, datetime.date(2010, 3, 19))


Facade.almacenar_temporada(temporada)


#
# Temporada 2009
#
inicio =  datetime.date(2009, 3, 12)
fin = datetime.date(2009, 11, 14)
temporada = Facade.nueva_temporada("Temporada 2009", "t_2009")
temporada.establecer_datos({'inicio': inicio, 'fin': fin, 'n_pilotos_parrilla': 24, 'n_pilotos_gp': 24, 'tabla_puntos': [25,18,15,12,10,8,6,4,1]})

nombre = "gp completo"
lugar = "Sakhir"
inicio = datetime.date(2009, 3, 12)
fin = datetime.date(2009, 3, 14)
n_vueltas = 49
gp01 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vueltas)

nombre = "gp solo parrilla"
lugar = "Melbourne"
inicio = datetime.date(2009, 3, 26)
fin = datetime.date(2009, 3, 28)
n_vuletas = 58
gp02 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vuletas)

for gp in [gp01, gp02]:
    temporada.anadir_GP(gp)


vettel = Facade.nuevo_piloto("Sebastian Vettel")
massa = Facade.nuevo_piloto("Felipe Massa")
alonso = Facade.nuevo_piloto("Fernando Alonso")
hamilton = Facade.nuevo_piloto("Lewis Hamilton")
rosberg = Facade.nuevo_piloto("Nico Rosberg")
webber = Facade.nuevo_piloto("Mark Webber")
schumacher = Facade.nuevo_piloto("Michael Schumacher")
button = Facade.nuevo_piloto("Jenson Button")
kubica = Facade.nuevo_piloto("Robert Kubica")
sutil = Facade.nuevo_piloto("Adrian Sutil")
barrichello = Facade.nuevo_piloto("Rubens Barrichello")
liuzzi = Facade.nuevo_piloto("Vitantonio Liuzzi")
hulkenberg = Facade.nuevo_piloto("Nico Hulkenberg")
delarosa = Facade.nuevo_piloto("Pedro De la Rosa")
buemi = Facade.nuevo_piloto("Sebastien Buemi")
kobayashi = Facade.nuevo_piloto("Kamui Kobayashi")
petrov = Facade.nuevo_piloto("Vitaly Petrov")
alguersuari = Facade.nuevo_piloto("Jaime Alguersuari")
glock = Facade.nuevo_piloto("Timo Glock")
trulli = Facade.nuevo_piloto("Jarno Trulli")
kovalainen = Facade.nuevo_piloto("Heikki Kovalainen")
digrassi = Facade.nuevo_piloto("Lucas di Grassi")
senna = Facade.nuevo_piloto("Bruno Senna")
chandhok = Facade.nuevo_piloto("Karun Chandhok")

for piloto in [ vettel, massa, alonso, hamilton, rosberg, webber, schumacher, button, kubica, sutil, barrichello, liuzzi, hulkenberg, delarosa, buemi, kobayashi, petrov, alguersuari, glock, trulli, kovalainen, digrassi, senna, chandhok ]:
    temporada.anadir_piloto(piloto)

redbull= Facade.nuevo_equipo("Red Bull")
ferrari = Facade.nuevo_equipo("Ferrari")
mclaren = Facade.nuevo_equipo("McLaren")
renault = Facade.nuevo_equipo("Renault")
mercedes = Facade.nuevo_equipo("Mercedes GP")
forceindia = Facade.nuevo_equipo("Force India")
williams = Facade.nuevo_equipo("Williams")
sauber = Facade.nuevo_equipo("Sauber")
tororosso = Facade.nuevo_equipo("Toro Rosso")
virgin = Facade.nuevo_equipo("Virgin Racing")
lotus = Facade.nuevo_equipo("Lotus F1 Racing")
hispania = Facade.nuevo_equipo("Hispania Racing F1 Team")

for equipo in [ redbull, ferrari, mclaren, renault, mercedes, forceindia, williams, sauber, tororosso, virgin, lotus, hispania]:
    temporada.anadir_equipo(equipo)


fecha = datetime.date(2009,1,1)
vettel.fichar_por_equipo(redbull, fecha)
massa.fichar_por_equipo(ferrari, fecha)
alonso.fichar_por_equipo(ferrari, fecha)
hamilton.fichar_por_equipo(mclaren, fecha)
rosberg.fichar_por_equipo(mercedes, fecha)
webber.fichar_por_equipo(redbull, fecha)
schumacher.fichar_por_equipo(mercedes, fecha)
button.fichar_por_equipo(mclaren, fecha)
kubica.fichar_por_equipo(renault, fecha)
sutil.fichar_por_equipo(forceindia, fecha)
barrichello.fichar_por_equipo(williams, fecha)
liuzzi.fichar_por_equipo(forceindia, fecha)
hulkenberg.fichar_por_equipo(williams, fecha)
delarosa.fichar_por_equipo(sauber, fecha)
buemi.fichar_por_equipo(tororosso, fecha)
kobayashi.fichar_por_equipo(sauber, fecha)
petrov.fichar_por_equipo(renault, fecha)
alguersuari.fichar_por_equipo(tororosso, fecha)
glock.fichar_por_equipo(virgin, fecha)
trulli.fichar_por_equipo(lotus, fecha)
kovalainen.fichar_por_equipo(lotus, fecha)
digrassi.fichar_por_equipo(virgin, fecha)
senna.fichar_por_equipo(hispania, fecha)
chandhok.fichar_por_equipo(hispania, fecha)


gp01.establecer_parrilla([ kovalainen, massa, alonso, hamilton, rosberg, webber, schumacher, button, kubica, sutil, barrichello, liuzzi, hulkenberg, delarosa, buemi, kobayashi, petrov, alguersuari, glock, trulli, vettel, digrassi, senna, chandhok ])
gp01.establecer_resultado([alonso, trulli, hamilton, vettel, rosberg, schumacher, button, webber, liuzzi, barrichello, kubica, sutil, alguersuari, hulkenberg, kovalainen, buemi, massa, delarosa, senna, glock, petrov, kobayashi, digrassi, chandhok], 49) 

gp02.establecer_parrilla([ kovalainen, massa, alonso, hamilton, rosberg, webber, schumacher, button, kubica, sutil, barrichello, liuzzi, hulkenberg, delarosa, buemi, kobayashi, petrov, alguersuari, glock, trulli, vettel, digrassi, senna, chandhok ])

trulli.fichar_por_equipo(virgin, datetime.date(2009, 3, 19))
digrassi.fichar_por_equipo(lotus, datetime.date(2009, 3, 19))


Facade.almacenar_temporada(temporada)

#
# Temporada 2008
#
inicio =  datetime.date(2008, 3, 12)
fin = datetime.date(2008, 11, 14)
temporada = Facade.nueva_temporada("Temporada 2008", "t_2008")
temporada.establecer_datos({'inicio': inicio, 'fin': fin, 'n_pilotos_parrilla': 24, 'n_pilotos_gp': 24, 'tabla_puntos': [25,18,15,12,10,8,6,4,1]})

nombre = "gp completo"
lugar = "Sakhir"
inicio = datetime.date(2008, 3, 12)
fin = datetime.date(2008, 3, 14)
n_vueltas = 49
gp01 = Facade.nuevo_GP(nombre, lugar, inicio, fin, n_vueltas)

for gp in [gp01]:
    temporada.anadir_GP(gp)


vettel = Facade.nuevo_piloto("Sebastian Vettel")
massa = Facade.nuevo_piloto("Felipe Massa")
alonso = Facade.nuevo_piloto("Fernando Alonso")
hamilton = Facade.nuevo_piloto("Lewis Hamilton")
rosberg = Facade.nuevo_piloto("Nico Rosberg")
webber = Facade.nuevo_piloto("Mark Webber")
schumacher = Facade.nuevo_piloto("Michael Schumacher")
button = Facade.nuevo_piloto("Jenson Button")
kubica = Facade.nuevo_piloto("Robert Kubica")
sutil = Facade.nuevo_piloto("Adrian Sutil")
barrichello = Facade.nuevo_piloto("Rubens Barrichello")
liuzzi = Facade.nuevo_piloto("Vitantonio Liuzzi")
hulkenberg = Facade.nuevo_piloto("Nico Hulkenberg")
delarosa = Facade.nuevo_piloto("Pedro De la Rosa")
buemi = Facade.nuevo_piloto("Sebastien Buemi")
kobayashi = Facade.nuevo_piloto("Kamui Kobayashi")
petrov = Facade.nuevo_piloto("Vitaly Petrov")
alguersuari = Facade.nuevo_piloto("Jaime Alguersuari")
glock = Facade.nuevo_piloto("Timo Glock")
trulli = Facade.nuevo_piloto("Jarno Trulli")
kovalainen = Facade.nuevo_piloto("Heikki Kovalainen")
digrassi = Facade.nuevo_piloto("Lucas di Grassi")
senna = Facade.nuevo_piloto("Bruno Senna")
chandhok = Facade.nuevo_piloto("Karun Chandhok")

for piloto in [ vettel, massa, alonso, hamilton, rosberg, webber, schumacher, button, kubica, sutil, barrichello, liuzzi, hulkenberg, delarosa, buemi, kobayashi, petrov, alguersuari, glock, trulli, kovalainen, digrassi, senna, chandhok ]:
    temporada.anadir_piloto(piloto)

redbull= Facade.nuevo_equipo("Red Bull")
ferrari = Facade.nuevo_equipo("Ferrari")
mclaren = Facade.nuevo_equipo("McLaren")
renault = Facade.nuevo_equipo("Renault")
mercedes = Facade.nuevo_equipo("Mercedes GP")
forceindia = Facade.nuevo_equipo("Force India")
williams = Facade.nuevo_equipo("Williams")
sauber = Facade.nuevo_equipo("Sauber")
tororosso = Facade.nuevo_equipo("Toro Rosso")
virgin = Facade.nuevo_equipo("Virgin Racing")
lotus = Facade.nuevo_equipo("Lotus F1 Racing")
hispania = Facade.nuevo_equipo("Hispania Racing F1 Team")

for equipo in [ redbull, ferrari, mclaren, renault, mercedes, forceindia, williams, sauber, tororosso, virgin, lotus, hispania]:
    temporada.anadir_equipo(equipo)


fecha = datetime.date(2008,1,1)
vettel.fichar_por_equipo(redbull, fecha)
massa.fichar_por_equipo(ferrari, fecha)
alonso.fichar_por_equipo(ferrari, fecha)
hamilton.fichar_por_equipo(mclaren, fecha)
rosberg.fichar_por_equipo(mercedes, fecha)
webber.fichar_por_equipo(redbull, fecha)
schumacher.fichar_por_equipo(mercedes, fecha)
button.fichar_por_equipo(mclaren, fecha)
kubica.fichar_por_equipo(renault, fecha)
sutil.fichar_por_equipo(forceindia, fecha)
barrichello.fichar_por_equipo(williams, fecha)
liuzzi.fichar_por_equipo(forceindia, fecha)
hulkenberg.fichar_por_equipo(williams, fecha)
delarosa.fichar_por_equipo(sauber, fecha)
buemi.fichar_por_equipo(tororosso, fecha)
kobayashi.fichar_por_equipo(sauber, fecha)
petrov.fichar_por_equipo(renault, fecha)
alguersuari.fichar_por_equipo(tororosso, fecha)
glock.fichar_por_equipo(virgin, fecha)
trulli.fichar_por_equipo(lotus, fecha)
kovalainen.fichar_por_equipo(lotus, fecha)
digrassi.fichar_por_equipo(virgin, fecha)
senna.fichar_por_equipo(hispania, fecha)
chandhok.fichar_por_equipo(hispania, fecha)


gp01.establecer_parrilla([ kovalainen, massa, alonso, hamilton, rosberg, webber, schumacher, button, kubica, sutil, barrichello, liuzzi, hulkenberg, delarosa, buemi, kobayashi, petrov, alguersuari, glock, trulli, vettel, digrassi, senna, chandhok ])
gp01.establecer_resultado([alonso, trulli, hamilton, vettel, rosberg, schumacher, button, webber, liuzzi, barrichello, kubica, sutil, alguersuari, hulkenberg, kovalainen, buemi, massa, delarosa, senna, glock, petrov, kobayashi, digrassi, chandhok], 49)

trulli.fichar_por_equipo(virgin, datetime.date(2008, 3, 19))
digrassi.fichar_por_equipo(lotus, datetime.date(2008, 3, 19))


Facade.almacenar_temporada(temporada)
