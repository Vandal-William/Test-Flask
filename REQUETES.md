# Projet SQL Hetic

## GROUPE DE TRAVAIL

```
VANDAL William
YALMAN Lucas
KENGNI Théophane
YAICH Mohamed
```

## LANCER FLASK

```
cf. README.md
```


## Groupe 1 : SELECT (Sans jointures) (0.5/20)

1. Lister le nom et le prénom des musiciens, ordonnées par leur date de naissance

```sql
SELECT first_name, last_name
FROM artist
ORDER BY birthdate;
```
```bash
nombres de résultats : 200
```

2. Lister le nom et la capacité des lieux disponibles, ordonnés par capacité croissante

```sql
SELECT name, max_spectators
FROM place
ORDER BY max_spectators ASC; 
```
```bash
nombres de résultats : 5
```

3. Lister les 5 prochains concerts

```sql
SELECT * FROM event
WHERE discr = 'concert'
ORDER BY start_time
ASC LIMIT 5;
```
```bash
nombres de résultats : 5
```

## Groupe 2 : WHERE (0.5/20)

1. Lister les spectateurs originaires de Croatie

```sql
SELECT *
FROM spectateur
WHERE country = 'Croatia'; 
```
```bash
nombres de résultats : 7
```

2. Lister les musiciens nés entre 1970 et 1990

```sql
SELECT last_name, first_name, birthdate
FROM artist
WHERE birthdate
BETWEEN '1970-01-01' AND '1990-12-31';
```
```bash
nombres de résultats : 113
```

3. Lister les spectateurs dont le nom commence par B et nés avant 1970

```sql
SELECT *
FROM spectateur
WHERE last_name LIKE 'B%'
AND birthdate < '1970-01-01'; 
```
```bash
nombres de résultats : 15
```

4. Lister les concerts (id et date) par ordre chronologique

```sql
SELECT * FROM event
WHERE discr = 'concert'
ORDER BY date ASC;
```
```bash
nombres de résultats : 10
```

## Groupe 3 : JOIN (1/20)

1. Lister les concerts et afficher les artistes présent à chacun d’eux
```sql
```
```bash
nombres de résultats : 
```

2. Lister les concerts en indiquant le lieu dans lequel ils se déroulent
```sql
```
```bash
nombres de résultats : 
```

3. Lister les instruments de chaque groupe

```sql
SELECT g.name, GROUP_CONCAT(DISTINCT a.instrument
ORDER BY a.instrument SEPARATOR ', ') AS instruments
FROM `group` g
LEFT JOIN artist a ON g.id = a.id
GROUP BY g.id;
```
```bash
nombres de résultats : 60
```

4. Lister les concerts auxquels va assister Retha Dookie, avec la liste des membres du groupe, le lieu et la date/heure

```sql
SELECT spectateur.first_name, spectateur.last_name, event.start_time, event.discr, place.name FROM spectateur
JOIN ticket ON spectateur.id = ticket.spectator_id
JOIN concert ON ticket.concert_id = concert.id
JOIN event ON concert.id = event.id
JOIN place ON event.place_id = place.id
WHERE spectateur.first_name = 'Retha'; 
```
```bash
nombres de résultats : 3
```

5. Calculer le panier moyen des ventes

```sql
SELECT ticket.price_id, COUNT(ticket.price_id) AS nombre_tickets, price.price, price.price * COUNT(ticket.price_id) AS prix_total, SUM(price.price * COUNT(ticket.price_id))
OVER () AS chiffre_affaire, ( SELECT COUNT(*)
FROM spectateur ) AS max_spectateur , (SUM(price.price * COUNT(ticket.price_id))
OVER () / ( SELECT COUNT(*)
FROM spectateur ) ) AS panier_moyen
FROM ticket
LEFT JOIN price ON ticket.price_id = price.id
GROUP BY ticket.price_id, price.price; 
```
```bash
nombres de résultats : 10
```

6. Lister qui est en première et seconde partie de chaque concert (et indiquer s’il n’y a personne)

```sql
SELECT place.name, artist.first_name, artist.last_name, concert_part.gig FROM concert_part
JOIN artist ON concert_part.artist_id = artist.id
JOIN concert ON concert_part.concert_id = concert.id
JOIN event ON concert.id = event.id
JOIN place ON event.place_id = place.id
WHERE concert_part.status = 'signed'
OR concert_part.status = 'cancelled';
```
```bash
nombres de résultats : 8
```

