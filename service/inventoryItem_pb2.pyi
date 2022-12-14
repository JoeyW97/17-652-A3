import book_pb2 as _book_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InventoryItem(_message.Message):
    __slots__ = ["inventoryId", "item", "status"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AVAILABLE: InventoryItem.Status
    INVENTORYID_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TAKEN: InventoryItem.Status
    inventoryId: str
    item: _book_pb2.Book
    status: InventoryItem.Status
    def __init__(self, inventoryId: _Optional[str] = ..., item: _Optional[_Union[_book_pb2.Book, _Mapping]] = ..., status: _Optional[_Union[InventoryItem.Status, str]] = ...) -> None: ...
