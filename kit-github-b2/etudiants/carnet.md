# Parcours de TP GitHub en autonomie

20 étudiants, cinq groupes de quatre, Python. Durée conservée : 2 h + 3 h + 3 h + 4 h, pauses incluses. Le fil rouge est Campus Events. Le kit fonctionne hors connexion pour la lecture, Python et Git local ; les PR et Actions nécessitent un accès GitHub.

## La règle du jeu

Chaque TP suit le même cycle : comprendre le besoin, formuler une hypothèse, choisir une expérience, observer, produire une preuve, faire vérifier par un pair, restituer et consigner. Les critères sont connus dès le début ; la solution ne l'est pas.

Avant de solliciter une aide, apportez votre objectif, la commande ou l'action exacte, le résultat attendu, le résultat observé et une tentative expliquée. Après cinq à huit minutes sans progrès, ouvrez un indice ou demandez de l'aide : l'autonomie n'est pas l'abandon face à un blocage.

Les ressources sont consultables dès le départ. Commencez par chercher une réponse précise ; ouvrez les indices dans l'ordre seulement si nécessaire. Utiliser un indice ne retire aucun point. Vous devez pouvoir expliquer, adapter et vérifier toute solution trouvée, y compris avec une assistance numérique. Ne soumettez aucun identifiant ou secret à un service externe.

## Quatre rôles qui tournent à chaque TP

Pilote : répartit les tâches et surveille le temps. Investigateur : formule les hypothèses et cherche les références. Contradicteur : choisit des cas qui pourraient invalider la solution. Rapporteur : collecte les preuves et anime la restitution.

TP1 et TP5 : A pilote, B investigateur, C contradicteur, D rapporteur.
TP2 et TP6 : B pilote, C investigateur, D contradicteur, A rapporteur.
TP3 et TP7 : C pilote, D investigateur, A contradicteur, B rapporteur.
TP4 et TP8 : D pilote, A investigateur, B contradicteur, C rapporteur.

Ces responsabilités ne remplacent pas les contributions individuelles : chaque membre doit écrire, tester et relire. Changez de personne au clavier dans les expériences en binôme. Au TP3 chacun possède son incident ; au TP6 chacun possède son document.

## Passer au TP suivant

Le groupe vérifie les critères et un pair inscrit validé, à reprendre ou bloqué, avec une preuve et une prochaine action. Ce verdict est formatif et déclaratif, pas une note automatique. Le formateur peut le vérifier. Un blocage ne doit pas disparaître du journal pour respecter l'horaire.

Au début de chaque TP, vérifiez votre branche et l'état de travail. Une version de secours peut être fournie par le formateur si un blocage empêcherait tout le groupe de travailler ; indiquez son usage, gardez votre première tentative et ne la présentez pas comme votre réalisation.

## Plan sur 12 heures

| Séance | Déroulement | Total |
| --- | --- | --- |
| 1 | 0–10 lancement ; 10–55 TP1 ; 55–65 pause ; 65–115 TP2 ; 115–120 bilan | 120 min |
| 2 | 0–5 reprise ; 5–60 TP3 ; 60–115 TP4 ; 115–125 pause ; 125–175 TP5 ; 175–180 bilan | 180 min |
| 3 | 0–5 reprise ; 5–55 TP6 ; 55–110 TP7 ; 110–120 pause ; 120–175 TP8 ; 175–180 bilan | 180 min |
| 4 | Cinq passages de 30 min, audit simultané, rétrospective et bilan individuel | 240 min |

Le temps de restitution fait partie de chaque TP, pas d'un travail à terminer à la maison. Aucune préparation étudiante obligatoire hors séance.


# TP01 Cartographier un dépôt inconnu

Séance 1 · 45 minutes, restitution incluse.
30 min d’enquête · 10 min de restitution croisée · 5 min de trace

## Mission

Vous reprenez un projet sans son auteur. Établissez comment il fonctionne, comment le vérifier et où intervenir, sans modifier le code métier.

## Ressources disponibles

- Dépôt Campus Events fourni, README.md, campus.py et tests/.
- Outil tools/diagnostic.py ; fiche ressources et terminal Git.

