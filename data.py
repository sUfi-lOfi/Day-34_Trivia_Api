import requests
request = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean")
request.raise_for_status()
question_list = request.json()["results"]