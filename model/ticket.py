#_*_ coding: utf-8 _*_

class Ticket:
    def __init__(self, transaction_id, show_id, user_id, seat_id):
        self.transaction_id = transaction_id
        self.show_id = show_id
        self.user_id = user_id
        self.seat_id = seat_id