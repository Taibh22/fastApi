# fastApi
This repository contains a FastAPI application with several endpoints and dependencies. The application includes user authentication, token generation, and CRUD operations for tasks.

Installation
To run the application, follow these steps:

Clone the repository:

bash
Copy
git clone https://github.com/your/repo.git
Install the dependencies using pip:

bash
Copy
pip install -r requirements.txt
Run the application:

bash
Copy
uvicorn main:app --reload
The application will be accessible at http://localhost:8000.

Endpoints
/all - Get details of currently logged in user
Method: GET
Summary: Get details of the currently logged in user.
Response:
UserOut schema with user details.
/signup - Create new user
Method: POST
Summary: Create a new user.
Request:
UserAuth schema with email and password.
Response:
UserOut schema with the created user details.
/login - Create access and refresh tokens for user
Method: POST
Summary: Create access and refresh tokens for a user.
Request:
OAuth2PasswordRequestForm with username and password.
Response:
TokenSchema with the access and refresh tokens.
/ - Create user
Method: POST
Summary: Create a new user.
Request:
CreateUser schema with name and password.
Response:
UserOutput schema with the created user details.
/task - Create a task
Method: POST
Summary: Create a new task.
Request:
TaskCreate schema with title and description.
Response:
Task schema with the created task details.
/task/{id} - Read a task
Method: GET
Summary: Get details of a specific task.
Path parameters:
id: int - The ID of the task to retrieve.
Response:
Task schema with the task details.
/task/{id} - Update a task
Method: PUT
Summary: Update the details of a specific task.
Path parameters:
id: int - The ID of the task to update.
Request:
str - The updated task title.
Response:
Task schema with the updated task details.
/task/{id} - Delete a task
Method: DELETE
Summary: Delete a specific task.
Path parameters:
id: int - The ID of the task to delete.
Response:
No content.
/task - Read all tasks
Method: GET
Summary: Get details of all tasks.
Response:
List of Task schemas with the task details.
Dependencies
The application uses the following dependencies:

FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.
SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) for Python.
Pydantic: A library for data validation and serialization using Python type hints.
jose: A JavaScript Object Signing and Encryption (JOSE) library for Python.
uvicorn: An ASGI server implementation, using the uvloop and httptools libraries.
replit: A Python library for accessing the Replit database.
Database
The application uses an SQLite database. The database file is fastapidb.db. The models for the database tables are defined in models.py.

Utilities
The application includes utility functions in utils.py:

create_access_token: Generates an access token.
create_refresh_token: Generates a refresh token.
get_hashed_password: Hashes a password.
verify_password: Verifies a password.
Dependencies
The application includes dependency functions in deps.py:

get_current_user: Retrieves the current user based on the access token.
OAuth
The application includes OAuth-related functions in oauth.py:

create_access_token: Generates an access token.
verify_token_access: Verifies an access token.
get_current_user: Retrieves the current user based on the access token.
Schemas
The application includes several Pydantic schemas in schemas.py:

TaskCreate: Schema for creating a task.
Task: Schema for a task.
CreateUser: Schema for creating a user.
UserLogin: Schema for user login.
Token: Schema for an access token.
DataToken: Schema for token data.
UserOutput: Schema for user details.
Contributing
Contributions to the application are welcome. If you find any issues or would like to add new features, please submit a pull request or open an issue.
