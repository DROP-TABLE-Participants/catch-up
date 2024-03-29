SERVER_CONTAINER := catch-up-server-1

freeze-deps:
	docker exec ${SERVER_CONTAINER} bash -c "pip3 freeze > requirements.txt"
migrate:
	docker exec ${SERVER_CONTAINER} bash -c "python3 manage.py migrate"
makemigrations:
	docker exec ${SERVER_CONTAINER} bash -c "python3 manage.py makemigrations"