## Questions à explorer avant de demander une procédure

- Qu’est-ce qui est local, distant, versionné ou généré ?
- Pourquoi quatre tests verts ne suffisent-ils pas à conclure que le projet est correct ?
- Comment distinguer un problème d’environnement d’un défaut du programme ?

## Travail à organiser

- Chacun explore une zone : A code, B tests, C documentation, D Git et outils. Faites ensuite expliquer sa zone par un autre membre.
- Exécutez le diagnostic, puis les tests existants. Avant toute commande, écrivez une prédiction de son résultat.
- Dessinez une carte des fichiers et de leurs responsabilités. Identifiez deux comportements non testés, sans les corriger.
- Comparez git status, git log et ce qui est visible sur GitHub ; identifiez une preuve de synchronisation ou expliquez pourquoi le dépôt est encore local.

## Expériences obligatoires

- Comparez l’affichage de git diff avant et après une modification provisoire d’un fichier brouillon, puis après son indexation. Ne touchez pas à campus.py.
- Expliquez pourquoi build/ et __pycache__/ ne doivent pas apparaître comme sources à committer.

## Productions à remettre

- Une carte du dépôt avec au moins six éléments et leurs relations.
- La commande de test réellement utilisée, son résultat et deux limites de cette preuve.
- Une difficulté rencontrée et la recherche qui l’a résolue.

## Critères de réussite connus avant de commencer

- Un pair retrouve le fichier métier, les tests, les documents et la génération en moins de deux minutes.
- Chaque membre distingue fichier de travail, index, commit et distant avec un exemple observé.
- Les quatre tests initiaux passent, ou un blocage d’environnement est précisément décrit et pris en charge.

## Restitution systématique

Dans chaque groupe, deux binômes échangent leurs cartes : un binôme demande « où changer la règle ? » et « comment le prouver ? », l’autre montre les fichiers. Inversez. Le rapporteur conserve les deux questions et les réponses.

Compléter ateliers/preuves/tp01.md dans votre dépôt. Le démonstrateur du jour ne montre pas uniquement son propre travail. Un pair renseigne son verdict et ce qui reste à reprendre. Un contrôle automatique vert ne valide pas cette restitution.

## Pour aller plus loin si le socle est validé

Expliquez pourquoi un clone possède son propre historique local et n’est pas un dossier synchronisé en permanence.

## Indices à consulter progressivement

### Indice 1

Commencez par la liste des fichiers et README.md. Une lecture ciblée vaut mieux qu’une lecture complète sans question.

### Indice 2

Depuis le dossier contenant campus.py : python tools/diagnostic.py, puis python -m unittest discover -s tests -v.

### Indice 3

Pour comparer les états : git status, git diff, git add CHEMIN, git diff --staged. Pour retirer seulement le fichier brouillon de l’index : git restore --staged CHEMIN ; conservez le fichier si vous en avez besoin.

# TP02 Se coordonner sans écraser le travail des autres

Séance 1 · 50 minutes, restitution incluse.
35 min de construction · 10 min de démonstration interne · 5 min de trace

## Mission

Construisez la carte d’identité de votre équipe dans le dépôt, sans écrire directement sur main. Chaque personne doit publier et relire un changement.

## Ressources disponibles

- Modèles d’issue et de PR dans .github/.
- Fichiers equipe/A.md à equipe/D.md à créer ; contrat de contribution CONTRIBUTING.md.

## Questions à explorer avant de demander une procédure

- Comment choisir la base et la branche source d’une PR ?
- À quel moment un changement local devient-il visible par les autres ?
- Qui peut approuver et qui peut fusionner dans votre dépôt ?

## Travail à organiser

- Décidez d’une convention de branches et de titres. Rédigez une issue par personne avec trois critères : pseudonyme, compétence, question.
- Chacun produit un fichier d’équipe distinct sur sa branche, puis une PR liée à son issue. Choisissez vos commandes à l’aide du mémo.
- Avant de pousser, faites constater par un pair que votre changement n’est pas encore sur le distant. Puis montrez la différence après publication.
- A relit B, B relit C, C relit D, D relit A. Fusionnez après validation puis retrouvez le travail des quatre membres dans vos copies locales.

