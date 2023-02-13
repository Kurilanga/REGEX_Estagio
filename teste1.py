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

src_dir = "2019"
dest_dir = "certificados_crt"

regex_crt = re.compile(r'(.*crt$)')
regex_key = re.compile(r'(.*key$)')
#Queria saber tambem porque nao esta funcionando esta parte, se eu mando printar os arquivos ele me mostra todos os .crt e os .key certinho
# mas quando tento move-los para pasta "certificados" ele da alguns erros.
for root, dirs, files in os.walk(src_dir):
    for file in files:
        if (regex_crt.match(file)):
            print(file)
            shutil.copy(file, dest_dir)









