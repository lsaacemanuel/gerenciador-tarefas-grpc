from __future__ import print_function

import grpc
import tarefas_pb2
import tarefas_pb2_grpc

def testar_criar_tarefa():

    channel = grpc.insecure_channel('localhost:50051')
    stub = tarefas_pb2_grpc.gerenciadorDeTarefasStub(channel)

    requisicao = tarefas_pb2.CriarRequest(
        titulo="Estudar Protocol Buffers",
        descricao="criando um .proto",
        envolvidos="Isaac, Massena, Andressa, Gabrielle"
    )

    print("Enviando requisição de criação...")
    resposta = stub.CriarTarefa(requisicao)

    print("Resposta Recebida do Servidor ->")
    print("ID Gerado: " + resposta.id)
    print("Título: " + resposta.titulo)
    print("Descrição: " + resposta.descricao)
    print("Envolvidos: " + resposta.envolvidos)

if __name__ == '__main__':
    testar_criar_tarefa()

def run():
    response = None
    print("Tentando conectar ao servidor gRPC...")

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = tarefas_pb2_grpc.gerenciadorDeTarefasStub(channel)
        response = stub.ListarTarefas(tarefas_pb2.ListarRequest())

    print("O sistema identificou as tarefas:\n"  + str(response.tarefas))


if __name__ == "__main__":
    run()
