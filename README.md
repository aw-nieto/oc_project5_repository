# oc_project5_repository
OpenClassrooms - Projet5 - Catégorisez automatiquement des questions

## How to use the API ?

### Resources
* Github: https://github.com/aw-nieto/oc_project5_repository
* Heroku: https://oc-p5-app.herokuapp.com/

Note: The heroku server will probably be down (hence not usable)

### Endpoint
* label

### post request
**Post a new stackoverflow comment and get the tags**

**params:**
* Title (document's Title)
* Body (document's Body)

### example code
* Note (Comment_Title and Comment_Body are to be replaced)

```python
import requests
json_request = {
    'Title': <Comment_Title>,
    'Body': <Comment_Body>
}
    
r = requests.post('https://oc-p5-app.herokuapp.com/label/', json=json_request)
print(f'HTTP Status Code: {r.status_code}')
print(r.json())
```

* If there is not any tag predicted, return 404 status

### examples

* e1 

Title: 	What is the correct JSON content type?

Body:	I've been messing around with JSON for some time, just pushing it out as text and it hasn't hurt anybody (that I know of), but I'd like to start doing things properly.
	I have seen so many purported "standards" for the JSON content type:
	application/json
	application/x-javascript
	text/javascript
	text/x-javascript
	text/x-json
	But which one is correct, or best? I gather that there are security and browser support issues varying between them.
	I know there's a similar question, What MIME type if JSON is being returned by a REST API?, but I'd like a slightly more targeted answer.

-> Predicted: json

* e2

Title: 	What is the “-->” operator in C/C++?

Body: 	After reading Hidden Features and Dark Corners of C++/STL on comp.lang.c++.moderated, I was completely surprised that the following snippet compiled and worked in both Visual Studio 2008 and G++ 4.4.
	Here's the code:
	#include <stdio.h>
	int main()
	{
		int x = 10;
		while (x --> 0) // x goes to 0
		{
			printf("%d ", x);
		}
	}
	Output:
	9 8 7 6 5 4 3 2 1 0
	I'd assume this is C, since it works in GCC as well. Where is this defined in the standard, and where has it come from?

-> Predicted: c, c++