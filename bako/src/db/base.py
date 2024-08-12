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

import pymongo.results
import pymongo
import bako.src.db.utils as db_utils

class BakoModel(object):
    """
    Define a base abstract Model

    Attributes:
        database_name (str): DB name
        collection_name (str): DB collection name
        id (ObjectId): The _id of the document if it has already been created
    """
    database_name: str = None
    collection_name: str = None

    def __init__(self, _id = None) -> None:
        """The constructor special method"""
        self.__id = _id

    def create_doc(self, unique: str = None) -> pymongo.results.InsertOneResult:
        """Insert a document in the corresponding collection for this instance
        This method should be called only once for a given instance

        Args:
            unique (str, optional): document field to look for redundacy. Defaults to None.
        """
        doc = self.to_doc()

        if unique:
            assert not self.dupplicate_check(unique_field=unique, value=doc[unique]), f"Field {unique}\
                should be unique but there is already a document with {unique} = {doc[unique]}"
        insert_result = db_utils.insert(data=doc, collection_name=self.collection_name,
                               database_name=self.database_name)
        self.__id = insert_result.inserted_id
        return insert_result

    def update(self) -> pymongo.results.UpdateResult:
        """Commit updates to MongoDB 

        Returns:
            pymongo.results.UpdateResult
        """
        new_values = self.to_doc()
        return db_utils.update(fil={"_id": self.id}, collection_name=self.collection_name,
                               database_name=self.database_name, update_data=new_values)

    def to_doc(self) -> dict:
        """Return a document dictionary from the object
        """
        doc = self.__dict__.copy()
        # ID is already immutable and present in MongoDB
        doc.pop("_BakoModel__id")
        return doc

    def dupplicate_check(self, unique_field, value) -> bool:
        """Check if a document with unique_field=value already exists
        """
        result = db_utils.find(fil={unique_field: value}, collection_name=self.collection_name,
                             database_name=self.database_name, limit_one=True)
        return bool(result)

    @property
    def id(self):
        """Getter for self.__id
        """
        return self.__id

    @classmethod
    def from_doc(cls, doc: dict):
        """Create an instance from a saved document

        Args:
            doc (dict): The document with the values for the attributes
            database_name (str): The name of the database from which this document comes from
            collection_name (str): The name of the collection from which this document comes from
        """
        return cls(**doc)
