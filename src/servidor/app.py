from concurrent import futures

import grpc
import os
import uuid
import tarefas_pb2
import tarefas_pb2_grpc


class gerenciadorDeTarefas(tarefas_pb2_grpc.gerenciadorDeTarefasServicer):

    def CriarTarefa(self, request, context):
        id_unico = str(uuid.uuid4())

        path_tarefa = os.path.join(os.path.dirname(__file__), "database", f"{id_unico}.txt")

        with open(path_tarefa, "w", encoding="utf-8") as nf:
            nf.write("Titulo: " + request.titulo + "\n")
            nf.write("Descricao: " + request.descricao + "\n")
            nf.write("Envolvidos: " + request.envolvidos + "\n")
            nf.write("ID da Tarefa: " + id_unico + "\n")

        reply = tarefas_pb2.CriarReply()
        reply.id = id_unico
        reply.titulo = request.titulo
        reply.descricao = request.descricao
        reply.envolvidos = request.envolvidos

        return reply


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
