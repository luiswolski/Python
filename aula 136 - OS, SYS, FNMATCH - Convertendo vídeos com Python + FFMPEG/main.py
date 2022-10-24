# https://ffmpeg.org/documentation.html

import os
import fnmatch
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:20'

caminho_origem = r'D:\Fotos_test\filme1'
caminho_destino = r'D:\Fotos_test2\filme2'

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*mkv'):
            continue

        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
        caminho_legenda = nome_arquivo + '.srt'

        if os.path.isfile(caminho_legenda):
            input_legenda = f'-i "{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_legenda = ''
            map_legenda = ''

        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

        arquivo_saida = f'{caminho_destino}/{nome_arquivo}_NOVO.mp4'


        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda}' \
                  f' {codec_video} {crf} {preset} {codec_audio} {bitrate_audio}' \
                  f' {debug} {map_legenda} "{arquivo_saida}"'

        os.system(comando)
