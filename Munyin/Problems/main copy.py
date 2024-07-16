def to_list(string):
    return [name.strip() for name in string.split(",") if name.strip()]
user_input = "Solaire, Astel, Kaine, Emil, Rathalos"
result = to_list(user_input)
print(result) 