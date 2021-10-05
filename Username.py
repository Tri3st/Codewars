#exercise for udemy course
users = [
  (0, "Bob",  "password"),
  (1, "Rolf", "bob122"),
  (2, "José", "long4password"),
  (3, "username", "1234")
]

username_mapping = {user[1]: user for user in users}

#print(username_mapping)

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

if not username_input in username_mapping:
  print("Wrong username")
else:

  _, username, password = username_mapping[username_input]

  if  password_input == password:
    print("Your credentials are correct")
  else:
    print("No!! HACKERZ!")