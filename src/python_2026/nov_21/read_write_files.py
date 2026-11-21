import json
from dataclasses import dataclass


@dataclass
class User:
    name: str  # pola, ang. "fields"
    age: int
    instagram: str

def read_users_from_json(filename: str) -> list[User]:
    with open(filename, 'r') as file:
        users_data = json.load(file)
        return [User(**user_data) for user_data in users_data]


def write_users_to_json(filename: str, users: list[User]):
    with open(filename, 'w') as file:
        json.dump([user.__dict__ for user in users], file)



if __name__ == '__main__':
    ursula = User('Ursula von der Leyen', 68, '@ursulavonderleyen')
    antonio = User('Antonio Costa', 65, "@antoniocosta.eu")
    roberta = User('Roberta Metsola', 47, '@robert.metsola')
    kaja = User('Kaja Kallas', 49, '@kajakallas')

    users = [ursula, antonio, roberta, kaja]
    write_users_to_json('users.json', users)
    new_users = read_users_from_json('users.json')
    print(new_users)


    germans = read_users_from_json('german_leaders.json')
    print(germans)