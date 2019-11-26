#_*_ coding: utf-8 _*_

class Billboard:
    def __init__(self, show_id, movie_id, id_sala, schedule, languaje=''):
        self.show_id = show_id
        self.movie_id = movie_id
        self.id_sala = id_sala
        self.schedule = schedule
        self.languaje = languaje