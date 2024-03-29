SERVER_CONTAINER := catch-up-server-1

freeze-deps:
	docker exec ${SERVER_CONTAINER} bash -c "pip3 freeze > requirements.txt "