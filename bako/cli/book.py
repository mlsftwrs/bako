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
import pandas as pd
from bako.src.db.models import Book

def df_to_book(book_tile: str, df: pd.DataFrame) -> Book:
    """Return a book object from a sheet dataframe

    Args:
        df (pd.DataFrame): The sheet dataframe
    """
    content: dict[str, list] = {}
    for idx, page_ref in df["Page No"].items():
        if page_ref in content:
            content[page_ref].append(df["RobotsMali adjusted-Review "][idx])
        else: content[page_ref] = [df["RobotsMali adjusted-Review "][idx]]
    return Book(title=book_tile, content=content)

def add_books_to_mongodb(path_to_excel: str):
    """Adds new books to the book collection in our MongoDB deployment

    Args:
        path_to_excel (str): Path to an excel file. Each sheet should hold the texts for only one book
    """
    excel_file = pd.ExcelFile(path_to_excel)
    for story_book in excel_file.sheet_names:
        df = excel_file.parse(story_book)
        book = df_to_book(book_tile=story_book, df=df)
        book.create_doc()
    