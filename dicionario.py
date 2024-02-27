alunos= {
    1: "Alberto",
    2: "Neto",
    3: "Sandra",
    4: "Paulo",
    5: "Pricila"
}

print(alunos[1])
alunos['nome'] = "Silas"
print(alunos)
del alunos["novo"]

for chave, valor in alunos.items():
    print(chave, valor)
