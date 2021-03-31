from resources.resource_users import Users

print(Users.get_all_users())
print(Users.get_user(0))
print(Users.add_user("henrik", [], {}))
print(Users.delete_user(0))
print(Users.update_user(1, "jonas", [], {}))