## Expériences obligatoires

- Observez main avant la fusion d’une PR : pousser une branche l’a-t-il modifié ?
- Comparez les identifiants de commit local et distant après synchronisation. En cas de décalage, expliquez-le avant de relancer une commande.

## Productions à remettre

- Quatre issues et quatre PR de présentation avec liens réels.
- Quatre revues ; une preuve de synchronisation après fusion.
- Une convention de travail courte adoptée par le groupe.

## Critères de réussite connus avant de commencer

- Chaque étudiant est auteur d’une PR et relecteur d’une autre.
- Les quatre fichiers se trouvent sur main sans perte de contenu.
- Un membre qui n’a pas réalisé la dernière fusion explique le parcours d’un changement.

## Restitution systématique

Chaque personne dispose de deux minutes pour montrer sa PR et la revue qu’elle a faite. Les deux minutes restantes servent à vérifier les quatre fichiers sur main. Une phrase seule sans lien ni écran ne constitue pas une preuve.

Compléter ateliers/preuves/tp02.md dans votre dépôt. Le démonstrateur du jour ne montre pas uniquement son propre travail. Un pair renseigne son verdict et ce qui reste à reprendre. Un contrôle automatique vert ne valide pas cette restitution.

## Pour aller plus loin si le socle est validé

Testez une draft PR et expliquez à votre équipe quand la passer en Ready for review.

## Indices à consulter progressivement

### Indice 1

Une branche par personne et un fichier distinct évitent un conflit inutile à ce stade.

### Indice 2

Dans la PR : base main ; compare votre branche. Un commit reste local tant qu’il n’est pas poussé.

### Indice 3

Séquence de secours : git switch main ; git pull --ff-only ; git switch -c docs/presentation-a ; modifier le fichier ; git add equipe/A.md ; git commit -m "Présenter A" ; git push -u origin docs/presentation-a. Demandez une revue sur GitHub.

# TP03 Prouver un défaut avant de le corriger

Séance 2 · 55 minutes, restitution incluse.
40 min d’investigation · 10 min de démonstration interne · 5 min de trace

## Mission

Le service de vie étudiante vous transmet quatre incidents. Produisez des preuves de défaut, puis des correctifs ciblés, sans fusionner avant la revue du TP4.

## Ressources disponibles

- ateliers/incidents.md et contrat de README.md.
- ateliers/cas-exploration.json ; tests nominaux ; tools/verifier.py.

## Questions à explorer avant de demander une procédure

- Quelle entrée permet de distinguer le programme actuel du comportement attendu ?
- Votre test échoue-t-il pour la bonne raison ?
- Comment éviter de confondre règle métier, validation et problème de type hors périmètre ?

## Travail à organiser

- Répartissez les incidents A à D. Chacun rédige l’issue de son incident et construit une matrice nominal / frontière / invalide.
- Avant de lire les indices, calculez les résultats attendus de deux entrées et confrontez-les au programme.
- Ajoutez un test de régression dans un fichier personnel ; capturez son échec avant la correction. Corrigez votre fonction puis ajoutez les autres cas utiles.
- Mettez à jour la docstring et ouvrez votre PR avec la preuve rouge → verte. Laissez-la ouverte pour le TP4.

## Expériences obligatoires

- Pour votre incident, démontrez un cas normal, un cas limite et un cas invalide.
- Ajoutez au moins un cas pertinent qui ne figure pas dans le jeu fourni. Expliquez ce qu’il apporte.

## Productions à remettre

- Quatre PR de code ouvertes, chacune liée à une issue.
- Pour chaque auteur : résultat attendu, trace d’échec, trace après correction et limites connues.
- Une matrice de tests avec un scénario original par étudiant.

## Critères de réussite connus avant de commencer

- Le test de régression échouait sur le code initial et passe sur la branche corrigée.
- Les anciens tests continuent de passer.
- Le vérificateur ciblé réussit pour votre mission ; les autres missions peuvent encore échouer sur votre branche.

