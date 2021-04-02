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

### example code
* Note (Comment_Title and Comment_Body are to be replaced)

import requests
json_request = {
    'Title': <Comment_Title>,
    'Body': <Comment_Body>
}
    
r = requests.post('https://oc-p5-app.herokuapp.com/label/', json=json_request)
print(f'HTTP Status Code: {r.status_code}')
print(r.json())

### examples

