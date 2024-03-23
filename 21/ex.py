import requests


client_id = "T59F2jvmMUrbGaTGJYQQ4g"


api_key = "7CxymDDzw5yceI---PE5_1IrqRpnxgBWLxkTA-oBrlUcZgAdGLV5WoASGs3v-TD8tWJyT7DTMluzJPqVmH-TLNpeW6I1psUXXwxpzyu37tCqlBWQzlthL47HqpL-ZXYx"

api_url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization":"Bearer " + api_key
}

params = {
    "limit":30,
    "location":"Miami"
}


response = requests.get(api_url, headers=headers, params=params)
print(response)
