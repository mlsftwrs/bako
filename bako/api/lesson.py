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

def bookmark(username: str, book_title: str, book_page_ref: str, reading_time: int) -> dict:
    """Mark a book as inprogress (call when user stopped a lesson)

    Args:
        username (str): The name of the user
        book_title (str): Title of the book
        book_page_ref (str): The page reference user stopped at

    Returns:
        dict
    """
    user_doc = db_utils.find(fil={"username": username}, collection_name=ReaderUser.collection_name,
                             database_name=ReaderUser.database_name, limit_one=True)
    reader_user = ReaderUser.from_doc(doc=user_doc)
    reader_user.bookmark(book_page_ref=book_page_ref, book_title=book_title, reading_time=reading_time)
    data = reader_user.to_doc()
    data.pop("password")
    return {"status": True, "msg": "Book marked as In Progress", "data": data}

def mark_book_as_completed(username: str, book_title: str,
                            num_errors: int = None, reading_time: float = None) -> dict:
    """Mark a book as completed

    Args:
        username (str): The name of the user
        book_title (str): Title of the book

    Returns:
        dict
    """
    user_doc = db_utils.find(fil={"username": username}, collection_name=ReaderUser.collection_name,
                             database_name=ReaderUser.database_name, limit_one=True)
    reader_user = ReaderUser.from_doc(doc=user_doc)
    reader_user.mark_book_as_completed(book_title=book_title,
                                       num_errors=num_errors, reading_time=reading_time)
    data = reader_user.to_doc()
    data.pop("password")
    return {"status": True, "msg": "Book marked as Completed", "data": data}
