from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Tarefa(_message.Message):
    __slots__ = ("titulo", "descricao", "envolvidos", "id")
    TITULO_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    ENVOLVIDOS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    titulo: str
    descricao: str
    envolvidos: str
    id: str
    def __init__(self, titulo: _Optional[str] = ..., descricao: _Optional[str] = ..., envolvidos: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class CriarRequest(_message.Message):
    __slots__ = ("titulo", "descricao", "envolvidos")
    TITULO_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    ENVOLVIDOS_FIELD_NUMBER: _ClassVar[int]
    titulo: str
    descricao: str
    envolvidos: str
    def __init__(self, titulo: _Optional[str] = ..., descricao: _Optional[str] = ..., envolvidos: _Optional[str] = ...) -> None: ...

class CriarReply(_message.Message):
    __slots__ = ("titulo", "descricao", "envolvidos", "id")
    TITULO_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    ENVOLVIDOS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    titulo: str
    descricao: str
    envolvidos: str
    id: str
    def __init__(self, titulo: _Optional[str] = ..., descricao: _Optional[str] = ..., envolvidos: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class ListarRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListarReply(_message.Message):
    __slots__ = ("tarefas",)
    TAREFAS_FIELD_NUMBER: _ClassVar[int]
    tarefas: _containers.RepeatedCompositeFieldContainer[Tarefa]
    def __init__(self, tarefas: _Optional[_Iterable[_Union[Tarefa, _Mapping]]] = ...) -> None: ...

class AtualizarRequest(_message.Message):
    __slots__ = ("titulo", "descricao", "envolvidos", "id")
    TITULO_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    ENVOLVIDOS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    titulo: str
    descricao: str
    envolvidos: str
    id: str
    def __init__(self, titulo: _Optional[str] = ..., descricao: _Optional[str] = ..., envolvidos: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class AtualizarReply(_message.Message):
    __slots__ = ("titulo", "descricao", "envolvidos", "id")
    TITULO_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    ENVOLVIDOS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    titulo: str
    descricao: str
    envolvidos: str
    id: str
    def __init__(self, titulo: _Optional[str] = ..., descricao: _Optional[str] = ..., envolvidos: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DeletarRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeletarReply(_message.Message):
    __slots__ = ("deletado",)
    DELETADO_FIELD_NUMBER: _ClassVar[int]
    deletado: str
    def __init__(self, deletado: _Optional[str] = ...) -> None: ...
