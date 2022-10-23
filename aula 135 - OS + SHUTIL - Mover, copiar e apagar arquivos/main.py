
import os
import shutil

caminho_original = r'D:\Fotos_test'
caminho_novo = r'D:\Fotos_test2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in