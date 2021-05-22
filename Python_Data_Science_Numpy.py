#!/usr/bin/env python
# coding: utf-8

# # <font color=green> PYTHON PARA DATA SCIENCE - NUMPY
# ---

# # <font color=green> 1. INTRODUÇÃO AO PYTHON
# ---

# # 1.1 Introdução

# > Python é uma linguagem de programação de alto nível com suporte a múltiplos paradigmas de programação. É um projeto *open source* e desde seu surgimento, em 1991, vem se tornando uma das linguagens de programação interpretadas mais populares. 
# >
# > Nos últimos anos Python desenvolveu uma comunidade ativa de processamento científico e análise de dados e vem se destacando como uma das linguagens mais relevantes quando o assunto é ciência de dados e machine learning, tanto no ambiente acadêmico como também no mercado.

# # 1.2 Instalação e ambiente de desenvolvimento

# ### Instalação Local
# 
# ### https://www.python.org/downloads/
# ### ou
# ### https://www.anaconda.com/distribution/

# ### Google Colaboratory
# 
# ### https://colab.research.google.com

# ### Verificando versão

# In[ ]:


get_ipython().system('python -V')


# # 1.3 Trabalhando com arrays Numpy

# In[ ]:


import numpy as np


# In[ ]:


km = np.loadtxt('carros-km.txt')


# In[ ]:


km


# In[ ]:


anos = np.loadtxt('carros-anos.txt', dtype = int)


# In[ ]:


anos


# ### Obtendo a quilometragem média por ano

# In[ ]:


km_media = km / (2019 - anos)


# In[ ]:


km_media


# In[ ]:


type(km_media)


# # <font color=green> 2. CARACTERÍSTICAS BÁSICAS DA LINGUAGEM
# ---

# # 2.1 Operações matemáticas
# 
# ### Operadores aritméticos: $+$, $-$, $*$, $/$, $**$, $\%$, $//$

# ### Adição ($+$)

# In[ ]:


2 + 2


# ### Subtração ($-$)

# In[ ]:


2 - 2


# ### Multiplicação ($*$)

# In[ ]:


2 * 3


# ### Divisão ($/$) e ($//$)
# A operação divisão sempre retorna um número de ponto flutuante

# In[ ]:


10 / 3


# In[ ]:


10 // 3


# ### Exponenciação ($**$)

# In[ ]:


2 ** 3


# ### Resto da divisão ($\%$)

# In[ ]:


10 % 3


# In[ ]:


10 % 2


# ### Expressões matemáticas

# In[ ]:


5 * 2 + 3 * 2


# In[ ]:


(5 * 2) + (3 * 2)


# In[ ]:


5 * (2 + 3) * 2


# ### A variável _
# 
# No modo interativo, o último resultado impresso é atribuído à variável _

# In[ ]:


5 * 2


# In[ ]:


_ + 3 * 2


# In[ ]:


_ / 2


# # 2.2 Variáveis 

# ### Nomes de variáveis
# 
# - Nomes de variáveis pode começar com letras (a - z, A - Z) ou o caractere *underscore* (_):
# 
#     > Altura
#     >
#     > _peso
#     
# - O restante do nome pode conter letras, números e o caractere "_":
# 
#     > nome_da_variavel
#     >
#     > _valor
#     >
#     > dia_28_11_
#     
# 
# - O nomes são *case sensitive*:
# 
#     > Nome_Da_Variável $\ne$ nome_da_variavel $\ne$ NOME_DA_VARIAVEL
#     
# ### <font color=red>Observações:
# - Existem algumas palavras reservadas da linguagem que não podem ser utilizadas como nomes de variável:
# 
# | |Lista de palavras <br>reservadas em Python| |
# |:-------------:|:------------:|:-------------:|
# | and           | as           | not           | 
# | assert        | finally      | or            | 
# | break         | for          | pass          | 
# | class         | from         | nonlocal      | 
# | continue      | global       | raise         | 
# | def           | if           | return        | 
# | del           | import       | try           | 
# | elif          | in           | while         | 
# | else          | is           | with          | 
# | except        | lambda       | yield         | 
# | False         | True         | None          | 

# ### Declaração de variáveis
# 
# ### Operadores de atribuição: $=$, $+=$, $-=$, $*=$, $/=$, $**=$, $\%=$, $//=$

# In[ ]:


ano_atual = 2019
ano_fabricacao = 2003
km_total = 44410.0


