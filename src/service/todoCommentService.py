from api.exceptions.idNotFoundException import IdNotFoundException
import database.todoStore as todoStore
import uuid
import datetime
import service.keywordFilterService as keywordFilterService


def addCommentToTodoItem(input, todoItemID):
    if todoItemID is None:
        raise KeyError("todoItemID not found")
    if "description" not in input:
        raise KeyError("Input does not contain a description")
    description = input["description"]
    keywordFilterService.checkForBlackListedWords(description)
    for index, item in enumerate(todoStore.getTodos()):
        if item["id"] == todoItemID:
            todoCommentItem = {
                "id": str(uuid.uuid4()),
                "description": description,
                "createdAt": datetime.datetime.now(),
            }
            todoStore.addCommentToTodoItem(todoCommentItem, index)
            return
    raise IdNotFoundException("Todo item with ID " + todoItemID + " was not found.")


def deleteComment(commentID):
    for todoItemIndex, item in enumerate(todoStore.getTodos()):
        for commentIndex, comment in enumerate(item["comments"]):
            if comment["id"] == commentID:
                todoStore.deleteComment(todoItemIndex, commentIndex)
                return
