docker_build:
	echo "Prepare docker here..."
	docker build -t lab1_python:latest .
docker_start:
	echo "Start docker here..."
	docker run -p 4080:4080 --name lab1_container_python lab1_python:latest &
docker_stop:
	echo "Stop docker here..."
	docker kill lab1_container_python
	docker container rm lab1_container_python
docker_clean:
	echo "Clean docker here..."
	-docker container rm lab1_container_python
	docker image rm lab1_python
