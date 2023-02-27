import shutil
import os
import re
import subprocess
import hashlib

def obter_md5_arquivo_crt(path_arquivo):
    result = subprocess.run(['openssl', 'x509', '-noout', '-modulus', '-in', path_arquivo],
                            check=True, stdout=subprocess.PIPE, universal_newlines=True)
    modulo = (result.stdout.split('=')[-1]).strip()
    hash_object = hashlib.md5(modulo.encode())
    md5_hash = hash_object.hexdigest()
    return md5_hash

def obter_md5_arquivo_key(path_arquivo):
    result = subprocess.run(['openssl', 'rsa', '-noout', '-modulus', '-in', path_arquivo],
                            check=True, stdout=subprocess.PIPE, universal_newlines=True)
    modulo = (result.stdout.split('=')[-1]).strip()
    hash_object = hashlib.md5(modulo.encode())
    md5_hash = hash_object.hexdigest()
    return md5_hash

##############################################################################

src_dir = "2019"
crt_dir = "certificados_crt"
key_dir = "certificados_key"

regex_crt = re.compile(r'(.*crt$)')
regex_key = re.compile(r'(.*key$)')




for root, dirs, files in os.walk(src_dir):
    for file in files:
        if (regex_crt.match(file)):
            path_completo_crt = os.path.join(root, file)
            shutil.copy(path_completo_crt, crt_dir)

        if (regex_key.match(file)):
            path_completo_key = os.path.join(root, file)
            shutil.copy(path_completo_key, key_dir)

############################################################################

lista = []

for root, dirs, files in os.walk(crt_dir):
    lista_crt = []
    lista_crt_hash = []
    for file in files:
        lista_crt.append(file)
        path_crt = os.path.join(root, file)
        hash_crt = obter_md5_arquivo_crt(path_crt)
        lista_crt_hash.append(hash_crt)
    lista.append(lista_crt)
    lista.append(lista_crt_hash)

for root, dirs, files in os.walk(key_dir):
    lista_key = []
    lista_key_hash = []
    for file in files:
        lista_key.append(file)
        path_key = os.path.join(root, file)
        hash_key = obter_md5_arquivo_key(path_key)
        lista_key_hash.append(hash_key)
    lista.append(lista_key)
    lista.append(lista_key_hash)

###############################################################################

lista_organizada = []
lista_crt_a = []
lista_key_a = []

for i in lista[1]:
    for j in lista[3]:
        if j == i:
            cordenada_j = lista[3].index(j)
            cordenada_i = lista[1].index(i)
            if cordenada_j >= len(lista[1]):
                break
            lista_crt_a.append(lista[0][cordenada_j])
            lista_key_a.append(lista[2][cordenada_i])

lista_organizada.append(lista_crt_a)
lista_organizada.append(lista_key_a)

print(lista_organizada)













