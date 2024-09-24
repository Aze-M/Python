#   Grundlegende Datentypen:
#
#   int - kurzform von Integer, speichern zahlen in Python3 bis zum ende des verfügbaren speichers, allerdings ist dieses natürlich systemabhängig
#   float - kurzvorm von floating point, eine dynamische zahl mit unterstützung für nachkommazahlen. Python gibt auch bei integer mathe einen float zurück wenn das endresultat nicht in einen integer passt, z.B. 3(int)/2(int) = 1.5(float)
#   str - strings, aus dem englischen da es sich hier um ketten an zeichen handelt, oder halt um einen string of characters. Ironischerweise besitzt python kein Char type.
#   list - eine datensammlung die beliebige typen in sich haben kann, und auch nicht intern konsistent sein muss. [1, "käse", 2] ist genauso valide wie [1, 2, 3]
#

# Basisfunktionen:

#   print("Text Hier!")
#
#   versucht den Text auszuwerfen der gegeben wurde, oder wenn es kein text ist wird versucht in text umzuwandeln. 
#   eine integer zum beispiel wird nicht als 1 geprinted, sondern intent als "1"
#

print("Hi, ich bin ein Python Print!")

#   if x == y:
#   
#   vergleicht den linken wert mit dem rechten, es muss zwingend ein booleanischer wert zurück kommen können, also Ja oder Nein ( True or False )
#   dieser befehl wird nur ein einziges mal ausgeführt, und die contents des statements werden nur bei zutreffen ausgeführt
#

#   simple zuweisungen immer mit einem gleichzeichen! Den typen nimmt sich python automatisch im interpreter.
x = 1
y = 1

# Wichtig is bei vergleichen immer das doppelte = , ein einzelnes = ist eine zuweisung!
if x == y:
    x = x + 1


#   while x < 100:
#
#   führt ebenfalls einen Ja/Nein (True/False) vergleich aus, allerginds wird der inhalt der schleife so lange wiederholt bis false rauskommt.
#   endlosschleifen lassen sich mit
#
#   while True:
#
#   starten, und laufen bis der thread beendet wird, oder von innerhalb das keyword break aufgerufen wird
#

#   diese schleife wird nur ausgeführt solange X unter 100 ist, im terminal kannst du dank des print befehls dieses nachverfolgen
while x < 100:
    x = x + 10
    print(x)

#   for element in iterator:
#
#   für iterierbare typen wie zum beispiel Listen ist es semantisch eine solche schleife zu verwenden, solange man auf jedes element nur ein mal agieren will.
#   in der liste [1,2,3,4] zum beispiel wäre element in der ersten schleife 1, dann 2, dann 3, dann 4 und schließlich würde der code sich an der schleife vorbei bewegen.
#

#   hier die liste aus dem beispiel
iterator = [1,2,3,4]

#   in der console kannst du sehen das einmal bis 4 gezählt wird, also jedes element einmal ausgeworfen wird
for element in iterator:
    print(element)

#
#   Als kleine aufgabe;
#   
#   schreibe eine for schleife die die oben definiertie liste iterator nacheinander auf eine neue variable start zurechnet, die du außerhalb der schleife mit start = 0 definierst
#   innerhalb der schleife also start = start + element, oder start += element
#   schreibe eine while schleife die dann start in einzelschritten bis 99 hochzählt , also start = start + 1, oder start+=1
#   schreibe ein if statement das nur greift wenn start 99 ist und nur dann erneut 1 hinzufügt um auf 100 zu kommen
#   werfe den wert von start mit print an die konsole aus
#   danach schreibe "Fertig!" in die konsole als output über print
#
