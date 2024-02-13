from api.models.user import User

def get_user_by_id(id):
    return User.query.filter_by(id=id).first()
