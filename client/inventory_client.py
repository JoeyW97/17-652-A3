# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 12:25
# @Author  : Jianqiao Wang
import grpc
from service import inventorySystem_pb2_grpc
from service import inventorySystem_pb2


class InventorySystemClient:
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = inventorySystem_pb2_grpc.InventorySystemStub(self.channel)

    def get_book(self, ISBN):
        return self.stub.GetBook(inventorySystem_pb2.BookISBN(ISBN = ISBN))

    def create_book(self, ISBN, title, author, genre, publishingYear):
        newBook = book_pb2.Book()
        newBook.ISBN = ISBN
        newBook.title = title
        newBook.author = author
        newBook.genre = genre
        newBook.publishingYear = publishingYear
        newISBN = self.stub.CreateBook(newBook)
        return newISBN

    def close(self):
        self.channel.close()
