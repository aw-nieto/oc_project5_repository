# oc_project5_repository
OpenClassrooms - Projet5 - Catégorisez automatiquement des questions

## How to use the API ?

### Endpoint
* classification

### get request
**From a corpus determines the tags associated with each document**

**param:** file_path (the corpus file relative path)

*Examples:* http://127.0.0.1:5000/[endpoint]?file_path=[path]

**Notes:**
If no path is given: 400 Bad Request
If the file is not found: 404 Not Found

### post request
**Allows to add a document to a corpus**

**params:**
* file_path (the corpus file relative path)
* Id (document's Id)
* Title (document's Title)
* Body (document's Body)

**Notes:**
* If no path is given: 400 Bad Request
* If the file is not found: 404 Not Found
* If the document already exists: 409 Conflict
* If the given Id is invalid: 400 Bad Request

### delete request
**Allows to remove a document from a corpus**

**params:**
* file_path (the corpus file relative path)
* Id (document's Id)

**Notes:**
* If no path is given: 400 Bad Request
* If the file is not found: 404 Not Found
* If the given Id is invalid: 400 Bad Request
* If the given Id doesn't match any Id from the corpus: 404 Not Found
