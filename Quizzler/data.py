import requests



my_param={
    "amount":10,
    "category":19,
    "type":"boolean"
}

response=requests.get(url="https://opentdb.com/api.php",params=my_param)
response.raise_for_status()
data=response.json()
question_data=data["results"]





