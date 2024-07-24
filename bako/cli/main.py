#!/usr/bin/env python

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
import unittest
import sys
from bako.tests.test_dbutils import DButilsTest
from bako.tests.test_models import TestCaseModels
from bako.cli.book import add_books_to_mongodb

def test_db_utils():
    """_summary_
    """
    suite = unittest.TestLoader().loadTestsFromTestCase(DButilsTest)
    unittest.TextTestRunner().run(suite)

def test_models():
    """_summary_
    """
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCaseModels)
    unittest.TextTestRunner().run(suite)

# A dictionary which keys are available commands and values are another dictionary of options-descriptions pairs
# This cli tools, for now, only demonstrate the unit tests of the database utility functions
COMMAND = {"unittest": {"db_utils": test_db_utils, "models": test_models},
           "add-books": add_books_to_mongodb}
HELP_SHORTCUTS = ["-h", "help", "--help"]

def print_help_message():
    """Show general help message
    """
    help_message = """bakoctl: bakoctl [command] [option]
    Command line interface of bakorm package
    
    Command:
      -h, --help, help: Show this help message
      
      unittest: Perform unit testing of the functions and methods 
      defined in the module speficified as option (should be one of available module aliases)
      
      add-books: Adds new books to the book collection in our MongoDB deployment,
      needs the path to an excel file containing the texts from the books to add
    """
    print(help_message)

def main():
    """_summary_
    """
    args = sys.argv
    if len(args) == 1:
        print("-----------Missing command!!--------------\n")
        print_help_message()

    elif args[1] in HELP_SHORTCUTS:
        print_help_message()

    elif args[1] not in COMMAND:
        print(f"No command named {args[1]}. Available commands are {COMMAND.keys()}")

    elif args[1] == "unittest":
        if len(args) < 3:
            print(f"Missing module names to perform unit testing on. Available names/aliases\
                are {COMMAND['unittest'].keys()}")
        else:
            for alias in args[2:]:
                COMMAND['unittest'][alias]()
    elif args[1] == "add-books":
        if len(args) < 3:
            print("Missing the paths to the excel files containing the texts from the books to add")
        else:
            for path in args[2:]:
                COMMAND["add-books"](path)

if __name__ == "__main__":
    main()
