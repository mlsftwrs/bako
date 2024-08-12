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

from typing import Optional, Union
import pymongo.results
import pymongo.collection
import pymongo.database
import pymongo.errors
from bako.utils import config as cfg

def client_connect(db_uri: str = cfg.CLUSTER_URI) -> Optional[pymongo.MongoClient]:
    """Function to connect to MongoDB

    Args:
        db_uri (str, optional): The MongoDB cluster uri. Defaults to constant cfg.CLUSTER_URI \
            (MongoDB deployment hosted on MongoDB Atlas, could be a localhost deployment)
        
    Returns:
        Optional[pymongo.MongoClient]: A MongoClient
    """
    client = pymongo.MongoClient(db_uri, serverSelectionTimeoutMS=5000)

    try:
        # Send a ping to confirm a successful connection
        client.admin.command({'ping': 1})
        return client
    except (pymongo.errors.PyMongoError) as e:
        print(f"PyMongo Exception '{e}' occured when trying to connect to MongoDB, \
            function client_connect returned None!")
        return None

def exist_collection(collection_name: str, database_name: str) -> bool:
    """Returns whether or not a collection exists in a given database

    Args:
        collection_name (str): The collection name
        database_name (str): The name of the database

    Returns:
        bool: _description_
    """
    client = client_connect()
    exists = True if collection_name in client[database_name].list_collection_names() else False
    # It is considered good practice to ensure the connection is closed when we are done with the client
    client.close()
    return exists

def exist_database(database_name: str) -> bool:
    """Returns whether or not a database exists in the MongoDB Cluster

    Args:
        database_name (str): The name of the database

    Returns:
        bool: _description_
    """
    client = client_connect()
    exists = True if database_name in client.list_database_names() else False
    client.close()
    return exists

def drop_collection(collection_name: str, database_name: str) -> None:
    """Delete a collection if it exists in a database 

    Args:
        collection_name (str): _description_
        database_name (str): The name of the database that possesses the wanted collection

    Returns:
        None: This function doesn't return anything
    """
    client = client_connect()

    db = client.get_database(name=database_name)
    if collection_name in db.list_collection_names():
        db.drop_collection(name_or_collection=collection_name)
    # close connection
    client.close()

def drop_database(database_name: str) -> None:
    """Delete a database from the MongoDB Cluster if it exists

    Args:
        database_name (str): _description_
    """
    client = client_connect()
    if database_name in client.list_database_names():
        client.drop_database(name_or_database=database_name)
    client.close()

def get_collection(collection_name: str, database_name: str
                   ) -> Optional[pymongo.collection.Collection]:
    """Returns a PyMongo collection if it exist and a lazy collection else

    Args:
        collection_name (str): The name of the collection we want to access
        database_name (str): The name of the database that possesses the wanted collection

    Returns:
        Optional[pymongo.collection.Collection]: A PyMongo Collection object
    """
    client = client_connect()

    db = client.get_database(name=database_name)
    # This line will return a reference of collections which do not exist the database
    # The actual collection will be created when we first insert data into it
    # Thus no need to check whether the collection exists or not before doing this
    collection = db[collection_name]
    # close connection
    client.close()
    return collection

def get_database(database_name: str) -> Optional[pymongo.database.Database]:
    """Returns a PyMongo Database if it exist in the cluster and a lazy database else

    Args:
        database_name (str): The name of the database that has the wanted collection

    Returns:
        Optional[pymongo.database.Database]: A PyMongo Database
    """
    client = client_connect()
    # The same logic as for collections
    # Note that is line is equivalent to "client.get_database(name=database_name)"
    db = client[database_name]
    client.close()
    return db

def count_documents(collection_name: str, database_name: str, fil: dict = None) -> int:
    """Returns the number of documents macthing the given filter in a collection
    If no filter is provided, it returns the number of document in the collection

    Args:
        collection_name (str): The name of the collection we want to access
        database_name (str): The name of the database that possesses the wanted collection
        fil (dict, optional): Filter dictionary. Defaults to None.

    Returns:
        int: The count
    """
    client = client_connect()
    collection = client[database_name][collection_name]

    return collection.count_documents(filter=fil)

def insert(data: Union[dict, list[dict]], collection_name: str, database_name: str
           ) -> Union[pymongo.results.InsertOneResult, pymongo.results.InsertManyResult]:
    """Insert one or more new document in a collection
        
    Args:
        data (dict | list[dict]): The dictionary of fields and values of the new document. 
            The insert method used will depend on the type of thd argument "data".
        collection_name (str): The name of the collection we want to access
        database_name (str): The name of the database that has the wanted collection

    Returns:
        pymongo.collection.Collection: 
    """
    client = client_connect()
    db = client[database_name]
    collection = db[collection_name]
    if isinstance(data, list):
        collection = collection.insert_many(data)
    else: collection = collection.insert_one(document=data)
    client.close()
    return collection

def find(fil: dict, collection_name: str, database_name: str, limit_one: bool = False
         ) -> Union[dict, list, None]:
    """Find documents in a collection that match the pattern specified with "fil"

    Args:
        fil (dict): Dictionary of fields and values describing the pattern
        collection_name (str): The name of the collection we want to access
        database_name (str): The name of the database that has the wanted collection
        limit_one (bool, optional): Whether to return only the first document that matches the \
            pattern. Defaults to False.

    Returns:
        pymongo.collection.Collection: _description_
    """
    client = client_connect()
    db = client[database_name]
    collection = db[collection_name]
    matches = collection.find_one(fil) if limit_one else list(collection.find(fil))
    client.close()
    return matches

def update(fil: dict, collection_name: str, database_name: str,
           update_data: dict, update_one: bool = True) -> pymongo.results.UpdateResult:
    """Update one or more documents in a collection that match the filter

    Args:
        fil (dict): Dictionary of fields and values describing the filter.
        update_data (dict): Dictionary of fields and values to update.
        collection_name (str): The name of the collection we want to access.
        database_name (str): The name of the database that has the wanted collection.
        update_one (bool, optional): Whether to update only the first document that matches the 
            filter. Defaults to True.

    Returns:
        pymongo.results.UpdateResult: The result of the update operation.
    """
    client = client_connect()
    db = client[database_name]
    collection = db[collection_name]

    if update_one:
        result = collection.update_one(fil, {'$set': update_data})
    else:
        result = collection.update_many(fil, {'$set': update_data})

    client.close()
    return result

def delete(fil: dict, collection_name: str, database_name: str,
           delete_one: bool = True) -> pymongo.results.DeleteResult:
    """Delete one or more documents in a collection that match the filter

    Args:
        fil (dict): Dictionary of fields and values describing the filter.
        collection_name (str): The name of the collection we want to access.
        database_name (str): The name of the database that has the wanted collection.
        delete_one (bool, optional): Whether to delete only the first document that matches the
            filter. Defaults to True.

    Returns:
        pymongo.results.DeleteResult: The result of the delete operation.
    """
    client = client_connect()
    db = client[database_name]
    collection = db[collection_name]

    if delete_one:
        result = collection.delete_one(fil)
    else:
        result = collection.delete_many(fil)

    client.close()
    return result
