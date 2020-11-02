import operator

cadenaPalabras = '''Soy ginebrino de nacimiento, y mi familia es una de las más distinguidas de esa república. Durante muchos años mis antepa­sados habían sido consejeros y jueces, y mi padre había ocupado con gran honor y buena reputación diversos cargos públicos. Todos los que lo conocían lo respetaban por su integridad e infatigable dedicación. Pasó su juventud dedicado por completo a los asuntos de su país, y sólo al final de su vida pensó en el matrimonio y así dar al Estado unos hijos que pudieran perpetuar su nombre y sus virtudes.

Puesto que las circunstancias de su matrimonio reflejan su personalidad, no puedo dejar de referirme a ellas. Uno de sus más íntimos amigos era un comerciante, que, debido a numerosos contratiempos, cayó en la miseria tras gozar de una muy desahogada situación. Este hombre, de nombre Beaufort, era de carácter orgulloso y altivo y se resistía a vivir en la pobreza y el olvido en el mismo país en el que, con anterioridad, se le distinguiera por su categoría y riqueza. Habiendo, pues, saldado sus deudas en la forma más honrosa, se retiró a la ciudad de Lucerna con su hija, donde vivió sumido en el anonimato y la desdicha. Mi padre profesaba a Beaufort una auténtica amistad, y su reclusión en estas desgraciadas circunstancias le afligió mucho. También sentía íntimamente la ausencia de su compañía, y se propuso encontrarlo y persuadirlo de que, con su crédito y ayuda, empezara de nuevo.

Beaufort había tomado medidas eficaces para esconderse, y mi padre tardó diez meses en descubrir su paradero. Entusiasmado con el descubrimiento, mi padre se apresuró hacia su casa situada en una humilde calle cerca del Reuss. Pero al llegar sólo encon­tró miseria y desesperación. Beaufort no había logrado salvar más que una pequeña cantidad de dinero de los despojos de su fortuna. Era suficiente para sustentarlo durante algunos meses y, mientras tanto, esperaba encontrar un trabajo respetable con algún comerciante. Así pues, pasó el intervalo inactivo; y, con tanto tiempo para reflexionar sobre su dolor, se hizo más profundo y amargo y, al fin, se apoderó de tal forma de él, que tres meses después estaba enfermo en cama, incapaz de realizar cualquier esfuerzo.'''

listaPalabras = cadenaPalabras.lower().split()

frecuenciaPalab = []
for w in listaPalabras:
    frecuenciaPalab.append(listaPalabras.count(w))

repeticiones = []

for x in range(0, len(listaPalabras)):
    repeticiones.append((listaPalabras[x], frecuenciaPalab[x]))

myList = list(set(repeticiones))

myList = sorted(myList, key=operator.itemgetter(1), reverse=True)


for x in range(0, len(myList)):
    print('La palabra ' + myList[x][0] + ' aparece ' + str(myList[x][1]) + ' veces.')