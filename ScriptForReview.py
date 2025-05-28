import requests

def requestCheck():
    url = "https://search.yandex-team.ru/suggest/?text=Саптех&version=2&people.per_page=10"
    response = requests.get(url)
    data = response.json()
    return parseChecker(data)

def parseChecker(response: dict) -> list[str]:
    logins = []
    if "people" in response and "per_page" in response["people"]:
        people = response["people"].get("items", [])
        for person in people:
            if "login" in person:
                logins.append(person["login"])
    return logins
if __name__ == "__main__":
    logins = requestCheck()
    print("Логины:", logins)
