todos = []

def getTodos():
    return todos

def addTodoItem(todoItem):
    todos.append(todoItem)
    pass

def deleteTodoItem(todoItem):
    todos.remove(todoItem)
    pass

def addCommentToTodoItem(todoCommentItem, todoItemIndex):
    if "comments" not in todos[todoItemIndex]:
        todos[todoItemIndex]["comments"] = []
    todos[todoItemIndex]["comments"].append(todoCommentItem)
    pass

def deleteComment(todoItemIndex, commentIndex):
    del todos[todoItemIndex]["comments"][commentIndex]
    pass
