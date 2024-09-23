palabra = 'Python es genial'

for letra in palabra:
    letrauno = palabra.index(letra)+1
    print(f"{letrauno} + {letra}")