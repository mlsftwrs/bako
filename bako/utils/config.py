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

import pathlib

# Development State
DEV_STATE = 1  # Toggle 1 for development 0 for Production

# Main Working Directory
PJ = pathlib.Path.joinpath
ROOT_DIR = pathlib.Path(__file__).parent.parent
HOME_DIR = PJ(pathlib.Path.home(), "bako_home")

# Database Configuration
## URI (Development)
DEV_CLIENT_NAME = "bakodb"

## Development Cluster URI
DEV_URI = "mongodb+srv://mlsftwrs:oaGbSd3Doe5gYELG@bakorm0.kuowxyy.mongodb.net/?retryWrites=true&w=majority&appName=bakoRM0" #"mongodb://localhost:27017/"
# TOOD: Replace current PROD URI with Project PROD URI
PROD_URI = "mongodb+srv://mlsftwrs:oaGbSd3Doe5gYELG@bakorm0.kuowxyy.mongodb.net/?retryWrites=true&w=majority&appName=bakoRM0"
CLUSTER_URI = DEV_URI if DEV_STATE else PROD_URI

# Loggging Configuration
LOG_MAIN = ROOT_DIR if DEV_STATE else HOME_DIR
LOG_MAIN_DIR = PJ(LOG_MAIN, "logs")
LOG_DEV_FILE = PJ(LOG_MAIN_DIR, "bako.dev.log")
LOG_PROD_FILE = PJ(LOG_MAIN_DIR, "bako.prod.log")
LOG_TEST_FILE = PJ(LOG_MAIN_DIR, "bako.test.log")

## CustomIDX
BDX = "tdx"  # Bako INDEX [Overwrite ObjectID]

# Collection IDs
COL_USER = "bako_user"
COL_BOOK = "bako_book"
