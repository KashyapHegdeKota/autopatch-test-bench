# user_service.py
class UserService:
    def __init__(self):
        self.users = []

    def add_user(self, user_data):
        """
        Adds a user to the list. 
        BUG: It does not check if 'email' exists in user_data, 
        causing a KeyError when processing later.
        """
        # Missing validation for required keys
        self.users.append(user_data)
        
    def get_user_emails(self):
        return [user['email'] for user in self.users]
#TEST
