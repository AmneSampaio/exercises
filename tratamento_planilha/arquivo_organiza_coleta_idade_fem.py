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
        mes = recorta_delimitador[0]
        dia = recorta_delimitador[1]
        idade_obito = recorta_delimitador[2]
        sexo = (recorta_delimitador[3])
        codigo_municipio_regiao_metropolitana = recorta_delimitador[4]
        causa_basica = recorta_delimitador[5]
        arquivo_final.write("{};{};{};{};{};{} \n".format(mes, dia, idade_obito,
                                                                  sexo, codigo_municipio_regiao_metropolitana,
                                                                  causa_basica))

#entrada_do_usuario = input("Por favor entre com o nome do arquivo csv: ")


idade_obito_selecionado = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


with open(arquivo_saida, 'r') as arquivoliz:
    linhas = arquivoliz.readlines()

valid_lines = []

arquivo_saida = arquivo_saida[:36] + "_filtrado_idade_fem.csv"
print(arquivo_saida)


lista_de_letras_validas = []

for letra in range(ord("0"),ord("10")):
    lista_de_letras_validas.append(chr(letra))

def checa_idade_obito(idade_obito):
    if idade_obito[0].lower() in lista_de_letras_validas:
        return True
    else:
        return False

with open(arquivo_saida, 'w') as arquivo_final:
    arquivo_final.write("{};{};{};{};{};{} \n".format("mes", "dia",
                                                      "idade_obito","sexo", "codigo_municipio_regiao_metropolitana",
                                                      "causa_basica"))
    for linha in linhas[1:]:
        recorta_delimitador = linha.split(';')
        codigo_municipio_regiao_metropolitana = recorta_delimitador[4]
        causa_basica = recorta_delimitador[5]
        idade_obito = recorta_delimitador[2]
        sexo = recorta_delimitador[3]
##        if (idade_obito in idade_obito_selecionado and
##                checa_idade_obito(idade_obito):
    valid_lines.append(linha)

arquivo_final.writelines(valid_lines)

print(valid_lines)
