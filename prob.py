import csv

with open("heart.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    header = next(leitor)
    nomes = []
    idades = []
    for linha in leitor:
        nomes.append((int(linha[2]), int(linha[13])))

contagem = 0
for i in range(len(nomes)):
    if nomes[i][0] == 0 and nomes[i][1] == 1:
        contagem += 1

print(contagem/len(nomes))