from model.model import Model
from view.view import View
from model import cinema_exceptions as c_e

class Controller:
    """
    *********************
    * Simpre controller *
    *********************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    """
    ***************
    * User Methods*
    ***************
    """
    def create_a_user(self, email, first_name, last_name, birthdate, password):
        try:
            self.model.create_a_user(email, first_name, last_name, birthdate, password)
        except:
            self.view.item_already_stored_error(e)
    
    def show_all_users(self):
        users_in_db = self.model.read_all_users()
        self.view.show_all_users(users_in_db, 1)

    """
    ****************
    * Movie Methods*
    ****************
    """

    """
    ***************
    * Sala Methods*
    ***************
    """

    """
    *********************
    * Billboard Methods *
    *********************
    """

    """
    *****************
    * Ticket Methods*
    *****************
    """