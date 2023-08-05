print("Hello world")
print("Oi, seja bem vindo ao curso de Python")

'''
TIPOS DE DADOS

Texto: str
Numérico: int, float, complex
Sequência: list, tuple, range
Mapa: dict
Coleção: set, frozenset
Booleano: bool ( true ou false)
Binário: bytes, byearray, memoryview
'''
print('Veja agora alguns exemplos de tipos de dados')
print(1+10) #Inteiro (int)
print(1.5+10) #ponto flutuante (float)
print(True) #booleano (bool)
print(False) #booleano (bool)
print('Python') #Texto (string)

'''
VARIÁVEIS E CONSTANTES

Variável: muda de valor de acordo com a necessidade de execução do programa
Constante: Não muda de valor, até o final da execução do programa

Na constante, o valor deve ser escrito com todas as letras em maiúsculo, e no lugar do espaço, deve se colocar o _

'''
print('Veja alguns exemplos de declacar variáveis')
nome = "John"
idade = 27

print(nome, idade)

limite_saque_diario = 1000
print(limite_saque_diario)

print('Exemplos de como declarar costantes')

BRAZILIAN_STATES = ['SP', 'RJ', 'MG', 'RS', 'AM']

print(BRAZILIAN_STATES)

'''
CONVERSÃO DE TIPOS E VARIÁVEIS
'''
print(int(1.9)) # float para interio
print(int('10')) #int para string
print(float('10.10')) #string para float
print(float(100)) #int para float

# Perguntando o tipo das classes

valor = 10
valor_str = str(valor) # int para string
print(type(valor))
print(type(valor_str))

print(100/2) # Com a barra simples na divisão, recebemos um resultado em float
print(100//2) # Dessa forma, usando barra dupla na divisão, conseguimos converter uma float para um int


'''
FUNÇÕES DE ENTRADA E SAÍDA

Input: lê os dados inseridos no TECLADO, ou seja, aquilo que o usuário digita.
Print: utilizada quando queremos mostrar algo na tela para o usuário.
'''
print('Exemplo de input')

nome = input('Informe seu nome:')
idade = input('Informe a sua idade')

print(nome)
print(idade)
print(nome, idade) # Outra opção que podemos utilizar para exibir uma ou mais variáveis de uma vez

