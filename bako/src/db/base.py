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

from typing import Union, Optional
from pymongo.typings import _DocumentType
import pymongo.results
import pymongo
import bako.src.db.utils as db_utils

class BakoModel(object):
    """
    Define a base abstract Model

    Attributes:
        database_name (str): DB name
        collection_name (str): DB collection name
        kwargs: Model's required attributes, in key, value format, if set.
    """

    def __init__(self, database_name: str, collection_name: str, **kwargs) -> None:
        """The constructor special method"""

        self.collection_name = collection_name
        self.database_name = database_name

        self.model_fields = kwargs
        self.selected = None # FIXME: cursor selected (item)

        for attr, value in kwargs.items():
            self.__setattr__(attr, value)

    def create(self, data: dict, *,
               unique: Optional[str]=None) -> pymongo.results.InsertOneResult:
        """
        Create a new document in a collection

        Args:
            data (dict): dictionary object of item to insert
            unique (bool | None): document field to look for redundacy. Defaults to None.

        Returns:
            None: Collection or Dupplicate error
            pymongo.results.InsertOneResult
        """
        if unique:
            assert self.dupplicate_check(unique, data[unique]), f"Field {unique} is supposed should\
            be unique but there is already a document with {unique} = {data[unique]}"

        return db_utils.insert(data=data, collection_name=self.collection_name,
                                   database_name=self.database_name)

    def insert(self, data: Union[dict, list[dict]], unique: Optional[str]=None
               ) -> Union[pymongo.results.InsertOneResult, pymongo.results.InsertManyResult]:
        """Insert one or more document into a collection.

        Args:
            data (dict | list[dict]): The documents to insert in the collection
            unique (Optional[str]): document field to look for redundacy.Defaults to None.

        Returns:
            Union[pymongo.results.InsertOneResult, pymongo.results.InsertManyResult]
        """
        if unique:
            assert self.dupplicate_check(unique, data[unique]), f"Field {unique} is supposed should\
            be unique but there is already a document with {unique} = {data[unique]}"

        return db_utils.insert(data=data, collection_name=self.collection_name,
                                   database_name=self.database_name)

    # I'm not sure this return type is actuallly correct
    def retrieve(self, fil: dict = None, limit_one: bool = False) -> _DocumentType:
        """
        Retrieve the documents that match the filter

        Args:
            filter: Dictionary based Key-Value filter 
                    for retrieving element - {key: value}
            limit_one (Optional[bool]): Whether to stop searching at the first element or return\
                all document the match the filter
        Returns:
            _DocumentType: pymongo Document type
        """
        return db_utils.find(fil=fil, collection_name=self.collection_name,
                             database_name=self.database_name, limit_one=limit_one)

    def change_values(self, fil: dict, update_data: dict, 
                      update_one: bool = True) -> pymongo.results.UpdateResult:
        """Set the values of the fields in update_data with the corresponding values

        Args:
            fil (dict): Dictionary based Key-Value filter 
            update_data (dict): A dictionary of the fields to update with their values.
            update_one (bool, optional): Whether to update just the first element that match the filter. Defaults to True.

        Returns:
            pymongo.results.UpdateResult: _description_
        """
        return db_utils.update(fil=fil, collection_name=self.collection_name,
                database_name=self.database_name, update_data=update_data, update_one=update_one)
    def delete(self, fil: dict, delete_one: bool = True) -> pymongo.results.DeleteResult:
        """Delete the documents that match the filter

        Args:
            fil (dict): Dictionary based Key-Value filter 
            delete_one (bool, optional): Whether to delete just the first element that match the filter. Defaults to True.

        Returns:
            pymongo.results.DeleteResult: _description_
        """
        return db_utils.delete(fil=fil, collection_name=self.collection_name,
                               database_name=self.database_name, delete_one=delete_one)

    def document(self, **kwargs) -> dict:
        """???
        """
        return {}

    def dupplicate_check(self, unique_field, value) -> bool:
        """Check if a document with unique_field=value already exists
        """
        result = self.retrieve(fil={unique_field: value}, limit_one=True)
        return bool(result)

    @property
    def next(self):
        """ Cursor selection property () """
        pass
