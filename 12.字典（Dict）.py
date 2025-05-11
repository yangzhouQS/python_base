d = {
    "name": "Mike",
    "age": 25,
    "city": "New York"
}
print(d)
print(d["name"])
print(type(d))
print(d.keys())
print(d.values())
print(d.items())
print(d.get('name'))
print(d.update({"age": 33}))
print(d)

for key, value in d.items():
    print(key, value)

for key in d.keys():
    print(key, d[key])




