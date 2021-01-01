username = "Alimou"
password = "1234"
print("interface de connexion de la NASA")
print("______________________________")
print(username,password)
userInput = input("Login:")
passwordInput = input("Password:")
if userInput==username and passwordInput==password:
    print("bienvenue",userInput," a la nasa")