## Restitution systématique

Deux minutes par personne : annoncer le contre-exemple, montrer le test rouge enregistré puis le résultat vert et expliquer la correction. Deux minutes de questions entre pairs. Le prochain relecteur choisit un cas à reproduire.

Compléter ateliers/preuves/tp03.md dans votre dépôt. Le démonstrateur du jour ne montre pas uniquement son propre travail. Un pair renseigne son verdict et ce qui reste à reprendre. Un contrôle automatique vert ne valide pas cette restitution.

## Pour aller plus loin si le socle est validé

Sur une copie non destinée à la fusion, revenez volontairement à l’ancien comportement d’une ligne : votre test le détecte-t-il ? Annulez cette modification dans l’éditeur.

## Indices à consulter progressivement

### Indice 1

Ne corrigez pas les quatre fonctions dans une même PR. Observez d’abord les frontières du contrat.

### Indice 2

Les points à explorer sont la capacité atteinte, les nombres hors domaine, les espaces autour d’un nom et la capacité nulle.

### Indice 3

Pour A : self.assertFalse(peut_inscrire(4,4)). Un test qui passe aussi sur le code initial ne prouve pas ce défaut. Les autres missions doivent construire leurs propres tests.

# TP04 Mener une revue contradictoire et intégrer

Séance 2 · 55 minutes, restitution incluse.
35 min de revues et révisions · 15 min de restitution interne · 5 min de trace

## Mission

Vous devez décider si les quatre PR peuvent entrer dans main. L’approbation doit résulter d’une vérification, pas d’un échange de bons procédés.

## Ressources disponibles

- Les quatre PR du TP3 ; grille ateliers/grille-revue.md.
- Mémo Git pour consulter la branche d’un pair ; modèle de commentaire argumenté.

## Questions à explorer avant de demander une procédure

- Le test prouve-t-il le contrat ou reproduit-il seulement le code ?
- Quel commentaire est bloquant et lequel est une préférence ?
- Comment réexaminer une PR après de nouveaux commits ?

## Travail à organiser

- Effectuez la revue circulaire A → B → C → D → A. Commencez par l’issue, pas par le style du code.
- Reproduisez le contre-exemple annoncé puis essayez une entrée supplémentaire choisie par vous. Notez commande, branche et résultat.
- Rédigez une décision argumentée : Comment, Request changes ou Approve. L’auteur répond ; le relecteur vérifie les nouveaux commits.
- Intégrez les PR acceptées et relancez la suite complète sur main. Ne fusionnez pas une PR bloquée pour gagner du temps.

## Expériences obligatoires

- Confrontez un test de la PR au code avant correction à partir de la trace fournie ; demandez une reproduction si elle ne suffit pas.
- Après fusion des quatre changements, exécutez python tools/verifier.py all et expliquez la différence avec une revue humaine.

## Productions à remettre

- Quatre grilles de revue signées par des relecteurs distincts des auteurs.
- Au moins une décision détaillée par PR, avec résultat de reproduction et suivi.
- Preuve de la suite complète sur main et liens des PR intégrées ou motif de blocage.

## Critères de réussite connus avant de commencer

- Chaque approbation cite les critères réellement vérifiés.
- Aucune remarque bloquante n’est ignorée ; pas de défaut inventé pour remplir la grille.
- Les quatre contrats et les tests du groupe passent ensemble, ou l’écart résiduel est clairement isolé.

## Restitution systématique

Trois minutes par personne : présenter la PR que vous avez relue, le cas supplémentaire testé et votre décision. Les trois minutes restantes servent à comparer « tests verts » et « prêt à fusionner ».

Compléter ateliers/preuves/tp04.md dans votre dépôt. Le démonstrateur du jour ne montre pas uniquement son propre travail. Un pair renseigne son verdict et ce qui reste à reprendre. Un contrôle automatique vert ne valide pas cette restitution.

## Pour aller plus loin si le socle est validé

Proposez une refactorisation de validation commune dans une PR séparée, seulement après intégration des quatre correctifs.

## Indices à consulter progressivement