# In[ ]:


ano_atual


# In[ ]:


ano_fabricacao


# In[ ]:


km_total


# # $$km_{média} = \frac {km_{total}}{(Ano_{atual} - Ano_{fabricação})}$$

# ### Operações com variáveis

# In[ ]:


km_media = km_total / (ano_atual - ano_fabricacao)
km_media


# In[ ]:


ano_atual = 2019
ano_fabricacao = 2003
km_total = 44410.0
km_media = km_total / (ano_atual - ano_fabricacao)
km_media


# In[ ]:


ano_atual = 2019
ano_fabricacao = 2003
km_total = 44410.0
km_media = km_total / (ano_atual - ano_fabricacao)

km_total = km_total + km_media
km_total


# In[ ]:


ano_atual = 2019
ano_fabricacao = 2003
km_total = 44410.0
km_media = km_total / (ano_atual - ano_fabricacao)

km_total += km_media
km_total


# ### Conclusão:
# ```
# "valor = valor + 1" é equivalente a "valor += 1"
# ```

# ### Declaração múltipla

# In[ ]:


ano_atual, ano_fabricacao, km_total = 2019, 2003, 44410.0


# In[ ]:


ano_atual


# In[ ]:


ano_fabricacao


# In[ ]:


km_total


# In[ ]:


ano_atual, ano_fabricacao, km_total = 2019, 2003, 44410.0
km_media = km_total / (ano_atual - ano_fabricacao)
km_media


# # 2.3 Tipos de dados

# Os tipos de dados especificam como números e caracteres serão armazenados e manipulados dentro de um programa. Os tipos de dados básicos do Python são:
# 
# 1. **Números**
#     1. ***int*** - Inteiros
#     - ***float*** - Ponto flutuante
# - **Booleanos** - Assume os valores True ou False. Essencial quando começarmos a trabalhar com declarações condicionais
# - ***Strings*** - Sequência de um ou mais caracteres que pode incluir letras, números e outros tipos de caracteres. Representa um texto.
# - **None** - Representa a ausência de valor

# ### Números

# In[ ]:


ano_atual = 2019


# In[ ]:


type(ano_atual)


# In[ ]:


km_total = 44410.0


# In[ ]:


type(km_total)


# ### Booleanos

# In[ ]:


zero_km = True


# In[ ]:


type(zero_km)


# In[ ]:


zero_km = False


# In[ ]:


type(zero_km)


# ### Strings

# In[ ]:


nome = 'Jetta Variant'
nome


# In[ ]:


nome = "Jetta Variant"
nome


# In[ ]:


nome = 'Jetta "Variant"'
nome


# In[ ]:


nome = "Jetta 'Variant'"
nome


# In[ ]:


carro = '''
  Nome
  Idade
  Nota
'''


# In[ ]:


type(carro)


# ### None

# In[ ]:


quilometragem = None
quilometragem


# In[ ]:


type(quilometragem)


# # 2.4 Conversão de tipos

# In[ ]:


a = 10
b = 20
c = 'Python é '
d = 'legal'


# In[ ]:


type(a)


# In[ ]:


type(b)


# In[ ]:


type(c)


# In[ ]:


type(d)


# In[ ]:


a + b


# In[ ]:


c + d


# In[ ]:


# c + a


# ### Conversões de tipo
# 
# Funções int(), float(), str()

# In[ ]:


str(a)


# In[ ]:


type(str(a))


# In[ ]:


c + str(a)


# In[ ]:


float(a)


# In[ ]:


var = 3.141592


# In[ ]:


int(var)


# In[ ]:


var = 3.99


# In[ ]:


int(var)


# # 2.5 Indentação, comentários e formatação de *strings*

# ### Indentação
# 
# Na linguagem Python os programas são estruturados por meio de indentação. Em qualquer linguagem de programação a prática da indentação é bastante útil, facilitando a leitura e também a manutenção do código. Em Python a indentação não é somente uma questão de organização e estilo, mas sim um requisito da linguagem.

# In[ ]:


ano_atual = 2019
ano_fabricacao = 2019

if (ano_atual == ano_fabricacao):
  print('Verdadeiro')
else:
  print('Falso')


# ### Comentários
# 
# Comentários são extremamente importantes em um programa. Consiste em um texto que descreve o que o programa ou uma parte específica do programa está fazendo. Os comentários são ignorados pelo interpretador Python. 
# 
# Podemos ter comentários de uma única linha ou de múltiplas linhas.

