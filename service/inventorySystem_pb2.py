# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventorySystem.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import book_pb2 as book__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15inventorySystem.proto\x1a\nbook.proto\"\x18\n\x08\x42ookISBN\x12\x0c\n\x04ISBN\x18\x01 \x01(\t2R\n\x0fInventorySystem\x12 \n\nCreateBook\x12\x05.Book\x1a\t.BookISBN\"\x00\x12\x1d\n\x07GetBook\x12\t.BookISBN\x1a\x05.Book\"\x00')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventorySystem_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOKISBN._serialized_start=37
  _BOOKISBN._serialized_end=61
  _INVENTORYSYSTEM._serialized_start=63
  _INVENTORYSYSTEM._serialized_end=145
# @@protoc_insertion_point(module_scope)
