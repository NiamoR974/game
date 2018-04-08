# Fond
image bg salon = "manoir_salon"
image bg cuisine = "manoir_cuisine"

# Personnage Test
image bertrand = "bert_test"
image elise = "elise_test"
image henry = "henry_test"
image lisa = "lisa_test"
image marie = "marie_test"
image sandrine = "sand_test"

# Personnage
define det = Character('[player]', color="#c8ffc8")
define srv = Character('Bertrand le majordome', color="#003300")
define s = Character('Sandrine', color="#ff0000")
define mc = Character('Marie la cuisinière', color="#8585ad")
define ef = Character('Henry', color="#29a3a3")
define es = Character('Lisa', color="#d966ff")
define hf = Character('Elise')
define hh = Character('...')
define mus = Character ('...')
define wtf = Character('...')
# Variables

init:
    $ reput_tuto = 0
    $ cuisinevisite = False
    $ balconvisite = False
    $ salonvisite = False
    $ reputation = 0

label start:
    show text "20:00, 18 juin 19XX, Paris" at truecenter
    with dissolve
    pause 3
    hide text
    with dissolve
    "J'ai été invité à une fête dans le manoir de ma ville."
    "Les hôtes sont les parents de la fille tuée."
    "Après des mois sans indices, ils ont fait appel à moi. En moins de deux jours, l'affaire était classée."
    "Encore aujourd'hui, ça les surprend."
    show bertrand with dissolve
    srv "Bonjour. Vous êtes ?"
    jump nameplayer

    return

label chapitre_1_nomdone:
    srv "Je me présente. Bertrand, serveur des hôtes. Je pense que vous devez vous demander où ils sont ?"
    srv "Et bien madame est dans sa chambre. Monsieur n'a pas été dans mon champ de vision depuis longtemps..."
    det "Ah bon ?"
    srv "Bien sûr."
    det "A la chasse ? Sur le trône ?"
    srv "Son arme est en réparation. Et le trône est occupé par un invité."
    det "Qui ?"
    srv "Je l'ignore..."
    srv "Je pense que vous voulez visiter les lieux ? Et bien je vous laisse tranquille."
    hide bertrand
    jump chapitre_1_visite

