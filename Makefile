rebuild:
	docker-compose stop
	docker-compose build
	docker-compose up -d

run:
	docker-compose up -d

restart:
	docker-compose stop
	docker-compose up -d
