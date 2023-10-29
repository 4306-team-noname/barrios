from emmett import App
from emmett.orm import Database
from models.User import User


def setup_app_commands(app: App, db: Database, auth):
    @app.command("setup_admin")
    def setup_admin():
        with db.connection():
            user = User.create(
                email="jcaldwell2@angelo.edu",
                first_name="Jeff",
                last_name="Caldwell",
                password="SuperSecret123!",
            )

            admins = auth.create_group("admin")
            auth.add_membership(admins, user.id)

    @app.command("setup_analyst")
    def setup_analyst():
        with db.connection():
            user = User.create(
                email="analyst@test.test",
                first_name="Analisa",
                last_name="Seriesdata",
                password="SuperSecret123!",
            )

            analysts = auth.create_group("analyst")
            auth.add_membership(analysts, user.id)
