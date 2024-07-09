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

import pymongo
from typing import Optional
from bako.utils import config as cfg


def client_connect(
    client_name: str = cfg.DEV_CLIENT_NAME, 
    db_uri: str = cfg.DEV_CLUSTER_URI
) -> Optional[pymongo.MongoClient]:
    """
    Function for connecting to a MongoDB Client
    """
    try:
        client = pymongo.MongoClient(
            db_uri, serverSelectionTimeoutMS=5000)
        client.admin.command("ismaster")
        return client[client_name]
    except (
        pymongo.errors.ServerSelectionTimeoutError, Exception) as e:
        return None


def collection(
    collection_name: str, client_name: str
) -> Optional[pymongo.collection.Collection]:
    """
    Collection retrieval / Creation function
    """
    client = client_connect(client_name=client_name)

    if client:
        db = client.get_database()
        if collection_name in db.list_collection_names():
            return db[collection_name]
        else:
            return db.create_collection(collection_name)
    return None
