import logging

import azure.functions as func
import json

dictionary = {
    'a': 'alpha',
    'b': 'bravo',
    'c': 'charlie',
    'd': 'delta',
    'e': 'echo',
    'f': 'fruit',
    'g': 'george',
    'h': 'henry',
    'i': 'india',
    'j': 'john',
    'k': 'king',
    'l': 'lincoln',
    'm': 'mango',
    'n': 'nancy',
    'o': 'orange',
    'p': 'peter',
    'q': 'queen',
    'r': 'robert',
    's': 'simple',
    't': 'tom',
    'u': 'umbrella',
    'v': 'victor',
    'w': 'william',
    'x': 'x-ray',
    'y': 'young',
    'z': 'zebra'
}

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request 1.')

    word = req.params.get('word').lower()
    if not word:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            word = req_body.get('word')

    if word:
        result = []
        for i in range(0, len(word)):
            try:
                result.append(dictionary[str(word[i])].capitalize())
            except KeyError:
                result.append(str(word[i]))

        return func.HttpResponse(json.dumps(result))
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a word in the query string to spell the word phonetically. For example, add this to the URL - ?word=apple",
             status_code=200
        )
