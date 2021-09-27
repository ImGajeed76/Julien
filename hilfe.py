# -----------------------------------------------------------
# Variables
# -----------------------------------------------------------
#
# Der name der Variablen, kann alles sein!!!
#
#
# String (Text)
string = "abc123.-+..."
#
# Int (Nummer ohne komma stellen)
integer = 1234
#
# Float (Nummer mit komma stellen)
Float = 12.3456
#
# Boolean (entweder Wahr/True oder Falsch/False)
boolean = True
#
# Array (eine ansamlung von variablen. Es kann auch ein Array in einem Array sein -> "2D Array")
array = [13, "", True, 13.45, [], 123]
#
#
#
#
# -----------------------------------------------------------
# if / elif / else / for / while
# -----------------------------------------------------------
#
# if (fragt ob etwas Wahr/True oder Falsh/False ist)
if "hallo" == string:
    print("do this")
#
# elif (wenn das if zuvor nicht zutrift und das hier Wahr/True oder Falsch7False ist)
elif "welt" == string:
    print("do this")
#
# else (wenn alles zuvor nicht zutrift)
else:
    print("do this")
#
#
# for ... in ... ( "für jedes element in" wieder holt so oft wie es elemente giebt und speichert das jeweilige in
# in diesem fall i. Das kann aber jede variable sein.)
for i in [1, 2, 3, 4, 5]:
    print(i)
#
# while ( "solange" wieder holt so lange etwas Wahr/True ist oder sie unterbrochen wird -> "break".)
while True:
    print("do this")
    break
#
#
#
#
# -----------------------------------------------------------
# Other
# -----------------------------------------------------------
#
# len() (die länge von einem object. z.b. von einem Array oder einem String.)
len(array)
#
# range() (kreirt eine art array von 0 bis zu einer zahl vor der die man mit giebt)
range(10)  # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# break (beendet if / elif / else / for oder while)
while True:
    break
#
#
#
#
# -----------------------------------------------------------
# Addition / Subtraction / Division / Multiplikation ...
# -----------------------------------------------------------
#
a = 1
b = 1
c = 1
#
#
# Addition (man kann auf zwei weisen variablen addieren und sie speichern)
a = a + b  # a ist das ergebnis von a + b
a += b  # b wird zu a hinzu addiert
# was aber nicht geht ist "a += b += c" das müsste man dann so machen "a += b + c"
#
# Subtraction (bei der subtraction ist es änlich)
a = a - b  # a ist das ergebnis von a - b
a -= b  # b wird von a abgezogen
# was aber nicht geht ist "a -= b -= c" das müsste man dann so machen "a -= b - c"
#
# bei den anderen ist es genau gleich
a = a / b
a /= b
# und
a = a * b
a *= b
#
#
#
# Hoch rechnen (das hoch rechnen ist in python sehr einfach. mann benutzt als operator einfach zwei sterne)
a = a ** b
a **= b
#
#
#
#
# -----------------------------------------------------------
# Arrays
# -----------------------------------------------------------
#
# um den inhalt einer bestimmten postion zu bekommen giebt es zwei wege
array[5]  # so bekomme ich den inhalt der 5 position von diesem array. Achtung die zählung beginnt bei 0.
array.__getitem__(5)  # das macht eigentlich genau das gleiche, es ist nur ausgeschrieben.
#
# um eine postion zu überschreiben, nimmt man einfach die position und setzt sie neu
array[5] = "bla"
#
# um etwas am ende des arrays hinzuzufügen benutzt man einfach append
array.append(123456)
#
#
# -----------------------------------------------------------
# Functions
# -----------------------------------------------------------
#
def add(a, b):
    return a + b
# eine funktion wird mit dem parameter "def" dekleriert.
# dann kommt der name der funktion. in diesem fall wäre das "add".
# in zwei klammern kommen die parameter die mit gegeben werden. a und b.
# return heisst zurück geben. Die Funktion soll also "a + b" zurück geben.
