from unittest import TestCase
import unittest
#from bako.utils import config as cfg
from bako.src.db.client import client_connect, collection

class ClientCollectionTest(TestCase):
    """A test case class where each method is a unit test

    Args:
        TestCase (unittest.TestCase): The parent class
    """
    def test_connection(self):
        """Test the client connection function with default arguments
        """
        client_name = client_connect()
        print(client_name)
        self.assertIsNotNone(client_name)
           
    def test_collection(self):
        """Test the collection creation/ retrieval function
        """
        db_collection = collection(collection_name="book")
        print(db_collection)
        self.assertIsNotNone(db_collection)

if __name__ == '__main__':
    unittest.main()
