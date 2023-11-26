#credenciales de aws
texto = """
aws_access_key_id=ASIA4QHKXAS7YXFCINHC
aws_secret_access_key=MU5IUDnGbgOmmXfO8jn/grhoWjaheEotppEmv2Wc
aws_session_token=FwoGZXIvYXdzED8aDJKBivNjQ3t5fgGjXCLKAWRN8ommaUFCNEnS6aOp0p8sAdKkTGXlvHS8VsfpF6yL9ywBTpD8uSLqCG71WV8s5eddPu5Zn3fo7Y7IzFEuotlEnU3PBZ7Ok5morzqvBtX50hIlWD1hMvyNwo6AecJnjzFw6khPAkOQETwweDzRCeuzl2iIITxLu5Qs1O9h6CoVanliZqYcLbx4oN/jiBE1JjC3hw/VQ4gTykLTxfZTRmmQu31Da3M72H0fjWV/4GhYOvqabVH1Qmpsw1n/GdYoPmBlvOHOjV4mv3wo8qeLqwYyLUtJPt0KZ6kt8uWy+Hqtiny4ELV7uoEJ+kh1PXv8tuq/y9K5axHlO0juN8k0ww==
"""

texto = texto.split('\n')
texto = {line.split('=')[0]: line.split('=')[1] for line in texto if line}
config = texto