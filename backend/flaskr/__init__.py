import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category, db

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    app.app_context().push()
    

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    CORS(app)
    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type': 'application/json', 'charset': 'utf-8, Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS, PATCH"
        )
        return response
    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """
    @app.route('/categories')
    def get_categories():  
        try:
            categories = db.session.query(Category).all()
            if len(categories) == 0:
                abort (404)
            else:
                return jsonify({
                    "success":True,
                    "categories": {category.id:category.type for category in categories},
                    "total_categories": len(categories)
                })
        except:
            db.session.rollback()
        finally:
            db.session.close()

    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """
    @app.route('/questions')
    def get_questions():
        error = False
        page = request.args.get('page', 1, type=int)
        try:
            questions = db.session.query(Question).order_by(Question.id).\
                paginate(page=page, per_page=QUESTIONS_PER_PAGE, error_out=False)
            categories = db.session.query(Category).all()
            formatted_questions = [question.format() for question in questions]
            if questions is None:
                abort(404)
            else:
                return jsonify({
                    'questions': formatted_questions,
                    'totalQuestions': questions.total,
                    'categories': {category.id:category.type for category in categories},
                    'currentCategory':None,
                })
        except:
            error = True
            if error:
                abort(404)
            db.session.rollback()
        finally:
            db.session.close()

    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """
    @app.route('/questions/<int:question_id>', methods=["DELETE"])
    def delete_question(question_id):
        error=False
        try:
            question = db.session.query(Question).filter(Question.id == question_id).one_or_none()
            if question is None:
                abort (404)
            else:
                question.delete()
                return jsonify({
                'success':True, 
                'deleted_question_id': question_id
                })
        except:
            error=True
            if error:
                abort(404)
            db.session.rollback()
        finally:
            db.session.close()
            
    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """
    @app.route('/questions', methods=["POST"])
    def create_new_question():
        error = False
        body = request.get_json()
        try:
            question = body.get("question", None)
            answer = body.get("answer", None)
            category= body.get("category", None)
            difficulty = body.get("difficulty", None)
            question = Question(question=question, answer=answer, category=category,difficulty=difficulty)
            question.insert()
        except:
            error = True
            db.session.rollback()
        finally:
            if error:
                abort(422)
            db.session.close()
            return jsonify(body)

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """
    @app.route('/questions/search', methods = ["POST"])
    def get_questions_by_searchTerm():
        error = False
        page = request.args.get('page', 1, type=int)
        search =request.get_json()["searchTerm"]
       
        try:
            questions = db.session.query(Question).filter(Question.question.ilike(f'%{search}%')).\
                paginate(page=page, per_page=QUESTIONS_PER_PAGE, error_out=False)
            formatted_question = [question.format() for question in questions]
            
            return jsonify({
                "success":True,
                "questions":formatted_question,
                'totalQuestions': questions.total,
                "currentCategory":None
            })
        except:
            error=True
            if error:
                abort(404)
            db.sessio.rollback()
        finally:
            db.session.close()
          

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    @app.route('/categories/<category_id>/questions')
    def get_questions_by_category(category_id):
        error=False
        try:
            questions=db.session.query(Question).filter(Question.category==str(category_id)).all()
            formatted_questions=[question.format() for question in questions]

            return jsonify({
                'success':True,
                'questions':formatted_questions,
                "currentCategory":category_id,
                'total_questions':len(questions)
            }) 
        except:
            error=True
            if error:
                abort(404)
            db.session.rollback()
        finally:
            db.session.close()
        
 

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """
    # A POST endpoint to get questions to play the quiz
    @app.route("/quizzes", methods=["POST"])
    def play_quiz():
        try:
        # Get the JSON data from the request
            data = request.get_json()

            # Check if 'quiz_category' and 'previous_questions' keys exist in the JSON data
            if 'quiz_category' not in data or 'previous_questions' not in data:
                abort(422)

            quiz_category = data['quiz_category']
            previous_questions = data['previous_questions']

            # Determine the available questions based on the category
            if quiz_category['type'] == 'click':
                available_questions = Question.query.filter(
                    Question.id.notin_(previous_questions)
                ).all()
            else:
                available_questions = Question.query.filter_by(category=quiz_category['id']).filter(
                    Question.id.notin_(previous_questions)
                ).all()

            # Choose a random question from the available questions, if any
            if available_questions:
                random_question = random.choice(available_questions).format()
            else:
                random_question = None

            return jsonify({"success": True, "question": random_question})

        except Exception as e:
            # Handle exceptions with a more informative response and status code
            return jsonify({"success": False, "error": str(e)}), 422



    """
    
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    @app.errorhandler(400)
    def bad_request(error):
        return (jsonify({
            'success': False,
            'error_code': 400,
            'error_message':'Bad Request'
        }), 400)

    @app.errorhandler(404)
    def resource_not_found(error):
        return (jsonify({
            'success': False,
            'error_code': 404,
            'error_message':'Resource not found'
        }), 404)
    
    @app.errorhandler(405)
    def unallowed_method(error):
        return (jsonify({
            'success': False,
            'error_code': 405,
            'error_message':'Method not allowed'
        }), 405)
    
    @app.errorhandler(422)
    def unprocessable(error):
        return (jsonify({
            'success': False,
            'error_code': 422,
            'error_message':'Request not processable'
        }), 422)
    

    return app

