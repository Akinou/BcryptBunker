import bcrypt

# Demander à l'utilisateur d'entrer le mot de passe à hacher
password = input("Entrez le mot de passe à hacher : ")
# Générer un sel aléatoire
salt = bcrypt.gensalt()
# Hacher le mot de passe en utilisant le sel
hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

# Afficher le sel et le mot de passe haché
print("Sel : " + salt.decode('utf-8'))
print("Mot de passe haché : " + hashed_password.decode('utf-8'))
