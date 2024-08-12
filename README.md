# Bako: Voice-based Reading Assistance Library

Bako is a library designed to provide voice-based reading assistance through a set of API endpoints. This README file will guide you through setting up the server, understanding the available endpoints, and the required configuration for development and deployment.

## Table of Contents

- [Installation](#installation)
- [Launching the Local Server](#launching-the-local-server)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Installation

Before you begin, ensure you have Python installed on your machine. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/mlsftwrs/bako.git
cd bako
pip install . -r requirements.txt
```

## Launching the Local Server

You can launch the server using the following command:

```bash
python bako_api/manage.py runserver 192.168.0.66:8000
```

## API Endpoints

### Account Creation

- **URL**: `/account_creation/`
- **Method**: `POST`
- **Parameters**:
  - `username` (string): The username of the new Reader
  - `password` (string): The password of the new Reader
  - `firstname` (string, optional): The first name of the User
  - `surname` (string, optional): The last name of the User
- **Response**:
  - `status` (bool): Indicates success or failure
  - `msg` (string): A message describing the result
  - `data` (NoneType): No data returned

### Login

- **URL**: `/login/`
- **Method**: `POST`
- **Parameters**:
  - `username` (string): The username of the Reader
  - `password` (string): The password of the Reader
- **Response**:
  - `status` (bool): Indicates success or failure
  - `msg` (string): A message describing the result
  - `token` (string): Authentication token for further requests

### Get User Data

- **URL**: `/user/`
- **Method**: POST
- **Parameters**:
  - `username` (string): The username of the Reader
- **Response**:
  - `status` (bool): Indicates success or failure
  - `msg` (string): A message describing the result
  - `data` (dict, optional): User data (document) if retrieval is successful.

### Change Username

- **URL**: `/change_username/`
- **Method**: `POST`
- **Parameters**:
  - `current_username` (string): Current username of the user
  - `new_username` (string): New username
  - `password` (string): Confirmation password
- **Response**:
  - `status` (bool): Indicates success or failure
  - `msg` (string): A message describing the result
  - `data` (dict, optional): Updated user data if username change is successful

### Change Password

- **URL**: `/change_password/`
- **Method**: `POST`
- **Parameters**:
  - `username` (string): Current username of the user
  - `current_password` (string): Current password
  - `new_password` (string): New password
- **Response**:
  - `status` (bool): Indicates success or failure
  - `msg` (string): A message describing the result
  - `data` (dict, optional): Updated user data if password change is successful

### Account Deletion

- **URL**: `/account_deletion/`
- **Method**: `POST`
- **Parameters**:
  - `username` (string): The username of the Reader
  - `password` (string): The password of the Reader
- **Response**:
  - `status` (bool): Indicates success or failure
  - `msg` (string): A message describing the result
  - `data` (NoneType): No data returned

### Get Book (deprecated)

- **URL**: `/book/`
- **Method**: `POST`
- **Parameters**:
  - `title` (string): The title of the book
- **Response**:
  - `status` (bool): Indicates success or failure
  - `msg` (string): A message describing the result
  - `data` (dict, optional): Book data if retrieval is successful

### Get Catalog (deprecated)

- **URL**: `/catalog/`
- **Method**: `POST`
- **Parameters**: None
- **Response**:
  - `status` (bool): Indicates success or failure
  - `msg` (string): A message describing the result
  - `data` (dict): Catalog data containing `num_books` and `titles`

### Bookmark

- **URL**: `/bookmark/`
- **Method**: `POST`
- **Parameters**:
  - `username` (string): The name of the user
  - `book_title` (string): Title of the book
  - `book_page_ref` (string): The page reference user stopped at
- **Response**:
  - `status` (bool): Indicates success or failure
  - `msg` (string): A message describing the result
  - `data` (dict, optional): Updated user data if bookmarking is successful

### Mark Book as Completed

- **URL**: `/book_completed/`
- **Method**: `POST`
- **Parameters**:
  - `username` (string): The name of the user
  - `book_title` (string): Title of the book
- **Response**:
  - `status` (bool): Indicates success or failure
  - `msg` (string): A message describing the result
  - `data` (dict, optional): Updated user data if marking as completed is successful

### Calculate Score (deprecated)

- **URL**: `/calculate_score/`
- **Method**: `POST`
- **Parameters**:
  - `username` (string): The name of the user
  - `book_title` (string): Title of the book
  - `num_errors` (int, optional): Number of errors made
  - `reading_time` (float, optional): Time taken to read
- **Response**:
  - `status` (bool): Indicates success or failure
  - `msg` (string): A message describing the result
  - `data` (dict, optional): Updated user data if score calculation is successful

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## TODO:

- Integrate Logging features
