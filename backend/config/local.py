#credenciales de aws
texto = """
aws_access_key_id=ASIA4QHKXAS7TAGZ7BAT
aws_secret_access_key=VKncJmHdnJ5NlfslvHrZpqk4eajMly1/1RetEODc
aws_session_token=FwoGZXIvYXdzEDIaDCytbHlcNntOL0KPOSLKAbcvnFXzml20Z0O+hOjMaTdtwFXrCaXBpWNYW9XarxlibWoutzSzQo8DYH0osuadACnVWT2E+njPJhiicZ7FKk0LGcRwccYtuQZs1PWO3QCB2XRL41erjU7+tFKIbFxhBKkkGN/paMBxZgnFMltAucuzT3T9PEJdqpeehJF3vQmrJt+WNQTuGnPMM4ehPlqSCMDMDiTKcs1PE6ctcstlALLorHMID3punilN3wy000sA2kkH8bOizWZc5aicga+/GqYWgg5tRjR8BkAos82IqwYyLWlb93p0OU5mNCbMmAGZSDiNwSTyfNhuwgJBqJ/4x5xL8YAcyBcArjQv84suQQ==
"""

texto = texto.split('\n')
texto = {line.split('=')[0]: line.split('=')[1] for line in texto if line}
config = texto