# College ERP — Placement Tracker

A Django application for managing college placement records: add, list, update
and delete placed-student entries (name, department, employer, date, package,
reference number). Staff login required for all data views; Django admin
included.

Stack: Django 4.2 LTS, Gunicorn, WhiteNoise, PostgreSQL (via `DATABASE_URL`)
on Heroku with SQLite fallback for local development.

## Local setup

```sh
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then edit SECRET_KEY etc.
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ and log in with the superuser account.

## Environment variables

| Variable        | Purpose                                        |
|-----------------|------------------------------------------------|
| `SECRET_KEY`    | Django secret key (generate a fresh one; never commit it) |
| `DEBUG`         | `True`/`False` (default `True` for local dev)   |
| `ALLOWED_HOSTS` | Comma-separated hosts (e.g. `.herokuapp.com,yourdomain.tech`) |
| `DATABASE_URL`  | Postgres URL. Unset → local `db.sqlite3` (gitignored) |

## Deploy to Heroku

```sh
heroku create your-app-name
heroku addons:create heroku-postgresql:essential-0
heroku config:set SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com,yourdomain.tech"
git push heroku modernize/erp-project:main
```

The `release` phase in the Procfile runs migrations automatically.
Static files are served by WhiteNoise (`collectstatic` runs at build).

> Note: an old `db.sqlite3` with demo data was previously committed to this
> repo and has been removed. If you cloned before that cleanup, rotate any
> credentials that may have been exposed and do not reuse the old database file.
