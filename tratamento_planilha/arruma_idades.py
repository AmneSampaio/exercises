entrada_do_usuario = input("Por favor entre com o nome do arquivo csv: ")


with open(entrada_do_usuario + ".csv", 'r') as arquivoliz:
    linhas = arquivoliz.readlines()

arquivo_saida = entrada_do_usuario + "_idade_obito.csv"
print(arquivo_saida)

with open(arquivo_saida, 'w') as arquivo_final:
    arquivo_final.write("{} \n".format("idade_obito"))

    for linha in linhas[1:]:

        recorta_delimitador = linha.split(';')
        # print(recorta_delimitador)
        idade_obito = int(recorta_delimitador[7])

        if (idade_obito != 999):

            if (idade_obito > 400 ):
                idade_obito = idade_obito - 400
            else:
                idade_obito = 0

            arquivo_final.write(str(idade_obito) + "\n")