# In[ ]:


# Isto é um comentário
ano_atual = 2019
ano_atual


# In[ ]:


# Isto
# é um 
# comentário
ano_atual = 2019
ano_atual


# In[ ]:


'''Isto é um
comentário'''
ano_atual = 2019
ano_atual


# In[ ]:


# Definindo variáveis
ano_atual = 2019
ano_fabricacao = 2019

'''
Estrutura condicional que vamos 
aprender na próxima aula
'''
if (ano_atual == ano_fabricacao):   # Testando se condição é verdadeira
  print('Verdadeiro')
else:                               # Testando se condição é falsa
  print('Falso')


# ### Formatação de *strings*

# ## *str.format()*
# 
# https://docs.python.org/3.6/library/stdtypes.html#str.format

# In[ ]:


print('Olá, {}!'.format('Rodrigo'))


# In[ ]:


print('Olá, {}! Este é seu acesso de número {}'.format('Rodrigo', 32))


# In[ ]:


print('Olá, {nome}! Este é seu acesso de número {acessos}'.format(nome = 'Rodrigo', acessos = 32))


# ## *f-Strings*
# 
# https://docs.python.org/3.6/reference/lexical_analysis.html#f-strings

# In[ ]:


nome = 'Rodrigo'
acessos = 32


# In[ ]:


print(f'Olá, {nome}! Este é seu acesso de número {acessos}')


# # <font color=green> 3. TRABALHANDO COM LISTAS
# ---

# # 3.1 Criando listas
# 
# Listas são sequências **mutáveis** que são utilizadas para armazenar coleções de itens, geralmente homogêneos. Podem ser construídas de várias formas:
# ```
# - Utilizando um par de colchetes: [ ], [ 1 ]
# - Utilizando um par de colchetes com itens separados por vírgulas: [ 1, 2, 3 ]
# ```

# In[ ]:


Acessorios = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
Acessorios


# In[ ]:


type(Acessorios)


# ### Lista com tipos de dados variados

# In[ ]:


Carro_1 = ['Jetta Variant', 'Motor 4.0 Turbo', 2003, 44410.0, False, ['Rodas de liga', 'Travas elétricas', 'Piloto automático'], 88078.64]
Carro_2 = ['Passat', 'Motor Diesel', 1991, 5712.0, False, ['Central multimídia', 'Teto panorâmico', 'Freios ABS'], 106161.94]


# In[ ]:


Carro_1


# In[ ]:


Carro_2


# In[ ]:


Carros = [Carro_1, Carro_2]
Carros


# # 3.2 Operações com listas
# 
# https://docs.python.org/3.6/library/stdtypes.html#common-sequence-operations

# ## *x in A*
# 
# Retorna **True** se um elemento da lista *A* for igual a *x*.

# In[ ]:


Acessorios


# In[ ]:


'Rodas de liga' in Acessorios


# In[ ]:


'4 X 4' in Acessorios


# In[ ]:


'Rodas de liga' not in Acessorios


# In[ ]:


'4 X 4' not in Acessorios


# ## *A + B*
# 
# Concatena as listas *A* e *B*.

# In[ ]:


A = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro']
B = ['Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']


# In[ ]:


A


# In[ ]:


B


# In[ ]:


A + B


# ## *len(A)*
# 
# Tamanho da lista A.

# In[ ]:


len(Acessorios)


# # 3.3 Seleções em listas

# ## *A[ i ]*
# 
# Retorna o i-ésimo item da lista *A*.
# 
# <font color=red>**Observação:**</font> Listas têm indexação com origem no zero.

# In[ ]:


Acessorios


# In[ ]:


Acessorios[0]


# In[ ]:


Acessorios[1]


# In[ ]:


Acessorios[-1]


# In[ ]:


Carros


# In[ ]:


Carros[0]


# In[ ]:


Carros[0][0]


# In[ ]:


Carros[0][-2]


# In[ ]:


Carros[0][-2][1]


# ## *A[ i : j ]*
# 
# Recorta a lista *A* do índice i até o j. Neste fatiamento o elemento com índice i é **incluído** e o elemento com índice j **não é incluído** no resultado.

# In[ ]:


Acessorios


# In[ ]:


Acessorios[2:5]


# In[ ]:


Acessorios[2:]


# In[ ]:


Acessorios[:5]


