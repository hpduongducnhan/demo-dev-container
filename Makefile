run-fastapi:
	poetry run uvicorn demotools.fastapi_app:app --host 0.0.0.0 --port 5000

docker-build:
	docker build --progress=plain -t testdevcontainer .