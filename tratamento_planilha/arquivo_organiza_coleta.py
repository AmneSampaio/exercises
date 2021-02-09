entrada_do_usuario = input("Por favor entre com o nome do arquivo csv: ")


with open(entrada_do_usuario + ".csv", 'r') as arquivoliz:
    linhas = arquivoliz.readlines()

arquivo_saida = entrada_do_usuario + "_seleciona_colunas.csv"
print(arquivo_saida)

with open(arquivo_saida, 'w') as arquivo_final:
    #arquivo_final.write("{};{};{};{};{};{} \n".format("mes", "dia", "idade_obito",
                                                      ##"sexo", "codigo_municipio_regiao_metropolitana",
                                                      ##"causa_basica"))
    arquivo_final.write("{};{};{};{} \n".format("idade_obito",
                                                      "sexo", "codigo_municipio_regiao_metropolitana",
                                                      "causa_basica"))

    for linha in linhas[1:]:
        recorta_delimitador = linha.split(';')
        #mes = recorta_delimitador[4]
        #dia = recorta_delimitador[5]
        idade_obito = recorta_delimitador[7]
        sexo = (recorta_delimitador[8])
        codigo_municipio_regiao_metropolitana = recorta_delimitador[15]
        causa_basica = recorta_delimitador[45]
        ##arquivo_final.write("{};{};{};{};{};{} \n".format(mes, dia, idade_obito,
                                                                  ##sexo, codigo_municipio_regiao_metropolitana,
                                                                  ##causa_basica))
        arquivo_final.write("{};{};{};{} \n".format(idade_obito,
                                                          sexo, codigo_municipio_regiao_metropolitana,
                                                          causa_basica))

#entrada_do_usuario = input("Por favor entre com o nome do arquivo csv: ")


codigo_municipio_selecionado = ["290570", "290650", "291005", "291610", "291920", "291992", "292100", "292520",
                                "292740", "292920", "292950", "293070", "293320"]


with open(arquivo_saida, 'r') as arquivoliz:
    linhas = arquivoliz.readlines()

valid_lines = []

arquivo_saida = arquivo_saida[:36] + "_filtrado.csv"
print(arquivo_saida)


lista_de_letras_validas = []

for letra in range(ord("a"), ord("s")):
    lista_de_letras_validas.append(chr(letra))

def checa_causa_de_morte(causa_basica):
    if causa_basica[0].lower() in lista_de_letras_validas:
        return True
    else:
        return False

with open(arquivo_saida, 'w') as arquivo_final:
    #arquivo_final.write("{};{};{};{};{};{} \n".format("mes", "dia",
                                                      #"idade_obito","sexo", "codigo_municipio_regiao_metropolitana",
                                                      #"causa_basica"))
    arquivo_final.write("{};{};{};{} \n".format("idade_obito","sexo", "codigo_municipio_regiao_metropolitana",
                         "causa_basica"))


    for linha in linhas[1:]:
        recorta_delimitador = linha.split(';')
        codigo_municipio_regiao_metropolitana = recorta_delimitador[2]
        causa_basica = recorta_delimitador[3]
        idade_obito = recorta_delimitador[0]
        sexo = recorta_delimitador[1]
        if (codigo_municipio_regiao_metropolitana in codigo_municipio_selecionado and
                checa_causa_de_morte(causa_basica) and
                idade_obito != "" and
                sexo != "0"):

            idade_obito = int(idade_obito)

            if (idade_obito != 999):

                if (idade_obito > 400):
                    idade_obito = idade_obito - 400

                else:
                    idade_obito = 0

                recorta_delimitador[0] = idade_obito
                valid_lines.append(recorta_delimitador.join(";"))

    arquivo_final.writelines(valid_lines)

print(valid_lines)