# # 3.4 Métodos de listas
# 
# https://docs.python.org/3.6/library/stdtypes.html#mutable-sequence-types

# In[ ]:


Acessorios = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']


# ## *A.sort()*
# 
# Ordena a lista *A*.

# In[ ]:


Acessorios


# In[ ]:


Acessorios.sort()
Acessorios


# ## *A.append(x)*
# 
# Adiciona o elemento *x* no final da lista *A*.

# In[ ]:


Acessorios.append('4 X 4')
Acessorios


# ## *A.pop(i)*
# 
# Remove e retorna o elemento de índice i da lista *A*.
# 
# <font color=red>**Observação:**</font> Por *default* o método *pop()* remove e retorna o último elemento de uma lista.

# In[ ]:


Acessorios.pop()


# In[ ]:


Acessorios


# In[ ]:


Acessorios.pop(3)


# In[ ]:


Acessorios


# ## *A.copy()*
# 
# Cria uma cópia da lista *A*.
# 
# <font color=red>**Observação:**</font> O mesmo resultado pode ser obtido com o seguinte código: 
# ```
# A[:]
# ```

# In[ ]:


Acessorios_2 = Acessorios
Acessorios_2


# In[ ]:


Acessorios_2.append('4 X 4')
Acessorios_2


# In[ ]:


Acessorios


# In[ ]:


Acessorios.pop()
Acessorios


# In[ ]:


Acessorios_2


# In[ ]:


Acessorios_2 = Acessorios.copy()
Acessorios_2


# In[ ]:


Acessorios_2.append('4 X 4')
Acessorios_2


# In[ ]:


Acessorios


# In[ ]:


Acessorios_2 = Acessorios[:]
Acessorios_2


# # <font color=green> 4. ESTRUTURAS DE REPETIÇÃO E CONDICIONAIS
# ---

# # 4.1 Instrução *for*
# 
# #### Formato padrão
# 
# ```
# for <variável> in <coleção>:
#     <instruções>
# ```

# ### Loops com listas

# In[ ]:


Acessorios = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
Acessorios


# In[ ]:


for item in Acessorios:
  print(item)


# ###  List comprehensions
# 
# https://docs.python.org/3.6/tutorial/datastructures.html#list-comprehensions

# *range()* -> https://docs.python.org/3.6/library/functions.html#func-range

# In[ ]:


range(10)


# In[ ]:


list(range(10))


# In[ ]:


for i in range(10):
  print(i ** 2)


# In[ ]:


quadrado = []
for i in range(10):
  quadrado.append(i ** 2)
  
quadrado


# In[ ]:


[i ** 2 for i in range(10)]


# # 4.2 Loops aninhados

# In[ ]:


dados = [ 
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]
dados


# In[ ]:


for lista in dados:
  print(lista)


# In[ ]:


for lista in dados:
  for item in lista:
    print(item)


# In[ ]:


Acessorios = []

for lista in dados:
  for item in lista:
    Acessorios.append(item)
    
Acessorios


# ## *set()*
# 
# https://docs.python.org/3.6/library/stdtypes.html#types-set
# 

# In[ ]:


list(set(Acessorios))


# ### List comprehensions

# In[ ]:


[item for lista in dados for item in lista]


# In[ ]:


list(set([item for lista in dados for item in lista]))


# # 4.3 Instrução *if*
# 
# #### Formato padrão
# 
# ```
# if <condição>:
#      <instruções caso a condição seja verdadeira>
# ```

# ### Operadores de comparação: $==$, $!=$, $>$, $<$, $>=$, $<=$
# ### e
# ### Operadores lógicos: $and$, $or$, $not$

# In[ ]:


# 1º item da lista - Nome do veículo
# 2º item da lista - Ano de fabricação
# 3º item da lista - Veículo é zero km?

dados = [
    ['Jetta Variant', 2003, False],
    ['Passat', 1991, False],
    ['Crossfox', 1990, False],
    ['DS5', 2019, True],
    ['Aston Martin DB4', 2006, False],
    ['Palio Weekend', 2012, False],
    ['A5', 2019, True],
    ['Série 3 Cabrio', 2009, False],
    ['Dodge Jorney', 2019, False],
    ['Carens', 2011, False]
]
dados


# In[ ]:


zero_km_Y = []

for lista in dados:
  if(lista[2] == True):
    zero_km_Y.append(lista)
    
zero_km_Y


# In[ ]:


zero_km_N = []

