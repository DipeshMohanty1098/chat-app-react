from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

#setup
app = Flask(__name__)
api = Api(app)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatRooms.db'
db = SQLAlchemy(app)

#make the data serializable
chat_room = reqparse.RequestParser()
chat_room.add_argument("chatRoomName", type=str, help="Chat Room Name")

resource_fields = {
    'id': fields.Integer,
    'chatRoomName': fields.String
}

#creating the main DB
class ChatRoomModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    chatRoomName = db.Column(db.String(200), nullable = False)

#db.create_all() (run only for the first time, to create the db)

class ChatRoom(Resource):
    
    #get all the records in db
    @marshal_with(resource_fields)
    def get(self):
        chat_rooms = ChatRoomModel.query.all()
        return chat_rooms, 200
    
    #create a nw record
    @marshal_with(resource_fields)
    def post(self):
        args = chat_room.parse_args()
        result = ChatRoomModel.query.filter_by(chatRoomName=args['chatRoomName']).first()
        if result:
            abort(409, message="Chat Room Name already taken!")
        chat_room_name = ChatRoomModel(chatRoomName=args['chatRoomName'])
        db.session.add(chat_room_name)
        db.session.commit()
        return chat_room_name, 201

#add route
api.add_resource(ChatRoom, "/chatRooms/")

if __name__ == "__main__":
    app.run(debug=True, host="192.168.0.108", port="5001")
