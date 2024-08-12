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

from pymongo.results import InsertOneResult
from bako.src.db.base import BakoModel
import bako.utils.config as cfg
import bako.src.db.utils as db_utils

class Book(BakoModel):
    """Book Class Model

    Args:
        title (str):  A unique title for the book
        content (dict): A dictionary where the keys are the page references and \
            the values are lists of all the sentences in that page
        database_name (str, optional): Defaults to vfg.DEV_CLIENT_NAME.
        collection_name (str, optional): Defaults to cfg.COL_BOOK.
    """
    collection_name: str = cfg.COL_BOOK
    database_name: str = cfg.DEV_CLIENT_NAME

    def __init__(self, title: str, content: dict, _id = None) -> None:
        """_summary_

        Args:
            title (str): A unique title for the book
            content (dict): A dictionary where the keys are the page references and \
                the values are lists of all the sentences in that page
            database_name (str, optional): Defaults to cfg.DEV_CLIENT_NAME.
            collection_name (str, optional): Defaults to cfg.COL_BOOK.
        """
        super().__init__(_id=_id)
        self.title = title
        self.content = content

    def create_doc(self, unique: str = "title") -> InsertOneResult:
        return super().create_doc(unique)

    @classmethod
    def list_books(cls) -> list[dict]:
        """Returns the list of all documents in the collection 

        Returns:
           list[dict]
        """
        list_of_book = db_utils.find(fil=None, collection_name=cls.collection_name,
                                     database_name=cls.database_name)
        return list_of_book

    @classmethod
    def get_num_books(cls, fil: dict = None) -> int:
        """Get the number of books that macth the filter. If No filter, the total number of books

        Args:
            fil (dict, optional): Dictionary filter. Defaults to None.
        """
        fil = {} if not fil else fil
        return db_utils.count_documents(collection_name=cls.collection_name,
                                        database_name=cls.database_name, fil=fil)
