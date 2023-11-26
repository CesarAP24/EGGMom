#credenciales de aws
texto = """
aws_access_key_id=ASIA4QHKXAS77EO4VJ6F
aws_secret_access_key=Z+rfPwZzg8mf4s/FqVSvtqIgjJT/uEoFHZyOYHmq
aws_session_token=FwoGZXIvYXdzEEYaDK+bWMka4diMWJ9eiiLKAf7B3x/eJKq67X+8CAHHT/JHgBaG4igmDi4/gaeoTvNmyxKSU415/5jjjMoJndQfi0fVP+B96WRcr1Z+rRKM3Dtlq1EI2Msyfknbuc32CsI+ig9rwXkfeB6382OIC3nocCHmgD4c6xWYt+2x3I9mChPHbL7h0aavu7H6lfcYYsmKuisWkFaE+ojXnvSLvVY00hy64auuBG82AQ7uwBEatpafPk4D9zp67hwE6BtaexEzOkXN1gWR4V547RIqfDMaStLpCn/h9otShXkowIKNqwYyLbKyQbdnM8fVgDvkYlexb6sWEo+F7dzByFuOoMzXI5SAJVeSAPkblYFRMYnbCw==
"""

texto = texto.split('\n')
texto = {line.split('=')[0]: line.split('=')[1] for line in texto if line}
config = texto