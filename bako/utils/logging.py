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
import logging

### Basic logging configuration

CUSTOM_LOGGER = logging.getLogger(name=__name__)
CUSTOM_LOGGER.setLevel("DEBUG")

# Define Handlers
console_handler = logging.StreamHandler()

file_handler = logging.FileHandler(
    filename=".app.log",
    encoding="utf-8"
)

# Define a Unique Formatter
formatter = logging.Formatter(
    fmt="{asctime} - {levelname} - {filename} - {funcName} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M"
)

console_handler.setLevel("INFO")
console_handler.setFormatter(formatter)
file_handler.setLevel("DEBUG")
file_handler.setFormatter(formatter)

# Add Handlers
CUSTOM_LOGGER.addHandler(console_handler)
CUSTOM_LOGGER.addHandler(file_handler)
