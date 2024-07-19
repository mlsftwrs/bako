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
from bako.src.db.models import AdminUser, ReaderUser, Book
import bako.src.db.utils as db_utils
from bako.utils.config import DEV_CLIENT_NAME

class TestCaseModels(unittest.TestCase):
    """A test case class for the Classes defined in bako.src.db.models
    """
    def test_01_create_admin(self):
        """Test Admin object and document creation and 
        """
        admin = AdminUser(username="admin1", firstname="Seb", surname="Diarra", email="x@gmail.com",
                          password="12345")
        insert_result = admin.create_doc(unique="username")
        print(insert_result)
        self.assertIsNotNone(insert_result)

    def test_02_from_doc_update(self):
        """Test .update() and .from_doc() methods BakoModel
        """
        admin1 = db_utils.find(fil={"username": "admin1"}, collection_name="admins",
                               database_name=DEV_CLIENT_NAME, limit_one=True)
        admin = AdminUser.from_doc(doc=admin1, database_name=DEV_CLIENT_NAME, collection_name="admins")
        print(admin.id, admin.username)
        admin.firstname = "Sebastien"
        update_result = admin.update()
        print(update_result)
        self.assertTrue(update_result.modified_count > 0)

    def test_03_create_reader(self):
        """Test Reader object and document creation and 
        """
        reader = ReaderUser(username="fdiarra", firstname="Fanta", surname="Diarra",
                          birthdate="2017-10-5", password="12345")
        insert_result = reader.create_doc(unique="username")
        print(insert_result)
        self.assertIsNotNone(insert_result)

    def test_reset(self):
        """Reset MongoBD"""
        db_utils.drop_collection(collection_name="admins", database_name=DEV_CLIENT_NAME)
        self.assertFalse(db_utils.exist_collection("admins", database_name=DEV_CLIENT_NAME))
        db_utils.drop_collection(collection_name="readers", database_name=DEV_CLIENT_NAME)
        self.assertFalse(db_utils.exist_collection("readers", database_name=DEV_CLIENT_NAME))
        db_utils.drop_database(database_name=DEV_CLIENT_NAME)
        self.assertFalse(db_utils.exist_database(database_name=DEV_CLIENT_NAME))