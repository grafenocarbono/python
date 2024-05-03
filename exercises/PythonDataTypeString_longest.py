#8. Write a Python function that takes a list of words 
#and return the longest word and the length of the longest one. 
#Sample Output:
#Longest word: Exercises
# Length of the longest word: 9

def longest_word(lista_palabras):
    primera = True
    for palabra in lista_palabras:
        if (primera):
            word = palabra
            length = len(palabra)
            primera = False
        else:
            if (len(palabra) > length):
                word = palabra
                length = len(palabra)
    resultado = []
    resultado.append(word)
    resultado.append(length)
    return resultado




lista_palabras = ["Google","Microsoft", "Oracle", "Apache",
                        "Linux","Apple"]

resultado = longest_word(lista_palabras)

txt = "The longest word is {} y su longitud es {}"
print(txt.format(resultado[0], resultado[1]))
