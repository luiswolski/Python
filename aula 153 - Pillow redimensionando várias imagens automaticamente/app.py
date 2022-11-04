import os
from PIL import Image


def main(main_images_folder, new_width=800):
    if not os.path.isdir(main_images_folder):
        raise NotADirectoryError(f'{main_images_folder} não existe!')

    # USANDO OS PARA DEFINIR O CAMINHO DAS IMAGENS

    for root, dirs, files in os.walk(main_images_folder):
        for file in files:
            file_full_path = os.path.join(root, file)
            file_name, extension = os.path.splitext(file)

            # RENOMEANDO AS IMAGENS COMO _CONVERTED, E UTILIZADO O MESMO CAMINHO PARA SALVAR
            converted_tag = '_CONVERTED'

            new_file = file_name + converted_tag + extension
            new_file_full_path = os.path.join(root, new_file)

            """
            # CASO VOCÊ QUEIRA REMOVER AS IMAGENS        
             if converted_tag in file_full_path:
                            os.remove(file_full_path)
            """

            if os.path.isfile(new_file_full_path):
                print(f'Arquivo {new_file_full_path} já existe!')
                continue

            # CHECANDO SE A IMAGEN JÁ FOI CONVERTIDA
            if converted_tag in file_full_path:
                continue

            # UTILIZANDO OS VALORES DE TAMANHO PARA DEFINIR OS NOVOS TAMANHOS DE IMAGEM
            img_pillow = Image.open(file_full_path)
            width, height = img_pillow.size
            new_height = round(new_width * height / width)

            # AGORA DE FATO SERÁ FEITO O REDIMENSIONAMENTO
            new_image = img_pillow.resize((new_width, new_height),
                                          Image.LANCZOS
                                          )

            new_image.save(
                new_file_full_path,
                optmize=True,
                quality=60,
                exif=img_pillow.info['exif']  # MANTÉM OS DADOS DAS FOTOS NAS CÓPIAS
            )

            print(f'{file_full_path} convertido com sucesso!')
            new_image.close()
            img_pillow.close()


if __name__ == '__main__':
    main_images_folder = r'D:\Fotos_test'
    main(main_images_folder, new_width=640)
