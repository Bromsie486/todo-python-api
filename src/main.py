from flask import Flask
from api.todoItemApi import todoEndpoints
from api.todoCommentApi import todoCommentEndpoints

app = Flask(__name__)
app.register_blueprint(todoEndpoints)
app.register_blueprint(todoCommentEndpoints)

if __name__ == "__main__":
    app.run(debug=True)
