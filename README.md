##Caveats:
Right now everybody can get, edit, create, and delete posts. 
In practise, I would use log-ins and scopes to restrict the access.

##Initialize:
`export FLASK_APP=main.py; python -m flask run`

##Example curl:

-Create Post:
`curl -X POST 'http://127.0.0.1:5000/api/post?user_id=1' -H "Content-Type: application/json"  -d '{"title": "In the beach", "description":"Falling down is an excuse to get back again."}'`

-Create User:
`curl -X POST 'http://127.0.0.1:5000/api/user' -H "Content-Type: application/json"  -d '{"username": "test", "first_name":"test_first_name", "last_name": "test_last_name"}'`
