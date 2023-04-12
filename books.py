from fastapi import FastAPI, Body

# FastAPI - Swagger UI: http://127.0.0.1:8000/docs

app = FastAPI()


'''
GET HTTP Request Method
request: 127.0.0.1:8000/first_api
'''
@app.get("/first_api")
async def first_api():
    return {'message': 'Hi There!'}


BOOKS = [
    {'title': 'title one', 'author': 'author one', 'category': 'science'},
    {'title': 'title two', 'author': 'author two', 'category': 'science'},
    {'title': 'title three', 'author': 'author three', 'category': 'history'},
    {'title': 'title four', 'author': 'author four', 'category': 'math'},
    {'title': 'title five', 'author': 'author five', 'category': 'math'},
    {'title': 'title six', 'author': 'author two', 'category': 'math'}
]


'''
creating books directory
request: 127.0.0.1:8000/books
'''
@app.get("/books")
async def read_all_books():
    return BOOKS


'''
PATH Parameters: request parameters that have been attached to the url to find information based on location

Function to return info of book with the given title like "Title One"
request: 127.0.0.1:8000/books/title%20one
'''
@app.get("/books/{book_title}")
async def read_book_by_title(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


'''
Query Parameter: a way to filter data based on the url provided 
and we can filter this data after the question mark.

Function to filter books by category by query
request: 127.0.0.1:8000/books/?category=math
'''
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


'''
a new API endpoint to get all books from a specific author
using query parameters
request example: 127.0.0.1:8000/books/byauthor?author=author%20two
'''
@app.get("/books/byauthor")
async def read_books_from_author(author:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)

    return books_to_return



'''
Function that searches by author and filter by category using path parameter
request: 127.0.0.1:8000/books/author%20four/?category=math
'''
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


''' 
POST HTTP Request Method: creating new book and adding ti the end of BOOKS list
request url: 127.0.0.1:800/books/create_book
request body: {"title": "title seven","author": "author two","category": "math"}
'''
@app.post("/book/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)



'''
PUT HTTP Request Method: update data of a book
request url: 127.0.0.1:800/books/update_book
request body: {"title": "title six","author": "author two","category": "history"}
'''
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book



'''
DELETE HTTP Request Method: delete data of a book by title
request url: 127.0.0.1:800/books/update_book
request body: {"title": "title six","author": "author two","category": "history"}
'''
@app.delete("/books/book_title")
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

