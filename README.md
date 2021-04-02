# oc_project5_repository
OpenClassrooms - Projet5 - Catégorisez automatiquement des questions

## How to use the API ?

### Endpoint
* label

### post request
**Post a new stackoverflow comment and get the tags**

**params:**
* Title (document's Title)
* Body (document's Body)

### examples
import requests
json_request = {
    'Title': 'How can I remove a specific item from an array?',
    'Body': "I have an array of numbers and I'm using the .push() method to add elements to it.\
        Is there a simple way to remove a specific element from an array\
        I'm looking for the equivalent of something like:\
            array.remove(number);\
        I have to use core JavaScript. Frameworks are not allowed."
}
    
r = requests.post('https://oc-p5-app.herokuapp.com/label/', json=json_request)
print(f'HTTP Status Code: {r.status_code}')
print(r.json())
