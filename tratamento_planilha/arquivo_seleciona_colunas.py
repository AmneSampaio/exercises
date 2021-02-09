
entrada_do_usuario = input("Por favor entre com o nome do arquivo csv: ")


with open(entrada_do_usuario + ".csv", 'r') as arquivoliz:
    linhas = arquivoliz.readlines()

arquivo_saida = entrada_do_usuario + "_seleciona_colunas.csv"
print(arquivo_saida)

with open(arquivo_saida, 'w') as arquivo_final:
    arquivo_final.write("{};{};{};{};{};{} \n".format("mes", "dia", "idade_obito",
                                                      "sexo", "codigo_municipio_regiao_metropolitana",
                                                      "causa_basica"))
    for linha in linhas[1:]:
        recorta_delimitador = linha.split(';')
        mes = recorta_delimitador[4]
        dia = recorta_delimitador[5]
        idade_obito = recorta_delimitador[6]
        sexo = (recorta_delimitador[7])
        codigo_municipio_regiao_metropolitana = recorta_delimitador[12]
        causa_basica = recorta_delimitador[17]
        arquivo_final.write("{};{};{};{};{};{} \n".format(mes, dia, idade_obito,
                                                                  sexo, codigo_municipio_regiao_metropolitana,
                                                                  causa_basica))



