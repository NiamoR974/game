label nameplayer:
    $ player = renpy.input("Quel est le nom du personnage",length=8)
    $ player = player.strip()

    if player == "":
        "Il faudrait que je donne mon nom..."
    elif player == "Sherlock":
        srv "Haha ! Quel rigolo... sauf si vous l'êtes vraiment."
    elif player == "Bertrand":
        srv "C'est rigolo. Quelqu'un dans ce manoir s'appelle comme ça... Je ne sais plus qui..."
    elif player == "Monika" or player == "Sayori" or player == "Yuri" or player == "Natsuki":
        if player == "Sayori":
            srv "J'aime bien ce nom. Ca me rappelle Doki Doki Literature Club !"
            srv "Sayori est ma préférée."
        else:
            srv "Ca me rappelle Doki Doki Literature Club !"
            srv "Je préfère Sayori pour être honnête..."
    elif player == "Romain" or player == "Kemley" or player == "Océane":
        srv "Vous savez que vous avez le même nom que l'un des anciens propriétaires ?"
        if player == "Romain":
            srv "Romain, c'était le prénom du tout premier propriétaire !"
        elif player == "Océane":
            srv "Océane, c'était la première propriétaire. La première femme. Elle adorait le dessin !"
        else:
            srv "Kemley, c'était le prénom du second propriétaire."
    # Blacklist des noms interdits
    elif player == "Pussy" or player == "Chatte" or player == "Bite" :
        srv "Ca vous amuse ? Vraiment, votre nom ?"
        jump nameplayer
    elif player == "FDP" or player == "PD" or player == "NTM" :
        srv "Ca vous amuse ? Vraiment, votre nom ?"
        jump nameplayer
    # Fin de la Blacklist
    else:
        srv "Oui ! Le grand détective [player]. Je ne vous avais pas reconnu, honte à moi."
    jump chapitre_1_nomdone
