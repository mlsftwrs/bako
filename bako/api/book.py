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
from bako.src.db.models import Book
import bako.src.db.utils as db_utils

def get_book(title: str) -> dict:
    """Return the specific book with this title to start a lesson

    Args:
        title (str): The title of the book
    """
    book_doc = db_utils.find(fil={"title": title}, collection_name=Book.collection_name,
                             database_name=Book.database_name, limit_one=True)
    if book_doc is None:
        return {"status": False, "msg": "No book with this title in the catalog", "data": None}

    data = book_doc.copy()
    data.pop("_id")
    return {"status": True, "msg": "Book ready", "data": data}

def get_catalog() -> dict:
    """Returns the titles of all the books in the catalog and the number of books

    Returns:
        dict
    """
    num_books = Book.get_num_books()
    all_books = Book.list_books()
    titles = [book["title"] for book in all_books]
    data = {"num_books": num_books, "titles": titles}
    return {"status": True, "msg": "Catalog ready", "data": data}
