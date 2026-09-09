from __future__ import print_function

import grpc
import tarefas_pb2
import tarefas_pb2_grpc
import time

# aqui é a função que estabelece a conexão com o servidor gRPC
def connect():
    print("Iniciando conexao com o servidor gRPC...")
    stub = None
    #with grpc.insecure_channel("192.168.18.10:50051") as channel: # no lugar de localhost, deve ficar o ip da máquina servidora
    channel = grpc.insecure_channel('localhost:50051')
    #stub = tarefas_pb2_grpc.gerenciadorDeTarefasStub(channel)
    pronto = grpc.channel_ready_future(channel)

    # tenta estabelecer a conexão 
    try:
        pronto.result(timeout=5)
        print("Conexao estabelecida com o servidor gRPC.")
        print("\n================================")
        return channel

    # se der erro, retorna vazio e vai dar erro na main
    except grpc.FutureTimeoutError:
        print("Erro: Nao foi possivel estabelecer conexao com o servidor gRPC.")
        channel.close()
        return None

# aqui é a main
def run():
    # cria o canal
    channel = connect()

    #criação da stub, representante do servidor gRPC que contém as funções
    stub = tarefas_pb2_grpc.gerenciadorDeTarefasStub(channel)

    while True:
        print("\nEscolha uma opcao:")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Atualizar tarefa")
        print("4 - Deletar tarefa")
        print("5 - Sair")

        opcao = input("Digite o numero da opcao desejada: ")

        match opcao:
            case "1":
                titulo = input("Digite o titulo da tarefa: ")
                descricao = input("Digite a descricao da tarefa: ")
                envolvidos = input("Digite os envolvidos na tarefa: ")

                request = tarefas_pb2.Tarefa(titulo=titulo, descricao=descricao, envolvidos=envolvidos)

                try:
                    stub.CriarTarefa(request)
                    print("Tarefa adicionada com sucesso!")
                except grpc.RpcError as e:
                    print(f"Erro ao adicionar tarefa: {e}")

            case "2":
                tarefas = stub.listarTarefas(tarefas_pb2.ListaTarefasRequest())
           

            case "3":
                id = input("Digite o ID da tarefa que deseja atualizar: ")

                titulo = input("\nDigite o novo titulo da tarefa que deseja atualizar: ")
                descricao = input("Digite a nova descricao da tarefa que deseja atualizar: ")
                envolvidos = input("Digite os envolvidos da tarefa que deseja atualizar: ")

                request = tarefas_pb2.Tarefa(titulo=titulo, descricao=descricao, envolvidos=envolvidos, id=id)

                try:
                    stub.AtualizarTarefa(request)
                    print("Tarefa atualizada com sucesso!")
                except grpc.RpcError as e:
                    print(f"Erro ao atualizar tarefa: {e}")
            
            case "4":
                id = input("Digite o ID da tarefa que deseja apagar: ")

                request = tarefas_pb2.DeletarRequest(id=id)

                try:
                    print("Tarefa deletada com sucesso!")
                except grpc.RpcError as e:
                    print(f"Erro ao deletar tarefa: {e}")

            case "5":
                print("Saindo do programa...")
                channel.close()
                break

            case _:
                print("Opcao invalida. Tente novamente.")



if __name__ == "__main__":
    run()