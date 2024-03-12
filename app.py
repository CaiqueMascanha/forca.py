from forca import Forca

forca = Forca()

while forca.tentativas > 0:
    print(forca.tentativas)
    print(forca.digitadas)
    print(forca.palavra)
    forca.play()
