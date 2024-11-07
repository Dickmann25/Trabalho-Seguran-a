from itertools import permutations
import re

#mensagem = texto que deverá ser codificado
#chave = chave
#retorna o texto codificado
def cifra_transposicao(mensagem, chave):
    # Remover espaços da mensagem
    mensagem = mensagem.replace(" ", "")
    
    # Determinar o número de colunas a partir do comprimento da chave
    num_colunas = len(chave)
    
    # Calcular o número de linhas necessárias
    num_linhas = len(mensagem) // num_colunas
    if len(mensagem) % num_colunas != 0:
        num_linhas += 1
    
    # Preencher a matriz de acordo com as colunas definidas pela chave
    matriz = []
    index = 0
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            if index < len(mensagem):
                linha.append(mensagem[index])
            else:
                linha.append('')  # Preencher células vazias
            index += 1
        matriz.append(linha)
    
    # Ordenar as colunas de acordo com a chave de permutação
    matriz_permutada = [''.join(linha[chave.index(j)] for linha in matriz)  for j in range(num_colunas)]
    
    # Concatenar as colunas permutadas para formar a mensagem cifrada
    mensagem_cifrada = ''.join(matriz_permutada)
    
    return mensagem_cifrada

# Exemplo de uso
mensagem = "ilovemywife"
chave = [6,3,4,0,1,7,2,5]  # Ordem de permutação das colunas
print("Mensagem original:", mensagem)
print("Mensagem cifrada:", cifra_transposicao(mensagem, chave))


#ciphertext = texto codificado
#max_key_length = tamanho maximo de chave para os testes
#resposta = texto descodificado, obviamente em uma situação normal nós não teriamos a resposta disponivel, mas para provar que a função consegue achar a resposta será necessário o texto original
def decipher_transposition(ciphertext, max_key_length,resposta):
    # Remover espaços e caracteres especiais do ciphertext para facilitar a análise
    cleaned_ciphertext = re.sub(r'\W+', '', ciphertext)

    # Tentar todas as possibilidades de chave até o comprimento máximo
    for key_length in range(2, max_key_length + 1):
        # Dividir o texto em colunas para o comprimento da chave atual
        columns = [cleaned_ciphertext[i::key_length] for i in (range(key_length))]
        
        # Gerar todas as permutações possíveis das colunas
        for permuted_columns in permutations(columns):
            # Juntar as colunas na ordem dada pela permutação
            possible_plaintext = ''.join(''.join(pair) for pair in zip(*permuted_columns))

            # Checa as possibilidades provaveis, para quando acha o texto decodificado
            if resposta == possible_plaintext:
                print("Foi encontrado uma permutação correta")
                break
            # Para facilitar a compreensão da função essa porção foi comentada
            """if is_plausible_text(possible_plaintext):
                print(f"Combinação promissora encontrada: {possible_plaintext}")"""


#Essa função serve para fazer uma análise manual das possiveis decodificações
#Ela retorna qualquer string que contem as palavras especificadas
def is_plausible_text(text):
    # Simples heurística para verificar se o texto faz sentido
    # Adicione validações baseadas no idioma do texto
    common_words = ["the", "and", "of", "to", "a", "in","my"] 
    for word in common_words:
        if word in text.lower():
            return True
            
    return False

# Texto cifrado para testar (exemplo)
ciphertext = "oivfeeiylwm"
max_key_length = 11  # Tentar chaves de até 10 colunas
decipher_transposition(ciphertext, max_key_length, "ilovemywife")