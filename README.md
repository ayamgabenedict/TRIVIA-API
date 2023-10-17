# API Development and Documentation Final Project

## Trivia API App

A bunch of team members got the idea to hold trivia on a regular basis and thus, created a webpage to manage the trivia app and play the game.
The Trivia API App allows team members to see who is is the most knowledgeable of the bunch by answering correctly the series of questions. Hope you have fun whiles learning from this trivia.

**Home Page**
![homepage](/homepage.png)

## What can you do with this App?

The Trivia API app has the following functionalities. It allows users to:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

# Getting Started

### The Frontend

The [frontend](./frontend/README.md) directory contains a complete React frontend to consume the data from the Flask server.

> _tip_: this frontend is designed to work with [Flask-based Backend](../backend) so it will not load successfully if the backend is not working or not connected. It is advisable to **stand up the backend first**, you can then test using Postman or curl.

> View the [Frontend README](./frontend/README.md) for more details.

#### Installing Dependencies

1. **Installing Node and NPM**
   This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

2. **Installing project dependencies**
   This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

> _tip_: `npm i`is shorthand for `npm install``

## Required Tasks

### Running Your Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use `npm start`.

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.

```bash
npm start
```

### The Backend

The [backend](./backend) directory contains a complete Flask App, running on the Flask server.

> View the [backend README](./backend/README.md) for more details.

#### Installing Dependencies

1.  **Python 3.7**

    Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2.  **Virtual Enviornment**

    We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3.  **PIP Dependencies**

    Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages necessary for your Flask App to up and running.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle our PostgreSQL database.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup

With Postgres running and from the `backend` directory, run the following in the terminal in order to restore the database:

```bash
psql trivia < trivia.psql
```

## Running the backend server

Ensure you are working in your virtual environment.
Navigate to your `backend` directory, open terminal and run the server by executing the commands:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

For windows, run this instead:

```bash
set FLASK_APP=flaskr
set FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application.

## Tasks

| No  | Completed | Task Description                                                                                                                                                                                                                                   |
| :-- | :-------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.  |  **[x]**  | Use Flask-CORS to enable cross-domain requests and set response headers..                                                                                                                                                                          |
| 2.  |  **[x]**  | Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. it.                                  |
| 3.  |  **[x]**  | Create an endpoint to handle GET requests for all available categories.                                                                                                                                                                            |
| 4.  |  **[x]**  | Create an endpoint to DELETE question using a question ID.                                                                                                                                                                                         |
| 5.  |  **[x]**  | Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score.                                                                                                                        |
| 6.  |  **[x]**  | Create a POST endpoint to get questions based on category.                                                                                                                                                                                         |
| 7.  |  **[x]**  | Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.                                                                                            |
| 8.  |  **[x]**  | Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. |
| 9.  |  **[x]**  | Create error handlers for all expected errors including 400, 404, 422 and 500.                                                                                                                                                                     |

## API

GET `\categories`
Fetches a dictionary of all available categories

- _Request parameters:_ none
- _Example response:_

```
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "success": true,
    "total_categories": 6
}

```

GET `\questions?page=<page_number>`
Fetches a paginated dictionary of questions of all available categories

- _Request parameters (optional):_ page:int
- _Example response:_

```{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "currentCategory": null,
    "questions": [
        {
            "answer": "Agra",
            "category": 3,
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        },
        {
            "answer": "Escher",
            "category": 2,
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist-initials M C was a creator of optical illusions?"
        }
    ],
    "totalQuestions": 18
}
```

DELETE `/questions/<question_id>`
Delete an existing questions from the repository of available questions

- _Request arguments:_ question_id:int
- _Example response:_

```
{
    "deleted_question_id": 37,
    "success": true
}
```

POST `/questions`
Add a new question to the repository of available questions

- _Request body:_ {question:string, answer:string, difficulty:int, category:string}
- _Example response:_

```
[
    {
        "answer": "1957",
        "category": 1,
        "difficulty": 3,
        "question": "Which year did Ghana get her independence?"
    },
    {
        "created": 67,
        "success": true
    }
]
```

POST `/questions/search`
Fetches all questions where a substring matches the search term (not case-sensitive)

- _Request body:_ {searchTerm:"title"}
- _Example response:_

```
{
    "currentCategory": null,
    "questions": [
        {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }
    ],
    "success": true,
    "totalQuestions": 2
}
```

GET `/categories/<int:category_id>/questions`
Fetches a dictionary of questions for the specified category

- _Request argument:_ category_id:int
- _Example response:_

```
{
  "current_category": 1,
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
  ],
  "success": true,
  "total_questions": 2
}
```

POST `/quizzes`
Fetches one random question within a specified category. Previously asked questions are not asked again.

- _Request body:_ {previous_questions: arr, quiz_category: {id:int, type:string}}
- _Example response_:

```
{
  "question": {
    "answer": "The Liver",
    "category": 1,
    "difficulty": 4,
    "id": 20,
    "question": "What is the heaviest organ in the human body?"
  },
  "success": true
}
```

## Testing

To run the tests, run

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Author

- [Benedict Ayamga](https://github.com/ayamgabenedict)

## Acknowledgements

- [Udacity](https://www.udacity.com/) The project was developed as a part of Udacity's Full Stack Nanodegree Program.

## Screenshots

**Playing trivia**

![play_trivia1](play_1.PNG)

![play_trivia2](play_2.PNG)

**Search a question**
![search](search_1.PNG)

![search](search_2.PNG)

**Add a question**
![add](add_new_trivia_question.PNG)
