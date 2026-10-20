from film import Film

class FilmRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from films')
        films = []
        for row in rows:
            item = Film(row["title"], row["director"], row["id"])
            films.append(item)
        return films

    def create(self, film):
        self._connection.execute('INSERT INTO films (title, director) VALUES (%s, %s)', [film.title, film.director])
        return None