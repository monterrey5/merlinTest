import requests


BASE_URL = "https://petstore.swagger.io/v2"


class User:
    user = {
        "id": 1122,
        "username": "Johnie",
        "firstName": "John",
        "lastName": "Smith",
        "email": "jsmith@gmail.com",
        "password": "pwd11",
        "phone": "333",
        "userStatus": 1
    }


class SoldPet:
    pets_id_name = None

    def __init__(self, id, name):
        self.id = id
        self.name = name
        if SoldPet.pets_id_name is None:
            SoldPet.pets_id_name = []
        SoldPet.pets_id_name.append(self)

    @classmethod
    def get_names_count(cls):
        names_count_dict = {}
        for pet in cls.pets_id_name:
            if pet.name not in names_count_dict:
                names_count_dict[pet.name] = 0
            names_count_dict[pet.name] += 1
        return names_count_dict


def create_user():
    try:
        new_user_url = f"{BASE_URL}/user"
        requests.post(url=new_user_url, json=User.user)
        print("\nNew user created.")
    except:
        print("\nError occurred when creating a user.")
    return


def get_user_info():
    user_info_url = f"{BASE_URL}/user/{User.user['username']}"
    user = requests.get(user_info_url).json()
    print(f"\nCreated User Info:\n{user}")
    return


def list_sold_pets():
    sold_pets_url = f"{BASE_URL}/pet/findByStatus?status=sold"
    pets = requests.get(sold_pets_url).json()
    print(f"\nList of sold pet ids and pet names:")
    for pet in pets:
        print(pet["id"], pet["name"])
        SoldPet(pet["id"], pet["name"])
    return


if __name__ == "__main__":
    create_user()
    get_user_info()
    list_sold_pets()
    if SoldPet.pets_id_name is None:
        print("No sold pets found.\n")
    else:
        names_count_dict = SoldPet.get_names_count()
        print(f"\nPet Names Count:\n{names_count_dict}\n")
