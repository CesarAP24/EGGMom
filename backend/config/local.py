#credenciales de aws
texto = """
aws_access_key_id=ASIA4QHKXAS72BJBKCEI
aws_secret_access_key=lRl2wl7jyzQgODyhnNvxlAvUaxWTZvIIFwg9+b0J
aws_session_token=FwoGZXIvYXdzEDsaDOSjsYGdUvdpzb+ruyLKAZSxP9pQi8aqUt8961geS6jEX1uahr1aUq3wYLPM/e6UOPVb19DVqd3/f1LU2XuVXSgAvPDWiE5zXq3DknbSjfiwkWhvWMFPV2gMXcaNQv0pfqCI+yk4I873NB2xD/T54xPARHpfFf6D5cU6nhMbZ7AsSmhMyHILsPHN+5qN1uZ1KVISLb65qtqxDMPuV+cEY7BHGB4aaujw5rKjLb1o/co4eaEJtsH1sROZD5jeId127699o0vO9oWGgZaom7gMfEqD7xAtPpktjZ4oubOKqwYyLaMwDOyJhk0TX6dBeY13LeWgTyHG2HzR9VI+02iWRDGOPgLzxQoyprPnqm2h2w==
"""

texto = texto.split('\n')
texto = {line.split('=')[0]: line.split('=')[1] for line in texto if line}
config = texto