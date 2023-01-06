import hashlib
import base64

def codificar_senha(senha):
    senha_encoded = senha.encode('utf-8')
    digest = hashlib.sha512(senha_encoded).digest()
    digest_b64_encoded = base64.b64encode(digest)
    digest_b64_encoded_utf8_decoded = digest_b64_encoded.decode('utf-8')
    return digest_b64_encoded_utf8_decoded

def combinacao(lista):
    result = []
    for i in lista:
        result.append(i)
        for j in lista:
            result.append(f'{i} {j}')
            for x in lista:
                result.append(f'{i} {j} {x}')
                for y in lista:
                    result.append(f'{i} {j} {x} {y}')
                    for z in lista:
                        result.append(f'{i} {j} {x} {y} {z}')
    return result

def ordenar_quebradas(lista):
    for elemento in range(len(lista)-1):
        for i in range(len(lista) - elemento - 1):
            if len(lista[i].split(':')[1])>len(lista[i+1].split(':')[1]):
                lista[i], lista[i+1] = lista[i+1], lista[i]
            elif len(lista[i].split(':')[1]) == len(lista[i+1].split(':')[1]) and lista[i].split(':')[1] > lista[i+1].split(':')[1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]

def ordenar_nao_quebradas(lista):
    for elemento in range(len(lista)-1):
        for i in range(len(lista) - elemento - 1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]

palavras = []
usuarios = []
senhas_codificadas = []

senhas_achadas = []
usuarios_achados = []

with open('usuarios_senhascodificadas.txt', 'r') as f:
    for line in f:
        usuario, senhacodificada = line.rstrip().split(':')
        usuarios.append(usuario)
        senhas_codificadas.append(senhacodificada)

with open('palavras.txt', 'r') as f:
    for line in f:
        palavras.append(line.rstrip())

combinacoes = combinacao(palavras)
for i in combinacoes:
    for index in range(len(senhas_codificadas)):
        if codificar_senha(i) == senhas_codificadas[index]:
            senhas_achadas.append(i)
            usuarios_achados.append(index)

senhas_quebradas = []
for i in range(len(usuarios_achados)):
    senhas_quebradas.append(f"{usuarios[usuarios_achados[i]]}:{senhas_achadas[i]}\n")

ordenar_quebradas(senhas_quebradas)

with open('senhas_quebradas.txt', 'w') as f:
    f.writelines(senhas_quebradas)


senhas_nao_quebradas = []
for i in range(len(usuarios)):
    if i not in usuarios_achados:
        senhas_nao_quebradas.append(f'{usuarios[i]}:{senhas_codificadas[i]}\n')

ordenar_nao_quebradas(senhas_nao_quebradas)

with open('senhas_nao_quebradas.txt', 'w') as f:
    f.writelines(senhas_nao_quebradas)
