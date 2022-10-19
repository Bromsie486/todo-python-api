import json
from api.exceptions.messageContainsBlackListedWordException import MessageContainsBlackListedWordException
import service.keywordFilterService as keywordFilterService
from flask import request, Blueprint, Flask
import service.todoItemService as todoItemService

todoEndpoints = Blueprint('todoEndpoints', __name__)

@todoEndpoints.get("/todo")
def getTodos():
    return todoItemService.getAllTodoItems()

@todoEndpoints.post("/todo")
def newTodo():
    input = json.loads(request.data)
    try:
        todoItemService.createNewTodoItem(input)
        return Flask.response_class(status=201)
    except KeyError as ex:
        return str(ex), 400
    except MessageContainsBlackListedWordException as ex:
        return str(ex), 451

@todoEndpoints.delete("/todo")
def deleteTodo():
    try:
        input = json.loads(request.data)
        todoItemService.deleteTodoItem(input)
        return Flask.response_class(status=202)
    except KeyError as ex:
        return str(ex), 400
