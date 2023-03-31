ano_atual = int(input("Digite o ano atual: "))
idade = int(input("Digite sua idade: "))
ano = int(input("Digite qualquer ano: "))
nome = input("Digite seu nome: ")

ano_nascimento = ano_atual - idade
resultado = ano - ano_nascimento

print( nome, "no ano de", ano, "você terá", resultado)