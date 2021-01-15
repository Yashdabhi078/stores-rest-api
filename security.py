from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username,password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password,password):   # for safly compare 2 string..
        return user
    
def identity(payload):  # when someone request "@JWT_require()" method,..that "JWT TOKEN" come with payload
    user_id = payload["identity"]   # from 'TOKEN' it check is,,user available..is yes then 
    return UserModel.find_by_id(user_id) # return user to JWT object and it allow user to use method(get,delete,post..etc)
    