for lista in dados:
  if(lista[2] == False):
    zero_km_N.append(lista)
    
zero_km_N


# ### List comprehensions

# In[ ]:


[lista for lista in dados if lista[2] == True]


# # 4.4 Instruções *if-else* e *if-elif-else*
# 
# #### Formato padrão
# 
# ```
# if <condição>:
#     <instruções caso a condição seja verdadeira>
# else:
#     <instruções caso a condição não seja verdadeira>
# ```

# In[ ]:


zero_km_Y, zero_km_N = [], []

for lista in dados:
  if(lista[2] == True):
    zero_km_Y.append(lista)
  else:
    zero_km_N.append(lista)


# In[ ]:


zero_km_Y


# In[ ]:


zero_km_N


# #### Formato padrão
# 
# ```
# if <condição 1>:
#     <instruções caso a condição 1 seja verdadeira>
# elif <condição 2>:
#     <instruções caso a condição 2 seja verdadeira>
# elif <condição 3>:
#     <instruções caso a condição 3 seja verdadeira>
#                         .
#                         .
#                         .
# else:
#     <instruções caso as condições anteriores não sejam verdadeiras>
# ```

# In[ ]:


dados


# In[ ]:


print('AND')
print(f'(True and True) o resultado é: {True and True}')
print(f'(True and False) o resultado é: {True and False}')
print(f'(False and True) o resultado é: {False and True}')
print(f'(False and False) o resultado é: {False and False}')


# In[ ]:


print('OR')
print(f'(True or True) o resultado é: {True or True}')
print(f'(True or False) o resultado é: {True or False}')
print(f'(False or True) o resultado é: {False or True}')
print(f'(False or False) o resultado é: {False or False}')


# In[ ]:


A, B, C = [], [], []

for lista in dados:
  if(lista[1] <=2000):
    A.append(lista)
  elif(lista[1] > 2000 and lista[1] <= 2010):
    B.append(lista)
  else:
    C.append(lista)


# In[ ]:


A


# In[ ]:


B


# In[ ]:


C


# In[ ]:


A, B, C = [], [], []

for lista in dados:
  if(lista[1] <=2000):
    A.append(lista)
  elif(2000 < lista[1] <= 2010):
    B.append(lista)
  else:
    C.append(lista)


# # <font color=green> 5. NUMPY BÁSICO
# ---
# 
# Numpy é a abreviação de Numerical Python e é um dos pacotes mais importantes para processamento numérico em Python. Numpy oferece a base para a maioria dos pacotes de aplicações científicas que utilizem dados numéricos em Python (estruturas de dados e algoritmos). Pode-se destacar os seguintes recursos que o pacote Numpy contém:
# 
# - Um poderoso objeto array multidimensional;
# - Funções matemáticas sofisticadas para operações com arrays sem a necessidade de utilização de laços *for*;
# - Recursos de algebra linear e geração de números aleatórios
# 
# Além de seus óbvios usos científicos, o pacote NumPy também é muito utilizado em análise de dados como um eficiente contêiner multidimensional de dados genéricos para transporte entre diversos algoritmos e bibliotecas em Python.
# 
# **Versão:** 1.16.5
# 
# **Instalação:** https://scipy.org/install.html
# 
# **Documentação:** https://numpy.org/doc/1.16/

# ### Pacotes
# 
# Existem diversos pacotes Python disponíveis para download na internet. Cada pacote tem como objetivo a solução de determinado tipo de problema e para isso são desenvolvidos novos tipos, funções e métodos.
# 
# Alguns pacotes são bastante utilizados em um contexto de ciência de dados como por exemplo:
# 
# - Numpy
# - Pandas
# - Scikit-learn
# - Matplotlib
# 
# Alguns pacotes não são distribuídos com a instalação default do Python. Neste caso devemos instalar os pacotes que necessitamos em nosso sistema para podermos utilizar suas funcionalidades.

# ### Importando todo o pacote

# In[ ]:


import numpy


# https://numpy.org/doc/1.16/reference/generated/numpy.arange.html

# In[ ]:


numpy.arange(10)


# ### Importando todo o pacote e atribuindo um novo nome 

# In[ ]:


import numpy as np


# In[ ]:


np.arange(10)


# ### Importando parte do pacote

# In[ ]:


from numpy import arange


# In[ ]:


arange(10)


# # 5.1 Criando arrays Numpy

# In[ ]:


