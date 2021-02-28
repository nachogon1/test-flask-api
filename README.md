## Initialize:
`export FLASK_APP=main.py; python -m flask run`

## Swagger:
You can test the api in swagger by going to http://127.0.0.1:5000

## Example curl:

-Create User:
`curl -X POST 'http://127.0.0.1:5000/api/user' -H "Content-Type: application/json"  -d '{"username": "test", "first_name":"test_first_name", "last_name": "test_last_name"}'`

-Create Post:
`curl -X POST 'http://127.0.0.1:5000/api/post?user_id=1' -H "Content-Type: application/json"  -d '{"title": "In the beach", "description":"Falling down is an excuse to get back again."}'`

-Give Like (Don't forget to change the post_id):
`curl -X PUT 'http://127.0.0.1:5000/api/post/like?user_id=1&post_id=<PASTE_POST_ID_FROM_RESPONSE>'`

-Create Comment (Don't forget to change the post_id):
 `curl -X POST 'http://127.0.0.1:5000/api/post/comment?user_id=1&post_id=<PASTE_POST_ID_FROM_RESPONSE>'   -H "Content-Type: application/json" -d '{"text": "Me", "description":"With my friends."}'`

## Test:
Write in the base folder of the project
`pytest`

## Caveats:
Right now everybody can get, edit, create, and delete posts. 
In practise, I would use log-ins and scopes to restrict the access.
