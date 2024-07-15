import requests


response = requests.post('http://localhost:5000/cars')
expected = "Creating new car"
actual = response.text
assert expected == actual
expected = 201
actual = response.status_code
assert expected == actual
print(response.text)
