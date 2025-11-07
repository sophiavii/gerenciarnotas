
alunos = []


notas = []


alunos.append("Ana")
alunos.append("Bruno")
alunos.append("Carla")


notas_ana = [8, 9, 7]
notas_bruno = [6, 7, 8]
notas_carla = [9, 10, 8]


notas.append(notas_ana)
notas.append(notas_bruno)
notas.append(notas_carla)


for i in range(len(alunos)):
    print(f"Aluno: {alunos[i]} - Notas: {notas[i]}")


media_ana = sum(notas[0]) / len(notas[0])
print(f"Média de {alunos[0]}: {media_ana:.2f}")


menor_nota_bruno = min(notas[1])
notas[1].remove(menor_nota_bruno)
print(f"Notas de {alunos[1]} após remover a menor ({menor_nota_bruno}): {notas[1]}")


notas[2].append(9)
print(f"Notas de {alunos[2]} após adicionar nova nota: {notas[2]}")


notas[0].sort()
print(f"Notas de {alunos[0]} ordenadas: {notas[0]}")


notas[1].clear()
print(f"Notas de {alunos[1]} após limpar: {notas[1]}")