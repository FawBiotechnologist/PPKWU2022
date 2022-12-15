docker_name:=lab6_python
container_name:=lab6_container_python

docker_build:
	echo "Prepare docker here..."
	docker build -t $(docker_name):latest .
docker_start:
	echo "Start docker here..."
	docker run -p 4080:4080 --name $(container_name) $(docker_name):latest &
docker_stop:
	echo "Stop docker here..."
	docker kill $(container_name)
	docker container rm $(container_name)
docker_clean:
	echo "Clean docker here..."
	-docker container rm $(container_name)
	docker image rm $(docker_name)
docker_restart:
	echo "Rebooting docker here ..."
	docker kill $(container_name)
	docker container rm $(container_name)
	docker image rm $(docker_name)
	echo "Prepare docker here ..."
	docker build -t $(docker_name):latest .
	docker run -p 4080:4080 --name $(container_name) $(docker_name):latest &
	echo "Docker rebooted"
