print("        LABORATÓRIO DE CRIAÇÃO        ")
print("              PRINCESS.EXE")

print("\nEscolha as características da personagem:")

cabelo = input("Cabelo (castanho/longo): ").lower()
roupa = input("Roupa (amarela/roxa): ").lower()
personalidade = input("Personalidade (gentil/alegre): ").lower()
acessorio = input("Acessório (rosa/flor): ").lower()

print("PROCESSANDO CRIAÇÃO...")

if (cabelo == "castanho" and
        roupa == "amarela" and
        personalidade == "gentil" and
        acessorio == "rosa"):

    print("\nBELA FOI CRIADA COM SUCESSO!")

elif (cabelo == "longo" and
      roupa == "roxa" and
      personalidade == "alegre" and
      acessorio == "flor"):

    print("\nRAPUNZEL FOI CRIADA COM SUCESSO!")

else:

    print("\nCOMBINAÇÃO NÃO CORRESPONDE À NENHUMA PRINCESA!")
    print("\nProcessando resultado inesperado...")
    print("\nMALÉVOLA FOI CRIADA!")