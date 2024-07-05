## Comment j'ai deviné les pastebins à chercher

J'ai utilisé les premières lettres des titres d'albums dans différents ordres pour générer la liste. \
Les pastebins ont des URLs de **8 caractères**, j'ai donc parfois retiré 'CHICA & BONNIE' car c'est le seul titre avec '&', et parfois 'Kayfabe' et 'Chimera' car c'est aussi le nom de l'album, voici les différentes approches que j'ai suivies :

1. **Ordre des albums** : J'ai pris les premières lettres des titres d'albums dans l'ordre défini par le dictionnaire `ALBUM`.
    - Par exemple, `GCSLGKKC` correspond à:
      - **G**LAMROCK **C**ENTIPEDE
      - **S**OEUR **L**OCATION
      - **G**EM **K**ARSON
      - **K**AYFABE
      - **C**HIMERA

2. **Ordre de l'histoire FNAF** : J'ai également généré des chaînes de caractères basées sur l'ordre de l'histoire de Five Nights at Freddy's (FNAF). Par exemple, `GKKSLGCC` correspond à l'ordre défini par `fnaf_order[0]`, l'ordre des jeux dans le lore étant 4/5, 2, 1, 3, 6.

3. **Vraies inversions** : Pour certaines chaînes, j'ai inversé l'ordre des sons, `GCSLGKKC` devient `CKKGLSCG`.

4. **Inversions littérales** : Pour certaines chaînes, j'ai complètement inversé l'ordre des lettres, comme `CKKGLSCG` qui est l'inverse de `GCSLGKKC`.

En résumé, j'ai essayé différentes combinaisons d'ordres, d'inversions et d'exclusions pour couvrir un large éventail de possibilités et augmenter les chances de trouver des Pastebins liés aux albums.

```py
strings = [
    "GCSLGKKC", # album order  | without CHICA & BONNIE
    "GCSLCBGK", # album order  | without KAYFABE + CHIMERA
    "GKKSLGCC", # fnaf order 1 | without CHICA & BONNIE
    "GKSLGCCB", # fnaf order 1 | without KAYFABE + CHIMERA     +     fnaf order 2 | without KAYFABE + CHIMERA
    "KGKSLGCC", # fnaf order 2 | without CHICA & BONNIE
    "CKKGLSCG", # album order  | without CHICA & BONNIE                                                            + TRUE REVERSE
    "KGBCLSCG", # album order  | without KAYFABE + CHIMERA                                                         + TRUE REVERSE
    "CCGLSKKG", # fnaf order 1 | without CHICA & BONNIE                                                            + TRUE REVERSE
    "BCCGLSKG", # fnaf order 1 | without KAYFABE + CHIMERA     +     fnaf order 2 | without KAYFABE + CHIMERA      + TRUE REVERSE
    "CCGLSKGK", # fnaf order 2 | without CHICA & BONNIE                                                            + TRUE REVERSE
    "CKGKSLGC", # album order  | without CHICA & BONNIE        + REVERSE
    "GKCBSLGC", # album order  | without KAYFABE + CHIMERA     + REVERSE
    "CGCSLKGK", # fnaf order 1 | without CHICA & BONNIE        + REVERSE
    "CBGCSLGK", # fnaf order 1 | without KAYFABE + CHIMERA     + REVERSE
    "CGCSLGKK", # fnaf order 2 | without CHICA & BONNIE        + REVERSE
    "CNGCSMGK", # fnaf order 2 | without KAYFABE + CHIMERA     + REVERSE
]
```

## Fonctionnement du script

Ce script Python a pour but de récupérer le contenu de Pastebins en se basant sur la liste des potentiels liens.

### Calculer le nombre de requêtes à effectuer
- Le nombre de combinaisons possibles pour une seule chaîne de longueur 8 est donc 2⁸ = 256.
- Comme il y a 16 chaînes de caractères et que chaque chaîne peut avoir 256 combinaisons possibles de majuscules/minuscules, le nombre total de combinaisons possibles pour les 16 chaînes est 256 * 16. 
- 256 * 16 = 4096.
Le nombre total de combinaisons est donc **4096**.

### Fonctionnement du script :

1. Il importe la liste de chaînes de caractères depuis le fichier `data.py`.

2. Pour chaque combinaison d'url, il génère toutes les combinaisons possibles de majuscules/minuscules, car pastebin donne une url à majuscules aléatoires.
```py
for string in strings: 
    combos = [''.join(x) for x in itertools.product(*([c.upper(), c.lower()] for c in string))]
```

3. Il construit une URL Pastebin pour chaque combinaison en utilisant ces variations.
```py
url = f"https://pastebin.com/raw/{combo}"
```

4. Il envoie une requête HTTP GET à chaque URL. ()
```py
response = requests.get(url)
```

5. Si la réponse ne contient pas "404" (code d'erreur pour page non trouvée), cela signifie qu'un Pastebin a été trouvé. Je n'ai pas utilisé `if response` pour savoir s'il ne sagit pas d'une erreur 429 “Too many requests”.
```py
if '404' not in response.text:
```

6. Le contenu du Pastebin est alors affiché et enregistré dans un fichier texte nommé d'après la combinaison de majuscules/minuscules.
```py
print(response.text)
with open(f"OUTPUT-{combo}.txt", "w") as f: f.write(response.text)
```

En résumé, ce script permet de récupérer automatiquement le contenu de Pastebins potentiellement liés aux albums en testant toutes les variations possibles de majuscules/minuscules dans les titres.

## Crédits

Twitter: [LenochJ](https://x.com/LenochJ) \
GitHub: https://github.com/Lenochxd (svp allez voir vite fait ce que je fais c sympa)


Pour plus de détails, consultez également le document de recherche sur KAYFABE CHIMERA [ici](https://docs.google.com/document/d/1SLhbY3WaDxb8DcWcZYzIluFm9DeSRDdV1CH3rmn6bbI/edit).
