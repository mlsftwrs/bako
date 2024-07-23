#!/home/diarray/office/BambaraLiteracyApp/venv/bin/python
### You should change the path above to your python interpreter path before running the script

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
from bako.src.db.models import ReaderUser, Book
import bako.src.db.utils as db_utils

class TestCaseModels(unittest.TestCase):
    """A test case class for the Classes defined in bako.src.db.models
    """
    def test_01_create_reader(self):
        """Test Admin object and document creation and 
        """
        reader = ReaderUser(username="diarray", firstname="Yac", surname="Diarra", password="12345")
        insert_result = reader.create_doc()
        print(insert_result)
        self.assertIsNotNone(insert_result)

    def test_02_from_doc_update(self):
        """Test .update() and .from_doc() methods BakoModel
        """
        reader = db_utils.find(fil={"username": "diarray"},
                               collection_name=ReaderUser.collection_name,
                               database_name=ReaderUser.database_name, limit_one=True)
        reader = ReaderUser.from_doc(doc=reader)
        print(reader.id, reader.username)
        reader.firstname = "Yacouba"
        update_result = reader.update()
        print(update_result)
        self.assertTrue(update_result.modified_count > 0)

    def test_03_bookmark_inc_readerxp(self):
        """BookMarking methods and increase reader_xp 
        """
        reader = db_utils.find(fil={"username": "diarray"},
                               collection_name=ReaderUser.collection_name,
                               database_name=ReaderUser.database_name, limit_one=True)
        reader = ReaderUser.from_doc(doc=reader)
        reader.bookmark(book_title="One Piece", book_page_ref="Page 114")
        reader.mark_book_as_completed(book_title="Naruto")
        reader.increase_xp(xp_to_add=15)
        print(reader.to_doc())
        update_result = reader.update()
        self.assertTrue(update_result.modified_count > 0)
    
    def test_04_create_book(self):
        """Test Book creation """
        book = Book(title="One piece", content={"page0": ["", ""]})
        insert_result = book.create_doc()
        print(insert_result)
        self.assertIsNotNone(insert_result)
    
    def test_05_bookclass_methods(self):
        """Test the class methods of Book
        """
        num_book = Book.get_num_books()
        self.assertEqual(num_book, 1)
        books = Book.list_books()
        print(books)
        self.assertIsNotNone(books)

    def test_reset(self):
        """Reset MongoBD"""
        db_utils.drop_collection(collection_name=ReaderUser.collection_name, database_name=ReaderUser.database_name)
        self.assertFalse(db_utils.exist_collection(ReaderUser.collection_name, database_name=ReaderUser.database_name))
        db_utils.drop_collection(collection_name=Book.collection_name, database_name=Book.database_name)
        self.assertFalse(db_utils.exist_collection(Book.collection_name, database_name=Book.database_name))
        db_utils.drop_database(database_name=ReaderUser.database_name)
        self.assertFalse(db_utils.exist_database(database_name=ReaderUser.database_name))
