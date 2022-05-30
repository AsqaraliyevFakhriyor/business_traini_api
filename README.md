## Business API for www.alisherisayev.netlify.app

### This project was maded only for learning purposes!😉

### Project deployed on heroku
> https://alisherisayev.herokuapp.com

## Models:
1. User's model with `username`, `email`, `password` etc.
2. Application's model with columns `username`, `email`, `phone_number`, `business_type`

## Endpoinds: 🍔
1. **`POST`** ***/api/register***
    > User sign up
    with this endpoint users can register to the WebSite

    **Request**
    ```json
        {
            "username": "<USERNAME>",
            "email": "<EMAIL_ADDRESS",
            "password": "<PASSWORD>"
        }
    ```
    **Response**
    ```json
        {
            "status_code": 200,
            "user_data": {
                "id": "<ID>",
                "username": "<USERNAME",
                "email": "<EMAIL_ADDRESS>"
            }
        }
    ```
    **If user for `<USERNAME>` already exists, it will return `400 Bad Request`**
    
    **Response**
    ```json
        {
          "username": [
            "A user with that username already exists."
          ]
        }
    ```

2. **`POST`** ***/api/login***

    > Endpoint to log in, it will generate jwt token then store it to  COOKIES

    **Request**
    ```json
        {
            "username": "<NAME>",
            "password": "<PASSWORD>"
        }
    ```
    **If there are no `errors` it will return `200 OK` and set the generated token to cookies.**
    
    **Response**
    ```json
        {
          "status_code": 200
        }
    ```
    
    **If password is incorrect for `<USERNAME>`, it will return `403 Forbidden`**
    
    **Response**
    ```json
        {
          "detail": "wrong password for <USERNAME>"
        }
    ```
3. **`GET`** ***/api/user***

    > Endpoint to get logged user's info

    **If token is not expired, it will return `200 OK`**
    
    **Response**
    ```json
        {
            "status_code": 200,
            "user_data": {
                "id": <ID>,
                "username": "<USERNAME>",
                "email": "<EMAIL_ADDRESS>"
            }
        }
    ```
    
    **If token is expired, it will return `401 UNAUTHORIZED`**
    
    **Response**
    ```json
        {
            "detail": "token expired",
        }
    ```
    
    **If token is missing or user logged out, it will return `401 UNAUTHORIZED`**
    
    **Response**
    ```json
        {
            "detail": "token missing",
        }
    ```
    
4. **`POST`** ***/api/logout***
    
    > Endpoint to log out, delete COOKIE

    **Response**
    ```json
        {
            "status_code": 200
        }
        
5. **`GET`** ***/api/applications***
    
    > Endpoint to get list of applications
    
    **Response**
    ```json
        {
            "status_code": 200,
            "applications": [
                {
                    "id": <ID>,
                    "username": "<USERNAME>",
                    "email": "<EMAIL_ADDRESS",
                    "phone_number": "<PHONE_NUMBER>",
                    "business_type": "<BUSSINES_TYPE",
                    "contacted": <BOOLEAN>
                },
                {
                    "id": <ID>,
                    "username": "<USERNAME>",
                    "email": "<EMAIL_ADDRESS",
                    "phone_number": "<PHONE_NUMBER>",
                    "business_type": "<BUSSINES_TYPE",
                    "contacted": <BOOLEAN>
                },
            ],
            "user": {
                "id": <ID>,
                "username": "<USERNAME>",
                "email": "<EMAIL_ADDRESS>"
            }
        }
    ```
    
6. **`POST`** ***/api/create/application***

    > Endpoint to create new application
    
    **Request**
    ```json
        {
            "username": "<USERNAME>",
            "email": "<EMAIL_ADDRESS>",
            "phone_number": "<PHONE_NUMBER>",
            "business_type": "<BUSINESS_TYPE>",
            "contacted": <BOOOLEN>
        }
    ```
    
    **Response**
    ```json
        {
          "status_code": 200,
          "application": {
            "id": <ID>,
            "username": "<USERNAME>",
            "email": "<EMAIL_ADDRESS>",
            "phone_number": "<PHONE_NUMBER>",
            "business_type": "<BUSINESS_TYPE>",
            "contacted": <BOOLEAN>
          }
        }
    ```
    
7. **`DELETE`** ***/api/delete/application***

    > Endpoint to delete existing application by id

    **Request**
    ```json
        {
            "application_id": <ID>
        }
    ```
    
    **Response**
    ```json
        {
            "status_code": 200,
            "application_id": <ID>
        }
    ```
    **If application with <ID> does not exists, it will return `404 Not Flound`**
    
8. **`POST`** ***/api/contacted/application***

    > Endpoint to change contacted column in application

    **Request**
    ```json
        {
            "application_id": <ID>
        }
    ```
    
    **Response**
    ```json
        {
            "status_code": 200,
            "application_id": <ID>
        }
    ```
    **If application with <ID> does not exists, it will return `404 Not Flound`**
    



## Installing Dependencies
 - [x] Python-3.9.5 (recommended)

### Virtual Environment

    ```bash
        cd project_directory
        pip install venv
        python -m venv venv
        source venv/Script/active
    ```

### PIP Dependecies
> Once you have your **venv** setup and running, install dependencies by navigating
> to the root directory and running:
    ```bash
        pip install -r requirements.txt
    ```
>This will install all of the required packages included in the requirements.txt
>file.

### Exporting ENV VARIABES form setup.sh file
```bash
    source setup.sh
```

### Local Database Setup
> Once you create the database, open your terminal, navigate to the root folder, and run:
```bash
    python manage.py makemigrations
    python manage.py migrate
```


## Runing the Server
> From within the root directory, first ensure you're working with your created
venv. To run the server, execute the following:
```bash
    python manage.py runserver
```

### Project is ready to deploy HEROKU but you need to add POSGRESQL addon to your [`HEROKU`](https://heroku.com)  aplications


