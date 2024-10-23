# kolekcje języka Python
# przykład 1: listy

"""
komentarz wieloliniowy
pisz ile chcesz....
"""

kraje = ["Polska","Szwecja","Japonia","Niemcy","Hiszpania","Kosytaryka"]
mieszana = ["abc",34,5.66,True]

print(kraje)
print(type(kraje))

k1 = kraje[2]

print(k1)
print(type(k1))
print(kraje[1:4])
print(kraje[:5])
print(kraje[3:])
print(kraje[-1])

liczby = [4,75,3,78,32,88,102,-45,0,1,102,56,12,9,102]

print(liczby)
print(liczby[3:10:3])
print(liczby[::2])
print(liczby[::-1])

liczby.append(455)
print(liczby)
liczby.insert(3,100)
print(liczby)

liczby.remove(102)
print(liczby)

del liczby[5:7]
print(liczby)

info = "to jest kolejka za bardzo dobrymi pierogami"
print(info)
print(type(info))

print(info[9])
print(info[9:13])
infolist = list(info)
infolist.append('t')
print(infolist)

#przykład 2: krotka

animal = ("pies","kot","papuga","królik","pies","leniwiec","pies","słoń")
print(animal)
print(type(animal))

print(animal.index("kot"))
print(animal.count("pies"))
print(animal[2:5])

liczby.sort(reverse=True)
print(liczby)


# animal.sort()
# szybkie komentowanie/ odkomentowanie bloku tekstu: CTRL + /
# szybka duplikacja bloku tekstu: CTRL + D
