lista = []
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)

l2 = lista.copy()
print(lista)

print(id(l2), id(lista))

lista.clear()
print(lista)

cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

linguagens = ["python", "js", "c"]
print(linguagens) 

linguagens.extend(["java", "csharp"])
print(linguagens)

print(linguagens.index("java"))
print(linguagens.index("python"))

print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())

linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.remove("c")
print(linguagens)

linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.reverse()
print(linguagens)

linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort()
print(linguagens)
linguagens.sort(reverse=True)
print(linguagens)
linguagens.sort(key=lambda x: len(x))
print(linguagens)
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

linguagens = ['python', 'js', 'c', 'java', 'csharp']
print(len(linguagens))

linguagens = ['python', 'js', 'c', 'java', 'csharp']
print(sorted(linguagens, key=lambda x: len(x)))
print(sorted(linguagens, key=lambda x: len(x), reverse=True))