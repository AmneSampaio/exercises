dias_meses = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
meses = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dec']
tabela_final = {}

entrada_do_usuario = input("Por favor entre com o nome do arquivo csv: ")

with open(entrada_do_usuario + ".csv", 'r') as arquivoliz:
    linhas = arquivoliz.readlines()

    for linha in linhas[1:]:

        recorta_delimitador = linha.split(';')
        # print(recorta_delimitador)
        mes = int(recorta_delimitador[4])
        # print(type(mes))
        dia = recorta_delimitador[5]
        posicao = dia + "." + meses[mes - 1]

        if posicao in tabela_final:
            tabela_final[posicao] += 1
        else:
            tabela_final[posicao] = 1

arquivo_saida = entrada_do_usuario + "_saida.csv"
print(arquivo_saida)

with open(arquivo_saida, 'w') as arquivo_final:
    mes_corrente = 0
    for mes in dias_meses:
        for dia in range(1, dias_meses[mes_corrente]):
            posicao = str(dia) + "." + str(meses[mes_corrente])
            if posicao in tabela_final:
                arquivo_final.write("{};{}".format(posicao, tabela_final[posicao]))
            else:
                arquivo_final.write("{};{}".format(posicao, "0"))
            arquivo_final.write("\n")
        mes_corrente += 1
