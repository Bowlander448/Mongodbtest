from mongoengine import *


class Highscores(Document):
    username = StringField()
    score = IntField(default=0)

    def __repr__(self):
        return f"<Highscores:{self.username} - {self.score}>"

connect("Highscore")

#Highscores.objects shows you the list you  have made
#Highscores.object.count() shows you how many you have made
#Highscores.objects(score=400) shows what highscore has that same number
#Highscores.objects(score__gte=30400), lte,lt,gt shows you what number is bigger,smaller, or the same
pass