### Indice 1

Une revue peut conclure que le code est correct. Dans ce cas, rendez visibles les cas et les critères vérifiés.

### Indice 2

Dans Files changed, commentez une ligne précise ; présentez constat, conséquence, proposition et test attendu.

### Indice 3

Pour récupérer une branche du même dépôt : git fetch origin puis git switch --track origin/NOM. Si elle existe déjà localement : git switch NOM puis git pull --ff-only. Vérifiez git status avant de changer de branche.

# TP05 Négocier et résoudre un conflit

Séance 2 · 50 minutes, restitution incluse.
35 min de laboratoire · 10 min de démonstration interne · 5 min de trace

## Mission

Deux décisions compatibles ont été rédigées séparément sur la même ligne. Produisez une version commune et prouvez que vous avez conservé les deux intentions.

## Ressources disponibles

- docs/regles.md : ligne « Revue requise : 1 personne. ».
- Deux binômes partent du même main : A-B choisit deux personnes ; C-D choisit une personne différente de l’auteur.

## Questions à explorer avant de demander une procédure

- Quelles conditions rendent le conflit reproductible ?
- Que représentent HEAD et la version entrante pendant votre opération ?
- Pourquoi « accepter notre version » n’est-il pas une décision métier suffisante ?

## Travail à organiser

- Depuis le même commit, créez deux branches. Chaque binôme remplace exactement la ligne indiquée, commit et ouvre sa PR.
- Après revue, fusionnez la PR A-B. Dans la branche C-D, récupérez puis intégrez le nouveau main. Observez et conservez la preuve du conflit.
- Négociez une phrase qui préserve les deux contraintes. Résolvez, enregistrez, testez et faites relire la résolution avant fusion.
- Faites expliquer l’opération par les membres qui n’étaient pas au clavier. Notez comment abandonner proprement une tentative avant son commit.

## Expériences obligatoires

- Prédisez l’effet de la deuxième fusion avant son exécution.
- Vérifiez l’absence de marqueurs et surtout la présence des deux exigences dans la règle finale.

## Productions à remettre

- Liens des deux PR ; marqueurs ou message de conflit capturés.
- La règle finale et la justification des deux intentions conservées.
- Un schéma des branches avant et après résolution.

## Critères de réussite connus avant de commencer

- Le conflit a été réellement observé, pas seulement raconté.
- La règle comporte deux relecteurs différents de l’auteur.
- Le contenu restant est préservé, le dépôt est propre après commit et les tests passent.

## Restitution systématique

Les binômes s’échangent le rôle de démonstrateur. Chacun explique une version et le compromis final, puis répond à « que ferait-on si la résolution était mauvaise ? ». Conservez le schéma et le lien de commit.

Compléter ateliers/preuves/tp05.md dans votre dépôt. Le démonstrateur du jour ne montre pas uniquement son propre travail. Un pair renseigne son verdict et ce qui reste à reprendre. Un contrôle automatique vert ne valide pas cette restitution.

## Pour aller plus loin si le socle est validé

Expliquez un exemple de conflit logique possible sans conflit textuel, comme deux fonctions qui n’utilisent plus la même unité.

## Indices à consulter progressivement

### Indice 1

Les deux branches doivent partir du même commit avant la première fusion, et modifier la même ligne.

### Indice 2

Sur C-D : git fetch origin puis git merge origin/main. HEAD désigne ici C-D. Ne lancez aucune commande destructive pour faire disparaître le message.

### Indice 3

Éditez la phrase commune puis retirez les marqueurs. git add docs/regles.md ; git commit ; tests ; git push. Avant le commit de résolution, git merge --abort permet d’annuler la tentative. Cette règle écrite ne modifie pas les protections GitHub.

# TP06 Écrire pour une équipe absente

Séance 3 · 50 minutes, restitution incluse.
35 min de rédaction et revue · 10 min de test de lecture · 5 min de trace

## Mission

Demain, une autre équipe doit reprendre Campus Events sans vous appeler. Produisez la documentation minimale suffisante pour qu’elle comprenne, exécute et maintienne le projet.

