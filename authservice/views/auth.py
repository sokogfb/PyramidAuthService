from authservice.models.user import User


class AuthView(object):
    def __init__(self, request):
        self.request = request

    def authenticate(self, login, password):
        user = User.get_user(login, self.request.dbsession)
        if user and user.validate_password(password):
            return user
        return None

    def login(self):
        login = self.request.POST['login']
        password = self.request.POST['password']
        user = self.authenticate(login, password)  # You will need to implement this.
        if user:
            return {
                'result': 'ok',
                'token': self.request.create_jwt_token(user.id)
            }
        else:
            return {
                'result': 'error'
            }


# include the following in your __init__ main function
#     config.add_route('login', '/login')
#     config.add_view(AuthView,
#                     attr='login',
#                     request_method='POST',
#                     renderer='json',
#                     route_name='login')