import numpy as np


# ### A partir de listas
# 
# https://numpy.org/doc/1.16/user/basics.creation.html

# In[ ]:


km = np.array([1000, 2300, 4987, 1500])


# In[ ]:


km


# In[ ]:


type(km)


# https://numpy.org/doc/1.16/user/basics.types.html

# In[ ]:


km.dtype


# ### A partir de dados externos
# 
# https://numpy.org/doc/1.16/reference/generated/numpy.loadtxt.html

# In[ ]:


km = np.loadtxt(fname = 'carros-km.txt', dtype = int)


# In[ ]:


km


# In[ ]:


km.dtype


# ### Arrays com duas dimensões

# In[ ]:


dados = [ 
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]
dados


# In[ ]:


Acessorios = np.array(dados)


# In[ ]:


Acessorios


# In[ ]:


km.shape


# In[ ]:


Acessorios.shape


# ### Comparando desempenho com listas

# In[ ]:


np_array = np.arange(1000000)


# In[ ]:


py_list = list(range(1000000))


# In[ ]:


get_ipython().run_line_magic('time', 'for _ in range(100): np_array *= 2')


# In[ ]:


get_ipython().run_line_magic('time', 'for _ in range(100): py_list = [x * 2 for x in py_list]')


# # 5.2 Operações aritméticas com arrays Numpy

# ### Operações entre arrays e constantes

# In[ ]:


km = [44410., 5712., 37123., 0., 25757.]
anos = [2003, 1991, 1990, 2019, 2006]


# In[ ]:


# idade = 2019 - anos


# In[ ]:


km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])


# In[ ]:


idade = 2019 - anos


# In[ ]:


idade


# ### Operações entre arrays

# In[ ]:


km_media = km / idade


# In[ ]:


km_media


# In[ ]:


44410 / (2019 - 2003)


# In[ ]:


5712 / (2019 - 1991)


# ### Operações com arrays de duas dimensões

# In[ ]:


dados = np.array([km, anos])


# In[228]:


dados


# In[ ]:


dados.shape


# ![1410-img01.png](https://caelum-online-public.s3.amazonaws.com/1410-pythondatascience/01/1410-img01.png)

# In[ ]:


dados[0]


# In[ ]:


dados[1]


# In[ ]:


km_media = dados[0] / (2019 - dados[1])


# In[ ]:


km_media


# # 5.3 Seleções com arrays Numpy

# ![1410-img01.png](https://caelum-online-public.s3.amazonaws.com/1410-pythondatascience/01/1410-img01.png)

# In[259]:


dados


# ![1410-img02.png](https://caelum-online-public.s3.amazonaws.com/1410-pythondatascience/01/1410-img02.png)

# ### Indexação 
# 
# <font color=red>**Observação:**</font> A indexação tem origem no zero.

# In[260]:


contador = np.arange(10)
contador


# In[261]:


contador[0]


# In[264]:


item = 6
index = item - 1
contador[index]


# In[265]:


contador[-1]


# In[266]:


dados[0]


# In[267]:


dados[1]


# ## <font color=green>**Dica:**</font>
# ### *ndarray[ linha ][ coluna ]* ou *ndarray[ linha, coluna ]*

# In[268]:


dados[1][2]


# In[269]:


dados[1, 2]


#  ### Fatiamentos
#  
# A sintaxe para realizar fatiamento em um array Numpy é $i : j : k$ onde $i$ é o índice inicial, $j$ é o índice de parada, e $k$ é o indicador de passo ($k\neq0$)
#  
# <font color=red>**Observação:**</font> Nos fatiamentos (*slices*) o item com índice i é **incluído** e o item com índice j **não é incluído** no resultado.

# ![1410-img01.png](https://caelum-online-public.s3.amazonaws.com/1410-pythondatascience/01/1410-img01.png)

# In[270]:


contador = np.arange(10)
contador


# In[271]:


contador[1:4]


# In[272]:


contador[1:8:2]


# In[273]:


contador[::2]


# In[274]:


contador[1::2]


# In[275]:


dados


# In[277]:


dados[:, 1:3]


# In[280]:


dados[:, 1:3][0] / (2019 - dados[:, 1:3][1])


# In[281]:


dados[0] / (2019 - dados[1])


# ### Indexação com array booleano
# 
# <font color=red>**Observação:**</font> Seleciona um grupo de linhas e colunas segundo os rótulos ou um array booleano.

