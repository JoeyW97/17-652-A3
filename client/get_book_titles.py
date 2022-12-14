# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 12:29
# @Author  : Jianqiao Wang
import grpc
from typing import List
import inventory_client
from service import inventorySystem_pb2


def get_book_titles(client: inventory_client.InventorySystemClient, ISBNs: list) -> List[str]:
    titles = []
    for ISBN in ISBNs:
        book = client.get_book(ISBN)
        titles.append(book.title)
    return titles


if __name__ == '__main__':
    client = inventory_client.InventorySystemClient()
    print(get_book_titles(client, ['1', '2']))
