import numpy as np
import random

"""
A mensagem que sera envia é estruturada em uma matriz (A).Posteriormente, utilizo uma outra matriz (B) como chave 
para encriptar a mensagem que desejo enviar,de modo que o resultado da multiplicação das matrizes (A) e (B) é a 
mensagem encriptada.Quando o destinatário receber a matriz (C), produto de (A) por (B) ele deve utilizar a matriz 
inversa de (B) para desencriptar a mensagem.

Obs: Para a construção e manipulação das matrizes utiliza-se a biblioteca (numpy) e (random)
"""

"""
Trabalho que criptografia utilizando algebra linear (Matrizes)

"""
######################################################################################################################
                                        #  TEXTO PARA SER ENCRIPTADO
######################################################################################################################


sec = 'É importante que as pessoas tenham consciência dos males da destruição da natureza e criem hábitos que ' \
      'ajudem na preservação do meio ambiente, pois com pequenas atitudes teremos grandes conquistas, uma das mais ' \
      'importantes é a reciclagem do lixo. "A maior arma contra destruição das Matas e do Meio Ambiente em geral, é ' \
      'a conscientização pessoal,que unida coletividade, resultará em benefícios que se sentirá no lar de cada um, ' \
      'e atingirá o Planeta Terra que tanto clama por socorro!"'.strip()

print(f"Tamanho do texto: {len(sec)} caracteres.")
print()
######################################################################################################################
                                        # ENCRIPTANDO O TEXTO
######################################################################################################################

#  Coloca a Mensagem (secreta) em uma lista de caracteres inteiros
message_ascii = []
for index in range(len(sec)):
    message_ascii.append(ord(sec[index]))
print(f"lista de caracteres inteiros : \n{message_ascii}")
print()


# Coloca a Mensagem (secreta/lista) em uma Matriz de caracteres inteiros
message_ascii = np.matrix(message_ascii)
print(f"Matriz de caracteres inteiros: \n{message_ascii}")
print()

# A Matriz (22 x 22)
message_ascii = message_ascii.reshape(22, 22)
print(f"A Matriz (22 x 22): \n{message_ascii}")
print()


# Gerando nossa Key
key = np.random.randint(10, size=(22, 22))
print(f"A Chave: \n{key}")
print()

# Encriptando a mensagem
encrypted_message = np.dot(key, message_ascii)
print(f"Encriptando a mensagem: \n{encrypted_message}")
print()

# Inversa da Chave
inv_key = np.linalg.inv(key)
print(f"Inversa da chave: \n{inv_key}")

######################################################################################################################
                                    # DESENCRIPTANDO O TEXTO
######################################################################################################################
print("-=-"*40)
print("-----------------------DESENCRIPTANDO O TEXTO---------------------------")
print("-=-"*40)

# Multiplicação da Inversa pela mensagem cifrada:

decrypted_message = np.dot(inv_key, encrypted_message)
print(f"Multiplicação da Inversa pela mensagem cifrada: \n{decrypted_message}")
print()

message_ascii = message_ascii.reshape((1, 484))

mensagem = []

for index in range(484):
    mensagem.append(str(chr(int(message_ascii[0, index]))))
print(f"A mensagem: \n{mensagem}")

message_ascii = ""
for index in range(len(mensagem)):
    message_ascii += mensagem[index]
print(f"\033[1;32;0mNosso texto desifrado: \n{message_ascii}")
