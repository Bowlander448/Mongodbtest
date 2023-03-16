import os
from random import randint, sample
import logging
from mongoengine import *
from filler_creatures import creatures, abilities

logging.basicConfig(level=logging.DEBUG)

#Ojala my internet fuele asi

class Ability(Document):
    name = StringField(required=True, unique=True)
    effect_stat = IntField()
    effect_status = StringField()

    description = StringField()

    meta = {'strict': False}


class Creature(Document):
    name = StringField(required=True, unique=True)
    image = StringField()

    hp = IntField(default=50, required=True)
    attack = IntField(required=True)
    defense = IntField(required=True)
    speed = IntField(required=True)
    ability = ReferenceField(Ability)
    description = StringField()
    lore = StringField()

    meta = {'strict': False}

    def __repr__(self):
        ability_name = self.ability.name if self.ability else "No Ability yet"
        return f"<Creature {self.name} - Atk {self.attack}: {ability_name}>"


if os.getenv("USE_LOCAL"):
    connect("Creatures")
    logging.debug("Running on local database.")
else:
    connect(host=os.getenv("CREATURE_DEN_DATABASE_URL"))
    logging.debug("Running on the cloud.")


Creature.drop_collection()
Ability.drop_collection()

# Your code goes here
a = Ability(name="Sturdy" , effect_stat=30 , description="Survives any blow leaving you with 1 hp")
c = Creature(name="Salvatore" , hp=3000 , attack=300, defense=1000 , speed=100 ,  image="13" , description="An Honorary Knight that defends his friends and loved ones")

a.save()
c.ability = a
c.save()


a = Ability(name="Electric Skin" , effect_status="Paralyze", description="If he or his opponents attack Sala's skin can paralyze anyone" )
c = Creature(name="Sala" , hp=3200 , attack=230 , defense=150 , speed=200 , image="15" , description="A nice creature with a ferocious electric skin")

a.save()
c.ability = a
c.save()

a = Ability(name="Brick" , effect_status="Fury" , description= "A supporter that helps anyone in danger")
c = Creature(name="Nick-er" , hp=1000, attack=300 , defense=200, speed=200 , image="18" , description= "His furry can stop and give hard attacks, but at a cost it can tire you")

a.save()
c.ability = a
c.save()

a = Ability(name="Ivestigator" , effect_status="Mystery Solver" , description=" A Geko that solves crimes wth his crew")
c = Creature(name= "Amogus", hp=1000 , attack=500 , defense=100 , speed=300 , image="730" ,  description= "A wierd crewmate with a job to guess who is the Imposter")

a.save()
c.ability = a
c.save()

a = Ability(name="Get Wrecked" , effect_status="Rage", description="t bags you when you get killed")
c = Creature(name="Sweats" , hp=1000 , attack=5000 , defense=100 , speed=1000 , image="300" , description= "A monster that tries to 360 no scope you with easy tricks, it will t bag you if it kills you")

a.save()
c.ability = a
c.save()

a = Ability(name="Rick" , effect_status="Big Brain", description="The biggest brain = the biggest smart moves")
c = Creature(name="Muart" , hp=1 , attack=5000 , defense=100 , speed=100000 , image="205" , description= "a creature with God like intelligence, likes to drink")

a.save()
c.ability = a
c.save()

a = Ability(name="Profe" , effect_status="meh", description="Alwas says hes not ok")
c = Creature(name="Mujica" , hp=1000 , attack=5000 , defense=10000 , speed=1000 ,  image="100" , description= "An awesome professor with a power of coding, but never says hes good, he always says he's meh")

a.save()
c.ability = a
c.save()

a = Ability(name="Guilt" , effect_status="Sadness", description="Makes you think you are the worst person when youre not")
c = Creature(name="Salva" , hp=1000 , attack=5000 , defense=100 , speed= 1000 , image="400" , description= "A crearure that makes you think you are the bad person but you are really not")

a.save()
c.ability = a
c.save()
# Generating filler creatures

#find already used images

pics_already_used = Creature.objects().distinct("image")

all_pics = [str(n)for n in range(1, 829)]

unused_pics = list(set(all_pics).difference(pics_already_used))

for each_filler_creature, each_ability in zip(creatures, abilities):
    creature_name = each_filler_creature
    ability_name = each_ability

    creature_description = creatures[creature_name]["description"]
    creature_lore = creatures[creature_name]["lore"]
    ability_description = abilities  [ability_name]

    hp = randint(1, 100)

    attack = randint(1, 100)

    defense = randint(1, 100)

    speed = randint(1, 100)

    image = sample(unused_pics, 1)[0]
    c = Creature(name=creature_name, description=creature_description,
                 hp=hp, attack=attack, defense=defense, speed=speed,
                  lore=creature_lore)

    a = Ability(name=ability_name,description=ability_description)

    a.save()
    c.ability = a
    c.save()
    pass


pass


def creature():
    return None