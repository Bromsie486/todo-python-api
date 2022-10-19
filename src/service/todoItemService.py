import database.todoStore as todoStore
import uuid
import datetime
import service.keywordFilterService as keywordFilterService


def getAllTodoItems():
    return todoStore.getTodos()


def createNewTodoItem(input):
    if "title" not in input:
        raise KeyError("Title not in input")
    keywordFilterService.checkForBlackListedWords(input["title"])
    todoItem = {}
    todoItem["title"] = input["title"]
    todoItem["createdAt"] = datetime.datetime.now()
    todoItem["id"] = str(uuid.uuid4())
    if "description" in input:
        todoItem["description"] = input["description"]
        keywordFilterService.checkForBlackListedWords(input["description"])
    todoStore.addTodoItem(todoItem)
    pass


def deleteTodoItem(input):
    if "id" not in input:
        raise KeyError("ID not in input")
    todos = getAllTodoItems()
    for item in todos:
        if item["id"] == input["id"]:
            todoStore.deleteTodoItem(item)
    pass
