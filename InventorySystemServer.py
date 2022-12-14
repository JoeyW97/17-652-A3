# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 17:14
# @Author  : Jianqiao Wang
from concurrent import futures

import grpc

from service import book_pb2
from service import inventorySystem_pb2
from service import inventorySystem_pb2_grpc
from service import inventoryItem_pb2_grpc
from service import inventoryItem_pb2

"""
I used a python dictionary as the database. Items are stored in a list to the key "items".
"""
db = {'items': [{'inventoryId': "100", 'status': inventoryItem_pb2.InventoryItem.Status.Value('AVAILABLE'),
                 'item': book_pb2.Book(ISBN = '1', title = 'ABC', author = 'Joey', genre = 'comic',
                                       publishingYear = 2020)},
                {'inventoryId': "101", 'status': inventoryItem_pb2.InventoryItem.Status.Value('TAKEN'),
                 'item': book_pb2.Book(ISBN = '2', title = 'DEF', author = 'Jack', genre = 'cartoon',
                                       publishingYear = 2022)}]}
inventoryId = 102


class InventorySystem(inventorySystem_pb2_grpc.InventorySystemServicer):
    def GetBook(self, request, context):
        for item in db['items']:
            book = item['item']
            # Compare the ISBN of books in the database to the input ISBN to find the match.
            if book.ISBN == request.ISBN:
                return book

    def CreateBook(self, request, context):
        global inventoryId
        newBook = book_pb2.Book()
        newBook.ISBN = request.ISBN
        newBook.title = request.title
        newBook.author = request.author
        newBook.genre = request.genre
        newBook.publishingYear = request.publishingYear
        # append the new book to the list in the db dict.
        inventoryId += 1
        db['items'].append(
            {'inventoryId': inventoryId, 'status': inventoryItem_pb2.InventoryItem.Status.Value('AVAILABLE'),
             'item': newBook})
        print('New Inventory: ', db)
        return inventorySystem_pb2.BookISBN(ISBN = request.ISBN)


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    inventorySystem_pb2_grpc.add_InventorySystemServicer_to_server(InventorySystem(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
