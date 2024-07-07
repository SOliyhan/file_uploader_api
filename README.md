## File Uploader API

This is a backend project for uploading CSV file through google spreadsheet url to the database with filtering support. The technologies used in the project are Django, Python, DRF, JWT, SQLite.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/SOliyhan/file_uploader_api.git
   ```

2. Navigate to the project directory:
   ```sh
   cd file_uploader_api
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
2. Access the Admin Interface:
   Open your web browser and navigate to http://127.0.0.1:8000/admin/ (locally). Log in using the superuser credentials.
3. Add a New User:
   Once logged in, navigate to the Users section.
   Click on Add to create a new user.
   Fill in the username, password, and other required fields.
   Save the new user.
4. Start the server (for locall):
   ```sh
    python manage.py runserver
   ```
5. The API will be running at `http://localhost:8000` (locally).
6. Use tools like Postman, Thunder Client, etc to access the endpoints.

## API Endpoints

### Homepage

- **GET /** : Homepage of the File Uploader API.

**Example Response:**

```json
{
  "message": "Welcome to the File Uploader API. Read documentation on github for more details"
}
```

**Permissions:**

- AllowAny - Any user can access this endpoint.

### Token

- **POST api/token**: generate a token for a existing user.
- **POST api/token/refresh**: generate access token using a refresh token.

**Permissions:**

- AllowAny - Any user can access these endpoint.

**1. Generating Token (POST):**

Endpoint: `/api/token`

Example Request:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

Example Response (success):

```json
{
  "access": "<your_access_token>",
  "refresh": "<your_refresh_token>"
}
```

**2. Generating Access Token from Refresh Token (POST):**

Endpoint: `/api/token`

Example Request:

```json
{
  "refresh": "<your_refresh_token>"
}
```

Example Response (success):

```json
{
  "access": "<your_access_token>"
}
```

### Upload

- **POST /upload**: Upload CSV file to database.
- **POST /search**: This endpoint accepts parameters in the form of field, value to query the data from csv. The service support query by any field in the csv.

**1. File Upload (POST):**

Endpoint: `/upload`

- Headers: `Authorization` : `Bearer <your_access_token>` generated from /api/token`
- Body: multipart/form-data;
  **Description:**

This endpoint allows users to upload the csv file of the mentioned format on the application. Upon successfully filing request body, a new table is created in the database.

**Permissions:**

- IsAuthenticated - only authenticated users are able to upload files to database

Example Request:

```
Form-Fields:
field name ---> "file_url"
field value ---> "<your google spreadsheet link>"
```

Example Response (success):

```json
{
  "message": "File uploaded successfully"
}
```

**2. Search in database (GET):**

Endpoint: `/search`

- Headers: `Authorization` : `Bearer <your_access_token>` generated from /api/token`
- Body: application/json;

**Description:**

This endpoint allows users to query the csv file in the database with provided field and value of the mentioned format on the application. Upon successfully filing request body, user can view the search result in json format.

**Permissions:**

- IsAuthenticated - only authenticated users are able to upload files to database

Example Request:

```json
{
  "field": "name",
  "value": "Max"
}
```

Example Response (success):

```json
[
  {
    "app_id": 12140,
    "name": "Max Payne",
    "release_date": "2011-01-06",
    "required_age": 17,
    "price": "3.49",
    "dlc_count": 0,
    "about_the_game": "<description about game>",
    "supported_languages": "['English']",
    "on_windows": true,
    "on_mac": false,
    "on_linux": false,
    "positive": 9516,
    "negative": 1114,
    "score_rank": null,
    "developers": "Remedy Entertainment",
    "publishers": "Rockstar Games",
    "categories": "Single-player",
    "genres": "Action",
    "tags": "Action,Noir,Classic,Third-Person Shooter,Bullet Time,Story Rich,Atmospheric,Dark,Third Person,Singleplayer,Shooter,Great Soundtrack,Detective,Cinematic,Linear,Crime,Violent,Adventure,Horror,Psychological Horror"
  }
]
```
