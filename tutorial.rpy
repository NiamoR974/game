label tuto:
    srv "En arrivant ici, il faut savoir que vous avez une réputation stable."
    # TODO : Faire le reste du blabla
    srv "Si votre réputation est trop basse, ça ne sert à rien de continuer à discuter."
    srv "Si votre réputation est trop haute... j'ignore ce qu'il pourrait se passer."
    srv "Votre réputation change selon vos choix. Faisons un essai."
    srv "Répondez à ma question, et selon le choix, vous aurez une réponse qui pourrait changer."
    srv "Comment allez-vous ?"
    menu:
        "Répondez à cette question !"
        "Ca va très bien et vous ?":
            $ reput_tuto = reput_tuto + 1
            srv "Je vais très bien !"
            srv "Là, vous recevez un point de réputation en plus."
        "Comme si ça pouvait vous regarder.":
            $ reput_tuto = reput_tuto - 1
            srv "Un peu violent comme réponse..."
            srv "Là, vous avez perdu un point de réputation."
        "...":
            srv "Bon... Faisons comme si c'était une réputation"
            srv "Là, vous ne recevez pas de point de réputation. Mais vous n'en perdez pas !"
    srv "Bien, répondez à cette question pour avoir votre score final."
    srv "Que pensez-vous de cette maison ?"
    menu:
        "Répondez à cette question !"
        "C'est un beau manoir.":
            $ reput_tuto = reput_tuto + 1
            srv "Une réponse assez simple"
        "Un manoir un peu sale...":
            srv "Oui il y a de la poussière dans les coins, mais rien de grave."
        "La cuisine est plus intéressant":
            $ reput_tuto = reput_tuto - 1
            srv "Quel... goinfre..."
            if reput_tuto == -1:
                srv "Encore une fois, vous perdez un point."
            else:
                srv "Vous perdez ici un point."
    srv "Voici la note finale."
    srv "Votre réputation est de [reput_tuto]."
    if reput_tuto == -2:
        srv "Avec ce score, les gens ne vous apprécieront pas. Ils vous demanderont donc de quitter les lieux."
    elif reput_tuto == 2:
        srv "Avec ce score, les gens vous adoreront ! Mais qui sait... peut-être que la jalousie pourrait être présente."
    else:
        srv "C'est un score pas mal. Néanmoins, les gens auront une vision de vous différente :"
        if reput_tuto == -1:
            srv "Avec ce score par exemple, les gens auront une vision de vous péjorative, mais vous apprécieront quand même."
        elif reput_tuto == 0:
            srv "Ce score est parfait. Les gens auront une vision stable de vous."
        elif reput_tuto == 1:
            srv "Les gens auront une vision méliorative, mais certains pourront vous détester."
        "Qui sait... Avec un autre score, vous aurez une autre fin."
    srv "Merci de m'avoir écouté."