## Ressources disponibles

- docs/architecture.md, guide-technique.md, adr-001.md et changelog.md.
- ateliers/checklist-documentation.md ; docstrings ; générateur tools/build_docs.py.

## Questions à explorer avant de demander une procédure

- Quelles informations peuvent être extraites du code et lesquelles doivent être argumentées ?
- Que doit montrer une ADR pour être utile à une décision future ?
- Comment déceler une instruction qui fonctionne seulement sur le poste de son auteur ?

## Travail à organiser

- A prend l’architecture, B le guide, C l’ADR, D le changelog. Chaque personne ouvre sa PR documentaire.
- Écrivez des exemples vérifiables, les prérequis, les responsabilités et les limites. Une ADR compare au moins deux options.
- Échangez vos PR : le relecteur confronte les affirmations au code et exécute les commandes annoncées. Fusionnez les documents acceptés.
- Générez le rapport et examinez-le. Corrigez les sources, jamais le fichier généré.

## Expériences obligatoires

- Modifiez une docstring, régénérez et retrouvez le changement dans l’API du rapport.
- Identifiez une information techniquement correcte mais insuffisante pour un nouvel arrivant ; améliorez-la après le test de lecture.

## Productions à remettre

- Quatre PR documentaires et leurs revues.
- Un rapport HTML issu des sources relues.
- Un écart de compréhension détecté et sa correction, ou le détail des instructions réussies si aucun écart.

## Critères de réussite connus avant de commencer

- Aucun TODO dans les quatre documents livrés ; prérequis et commandes vérifiables.
- Architecture avec responsabilités et limites ; ADR avec options, décision, conséquences et test.
- Le rapport correspond au code ; chaque affirmation essentielle peut être reliée à une preuve.

## Restitution systématique

Échangez les guides entre les deux binômes. Pendant quatre minutes chacun, un lecteur suit le guide sans aide orale. Les deux minutes finales servent à consigner les lacunes et les corrections.

Compléter ateliers/preuves/tp06.md dans votre dépôt. Le démonstrateur du jour ne montre pas uniquement son propre travail. Un pair renseigne son verdict et ce qui reste à reprendre. Un contrôle automatique vert ne valide pas cette restitution.

## Pour aller plus loin si le socle est validé

Ajoutez un diagramme textuel de flux, puis demandez à un pair de détecter une dépendance ou une limite oubliée.

## Indices à consulter progressivement

### Indice 1

Posez quatre questions : où changer, comment exécuter, pourquoi ce choix, qu’est-ce qui a changé ?

### Indice 2

La capacité nulle est une décision métier à expliquer. La documentation automatique ne connaît pas les options que vous avez écartées.

### Indice 3

Depuis la racine : python tools/build_docs.py ; ouvrir build/documentation.html. Le rendu Markdown est volontairement simple : titres, paragraphes et code.

# TP07 Enquêter sur une automatisation défaillante

Séance 3 · 55 minutes, restitution incluse.
40 min d’expérience · 10 min de diagnostic croisé · 5 min de trace

## Mission

Démontrez que votre chaîne automatique distingue un projet vérifié d’un projet en échec, et que le document livré correspond aux bonnes sources.

## Ressources disponibles

- .github/workflows/qualite.yml ; générateur ; accès Actions ou mode local.
- Fiche ateliers/incident-ci.md ; mémo workflow, run, job, étape et artefact.

## Questions à explorer avant de demander une procédure

- Quels événements déclenchent ce workflow et lesquels ne le déclenchent pas ?
- Pourquoi un ancien artefact vert ne prouve-t-il pas que la dernière modification est correcte ?
- Que peut désigner le SHA d’un run de PR par rapport au SHA de main ?

## Travail à organiser

- Dessinez la chaîne avant de lancer quoi que ce soit : sources, environnement, tests, génération, stockage.
- Sur une branche d’essai et une PR non destinée à être fusionnée, provoquez l’échec contrôlé décrit dans la fiche. Prédisez l’étape qui échouera.
- Retrouvez la première erreur utile dans le log, expliquez sa cause et vérifiez qu’aucun nouvel artefact n’est livré par ce run. Réparez et poussez.
- Téléchargez le résultat du run réussi ; comparez la révision affichée avec le contexte du run. Fermez la PR d’essai sans la fusionner.

