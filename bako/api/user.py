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
from bako.src.db.models import ReaderUser
import bako.src.db.utils as db_utils

def create_reader_account(username: str, password: str,
                   firstname: str = None, surname: str = None) -> dict:
    """Create an account in MongoDB for a ReaderUser 

    Args:
        username (str): The username of the new Reader
        password (str): The password of the new Reader
        firstname (str, optional): The first name of the User (Not required). Defaults to None.
        surname (str, optional): The last name of the User (Not required). Defaults to None.

    Returns:
        dict
    """
    new_reader = ReaderUser(username=username, password=password, firstname=firstname, surname=surname)
    try:
        new_reader.create_doc()
        return {"status": True, "msg": "New account succesfully created", "data": None}
    except AssertionError:
        return {"status": False, "msg": "Username Unavailable", "data": None}

def login_reader_user(username: str, password: str) -> dict:
    """Reader User Login

    Args:
        username (str):  The username of the Reader
        password (str): The password of the Reader

    Returns:
        dict
    """
    doc = db_utils.find(fil={"username": username}, collection_name=ReaderUser.collection_name,
                        database_name=ReaderUser.database_name, limit_one=True)
    if doc is None:
        return {"status": False, "msg": "This account doesn't exist", "data": None}
    elif doc["password"] != password:
        return {"status": False, "msg": "Password incorrect", "data": None}
    else:
        doc = doc.copy()
        doc.pop("_id")
        doc.pop("password")
        return {"status": True, "msg": "Login Succesful", "data": doc}

def get_user_data(username: str) -> dict:
    """Returns the data of a specific user | Implicitly suppose user has already logged in!

    Args:
        username (str):  The username of the Reader

    Returns:
        dict
    """
    doc = db_utils.find(fil={"username": username}, collection_name=ReaderUser.collection_name,
                        database_name=ReaderUser.database_name, limit_one=True)
    if doc is None:
        return {"status": False, "msg": "This account doesn't exist", "data": None}

    doc = doc.copy()
    doc.pop("_id")
    doc.pop("password")
    return {"status": True, "msg": "Login Succesful", "data": doc}


def edit_username(current_username: str, new_username: str, password: str) -> dict:
    """Edit the username of a user

    Args:
        current_username (str): Current username of the user
        new_username (str): Username to change for
        password (str): confirmation password

    Returns:
        dict
    """
    username_already_inuse = doc = db_utils.find(fil={"username": new_username},
                        collection_name=ReaderUser.collection_name,
                        database_name=ReaderUser.database_name, limit_one=True)
    if username_already_inuse:
        return {"status": False, "msg": "Username Unavailable", "data": None}

    doc = db_utils.find(fil={"username": current_username},
                        collection_name=ReaderUser.collection_name,
                        database_name=ReaderUser.database_name, limit_one=True)
    if password != doc['password']:
        return {"status": False, "msg": "Password incorrect", "data": None}

    reader_user = ReaderUser.from_doc(doc=doc)
    reader_user.username = new_username
    reader_user.update()
    data = reader_user.to_doc()
    data.pop("password")
    return {"status": True, "msg": "Username has been Changed", "data": data}

def edit_password(username: str, current_password: str, new_password: str) -> dict:
    """Change password

    Args:
        username (str): Current username of the user
        current_password (str): confirmation password
        new_password (str): New_password

    Returns:
        dict
    """
    doc = db_utils.find(fil={"username": username},
                        collection_name=ReaderUser.collection_name,
                        database_name=ReaderUser.database_name, limit_one=True)
    if current_password != doc['password']:
        return {"status": False, "msg": "Confirmation Password incorrect", "data": None}

    reader_user = ReaderUser.from_doc(doc=doc)
    reader_user.password = new_password
    reader_user.update()
    data = reader_user.to_doc()
    data.pop("password")
    return {"status": True, "msg": "Password has been Changed", "data": data}

def delete_account(username: str, password: str) -> dict:
    """Delete an account

    Args:
        username (str):  The username of the Reader
        password (str): The password of the Reader

    Returns:
        dict
    """
    doc = db_utils.find(fil={"username": username}, collection_name=ReaderUser.collection_name,
                        database_name=ReaderUser.database_name, limit_one=True)
    if password != doc["password"]:
        return {"status": False, "msg": "Confirmation Password incorrect", "data": None}

    db_utils.delete(fil={"username": username}, collection_name=ReaderUser.collection_name,
                        database_name=ReaderUser.database_name)
    return {"status": True, "msg": "This account has been deleted", "data": None}
    