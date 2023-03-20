import requests
import os
from datetime import datetime


# ------------------------------------ CONSTSANTS -------------------------------------------#
APP_ID=os.getenv("APP_ID")
API_KEY=os.getenv("APP_KEY")
NUTRITIONS_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT="https://api.sheety.co/89f8da851a6c95fa1a7024ed31897215/workoutProject/workouts"
WEIGHT=56
HEIGHT=1.82
AGE=21
GENDER="male"
today=datetime.now().strftime("%Y/%m/%d")
time=datetime.now().strftime("%H:%M:%S")
TOKEN=os.getenv("TOKEN")


# ------------------------------------- PROJECT SETUP-------------------------------#
exercice=input("what have you done today ? : ")
headers={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
}


POST_REQUESTS_BODY={
    "query":exercice,
    "gender": GENDER,
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE
    
}
response=requests.post(url=NUTRITIONS_ENDPOINT,headers=headers,json=POST_REQUESTS_BODY)
response.raise_for_status()
data=response.json()
exercices=data["exercises"]


SHEETY_ENPOINT_headers={
    "Authorization": f"Bearer {TOKEN}"
}
for exercice in exercices:
    row={
        "workout":{
            "date":today,
            "time":time,
            "exercise":exercice["name"],
            "duration":exercice["duration_min"],
            "calories":exercice["nf_calories"]
        }
    }
    post_response=requests.post(url=SHEETY_ENDPOINT,json=row,headers=SHEETY_ENPOINT_headers)
    post_response.raise_for_status()
    print(post_response.json())