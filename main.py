#start просим ввести нужную операцию
user_request = input("Введите желаемый запрос ( доступные для ввода команды : GET, POST, PUT ): ")
user_url = input("Введите URL: ")

def get_request(user_request, user_url):
    import requests
    import json

    response = requests.get(f"{user_url}/products")
    GET = response.text
    json_data = json.loads(GET)

    with open("GET.json", "w") as file:
        json.dump(json_data, file, indent=4)
    print("Был создан файл 'GET.json', содержащий запрос GET")

if user_request == "GET":
    get_request(user_request, user_url)