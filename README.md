# Bako: Voice-based Reading Assistance Library

## TODO:
- Logging Modules

## Bako API Pre-Documentation

### Server URL (Waiting for deployment)

```
http://127.0.0.1:8000
```

### Endpoints

#### Account Creation

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

#### Login

- **URL**: `/login/`
- **Method**: `POST`
- **Parameters**:
  - `username` (string): The username of the Reader
  - `password` (string): The password of the Reader
- **Response**:
  - `status` (bool): Indicates success or failure
  - `msg` (string): A message describing the result
  - `data` (dict, optional): User data (document) if login is successful

#### Get User Data

- **URL**: `/user/`
- **Method**: POST
- **Parameters**:
  - `username` (string): The username of the Reader
- **Response**:
  - `status` (bool): Indicates success or failure
  - `msg` (string): A message describing the result
  - `data` (dict, optional): User data (document) if retrieval is successful.

#### Change Username

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

#### Change Password

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

#### Account Deletion

- **URL**: `/account_deletion/`
- **Method**: `POST`
- **Parameters**:
  - `username` (string): The username of the Reader
  - `password` (string): The password of the Reader
- **Response**:
  - `status` (bool): Indicates success or failure
  - `msg` (string): A message describing the result
  - `data` (NoneType): No data returned

#### Get Book

- **URL**: `/book/`
- **Method**: `POST`
- **Parameters**:
  - `title` (string): The title of the book
- **Response**:
  - `status` (bool): Indicates success or failure
  - `msg` (string): A message describing the result
  - `data` (dict, optional): Book data if retrieval is successful

#### Get Catalog

- **URL**: `/catalog/`
- **Method**: `POST`
- **Parameters**: None
- **Response**:
  - `status` (bool): Indicates success or failure
  - `msg` (string): A message describing the result
  - `data` (dict): Catalog data containing `num_books` and `titles`

#### Bookmark

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

#### Mark Book as Completed

- **URL**: `/book_completed/`
- **Method**: `POST`
- **Parameters**:
  - `username` (string): The name of the user
  - `book_title` (string): Title of the book
- **Response**:
  - `status` (bool): Indicates success or failure
  - `msg` (string): A message describing the result
  - `data` (dict, optional): Updated user data if marking as completed is successful

#### Calculate Score

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

### Example Request and Response

#### Example Request for Account Creation

```json
{
  "username": "testuser",
  "password": "password123",
  "firstname": "John",
  "surname": "Doe"
}
```

#### Example Response for Account Creation

```json
{
  "status": true,
  "msg": "New account successfully created",
  "data": null
}
```

### Additional Information

- All endpoints use the `POST` method and expect JSON-encoded request bodies.
- Responses are JSON-encoded and include a `status` key to indicate success or failure and a `msg` key for a descriptive message and a `data` key with returned data from operations if any.

This pre-documentation provides a concise overview of the available endpoints, their parameters, and expected responses. 

### Notes for the front end

- FrontEnd: One image per story book
  - To simplify database design, each book will be accompanied with only one image (usually the cover image). This image should be stored by the application (on device).

- FrontEnd: Story books are a scrollable list
  - The story books view from the HomeScreen (once reader logged in) is a scrollable list made with the catalog.

- FrontEnd: Story books should be visually distinguishable
  - In-progress, completed, and not started books should be visually distinguishable on the UI.