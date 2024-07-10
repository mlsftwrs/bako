import unittest
from bako.utils import config as cfg
from bako.src.db.utils import drop_collection, drop_database, get_database, get_collection,\
    client_connect, exist_collection, exist_database

class ClientCollectionTest(unittest.TestCase):
    """A test case class where each method is a unit test
    """
    def test_connection(self):
        """Test the client connection function with default arguments
        """
        client = client_connect()
        self.assertIsNotNone(client)

    def test_exist_collection(self):
        """Test the exist collection function
        """
        self.assertTrue(exist_collection("book", database_name=cfg.DEV_CLIENT_NAME))

    def test_exist_databae(self):
        """Test the exist database function
        """
        self.assertTrue(exist_database(database_name=cfg.DEV_CLIENT_NAME))

    def test_get_collection(self):
        """Test the collection creation/ retrieval function
        """
        collection = get_collection(collection_name="book", database_name=cfg.DEV_CLIENT_NAME)
        self.assertIsNotNone(collection)
        print(f"Collection '{collection.name}' ready to be used")

    def test_get_database(self):
        """_summary_
        """
        database = get_database(database_name=cfg.DEV_CLIENT_NAME)
        self.assertIsNotNone(database)

    def test_drop_collection(self):
        """_summary_
        """
        drop_collection(collection_name="book", database_name=cfg.DEV_CLIENT_NAME)
        self.assertFalse(exist_collection("book", database_name=cfg.DEV_CLIENT_NAME))

    def test_drop_database(self):
        """_summary_
        """
        drop_database(database_name=cfg.DEV_CLIENT_NAME)
        self.assertFalse(exist_database(database_name=cfg.DEV_CLIENT_NAME))

    def testagain_get_database(self):
        self.assertIsNone(get_database(database_name=cfg.DEV_CLIENT_NAME))

if __name__ == '__main__':
    unittest.main()
