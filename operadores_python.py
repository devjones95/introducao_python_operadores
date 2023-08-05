'''
OPERADORES ARITMÉTICOS

Os operadores aritméticos são ps que executam operações matemáticas, como adição, subtração, divisão e multiplicação.
+ adição
- subtração
* multiplicação
** exponenciação
/ divisão
// divisão inteira
'''

print('Veja alguns exemplos de operações')

abacaxi = 10
banana = 20
abacate = 15
laranja = 5.5
amora = 3.5

print(amora + banana)
print(abacaxi - banana)
print(abacate / laranja)
print(banana // amora)
print(abacate * banana)
print(amora ** abacaxi)

print('Outros Exemplos')
x = (10 * 5) + 20 / 2
y = (10 / 2) * 2 / 4

print(x)
print(y)

'''
OPERADORES DE COMPARAÇÃO

São utilzados para comparar 2 valores
'''
print('Exemplos de comparações de IGUALDADE')

saldo = 1000
saque = 500

print(saldo == saque) # Comparando se saldo é IGUAL a saque
print(saldo != saque) # Comparando se saldo é DIFERENTE de saque

# Nas comparações, o resultado sempre será booleano, ou seja, VERDADEIRO ou FALSO

# Maior, menor ou igual

print('Exemplos de comparações maior, menor ou igual')

saldo = 200
saque = 200

print(saldo > saque) # maior que
print(saldo < saque) # menor que
print(saldo >= saque) # maior que
print(saldo <= saque) # menor que

'''
OPERADORES DE ATRIBUIÇÃO
'''
saldo = 500
print(saldo)

saldo -= 50 # atribuição por subtração
print(saldo)

saldo *= 50 # atribuição por multiplicação
print(saldo)

saldo /= 50 # atribuição por divisão
print(saldo)

saldo //= 50 # atribuição por divisão inteira
print(saldo)

saldo += 50 # atribuição por adição
print(saldo)


'''
OPERADORES LÓGICOS

Operador E (and)
Operador OU (or)
Operador de NEGAÇÃO (not)
Parênteses ()

'''
print('Veja na pratica, os exemplos de operadores')

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or True)
print(False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(exp)


'''
OPERADORES DE IDENTIDADE

Operador IS
Operador IS NOT
'''
print('Exemplos de operadores de identidade')

saldo = 1000
limite = 500

print(saldo is limite)
print(saldo is not limite)

curso = "Curso de Python"
nome_curso = curso

print(curso is nome_curso)

'''
OPERADORES DE ASSOCIAÇÃO
Usado para confirmar se um item está dentro de uma determinada sequência de itens
'''
print("Exemplos de operadores de associação")

frutas = ["Limão","Laranja","Maçã","Uva"]

print("Laranja" in frutas) # Laranja está na lista de frutas

print("Abacaxi" in frutas) # Abacaxi NÃO está na lista de frutas

print("Uva", "Limão", "Laranja" in frutas)