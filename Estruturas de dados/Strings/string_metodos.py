nome = "GuIlHeRmO"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = " Olá mundo!   "
print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"
print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "-"))

titulo = "Python"
print("*".join(titulo))

# podemos usar um for, fica mais complicado mas fica muito parecido
for letra in titulo:
    print(letra, end="*")