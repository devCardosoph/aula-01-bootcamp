# Instruções:

CONSTANTE_BONUS = 1000

# O programa deve começar solicitando ao usuário que insira seu nome.
nome_usuario = input("Digite o seu nome: ")

# Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
salario_usuario = float(input("Digite o seu salário: "))

# Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
bonus_usuario = float(input("Digite o seu bonus: "))

# O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de xxxxxx".
print(f"Olá {nome_usuario}, o seu bonus foi de {valor_do_bonus}")