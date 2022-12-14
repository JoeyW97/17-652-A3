# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 12:44
# @Author  : Jianqiao Wang
from unittest.mock import MagicMock
import unittest
from service import book_pb2
from get_book_titles import get_book_titles
import InventorySystemServer
import inventory_client

mock_client = MagicMock()
mock_client.get_book.side_effect = [
    book_pb2.Book(ISBN = '1000', title = 'I Love API', author = 'Wang', genre = 'Tech',
                  publishingYear = 2020),
    book_pb2.Book(ISBN = '1001', title = 'I Love API 2', author = 'Wang', genre = 'Tech',
                  publishingYear = 2021),
    book_pb2.Book(ISBN = '1002', title = 'I Love API 3', author = 'Wang', genre = 'Tech',
                  publishingYear = 2022)
]


class TestInventorySystem(unittest.TestCase):

    def test_get_book_titles(self):
        titles = get_book_titles(mock_client, ['1001', '1002'])
        self.assertEqual(titles, ['I Love API', 'I Love API 2'])

    def test_get_book_titles_with_server(self):
        client = inventory_client.InventorySystemClient()
        titles = get_book_titles(client, ['1', '2'])
        self.assertEqual(titles, ['ABC', 'DEF'])


if __name__ == '__main__':
    unittest.main()