# In[282]:


contador = np.arange(10)
contador


# In[283]:


contador > 5


# In[284]:


contador[contador > 5]


# In[285]:


contador[[False, False, False, False, False, False,  True,  True,  True, True]]


# In[286]:


dados


# In[288]:


dados[1] > 2000


# In[289]:


dados[:, dados[1] > 2000]


# # 5.4 Atributos e métodos de arrays Numpy

# In[329]:


dados = np.array([[44410., 5712., 37123., 0., 25757.],
                  [2003, 1991, 1990, 2019, 2006]])
dados


# ### Atributos
# 
# https://numpy.org/doc/1.16/reference/arrays.ndarray.html#array-attributes

# ## *ndarray.shape*
# 
# Retorna uma tupla com as dimensões do array.

# In[330]:


dados.shape


# ## *ndarray.ndim*
# 
# Retorna o número de dimensões do array.

# In[331]:


dados.ndim


# ## *ndarray.size*
# 
# Retorna o número de elementos do array.

# In[332]:


dados.size


# ## *ndarray.dtype*
# 
# Retorna o tipo de dados dos elementos do array.

# In[333]:


dados.dtype


# ## *ndarray.T*
# 
# Retorna o array transposto, isto é, converte linhas em colunas e vice versa.

# In[334]:


dados.T


# In[335]:


dados.transpose()


# ### Métodos
# 
# https://numpy.org/doc/1.16/reference/arrays.ndarray.html#array-methods

# ## *ndarray.tolist()*
# 
# Retorna o array como uma lista Python.

# In[336]:


dados.tolist()


# ## *ndarray.reshape(shape[, order])*
# 
# Retorna um array que contém os mesmos dados com uma nova forma.

# In[337]:


contador = np.arange(10)
contador


# In[338]:


contador.reshape((5, 2))


# In[339]:


contador.reshape((5, 2), order='C')


# In[340]:


contador.reshape((5, 2), order='F')


# In[ ]:


km = [44410, 5712, 37123, 0, 25757]
anos = [2003, 1991, 1990, 2019, 2006]


# In[342]:


info_carros = km + anos
info_carros


# In[344]:


np.array(info_carros).reshape((2, 5))


# In[346]:


np.array(info_carros).reshape((5, 2), order='F')


# ## *ndarray.resize(new_shape[, refcheck])*
# 
# Altera a forma e o tamanho do array.

# In[347]:


dados_new = dados.copy()
dados_new


# In[ ]:


dados_new.resize((3, 5), refcheck=False)


# In[350]:


dados_new


# In[351]:


dados_new[2] = dados_new[0] / (2019 - dados_new[1])


# In[352]:


dados_new


# # 5.5 Estatísticas com arrays Numpy
# 
# https://numpy.org/doc/1.16/reference/arrays.ndarray.html#calculation
# 
# e
# 
# https://numpy.org/doc/1.16/reference/routines.statistics.html
# 
# e
# 
# https://numpy.org/doc/1.16/reference/routines.math.html

# In[ ]:


anos = np.loadtxt(fname = "carros-anos.txt", dtype = int)
km = np.loadtxt(fname = "carros-km.txt")
valor = np.loadtxt(fname = "carros-valor.txt")


# In[383]:


anos.shape


# https://numpy.org/doc/1.16/reference/generated/numpy.column_stack.html

# In[ ]:


dataset = np.column_stack((anos, km, valor))
dataset


# In[385]:


dataset.shape


# ## *np.mean()*
# 
# Retorna a média dos elementos do array ao longo do eixo especificado.

# In[387]:


np.mean(dataset, axis = 0)


# In[ ]:


np.mean(dataset, axis = 1)


# In[389]:


np.mean(dataset[:, 1])


# In[390]:


np.mean(dataset[:, 2])


# ## *np.std()*
# 
# Retorna o desvio padrão dos elementos do array ao longo do eixo especificado.

# In[391]:


np.std(dataset[:, 2])


# ## *ndarray.sum()*
# 
# Retorna a soma dos elementos do array ao longo do eixo especificado.

# In[392]:


dataset.sum(axis = 0)


# In[393]:


dataset[:, 1].sum()


# ## *np.sum()*
# 
# Retorna a soma dos elementos do array ao longo do eixo especificado.

# In[394]:


np.sum(dataset, axis = 0)


# In[395]:


np.sum(dataset[:, 2])


# In[ ]:




