class Film:
    def __init__(self, title, director, id = None):
        self.id = id
        self.title = title
        self.director = director

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.director})"