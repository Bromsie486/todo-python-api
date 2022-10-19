from flask import Blueprint, request, Flask
import json
from api.exceptions.idNotFoundException import IdNotFoundException
from api.exceptions.messageContainsBlackListedWordException import MessageContainsBlackListedWordException
import service.todoCommentService as todoCommentService
import service.keywordFilterService as keywordFilterService

todoCommentEndpoints = Blueprint('todoCommentEndpoints', __name__)

@todoCommentEndpoints.post("/todo/comment/<todoItemID>")
def addTodoComment(todoItemID):
    if todoItemID is None:
        return Flask.response_class(status=400)
    try:
        input = json.loads(request.data)
        todoCommentService.addCommentToTodoItem(input, todoItemID)
        return Flask.response_class(status=201)
    except KeyError as ex:
        return str(ex), 400
    except IdNotFoundException as ex:
        return str(ex), 404
    except MessageContainsBlackListedWordException as ex:
        return str(ex), 451

@todoCommentEndpoints.delete("/todo/comment/<todoCommentItemID>")
def deleteTodoComment(todoCommentItemID):
    if todoCommentItemID is None:
        return Flask.response_class(status=400)
    todoCommentService.deleteComment(todoCommentItemID)
    return Flask.response_class(status=202)
