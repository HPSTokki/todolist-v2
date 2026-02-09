# ToDo List Version 2
----------
## Inclusions
- FastAPI Basic Backend Configured
- SvelteKit Basic Frontend Configured
- Supabase Connection
- Tauri Configured to ship frontend as executable
- Basic `npm` and `pip` usage
- DB Migrations, Changes and Revisions with alembic(python)

----------

## How To Test

1. Clone this Repository:
```powershell
git clone https://github.com/HPSTokki/todolist-v2.git
```
2. Open or split Terminal and change directory to both to /backend and /frontend:
```powershell
cd /frontend
cd /backend
```
3. Run the following commands:
```powershell
For /backend:
python -m venv .venv
./.venv/bin(or Script)/Activate.ps1
pip install -r requirements.txt

For /frontend:
npm install
npm run dev
```
----------

## Alembic

I used Alembic to do auto or manual or helpful migrations to the supabase or basically just any url of database based on the `alembic.ini` file under the `sqlalchemy.url == db://url`

If you want to make changes and upload on the existing supabase of mine, change the python files under `/models` folder, either make a new one or just edit the existing, you can follow the pattern of existing `Task.py`

In case you want to see the migrations happening locally and use local sqlite also, change the `alembic.ini` file under the `sqlalchemy.url` into `sqlite:///local.db`, no quotes. Also remove the `database_url`, by the `/alembic/env.py` around the `url = config.get_main_option("sqlalchemy.url", database_url)`

After doing the changes you want just open up a terminal make sure python environment is active and do the following

```powershell
alembic revision -m "message here" --autogenerate
alembic upgrade head
```

If you did use local db, change the `engine.py` under `/backend/src`, I left a comment there.

Thank you!

