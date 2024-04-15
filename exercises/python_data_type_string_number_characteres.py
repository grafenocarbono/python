## =========================================================================================

# Write a Python program to count the number of characters (character frequency) in a string. 

# Sample String : google.com'

# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

# @grafenocarbono

## =========================================================================================



# Function that given a character and a list of characters returns the position
# where the character is found.
# But if the character is not found on the list the position -1 will be returned
def busca_posicion(letra, lista):
    posicion = 0
    for x in lista:
        if x == letra:
            # Element found. The function is finished by returning the value
            # of the position
            return posicion
        else:
            # In this position the element is not. It is still looking for
            posicion = posicion + 1
    posicion = -1
    return posicion

# Here begins the main part of the program

texto = input("Introduzca una palabra: ");
letras = []
frecuencia = []


#It runs through character by character
for x in texto:
    # A logic variable is used to detect if the character exists in the string
    exists = x in letras
    
    # If it doesn't exist it is recorded as the first ocurrence
    if (not exists):
        letras.append(x)
        frecuencia.append(1)
    # The element already exists in the table. The number of ocurrences is updated
    else:
        posicion = busca_posicion(x, letras)
        if (posicion != -1):
            frecuencia[posicion] = frecuencia[posicion] + 1
            
for i in range (0, len(letras)):
    print(letras[i]," - ", frecuencia[i])