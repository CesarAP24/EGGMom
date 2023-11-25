#credenciales de aws
texto = """
aws_access_key_id=ASIA4QHKXAS7V2QXSKXN
aws_secret_access_key=Y507NkuxO+CGuUGWu60bKdrspmzwYT4wu7VGx/Bq
aws_session_token=FwoGZXIvYXdzEDYaDEm1uh3Fq+WI2liHXiLKAZqOK+rUlriDeQx1rpGS2/3BME4Es8I41n1glqnD4htCVSvDODDlAsWj7/OSC2j3LG3UoO1SpEhx3KA80W0PaWpGhosgrMZSD8EQkst1xB+4sUsZog94hqGhbh18Fp3dXtBouTHjgx/GXf/KlZ7OVUETDWROqFGX6JSUzLavauQlxVcpAKjYHlD7TwjxqlyIp4I1o/9mUgEzeA8YpcsZozEyV48fW010dGVvuhmdGBnY+U2x60i4yHEk3ZYvgNRyPtWF8JGQLvUDSyco9L6JqwYyLY4ybLarymI+3ZJmvSVBTl2GS2C3mTgZEGzNH3mBEPlnU2npRfqsdVbrSfpmPw==
"""

texto = texto.split('\n')
texto = {line.split('=')[0]: line.split('=')[1] for line in texto if line}
config = texto