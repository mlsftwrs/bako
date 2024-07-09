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

import client
import pymongo
from pymongo.typings import _DocumentType
from typing import Union, Optional, Any


class BakoModel(object):
    """
    Define a base abstract Model

    Attributes:
        client: DB name [str]
        collection: DB collection name [str]
        kwargs: Model's required attributes, in key, value format, if set.
        create: Create document
        retrieve: Retrieve single document
        retrieve_all:

    Exception:
        raise (handshake error on unsuccessful connection to the collection) 
    """

    def __init__(self, client_name: str, collection: str, **kwargs) -> None:
        """Set model collection and fields"""

        self.collection = client.collection(collection, client_name)

        if(not self.collection): # FIXME: yields error None comparison
            # TODO: log error
            raise Exception(
                "Handshake error, unable to access")

        self.model_fields = kwargs
        self.selected = None # FIXME: cursor selected (item)

        for attr in kwargs:
            self.__setattr__(attr, kwargs[attr])

    def create(
            self, 
            data: dict,
            *, 
            unique: Optional[str]=None) -> Union[None, pymongo.results.InsertOneResult]:
        """
        Create collection document

        Args:
            data: dictionary object of item to insert
            unique: document field to look for redundacy

        Returns:
            None: Collection or Dupplicate error
            pymongo.results.InsertOneResult
        """
        if(
            self.collection and not self.dupplicate_check(
                unique, data[unique])):
            return self.collection.insert_one(data)
        return None

    def retrieve(self, filter: dict=None) -> Union[None, _DocumentType]:
        """
        Retrieve a single document

        Args:
            filter: Dictionary based Key-Value filter 
                    for retrieving element - {key: value}
        Returns:
            None: On item not found or collection error
            _DocumentType: pymongo Document type
        """
        return self.collection.find_one(filter)

    def retrieve_all(self, filter: dict=None) -> Optional[list]:
        """
        Retrieve all documents or all documents matching filter

        Args:
            filter: Dictionary based Key-Value
        
        Returns:
            None: On collection error
            list: list of _DocumentType (dicts)
        """
        return list[self.collection.find(filter)]

    def update(self, filter, update_data):
        """
        """
        return self.collection.update_one(filter, {"$set": update_data})

    def delete(self, filter):
        """
        """
        return self.collection.delete_many(filter)

    def document(self, **kwargs) -> dict:
        """
        """
        return {}

    def dupplicate_check(self, unique_field, value) -> bool:
        """ """
        result = self.retrieve({unique_field: value})
        return True if result else False

    @property
    def next(self):
        """ Cursor selection property () """
        pass
