from __future__ import print_function

import grpc
import tarefas_pb2
import tarefas_pb2_grpc


def run():
    response = None
    print("Tentando conectar ao servidor gRPC...")

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = tarefas_pb2_grpc.gerenciadorDeTarefasStub(channel)
        response = stub.ListarTarefas(tarefas_pb2.ListarRequest())

    print("O sistema identificou as tarefas:\n"  + str(response.tarefas))


if __name__ == "__main__":
    run()
