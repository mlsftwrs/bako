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

from bako.src.db.base import BakoModel
from bako.utils.config import DEV_CLIENT_NAME

class Book(BakoModel):
    """_summary_

    Args:
        title (str): A unique title for the book
        content (list[str]): A list of all the sentences in the book
        database_name (str, optional): _description_. Defaults to DEV_CLIENT_NAME.
        collection_name (str, optional): _description_. Defaults to "books".
    """
    def __init__(self, title: str, content: list[str], database_name: str = DEV_CLIENT_NAME,
                 collection_name: str = "books") -> None:
        """_summary_

        Args:
            title (str): A unique title for the book
            content (list[str]): A list of all the sentences in the book
            database_name (str, optional): _description_. Defaults to DEV_CLIENT_NAME.
            collection_name (str, optional): _description_. Defaults to "books".
        """
        super().__init__(database_name, collection_name)
        self.title = title
        self.content = content