7. Lister les salles/lieux et les contraintes techniques de chacune.

```sql
SELECT p.name, tc.equipment, tc.description
FROM place p
LEFT JOIN technical_constraints_place tcp ON p.id = tcp.place_id
LEFT JOIN technical_constraints tc ON tcp.technical_constraints_id = tc.id; 
```
```bash
nombres de résultats : 10
```

8. Lister les groupes et les salles où ils se produisent

```sql
SELECT place.name, group.name
FROM concert_part
JOIN artist ON concert_part.artist_id = artist.id
JOIN artist_group ON artist.id = artist_group.artist_id
JOIN `group` ON artist_group.group_id = group.id
JOIN concert ON concert_part.concert_id = concert.id
JOIN event ON concert.id = event.id
JOIN place ON event.place_id = place.id;
```
```bash
nombres de résultats : 14
```

## Groupe 4 : GROUP BY (1/20)

1. Lister les groupes et leur nombre de membres.

```sql
SELECT g.name AS groupe, COUNT(ag.artist_id) AS nombre_membres
FROM `group` AS g
INNER JOIN artist_group AS ag ON g.id = ag.group_id
GROUP BY g.id;
```
```bash
nombres de résultats : 60
```

2. Lister les concerts en indiquant le nombre de places vendues.

```sql
SELECT ticket.concert_id, COUNT(ticket.concert_id) AS places_vendues
FROM ticket
LEFT JOIN concert ON ticket.concert_id = concert.id
GROUP BY ticket.concert_id, concert.id ; 
```
```bash
nombres de résultats : 10
```

3. Lister le total des ventes pour chaque journée de festival (en se basant sur startTime)

```sql
SELECT DATE(event.start_time) AS date, SUM(price.price) AS total_journalier
FROM ticket
LEFT JOIN price ON ticket.price_id = price.id
LEFT JOIN concert ON ticket.concert_id = concert.id
LEFT JOIN event ON concert.id = event.id
GROUP BY DATE(event.start_time)
ORDER BY DATE(event.start_time);
```
```bash
nombres de résultats : 8
```

4. Lister la moyenne du montant des ventes pour chaque concert

```sql
SELECT ticket.concert_id, SUM(price.price) AS total_concert
FROM ticket
LEFT JOIN price ON ticket.price_id = price.id
LEFT JOIN concert ON ticket.concert_id = concert.id
LEFT JOIN event ON concert.id = event.id
GROUP BY ticket.concert_id; 
```
```bash
nombres de résultats : 10
```

5. Lister les concerts qui ont rassemblé plus de 100 spectateurs

```sql
SELECT place.name, ticket.concert_id, COUNT(spectator_id)
FROM ticket
JOIN concert ON ticket.concert_id = concert.id
JOIN event ON concert.id = event.id
JOIN place ON event.place_id = place.id
GROUP BY ticket.concert_id
HAVING COUNT(spectator_id) > 100;
```
```bash
nombres de résultats : 5
```

## Groupe 5 : Requêtes ensemblistes (3/20)

1. Lister les nom, prénom de ceux qui font le festival : Artistes et Bénévoles.
2. Pour les téméraires : reprenez la requête précédente et ajouter une colonne indiquant le rôle (artiste ou bénévole) de chacun.

```sql
SELECT a.first_name AS name, a.last_name, r.role_name FROM artist a
JOIN role r ON a.id = r.person_id
UNION ALL SELECT s.first_name AS name, s.last_name, r.role_name FROM staff s
JOIN role r ON s.id = r.person_id; 
```
```bash
nombres de résultats : 21
```

## Groupe 6 : Requêtes complexes (3/20)

1. Afficher les groupes qui passent en seconde partie de concert
```sql
```
```bash
nombres de résultats : 
```


2. Lister les gens qui ont dépensé plus que la moyenne du panier d’achat
```sql
```
```bash
nombres de résultats : 
```


3. Recommandation : Trouver des concerts qui pourraient intéresser un spectateur
```sql
```
```bash
nombres de résultats : 
```


Explications :

J’ai réservé une place pour un concert

Trouver les personnes qui ont aussi réservé une place pour ce même concert

Trouver les autres concerts auxquels ces personnes ont assisté

Sélectionner les 3 qui ont le meilleur « score »
