from concurrent import futures

import grpc
import tarefas_pb2
import tarefas_pb2_grpc


class gerenciadorDeTarefas(tarefas_pb2_grpc.gerenciadorDeTarefasServicer):

    def ListarTarefas(self, request, context):
        return tarefas_pb2.ListarReply(tarefas=[
            tarefas_pb2.Tarefa(
                id='1', 
                titulo="CriarTeste", 
                descricao="Testar o sistema", 
                envolvidos="Eu")
            ])


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tarefas_pb2_grpc.add_gerenciadorDeTarefasServicer_to_server(gerenciadorDeTarefas(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
