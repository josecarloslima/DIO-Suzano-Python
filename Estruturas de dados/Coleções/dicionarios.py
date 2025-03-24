dados = {"nome": "Guilherme", "idade": 28, "telefone":"3333-3333"}

print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "214-214"
print(dados)

# contatos = {
#    "guilherme@gmail.com": {"nome": "Guilherme", "telefone":"3333-3333"},
#   "giovanna@gmail.com": {"nome": "Giovanna", "telefone":"3333-4444"},
#   "chappie@gmail.com": {"nome": "Chappie", "telefone":"3333-5555"},
#   "elainee@gmail.com": {"nome": "Elaine", "telefone":"3333-6666"},
# }

# print(contatos["giovanna@gmail.com"]["telefone"])
# print(contatos["giovanna@gmail.com"])

# for chave in contatos:
#    print(chave, contatos[chave])

# for chave, valor in contatos.items():
#     print(chave, valor)

# contatos.clear()
# print(contatos)

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone":"3333-3333"}
}
copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}
print(contatos)
print(copia)

dicionario = dict.fromkeys(["nome", "telefone"])
print(dicionario)

dicionario2 = dict.fromkeys(["nome", "telefone"], "vazio")
print(dicionario2)

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone":"3333-3333"}
}

# print(contatos["chave"])
# print(contatos.get("chave"))
# print(contatos.get("chave", {}))
# print(contatos.get("guilherme@gmail.com", {}))
# print(contatos.items())
# print(contatos.keys())
print("---")
# print(contatos.pop("guilherme@gmail.com"))
# print(contatos.pop("guilherme@gmail.com", {}))
# contatos.setdefault("nome", "Giovanna")
# print(contatos)
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone":"3333-3333"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone":"3333-4444"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone":"3333-5555"},
    "elainee@gmail.com": {"nome": "Elaine", "telefone":"3333-6666"},
}

contatos.values()
print(contatos)

del contatos["guilherme@gmail.com"]["telefone"]
print(contatos)