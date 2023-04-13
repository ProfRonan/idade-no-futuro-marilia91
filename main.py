ano_atual = int(input())
idade = int(input())
ano = int(input())
nome = input()

ano_nascimento = ano_atual - idade
resultado = ano - ano_nascimento

print("{}, no ano de {} você terá {} anos".format(nome, ano, resultado))