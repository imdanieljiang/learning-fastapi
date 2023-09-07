import requests

localhost = "http://127.0.0.1:8000"

print("Adding an item:")
print(
    requests.post(
        f"{localhost}/",
        json={
            "name": "Screwdriver",
            "price": 3.99,
            "count": 10,
            "id": 4,
            "category": "tools"
        },
    ).json()
)
print(requests.get(f"{localhost}/").json())
print()

print("Updating an item:")
print(requests.put(f"{localhost}/items/0?count=9001").json())
print(requests.get(f"{localhost}/").json())
print()

print("Deleting an item:")
print(requests.delete(f"{localhost}/items/0").json())
print(requests.get(f"{localhost}/").json())