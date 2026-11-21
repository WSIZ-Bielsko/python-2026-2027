from dataclasses import dataclass


# klasa
@dataclass
class User:
    # captures all attributes of a user
    name: str  # pola, ang. "fields"
    age: int
    instagram: str


def display_users(user_list: list[User]) -> None:
    print(f"{'Imię i nazwisko':<20} {'Wiek':>4}  {'Instagram'}")
    print("-" * 45)
    for user in user_list:
        print(f"{user.name:<20} {user.age:>4}  {user.instagram}")

if __name__ == '__main__':
    names = ['Roman', 'Grzegorz', 'Cecylia', 'Karol']
    age = [25, 30, 28, 22]
    instagram = ['@roman', '@grzegorz', '@cecylia', '@karol']

    # instancje
    roman = User('Roman', 25, '@roman')
    karol = User('Karol', 22, '@karol')

    print(karol.name) # dostep do pojedynczego pola


    my_group = [roman, karol]

    for user in my_group:
        print(user)

    from dataclasses import dataclass

    roman = User('Roman', 25, '@roman')
    karol = User('Karol', 22, '@karol')

    ursula = User('Ursula von der Leyen', 68, '@ursulavonderleyen')
    antonio = User('Antonio Costa', 65, "@antoniocosta.eu")
    roberta = User('Roberta Metsola', 47, '@robert.metsola')
    kaja = User('Kaja Kallas', 49, '@kajakallas')

    my_group = [roman, karol]

    leaders = [ursula, antonio, roberta, kaja]

    for user in my_group:
        print(user)

    for leader in leaders:
        print(leader)

    german_leaders = [
        User(name="Joseph Wirth", age=41, instagram=""),
        User(name="Wilhelm Cuno", age=46, instagram=""),
        User(name="Gustav Stresemann", age=45, instagram=""),
        User(name="Wilhelm Marx", age=60, instagram=""),
        User(name="Hans Luther", age=46, instagram=""),
        User(name="Wilhelm Marx", age=63, instagram=""),
        User(name="Hermann Müller", age=52, instagram=""),
        User(name="Heinrich Brüning", age=44, instagram=""),
        User(name="Franz von Papen", age=52, instagram=""),
        User(name="Kurt von Schleicher", age=50, instagram=""),
        User(name="Adolf Hitler", age=43, instagram=""),
        User(name="Konrad Adenauer", age=73, instagram=""),
        User(name="Ludwig Erhard", age=66, instagram=""),
        User(name="Kurt Georg Kiesinger", age=62, instagram=""),
        User(name="Willy Brandt", age=55, instagram=""),
        User(name="Helmut Schmidt", age=55, instagram=""),
        User(name="Helmut Kohl", age=52, instagram=""),
        User(name="Gerhard Schröder", age=54, instagram=""),
        User(name="Angela Merkel", age=51, instagram=""),
        User(name="Olaf Scholz", age=63, instagram=""),
        User(name="Friedrich Merz", age=69, instagram=""),
    ]
    # german_leaders.sort(key=lambda user: user.name)
    sorted_leaders = sorted(german_leaders, key=lambda user: user.name)


    selected = []
    for u in sorted_leaders:
        if u.age > 60:
            selected.append(u)
    display_users(selected)

