from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, marshal_with,fields
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
db = SQLAlchemy(app)


send_Message = reqparse.RequestParser()
send_Message.add_argument("message", type=str, help="message field")
send_Message.add_argument("author", type=str, help="Author field")
send_Message.add_argument("chatRoom", type=str, help="Chat Room Name")

resource_fields = {
    'id': fields.Integer,
    'message': fields.String,
    'author': fields.String,
    'chatRoom': fields.String
}


class MessageModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    message = db.Column(db.String(100000000), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    chatRoom = db.Column(db.String(100), nullable=False)

#db.create_all()

class Messages(Resource):
    @marshal_with(resource_fields)
    def get(self, chatRoom):
        messages = MessageModel.query.filter_by(chatRoom=chatRoom).all()
        return messages, 200

    @marshal_with(resource_fields)
    def post(self,chatRoom):
        args = send_Message.parse_args()
        message = MessageModel(message=args['message'], author=args['author'], chatRoom=args['chatRoom'])
        db.session.add(message)
        db.session.commit()
        return message, 201

#api.add_resource(Messages, "/messages/")
api.add_resource(Messages, "/messages/<string:chatRoom>")

if __name__ == "__main__":
    app.run(debug=True, host="192.168.0.108")