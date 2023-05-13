build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

down-v:
	docker compose down -v

shell: ## Shell into web container
	docker compose exec app bash

migration: ## Create migrations using alembic
	docker compose exec app alembic revision --autogenerate -m "$(m)"

migrate-up: ## Run migrations using alembic
	docker compose exec app alembic upgrade head

test: migrate-up
	docker compose exec app pytest

logs:
	docker compose logs app -f -t