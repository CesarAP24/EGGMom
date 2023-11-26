#credenciales de aws
import requests
import os

#credenciales de aws
url = 'https://eggmom.s3.amazonaws.com/credentials.txt'
r = requests.get(url)
texto = r.text

texto = texto.split('\n')
texto = {line.split('=')[0]: line.split('=')[1] for line in texto if line}
config = texto