
import os
import shutil

caminho_original = r'D:\Fotos_test'
caminho_novo = r'D:\Fotos_test2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        os.remove(new_file_path)

# Como copiar arquivos
#       shutil.copy( old_file_path, new_file_path)
#       print(f'Arquivo {file} movido com sucesso.')

