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
from bako.src.db import base
import bako.utils.config as cfg

class UserModel(base.BakoModel):
    """Base class for user models inheriting from BakoModel
    
    Args:
        username (str): Unique username ID field
        firstname (str): The first name of the user
        surname (str): The User's surname
        password (str): The User's Password
        collection_name (str): The name of the collection to which this object belongs
        database_name (str): The name of the database to which this collection belongs
    """
    def __init__(self, username: str, firstname: str, surname: str, password: str, _id = None) -> None:
        """Constructor method to create a User object

        Args:
            username (str): Unique username ID field
            firstname (str): The first name of the user
            surname (str): The User's surname
            password (str): The User's Password
            collection_name (str): The name of the collection to which this object belongs
            database_name (str): The name of the database to which this collection belongs
        """
        super().__init__(_id=_id)
        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.password = password

    def create_doc(self, unique: str = "username") -> InsertOneResult:
        return super().create_doc(unique)

class ReaderUser(UserModel):
    """Reader user model
    
    Args:
        username (str): Unique username ID field
        firstname (str): The first name of the user (Optional)
        surname (str): The User's surname (Optional)
        collection_name (str, optional): The name of the collection to which\
            this object belongs. Defaults to cfg.COL_USER.
        database_name (_type_, optional): The name of the database to which\
            this collection belongs. Defaults to cfg.DEV_CLIENT_NAME.
    """
    collection_name : str = cfg.COL_USER
    database_name : str = cfg.DEV_CLIENT_NAME
    def __init__(self, username: str, password: str, firstname: str = None, surname: str = None,
                 reader_xp: int = 0, in_progress_books: list = None,
                 completed_books: list = None, _id = None) -> None:
        """_summary_

        Args:
            username (str): Unique username ID field
            firstname (str): The first name of the user (Optional)
            surname (str): The User's surname (Optional)
            collection_name (str, optional): The name of the collection to which\
                this object belongs. Defaults to cfg.COL_USER.
            database_name (_type_, optional): The name of the database to which\
                this collection belongs. Defaults to cfg.DEV_CLIENT_NAME.
        """
        super().__init__(firstname=firstname, surname=surname, username=username,
                         password=password, _id=_id)
        self.reader_xp = reader_xp
        self.in_progress_books = in_progress_books if in_progress_books else []
        self.completed_books = completed_books if completed_books else []

    def bookmark(self, book_title: str, book_page_ref: str, reading_time: int):
        """BookMark an in progress book in order to resume reading

        Args:
            book_title (str): The title of the book
            book_page_ref (str): The page ref for the bookmark
        """
        for bookmarked in self.in_progress_books:
            if book_title in bookmarked:
                bookmarked[book_title] = book_page_ref
                bookmarked["reading_time"] = reading_time
                return self.update()
        self.in_progress_books.append({book_title: book_page_ref, "reading_time": reading_time})
        return self.update()

    def mark_book_as_completed(self, book_title: str, num_errors: int = None, reading_time: float = None):
        """Mark a book as completed (Should reflect on UI)

        Args:
            book_title (str): The title of the book
        """
        for bookmarked in self.in_progress_books:
            if book_title in bookmarked:
                self.in_progress_books.remove(bookmarked)

        if not book_title in self.completed_books:
            self.completed_books.append(book_title)

        self.increase_xp(num_errors=num_errors, reading_time=reading_time)

        return self.update()

    def increase_xp(self, num_errors: int = None, reading_time: float = None):
        """Increment the performance measure of the reader

        Args:
            xp_to_add (int): The ammount of XP to add
        """
        xp_to_add = 10
        self.reader_xp += xp_to_add
        return self.update()

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
            this collection belongs. Defaults to cfg.DEV_CLIENT_NAME.
    """
    collection_name: str = None
    database_name: str = cfg.DEV_CLIENT_NAME
    def __init__(self, username: str, password: str, _id = None, firstname: str = None, 
                 surname: str = None, email: str = None, assigned_readers: list = None) -> None:
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
        super().__init__(username=username, firstname=firstname, surname=surname,
                         password=password, _id=_id)
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
