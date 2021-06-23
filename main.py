from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
app = Flask(__name__)
@app.route("/")
def hello():

  return "Hello World!"
BASE_URL = 'https://hiskenya.org'

username = 'Vee Ouma'
password = 'Milestone2019..'

headers = {
'Content-type': 'application/xml',
'Authorization': 'Basic {BSCAUTH}'
}


def data():
    kenya_url = requests.get('https://hiskenya.org/api/dataSets')
    print(kenya_url)
    return kenya_url


#chuck_url = requests.get('https://api.chucknorris.io/jokes/random')
#print(chuck_url.json())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)



