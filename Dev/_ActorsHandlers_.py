import urllib3
import datetime
from Workers import Helpers
from bs4 import BeautifulSoup

global http
http = urllib3.PoolManager()
class Actors:
    def __init__(self):
        '''Nothing Goes on here'''
        
    def _Age_(self, min_birthYear_Date, max_birthYear_Date = str(datetime.date.today()), URL_additions = ''):
        #Features needing added:
        #Name Groups (awards)
        #an actual gender switch
        #Star sign (why does IMDB even have this?)
        Link ="http://www.imdb.com/search/name?birth_date="
        Link += str(min_birthYear_Date)+','
        Link += str(max_birthYear_Date)
        Link += URL_additions
        Link = Helpers.sanitize(Link)
        webPage = http.request('GET', Link)
        webPageData = webPage.data
        soup = BeautifulSoup(webPageData)
        ActorList = []
        for ActorObject in soup.findAll('td', {'class': 'name'}):
            aTagObject = ActorObject('a')
            aTag_ActorNameOnly = aTagObject[0]
            NamedActorObject = aTag_ActorNameOnly.decode_contents()
            if len(ActorList)<50:
                        ActorList.append(str(NamedActorObject))
        return ActorList

    def _genericName_(self, name, URL_additions = ''):
        Link = "http://www.imdb.com/find?q="
        Link += name
        Link += "&s=nm"
        Link += URL_additions
        Link = Helpers.sanitize(Link)
        webPage = http.request('GET', Link)
        webPageData = webPage.data
        soup = BeautifulSoup(webPageData)
        ActorList = []
        for ActorObject in soup.findAll('td', {'class': 'result_text'}):
            aTagObject = ActorObject('a')
            aTag_ActorNameOnly = aTagObject[0]
            NamedActorObject = aTag_ActorNameOnly.decode_contents()
            if len(ActorList)<50:
                        ActorList.append(str(NamedActorObject))
        return ActorList
    def _specificName_(self, name, URL_additions = ''):
        Link = "http://www.imdb.com/find?q="
        Link += name
        Link += "&s=nm&exact=true"
        Link += URL_additions
        Link = Helpers.sanitize(Link)
        webPage = http.request('GET', Link)
        webPageData = webPage.data
        soup = BeautifulSoup(webPageData)
        ActorList = []
        for ActorObject in soup.findAll('td', {'class': 'result_text'}):
            aTagObject = ActorObject('a')
            aTag_ActorNameOnly = aTagObject[0]
            NamedActorObject = aTag_ActorNameOnly.decode_contents()
            if len(ActorList)<50:
                        ActorList.append(str(NamedActorObject))
        return ActorList
