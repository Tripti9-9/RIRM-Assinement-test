from fastapi import FastAPI
from pydantic import BaseModel


data = [
    {'social links':'https://www.facebook.com/fulioTech/:', 'email': 'support@ful.io', 'contact': '+1 343 303 6668'}
]    


class urls(BaseModel):
  social_links: str
  email: str
  contact:int
  
app = FastAPI()


@app.get("/urls")
def get_users(urls):
    r = requests.get(row['url'])
    return data
