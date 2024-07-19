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

import datetime
from bako.src.db import base
from bako.utils.config import DEV_CLIENT_NAME

class UserModel(base.BakoModel):
    """Base class for user models inheriting from BakoModel
    
    Args:
        user_name (str): Unique username ID field
        first_name (str): The first name of the user
        surname (str): The User's surname
        collection_name (str): The name of the collection to which this object belongs
        database_name (str): The name of the database to which this collection belongs
    """
    def __init__(self, username: str, firstname: str, surname: str, password: str,
                collection_name: str, database_name: str, _id = None) -> None:
        """Constructor method to create a User object

        Args:
            user_name (str): Unique username ID field
            firstname (str): The first name of the user
            surname (str): The User's surname
            collection_name (str): The name of the collection to which this object belongs
            database_name (str): The name of the database to which this collection belongs
        """
        super().__init__(collection_name=collection_name, database_name=database_name, _id=_id)
        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.password = password

class AdminUser(UserModel):
    """Admin user model
    
    Args:
        username (str): Unique username ID field
        firstname (str): The first name of the user
        surname (str): The User's surname
        email (str): The email of the admin User
        collection_name (str, optional): The name of the collection to which\
            this object belongs. Defaults to "admin".
        database_name (str, optional): The name of the database to which\
            this collection belongs. Defaults to DEV_CLIENT_NAME.
    """
    def __init__(self, username: str, firstname: str, surname: str, email: str,
                 password: str, _id = None, collection_name: str = "admins",
                 database_name: str = DEV_CLIENT_NAME, assigned_readers: list = None) -> None:
        """_summary_

        Args:
            username (str): Unique username ID field
            firstname (str): The first name of the user
            surname (str): The User's surname
            email (str): The email of the admin User
            collection_name (str, optional): The name of the collection to which\
                this object belongs. Defaults to "admin".
            database_name (str, optional): The name of the database to which\
                this collection belongs. Defaults to DEV_CLIENT_NAME.
        """
        super().__init__(username=username, firstname=firstname, surname=surname, password=password,
                         collection_name=collection_name, database_name=database_name, _id=_id)
        self.email = email
        self.assigned_readers = assigned_readers if assigned_readers else []

    def assign_book(self, reader_username: str, book_id):
        # Implement the logic to assign a book to a reader user
        pass

    def view_assigned_books(self, reader_username: str):
        # Implement the logic to view books assigned to a particular reader
        pass

    def remove_assigned_book(self, reader_username: str, book_id):
        # Implement the logic to remove a book from a reader's assigned list
        pass

class ReaderUser(UserModel):
    """Reader user model
    
    Args:
        username (str): Unique username ID field
        firstname (str): The first name of the user
        surname (str): The User's surname
        birthdate (str): The kid's date of birth (YYYY-MM-DD)
        collection_name (str, optional): The name of the collection to which\
            this object belongs. Defaults to "reader".
        database_name (_type_, optional): The name of the database to which\
            this collection belongs. Defaults to DEV_CLIENT_NAME.
    """
    def __init__(self, username: str, firstname: str, surname: str, password: str,
                 birthdate: str, collection_name: str = "readers", reader_xp: int = 0,
                 database_name = DEV_CLIENT_NAME, assigned_books: list = None,
                 completed_books: list = None, _id = None) -> None:
        """_summary_

        Args:
            username (str): Unique username ID field
            firstname (str): The first name of the user
            surname (str): The User's surname
            birthdate (datetime.date): The kid's date of birth
            collection_name (str, optional): The name of the collection to which\
                this object belongs. Defaults to "reader".
            database_name (_type_, optional): The name of the database to which\
                this collection belongs. Defaults to DEV_CLIENT_NAME.
        """
        super().__init__(firstname=firstname, surname=surname, username=username, password=password,
                         collection_name=collection_name, database_name=database_name, _id=_id)
        self.birthdate = birthdate
        self.reader_xp = reader_xp
        self.assigned_books = assigned_books if assigned_books else []
        self.completed_books = completed_books if completed_books else []

    def view_assigned_books(self):
        # Implement the logic to view the books assigned to the reader
        pass

    def mark_book_as_completed(self, book_id):
        # Implement the logic to mark a book as completed by the reader
        pass