label chapitre_1_visite:
    menu:
        "Qu'allons-nous visiter ?"

        "La cuisine" if cuisinevisite == False:
            $ cuisinevisite = True
            "Que se passe-t-il dans la cuisine."
            scene bg cuisine
            "Un lieu calme."
            show marie with dissolve
            "???" "Bonjour monsieur."
            det "Êtes-vous la cuisinière ?"
            mc "En effet, mais appelez moi Marie."
            det "Très bien, Marie."
            mc "Que faites-vous ici ?"
            menu:
                "Je l'ignore":
                    "Vous avez faim je pense, votre cerveau vous joue des tours !"
                "J'aimerais savoir ce qu'on mange ce soir !":
                    "Je n'ai pas encore préparé, mais je m'attendais à plus important...."
                    $ reputation = reputation - 1
                "Je visite les lieux, et je vous rencontre.":
                    "Je n'ai plus l'âge d'être draguée, vous savez. Quoi qu'il en soit, heureuse de vous rencontrer !"
                    $ reputation = reputation + 1
            mc "Les propriétaires de ces lieux m'ont dit qu'ils étaient très content que vous avez accepté."
            det "Accepté ? De quoi ?"
            mc "D'être venu ! L'hôte a même dit en rigolant que si il y a un meurtre, vous êtes là !"
            det "Vous en avez ri ?"
            mc "Oui, mais pour mon travail. Mon patron ne m'apprécie plus à cause d'une longue histoire."
            det "Laquelle ?"
            mc "Une longue histoire."
            det "Hmm..."
            if (balconvisite == False and salonvisite == False) or (balconvisite == False or salonvisite == False):
                det "Il me reste des lieux à visiter."
                mc "Je vous souhaite une bonne visite !"
            else:
                det "Je viens de finir la visite."
                mc "Vraiment ? Vous avez visité toutes les salles ?"
                det "La cuisine, le salon et le balcon me suffisent."
                mc "Et votre chambre pour ce soir ?"
                det "Ca sera une surprise pour moi"
            hide marie
            jump chapitre_1_visite

        "Le balcon" if balconvisite == False:
            $ balconvisite = True
            "Visitons le balcon."
            "Quel beau paysage."
            show sandrine with dissolve
            "???" "Oh, bonjour ! Vous êtes le détective [player]"
            det "Puis-je savoir qui vous-êtes ?"
            s "Oh... Excusez-moi. Sandrine. Je suis la soeur du propriétaire."
            det "Enchanté."
            s "Que faites-vous ici ?"

            # Cette question permettra de changer la réputation du personnage.
            menu:
                "Aucune idée":
                    s "Etonnant ! Je vais vous expliquer !"
                "Ici pour manger !":
                    s "Si on m'avait dit que le détective [player] était un goinfre."
                    $ reputation = reputation - 1
                "Bien évidemment, sinon je ne serai pas là":
                    s "C'est vrai ! Donc si je me trompe pas, vous êtes là pour la même raison que moi :"
                    $ reputation = reputation + 1

            s "Ma belle soeur nous a invité à son 25ème anniversaire, mais aussi à cette crémaillière."
            det "Que pensez-vous d'elle ?"
            s "Quelle question... Pour être honnête, je me moque d'elle. Du moment qu'elle n'importune pas mon frère."
            s "Enfin bon. J'espère que vous aimez ces lieux."
            det "En effet."
            if (cuisinevisite == False and salonvisite == False) or (cuisinevisite == False or salonvisite == False):
                det "Il me reste des lieux à visiter."
                s "Dans ce cas, bonne visite."
            else:
                det "Je viens de finir la visite."
                s "Etonnant, c'est quand même grand ces lieux."
                det "La cuisine, le salon et le balcon me suffisent."
                s "Et la chambre ?"
                det "Ca sera une surprise pour moi"
            jump chapitre_1_visite

        "La salon" if salonvisite == False:
            $ salonvisite = True
            "Visitons le salon"
            scene bg salon
            "Chaleureuse, malgré qu'il y ait du monde..."
            show lisa at right with dissolve
            "???" "Arrête ! T'es pas drôle !"
            show henry at left with dissolve
            "???" "Ca va, t'énerve pas."
            det "Les enfants calmez-vous."
            "???" "Vous êtes le détective [player] ?!"
            det "Oui, puis-je connaître vos noms ?"
            es "Je m'appelle Lisa, je suis la soeur de ce débile.."
            ef "Le débile s'appelle Henry."
            det "Enchanté !"
            es "Dites... Qui est pour vous le plus intelligent ?"
            ef "C'est moi..."
            es "Arrête de dire des bêtises !"
            menu:
                "Je ne peux pas répondre...":
                    ef "J'ai gagné !"
                    es "Non c'est moi..."
                    det "Enfin..."
                "Vous êtes tout les deux intelligents":
                    $ reputation = reputation + 1
                    ef "Pas de gagnant ?"
                    det "Si ! Vous deux !"
                    es "Bon bah, ça me va !"
                "Vous n'êtes pas du tout intelligent là... Voir le contraire":
                    $ reputation = reputation - 1
                    es "C'est pas très gentil ça..."
                    ef "Je suis d'accord avec elle."
                    det "Excusez-moi..."
            es "Papa et Maman sont dans la chambre."
            det "Que font-ils ?"
            ef "Ils se préparent pour la fête qui va bientôt commencer."
            det "Et vous êtes prêts vous ?"
            ef "Je me suis fait beau !"
            es "Dit moi merci pour la coiffure..."
            det "Ca se voit que vous êtes frères et soeurs."
            ef "J'espère que la maison vous plait."
            if (cuisinevisite == False and balconvisite == False) or (cuisinevisite == False or balconvisite == False):
                det "Il me reste des lieux à visiter."
                es "D'accord Monsieur !"
                ef "Entendu !"
            else:
                det "Je viens de finir la visite."
                es "Quoi ?!"
                ef "Vous êtes aussi rapide qu'un éclair !"
                det "La cuisine, le salon et le balcon me suffisent."
                es "Même pas la chambre ?"
                det "Ca sera une surprise pour moi"
            hide henry
            hide lisa
            jump chapitre_1_visite

        "Finir la visite":
            show bertrand
            srv "Avez-vous fini la visite ?"
            menu:
                "Oui":
                    srv "Suivez moi"
                    jump chapitre_1_rencontre
                "Non":
                    srv "Vous avez tout votre temps."
                    hide bertrand
                    jump chapitre_1_visite

label chapitre_1_rencontre:
    "Nous arrivons devant une porte. Bernard frappa à la porte"
    "???" "Oui ?"
    srv "L'invité est arrivé."
    "???" "Faites le rentrer !"
    srv "Entendu."
    hide bertrand
    "Le serveur m'ouvrit la porte. Une jeune femme m'accueillit"
    "???" "Enfin. Je vous attendais ! Heureuse que vous soyez-là à temps."
    det "Vous savez, après le meurtre de votre père qui est l'enquête la plus simple que j'ai connu, une fête ne me ferait pas de mal. Bonjour Elise."
    show elise
    hf "Et vous vous rappelez de moi ! Je suis heureuse !"

    ## TODO: Suite à faire.
    return
