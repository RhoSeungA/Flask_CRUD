from flask import request
from flask_restful import Resource
from api.services.todo_service import *

class TodoApi(Resource):
    def get(self):
        todos = get_all_todo()
        return {
            'status': 'success',
            'data':[todo.serialize() for todo in todos],
            'message': '모든 todo 조회'
        }

class UserTodoApi(Resource):
    # 사용자별 todo 조회
    def get(self):
        args = request.args
        user_id = args['user_id']
        todos = get_todo_by_user_id(user_id)

        return {
            'status': 'success',
            'data':[todo.serialize() for todo in todos],
            'message': '사용자별 todo 조회'
        }

    def post(self):
        try:
            data = request.json
            title = data['title']
            content = data['content']
            user_id = data['user_id']
            user = get_user_by_id(user_id)
            todo = add_todo(user=user,title=title,content=content)
            return {
                'status': 'success',
                'data': todo.serialize(),
                'message': 'todo 작성'
            }

        except InvalidTitleError as e:
            return {'status': 'fail', 'message': e.message}
        except InvalidContentError as e:
            return {'status': 'fail', 'message': e.message}

class updateTodoApi(Resource):
    def put(self, todo_id):
        try:
            data = request.json
            title = data['title']
            content = data['content']
            finish = data['finish']
            title, content,finish = title,content,finish

            todo = update_todo(todo_id, title, content,finish)

            return {
                'status': 'success',
                'data': todo.serialize(),
                'message': '게시물 수정'
            }

        except TodoNotExistError as e:
            return {'status': 'fail', 'message': e.message}

