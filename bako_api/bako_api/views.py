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
import json
from django.http import JsonResponse
import django.http
from django.views.decorators.csrf import csrf_exempt
from bako.api import create_reader_account, login_reader_user, delete_account,\
    mark_book_as_completed, bookmark, get_book, get_catalog, calculate_score,\
    edit_password, edit_username

@csrf_exempt
def create_account(request: django.http.request.HttpRequest) -> JsonResponse:
    """ReaderUser Account creation endpoint

    Args:
        request (django.http.request.HttpRequest): _description_

    Returns:
        JsonResponse: _description_
    """
    if request.method == 'POST':
        user_data = json.loads(request.body)
        result = create_reader_account(**user_data)
        return JsonResponse(result)

@csrf_exempt
def login(request: django.http.request.HttpRequest) -> JsonResponse:
    """ReaderUser login endpoint

    Args:
        request (django.http.request.HttpRequest): _description_

    Returns:
        _type_: _description_
    """
    if request.method == "POST":
        login_data = json.loads(request.body)
        result = login_reader_user(**login_data)
        return JsonResponse(result)

@csrf_exempt
def change_username(request: django.http.request.HttpRequest) -> JsonResponse:
    """Changing Username endpoint

    Args:
        request (django.http.request.HttpRequest): _description_

    Returns:
        _type_: _description_
    """
    if request.method == 'POST':
        username_data = json.loads(request.body)
        result = edit_username(**username_data)
        return JsonResponse(result)

@csrf_exempt
def change_password(request: django.http.request.HttpRequest) -> JsonResponse:
    """Changing Password endpoint

    Args:
        request (django.http.request.HttpRequest): _description_

    Returns:
        _type_: _description_
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        result = edit_password(**data)
        return JsonResponse(result)

@csrf_exempt
def account_deletion(request: django.http.request.HttpRequest) -> JsonResponse:
    """Account deletion endpoint

    Args:
        request (django.http.request.HttpRequest): _description_

    Returns:
        _type_: _description_
    """
    if request.method == 'POST':
        account_deletion_data = json.loads(request.body)
        result = delete_account(**account_deletion_data)
        return JsonResponse(result)

@csrf_exempt
def score_calculation(request: django.http.request.HttpRequest) -> JsonResponse:
    """Calculate score endpoint

    Args:
        request (django.http.request.HttpRequest): _description_

    Returns:
        JsonResponse: _description_
    """
    if request.method == 'POST':
        score_data = json.loads(request.body)
        result = calculate_score(**score_data)
        return JsonResponse(result)

@csrf_exempt
def get_book_endpoint(request: django.http.request.HttpRequest) -> JsonResponse:
    """Get book endpoint

    Args:
        request (django.http.request.HttpRequest): _description_

    Returns:
        JsonResponse: _description_
    """
    if request.method == "POST":
        book_data = json.loads(request.body)
        result = get_book(**book_data)
        return JsonResponse(result)

@csrf_exempt
def mark_book_as_inprogress(request: django.http.request.HttpRequest) -> JsonResponse:
    """Book Marking Endpoint

    Args:
        request (django.http.request.HttpRequest): _description_

    Returns:
        JsonResponse: _description_
    """
    if request.method == "POST":
        data = json.loads(request.body)
        result = bookmark(**data)
        return JsonResponse(result)

@csrf_exempt
def book_completed(request: django.http.request.HttpRequest) -> JsonResponse:
    """Mark book as completed Endpoint
    
    Args:
        request (django.http.request.HttpRequest): _description_

    Returns:
        JsonResponse: _description_
    """
    if request.method == "POST":
        data = json.loads(request.body)
        result = mark_book_as_completed(**data)
        return JsonResponse(result)

@csrf_exempt
def catalog(request: django.http.request.HttpRequest) -> JsonResponse:
    """Get catalog Endpoint
    
    Args:
        request (django.http.request.HttpRequest): _description_

    Returns:
        JsonResponse: _description_
    """
    if request.method == "POST":
        result = get_catalog()
        return JsonResponse(result)
