import datetime
import ActorsHandlers
import MoviesHandlers
class Actor:
    def __init__(self):
        '''Null'''
    def Age(self, min_birthYear_Date, max_birthYear_Date = str(datetime.date.today()), URL_additions = ''):
        Handler = ActorsHandlers.Actors().Age(min_birthYear_Date, max_birthYear_Date, URL_additions)
        return Handler
class Movie:
    def __init__(self):
        '''Null'''
    def Plot(self, Terms, URL_additions=''):
        Handler = MoviesHandlers.Movies().Plot(Terms, URL_additions)
        return Handler    
    def Genre(self, Genre, URL_additions=''):
        Handler = MoviesHandlers.Movies().Genre(Genre, URL_additions)
        return Handler
    def Keyword(self, Keyword, URL_additions=''):
        Handler = MoviesHandlers.Movies().Keyword(Keyword, URL_additions)
        return Handler
    def Title(self, movieTitle, URL_additions = ''):
        Handler = MoviesHandlers.Movies().Title(movieTitle, URL_additions)
        return Handler
