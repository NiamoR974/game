init python:
    class InfoChar:
        def __init__(self, name="", age="", gender="", sign="", desc=""):
            self.name = name
            self.age = age
            self.gender = gender
            self.sign = sign
            self.desc = desc

    info_s = InfoChar(
    name = "Sandrine",
    age = "35"
    gender = "Femme",
    sign = "Cheveux roses",
    desc = """\
La soeur du propriétaire, elle est très hotaîne.
Cependant, elle a du mal à apprécier sa belle soeur.
Pour quelle raison ?"""
    )

    info_srv = InfoChar(
    name = "Bertrand",
    age = "30",
    gender = "Homme",
    sign = "Cicatrice",
    desc = """\
Le majordome du manoir, il est très intelligent.
Si vous faites attention, il a une cicatrice.
Que s'est-il passé ?"""
    )

    info_ef = InfoChar(
    name = "Henry",
    age = "16",
    gender = "Homme",
    sign = "",
    desc = """\
L'aîné de la famille, il est le grand frère et moins timide que sa soeur.
Pourtant, il a des problèmes avec quelqu'un...
Qui est le problème ?"""
    )

    info_es = InfoChar(
    name = "Lisa",
    age = "12",
    gender = "Femme",
    sign = "",
    desc = """\
La petite dernière, elle est très timide par rapport à son frère.
Elle connaît cependant plus de chose que vous...
Que cache-t-elle ?"""
    )

    info_mc = InfoChar(
    name = "Marie",
    age = "20",
    gender = "Femme",
    sign = "",
    desc = """\
Cuisinière du manoir, elle est cependant très maladroite.
Le propriétaire ne l'aime pas, pour une longue histoire...
Qu'a-t-elle fait ?"""
    )

    info_mus = InfoChar(
    name = "???",
    age = "???",
    gender = "Homme",
    sign = "",
    desc = """\
Musicien du manoir."""
    )

    info_wtf = InfoChar(
    name = "",
    age = "",
    gender = "Femme",
    sign = "",
    desc = ""
    )
