#!/usr/bin/env python

"""
Copyright 2024 RobotsMali.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import unittest
from bako.utils import config as cfg
from bako.src.db.utils import drop_collection, drop_database, get_database, get_collection,\
    client_connect, exist_collection, exist_database, insert, find, update, delete

class DButilsTest(unittest.TestCase):
    """A test case class for the functions defined in bako.src.db.utils
    """
    # Note that methods are runned in alphabetical order (by default)
    # So putting a number just after the test pattern allow to control the execution order
    def test_01_connection(self):
        """Test the client connection function with default arguments
        """
        client = client_connect()
        self.assertIsNotNone(client)

    def test_04_insert(self):
        """Test the insertion function
        """
        result = insert({"author": "Yacouba Diarra", "title": "And What's Beyond the Infinity?"},
                        collection_name="book", database_name=cfg.DEV_CLIENT_NAME)
        print(result)
        self.assertTrue(exist_database(database_name=cfg.DEV_CLIENT_NAME))
        self.assertTrue(exist_collection("book", database_name=cfg.DEV_CLIENT_NAME))

    def test_05_update_and_find(self):
        """Test the update function"""
        result = update(fil={"author": "Yacouba Diarra"}, collection_name="book",
                        database_name=cfg.DEV_CLIENT_NAME, update_data={"author": "Diarray"})
        print(result)
        self.assertIsNotNone(result)
        self.assertIsNotNone(find(fil={"author": "Diarray"}, collection_name="book",
                        database_name=cfg.DEV_CLIENT_NAME))

    def test_06_delete_document(self):
        """Test delete function
        """
        result = delete(fil={"author": "Diarray"}, collection_name="book",
                        database_name=cfg.DEV_CLIENT_NAME)
        print(result)
        self.assertIsNone(find(fil={"author": "Diarray"}, collection_name="book",
                        database_name=cfg.DEV_CLIENT_NAME, limit_one=True))

    def test_03_get_collection(self):
        """Test the collection creation/ retrieval function
        """
        collection = get_collection(collection_name="book", database_name=cfg.DEV_CLIENT_NAME)
        self.assertIsNotNone(collection)
        print(f"Collection '{collection.name}' ready to be used")

    def test_02_get_database(self):
        """Test the get_database function
        """
        database = get_database(database_name=cfg.DEV_CLIENT_NAME)
        self.assertIsNotNone(database)

    def test_07_drop_collection(self):
        """Test the drop_collection function
        """
        drop_collection(collection_name="book", database_name=cfg.DEV_CLIENT_NAME)
        self.assertFalse(exist_collection("book", database_name=cfg.DEV_CLIENT_NAME))

    def test_08_drop_database(self):
        """Test the drop database function
        """
        drop_database(database_name=cfg.DEV_CLIENT_NAME)
        self.assertFalse(exist_database(database_name=cfg.DEV_CLIENT_NAME))

if __name__ == '__main__':
    unittest.main()
