from api.controllers.todo_controller import *

def init_routes(api):
    api.add_resource(TodoApi,'/api/AllTodo') # 모든 todo 조회
    api.add_resource(UserTodoApi,'/api/todo') # 사용자 별 todo 작성, 불러오기
    api.add_resource(updateTodoApi,'/api/todoUpdate/<todo_id>') # todoUpdate
