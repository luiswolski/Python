import subprocess

proc = subprocess.run(
    ['ping', '8.8.8.8'],
    capture_output=True,
    text=True
)

saida = proc.stdout
saida = saida.replace('bytes', 'NUMERO DE BYTES ENVIADOS')
print(saida)