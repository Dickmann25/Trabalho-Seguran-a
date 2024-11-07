#shift = deslocamento da cifra
#text = texto que deverá ser codificado
#retorna o texto codificado
def caesar_cipher(text, shift):
    result = ""

    for char in text:

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        else:
            result += char

    return result


#text = texto já codificado
#retorna um dicionário com todas as possibilidades de decodificação e seus deslocamentos
def caesar_decipher(text):
    result = {}

    for count in range(26):  
        temp = ""
        for char in text:
                
            if char.isupper():
                temp += chr((ord(char) - count - 65) % 26 + 65)

            elif char.islower():
                temp += chr((ord(char) - count - 97) % 26 + 97)

            else:
                temp += char
 
        result[temp] = count   
    return result

#código exemplo
texto = "Hello, World!"
deslocamento = 3
texto_cifrado = caesar_cipher(texto, deslocamento)
print(texto_cifrado)
texto_decifrado = caesar_decipher(texto_cifrado)
print(texto_decifrado)