## Expériences obligatoires

- Un run rouge puis un run vert, avec la même explication reproductible en local.
- Cherchez un scénario où les tests sont verts mais la documentation reste mauvaise ; expliquez qui doit le détecter.

## Productions à remettre

- Schéma de la chaîne ; liens des deux runs ou preuves locales explicitement étiquetées.
- Message d’erreur utile, hypothèse, cause et correction.
- Rapport téléchargé et explication de sa provenance.

## Critères de réussite connus avant de commencer

- L’équipe distingue recette et exécution, et sait retrouver l’étape responsable.
- La réparation traite la cause sans désactiver les tests.
- La preuve indique la révision et ne confond pas ancien rapport et nouveau résultat.

## Restitution systématique

Un binôme montre un log sans donner son diagnostic ; l’autre a quatre minutes pour expliquer la cause et proposer la vérification. Inversez sur la provenance du rapport ; concluez par deux minutes de comparaison avec vos prédictions.

Compléter ateliers/preuves/tp07.md dans votre dépôt. Le démonstrateur du jour ne montre pas uniquement son propre travail. Un pair renseigne son verdict et ce qui reste à reprendre. Un contrôle automatique vert ne valide pas cette restitution.

## Pour aller plus loin si le socle est validé

Proposez un contrôle documentaire automatisable et dites précisément ce qu’il ne pourrait pas garantir.

## Indices à consulter progressivement

### Indice 1

Le workflow déclenche la génération sur les PR vers main, les pushes sur main et manuellement ; pas sur les tags dans ce fichier.

### Indice 2

Dans Actions, ouvrez le run puis verification. Lire la première erreur utile évite de confondre l’échec initial avec ses conséquences.

### Indice 3

L’incident contrôlé est un test assertEqual(1,2) ajouté uniquement sur une branche d’essai. Le retirer répare cette panne artificielle. En local, build_docs.py retire son ancien rapport avant de tester ; un échec laisse le rapport absent.

# TP08 Passer le projet à une autre équipe

Séance 3 · 55 minutes, restitution incluse.
25 min d’audit · 10 min de correction · 15 min de restitution croisée · 5 min de trace

## Mission

Une équipe indépendante doit reproduire votre livraison. Vous devez l’observer travailler, comprendre ses constats et corriger ce qui bloque sans lui dicter les commandes.

## Ressources disponibles

- Audit en anneau : G1 → G2 → G3 → G4 → G5 → G1.
- ateliers/grille-audit.md ; sources de main, rapport et liens de preuves.

## Questions à explorer avant de demander une procédure

- Qu’est-ce qu’une preuve reproductible par quelqu’un d’autre ?
- Comment distinguer un problème du livrable d’un problème de préparation du poste ?
- Quel état exact du dépôt faut-il présenter à la restitution finale ?

## Travail à organiser

- Chaque groupe audite le dépôt du groupe suivant : G1 examine G2, G2 examine G3, G3 examine G4, G4 examine G5, G5 examine G1. Les propriétaires répondent par écrit aux questions sans dicter les commandes.
- Dans un nouveau dossier de clone, suivez uniquement le README : tests, contrat et génération. Vérifiez une issue, sa PR et une revue.
- Transmettez les constats par écrit puis consacrez dix minutes aux corrections prioritaires de votre propre projet avec revue. Vérifiez le dernier main vert.
- Complétez contributions et preuves. Un seul membre pose v1.0.0 sur le main retenu, ou une nouvelle version si le tag existe déjà.

## Expériences obligatoires

- Un clone propre doit permettre la reproduction sans copier de fichiers de build d’un autre poste.
- Le groupe auditeur choisit un nouveau cas métier, prédit le résultat à partir du contrat puis l’exécute.

## Productions à remettre

- Grille d’audit avec faits reproductibles et retours au groupe propriétaire.
- Liens de correction ou raisons argumentées de non-correction.
- Tag, SHA de main, run correspondant, rapport et contributions des quatre membres.

