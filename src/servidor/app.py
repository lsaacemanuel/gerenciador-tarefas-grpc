from concurrent import futures

import grpc
import os
import uuid
import tarefas_pb2
import tarefas_pb2_grpc


class gerenciadorDeTarefas(tarefas_pb2_grpc.gerenciadorDeTarefasServicer):

    def CriarTarefa(self, request, context):
        #gerando um id aleatorio
        id_unico = str(uuid.uuid4())
        #condensando o caminho do arquivo para ser aberto e modificado posteriormente
        path_tarefa = os.path.join(os.path.dirname(__file__), "database", f"{id_unico}.txt")
        #criando, abrindo o arquivo e escrevendo dados
        with open(path_tarefa, "w", encoding="utf-8") as nf:
            nf.write("Titulo: " + request.titulo + "\n")
            nf.write("Descricao: " + request.descricao + "\n")
            nf.write("Envolvidos: " + request.envolvidos + "\n")
            nf.write("ID da Tarefa: " + id_unico + "\n")

        #criando a reply de retorno
        reply = tarefas_pb2.CriarReply()
        reply.id = id_unico
        reply.titulo = request.titulo
        reply.descricao = request.descricao
        reply.envolvidos = request.envolvidos

        return reply

    def AtualizarTarefa(self, request, context):
        id_tarefa = request.id
        #condensando o caminho do arquivo para ser aberto e modificado posteriormente
        path_tarefa = os.path.join(os.path.dirname(__file__), "database", f"{id_tarefa}.txt")
        #abrindo o arquivo para atualizar os dados
        with open(path_tarefa, "w+", encoding="utf-8") as nf:
            nf.write("Titulo: " + request.titulo + "\n")
            nf.write("Descricao: " + request.descricao + "\n")
            nf.write("Envolvidos: " + request.envolvidos + "\n")
            nf.write("ID da Tarefa: " + id_tarefa + "\n")
        #montando a reply de retorno
        reply = tarefas_pb2.AtualizarReply()
        reply.titulo = request.titulo
        reply.descricao = request.descricao
        reply.envolvidos = request.envolvidos
                    
        return reply

    def DeletarTarefa(self, request, context):
        id_tarefa = request.id
        
        path_tarefa = os.path.join(os.path.dirname(__file__), "database", f"{id_tarefa}.txt")
        #apagando o arquivo do sistema
        os.remove(path_tarefa)

        reply = tarefas_pb2.DeletarReply()
        reply.deletado = "1"

        return reply
            
    def ListarTarefas(self, request, context):

        path_tarefa = os.path.join(os.path.dirname(__file__), "database")

        reply = tarefas_pb2.ListarReply()

        #pegando o caminho de cada arquivo do database
        for f in os.listdir(path_tarefa):
            #montando o caminho final de cada tarefa
            caminho = os.path.join(path_tarefa, f)

            try:
                #abrindo para leitura a tarefa
                with open(caminho, "r", encoding="utf-8") as f:
                    #tirando a quebra de linha e organizando em uma array cada linha do arquivo
                    conteudo = [linha.strip() for linha in f.readlines()]
                #montando cada campo da tarefa na reply
                dados = reply.tarefas.add()
                dados.titulo = conteudo[0]
                dados.descricao = conteudo[1]
                dados.envolvidos = conteudo[2]
                dados.id = conteudo[3]
            except Exception as e:
                print(f"Erro ao ler arquivo: {e}")
        return reply

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
