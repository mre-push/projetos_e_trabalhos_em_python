## ##Use for, split() e if para criar uma declaração que imprima as palavras que começam com 's':

st = 'Print only the words that start with s in this sentence'
palavras = st.split()
for palavra in palavras:
    if  "s" == palavra[0]:
        print(palavra)

##No código acima, só tive uma dificuldade quanto a quarta linha, mas cheguei a conclusão de que seria dessa forma aí colocada.

##Use range() para imprimir todos os números pares de 0 a 10.
range(0,10,2)

list(range(0,10,2))

x = range(0,10)

for num in x:
    if num % 2 == 0:
        print(num)

##Use a compreensão de lista para criar uma lista de todos os números entre 1 e 50 que são divisíveis por 3.
[x for x in range(1,50) if x % 3 == 0]

##Percorra a string abaixo e se o comprimento de uma palavra for par imprima "é par!"
st = 'Print every word in this sentence that has an even number of letters'
frase = "Print every word in this sentence that has an even number of letters"
palavras = frase.split()
for palavra in palavras:
    quant = len(palavra)
    if quant % 2 == 0:
        print( palavra, "é par!")

##Escreva um programa que imprima os números inteiros de 1 a 100. Para múltiplos de três imprima "Fizz" ao ivés do número, e para os múltiplos de cinco imprima "Buzz". Para números que são múltiplos de três e cinco imprima "FizzBuzz".
for x in range(1, 100):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0: 
        print("Fizz")
    elif x % 5 == 0: 
        print("Buzz")

##Use Compreensão em listas para criar uma lista das primeiras letras de cada palavra na string abaixo
st = 'Create a list of the first letters of every word in this string'
palavras = st.split()
[palavra[0] for palavra in palavras]