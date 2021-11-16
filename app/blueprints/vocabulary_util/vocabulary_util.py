from flask import Blueprint, request, Response
from app.blueprints.vocabulary_util.controller import VocabularyController
import json

vocabulary_controller = VocabularyController()


blueprint_vocabulary = Blueprint('vocabulary', __name__, url_prefix='/vocabulary')




# Set the route and accepted methods
@blueprint_vocabulary.route('/word', methods=['POST'])
def add_word():
    """
    Adds new word
        ---
        tags:
          - Word
        parameters:
          - name: word
            in: query
            type: string
            format: string
            required: true
        responses:
          200:
            description: Returns "True", if successful
            examples:
               'True'
          400:
            description: Given word is already in vocabulary
        """
    word = request.args.get("word")
    if word:
        word = word.strip()
    else:
        return Response("No word given", status=400)
    result = vocabulary_controller.add_word(word)
    return Response(result["description"], status=result["http_code"])

@blueprint_vocabulary.route('/words', methods=['POST'])
def add_words():
    """
    Adds all given words to the dictionary. If the word is already in the dictionary, it ignores it.
        ---
        tags:
          - Words
        parameters:
          - name: words
            in: body
            description: "Words passed to the vocabulary"
            required: true
            "schema": {
                "$ref": "#/definitions/Words"
                }
        definitions:
          Words:
            type: object
            properties:
              words:
                type: array
                items:
                  $ref: '#/definitions/Word'
          Word:
            type: string
        responses:
          200:
            description: Returns "True", if successful
            examples:
               'True'
          400:
            description: Incorrect JSON file
        """
    words = []
    try:
        words = json.loads(request.get_data(as_text=True)).get("words")
    except json.JSONDecodeError as e:
        return Response("Bad request", status=400)

    vocabulary_controller.add_words(words)
    return "Ok"

@blueprint_vocabulary.route('/words', methods=['PUT'])
def replace_words():
    """
        Replaces vocabulary with given words
            ---
            tags:
              - Words
            parameters:
              - name: words
                in: body
                description: "Words passed to the vocabulary"
                required: true
                "schema": {
                    "$ref": "#/definitions/Words"
                    }
            responses:
              200:
                description: Returns "Ok", if successful
                examples:
                   'Ok'
              400:
                description: Incorrect JSON file
            """
    words = []
    try:
        words = json.loads(request.get_data(as_text=True)).get("words")
    except json.JSONDecodeError as e:
        return Response("Bad request", status=400)

    vocabulary_controller.replace_words(words)
    return "Ok"


@blueprint_vocabulary.route('/word/count', methods=['GET'])
def get_words_count():
    """
    Gets word count
        ---
        tags:
          - Word
        parameters:
          - name: letters
            in: query
            type: string
            format: string
            required: true
        responses:
          200:
            description: Returns a quantity, if successful
            examples:
               7
          400:
            description: No letters given
        """
    letters = request.args.get("letters")
    if letters:
        letters = letters.strip()
    else:
        return Response("No letters given", status=400)
    result = vocabulary_controller.count_filtered_words(letters)
    return Response(result["description"], status=result["http_code"])



@blueprint_vocabulary.route('/words', methods=['GET'])
def get_words():
    """
    Gets words which have exactly or more given letters; 10 words per page
        ---
        tags:
          - Words
        parameters:
          - name: letters
            in: query
            type: string
            format: string
            required: true
          - name: page
            in: query
            type: integer
            required: false
        responses:
          200:
            description: Returns , if successful
            examples:
               'True'
          400:
            description: No letters given
        """
    letters = request.args.get("letters")
    try:
        page = int(request.args.get("page"))
    except Exception:
        page = 1
    if not page:
        page = 1
    if letters:
        letters = letters.strip()
    else:
        return Response("No letters given", status=400)
    result = vocabulary_controller.get_filtered_words(letters, page)
    return Response(result["description"], status=result["http_code"])