## Critères de réussite connus avant de commencer

- Un autre groupe réussit les commandes ou documente exactement le blocage.
- Les quatre membres possèdent des preuves d’écriture, de test et de revue.
- La livraison est identifiable et les limites sont annoncées sans présenter une simulation comme une preuve GitHub.

## Restitution systématique

Cinq échanges simultanés : deux ambassadeurs de chaque groupe vont chez le groupe suivant présenter leur audit ; les deux autres restent pour recevoir le groupe précédent. Cinq minutes de constats, cinq minutes de réponse des propriétaires, puis cinq minutes de regroupement pour partager les deux échanges. Consignez les décisions.

Compléter ateliers/preuves/tp08.md dans votre dépôt. Le démonstrateur du jour ne montre pas uniquement son propre travail. Un pair renseigne son verdict et ce qui reste à reprendre. Un contrôle automatique vert ne valide pas cette restitution.

## Pour aller plus loin si le socle est validé

Préparez une mini-demande de changement pour l’équipe suivante : besoin clair, exemple, critère de réussite et impact documentaire.

## Indices à consulter progressivement

### Indice 1

Règle unique : G1 audite G2 ; G2 audite G3 ; G3 audite G4 ; G4 audite G5 ; G5 audite G1. Chaque groupe reçoit donc les constats du précédent.

### Indice 2

N’expliquez pas une commande manquante oralement : faites-la ajouter au guide. Un défaut non corrigé doit avoir une issue et une conséquence explicitée.

### Indice 3

Sur main propre et validé : git pull --ff-only ; git rev-parse HEAD ; git tag -a v1.0.0 -m "Livraison pédagogique" ; git push origin v1.0.0. Le tag ne déclenche pas le workflow fourni : conservez le run du commit main associé.

## Restitution finale de quatre heures

Le dépôt et les preuves des huit TP remplacent un diaporama récapitulatif. Chaque groupe dispose de 30 minutes et chaque membre est interrogé.

| Minutes | Activité |
| --- | --- |
| 0–15 | Cadrage, ouverture des preuves, choix des cas à démontrer |
| 15–45 | Groupe 1 |
| 45–75 | Groupe 2 |
| 75–105 | Groupe 3 |
| 105–120 | Pause |
| 120–150 | Groupe 4 |
| 150–180 | Groupe 5 |
| 180–210 | Audit simultané en anneau sur un nouveau cas proposé par les pairs |
| 210–230 | Rétrospective : pratiques prouvées, limites et améliorations |
| 230–240 | Bilan individuel et remise finale des preuves |

### Chaque passage de 30 minutes

- 4 min : besoin, stratégie d'équipe et une recherche décisive.
- 8 min : choisir une chaîne issue → test rouge → PR → revue → correction → fusion et la montrer réellement.
- 6 min : reproduire un test puis générer un document et en expliquer la provenance.
- 8 min : questions individuelles, deux minutes par membre ; l'une porte sur un cas non préparé, dans le contrat connu.
- 4 min : retour des pairs fondé sur une preuve, pas sur une impression.

Pendant les démonstrations, les autres groupes remplissent une mini-grille : fait observé, preuve, question, limite. Chaque membre du groupe présenté parle au moins trois minutes avant les questions individuelles.

### Évaluation sur 20

12 points collectifs : traçabilité et huit restitutions 3 ; code et tests reproductibles 3 ; documentation et génération 4 ; transfert et démonstration 2.
8 points individuels : contribution expliquée 3 ; revue contradictoire 3 ; capacité à rechercher, tester et justifier devant un cas nouveau 2.

La recherche et le recours raisonné aux indices sont valorisés. Le nombre de commits, la rapidité et l'absence de demande d'aide ne sont pas des critères. Les cases cochées et les résultats automatiques ne remplacent pas l'appréciation du formateur.

Livraison : huit journaux de TP, contributions des quatre membres, liens des PR et revues, code et tests, sources documentaires, rapport généré, SHA de main, tag et run associé ou modalité locale clairement annoncée.
