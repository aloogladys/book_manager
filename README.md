# book_manager
simple django application to manage books

Features
1. Book Model with the following fields :
     `title`, `author`, `publication_date`, `isbn`, and `summary`.
   
3. API Endpoints
  - `GET /books/`: Retrieve all books.
  - `POST /books/`: Create a new book.
  - `GET /books/{id}/`: Retrieve a specific book.
  - `PUT /books/{id}/`: Update a specific book.
  -`PATCH /books/{id}/`: Update a specific book.
  - `DELETE /books/{id}/`: Delete a specific book.

3. Validation 
  - `isbn` must be unique and either 10 or 13 digits.
  - `publication_date` must be in the past.

Code Structure
- `book_app/models.py`: Defines the `Book` model.
- `book_app/serializers.py`: Handles serialization and validation.
- `book_app/views.py`: Implements the API views.
- `book_app/urls.py`: Defines the URL routes.
- `book_app/tests.py`: Contains unit tests for the API.

Running the Project
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run migrations: `python manage.py migrate`.
4. Start the server: `python manage.py runserver`.
5. Access the API at `http://localhost:8000/books/`.

used drf- yet another swagger (drf-yasg) for the ui of the api
