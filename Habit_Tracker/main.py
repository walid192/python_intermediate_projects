import requests
import os
from datetime import datetime

USERNAME="walid192"
TOKEN=os.getenv("TOKEN")
GRAPH_ID="graph1"

Pixela_endpoint="https://pixe.la/v1/users"
my_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",   
}



graph_endpoint=f"{Pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id":GRAPH_ID,
    "name":"coding",
    "unit":"hour",
    "type":"int",
    "color":"momiji"
  
}
headers={
    "X-USER-TOKEN":TOKEN
}


add_pixel_endpoint=f"{Pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today=datetime.now()

pixel_config={
    "date":today.strftime("%Y%m%d"),
    "quantity":"2"
    
}
response=requests.post(url=add_pixel_endpoint,json=pixel_config,headers=headers)
print(response.text)