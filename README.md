# Pour lancer l'application

## 1. installer le fichier venv

linux:

```shell
 python3 -m venv venv
```

windows:

```shell
 py -3 -m venv venv
```

## 2. Activer l'environnement

linux:

```shell
 . venv/bin/activate
```

windows:

```shell
 venv\Scripts\activate
```

## 3. Installer les dépendances

```shell
pip install Flask
pip install flask-mysqldb
```

## 4. Lancer l'application

```shell
flask --app main run --debug
```

## Installer MYSQL (ligne de commande)

```shell
sudo apt install mysql-server
```

1. créer un utilisateur flask

```shell
CREATE DATABASE nom_de_la_base
```

2. créer une bdd et la nommer flask

```shell
CREATE USER 'new_user' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON database.* TO 'user';
```

3. Importer la bdd

```shell
    mysql -u flask -p flask < path/de/mon/fichier.sql
```
