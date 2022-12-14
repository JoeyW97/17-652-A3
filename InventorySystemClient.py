# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 17:14
# @Author  : Jianqiao Wang
import grpc
from service import inventorySystem_pb2_grpc
from service import inventorySystem_pb2
from service import book_pb2


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = inventorySystem_pb2_grpc.InventorySystemStub(channel)
        # add a new book to the inventory
        newBook = book_pb2.Book()
        newBook.ISBN = "100"
        newBook.title = "XYZ"
        newBook.author = "JJ"
        newBook.genre = "romance"
        newBook.publishingYear = 2000
        newISBN = stub.CreateBook(newBook)
        print("New book added: ISBN = ", newISBN.ISBN)

        # Get the new added book
        book = stub.GetBook(inventorySystem_pb2.BookISBN(ISBN = "100"))
        print("The book with ISBN 100", book)


if __name__ == '__main__':
    run()
