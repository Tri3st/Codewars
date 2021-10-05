{}user = [
  (0, "Bob",  "password"),
  (1, "Rolf", "bob122"),
  (2, "José", "long4password"),
  (3, "username", "1234")
]

username_mapping = {user[1]: user for user in users}

print(username_mapping)