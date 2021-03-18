# oc_project5_repository
OpenClassrooms - Projet5 - Catégorisez automatiquement des questions

## How to use the API ?

### Endpoint
* classification

### post request
**Post a new stackoverflow comment and get the tags**

**params:**
* Title (document's Title)
* Body (document's Body)

**Notes:**
* If no path is given: 400 Bad Request
* If the file is not found: 404 Not Found
* If the document already exists: 409 Conflict
* If the given Id is invalid: 400 Bad Request
