class Error(Exception):
    pass

class InvalidTitleError(Error):
    def __init__(self, message='제목이 비어 있습니다.'):
        self.message = message
        super().__init__(message)


class InvalidContentError(Error):
    def __init__(self, message='내용이 비어 있습니다.'):
        self.message = message
        super().__init__(message)


class TodoNotExistError(Error):
    def __init__(self, message='존재하지 않는 Todo입니다.'):
        self.message = message
        super().__init__(message)