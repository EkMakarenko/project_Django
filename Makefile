.EXPORT_ALL_VARIABLES:
COMPOSE_FILE ?= docker-compose.yaml
TEST_COMPOSE_FILE ?= docker-compose.test.yaml

.PHONY: docker-build
docker-build:
	docker build --file=Dockerfile .

.PHONY: docker-up
docker-up:
	docker-compose -f $(COMPOSE_FILE) --env-file=.env up -d --build
	docker-compose ps

.PHONY: docker-logs
docker-logs:
	docker-compose logs --follow

.PHONY: docker-down
docker-down:
	docker-compose down

.PHONY: docker-prune
docker-prune:
	docker container prune -f
	docker volume prune -f

.PHONY: docker-system-prune
docker-system-prune:
	docker system prune -f

.PHONY: docker-bash
docker-bash:
	docker-compose -f $(COMPOSE_FILE) exec web bash

.PHONY: makemigrations
makemigrations:
	docker-compose -f $(COMPOSE_FILE) exec web python manage.py makemigrations

.PHONY: migrate
migrate:
	docker-compose -f $(COMPOSE_FILE) exec web python manage.py migrate

.PHONY: migrations
migrations: makemigrations migrate

.PHONY: tests
tests:
	docker-compose -f $(TEST_COMPOSE_FILE) --env-file=.test_env up --build
