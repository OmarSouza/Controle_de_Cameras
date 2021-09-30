import sqlite3

conexao = sqlite3.connect("estoque_cameras.db")
cursor = conexao.cursor()

retorno = 1

while(retorno == 1):
    retorno = 0

    print("-- Bem vindo:  --")
    print("-- 1 - Adicionar Kit:  --")
    print("-- 2 - Listar Kit:  --")
    print("-- 3 - Saida de Kit:  --")

    escolha = int(input("O que deseja fazer: "))

    if escolha == 1:
        kit_dataChegada = input("Chegada em (dd/mm/aaaa): ")
        kit_dataSaida = input("Retirado em (dd/mm/aaaa): ")
        kit_pessoa = input("Retirado por: ")
        kit_placa = input("Placa do Veiculo: ")
        kit_condicao = input("Condição do Kit: ")

        cursor.execute("""INSERT INTO cameras 
                        (dataChegada, pessoa, dataSaida, placa, condicaoKit) 
                        VALUES (?, ?, ?, ?, ?)""", (kit_dataChegada,
                                                 kit_pessoa, kit_dataSaida, kit_placa, kit_condicao))

        conexao.commit()

        print("Kit inserido com sucesso.")

        conexao.close()

        retornarMenu = input("Deseja retornar ao menu: [Y / N]")
        if retornarMenu == "Y":
            retorno = 1
            print("\n" * 10)
        else:
            print("Programa será finalizado")


    else:
        print("em Desenvolvimento")