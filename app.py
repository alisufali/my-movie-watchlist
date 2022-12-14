import pytz

from pathlib import Path
from typing import Optional

from modules.config import Config
from modules.database import Database
from modules.enums import MenuFunctionalities
from modules.menu import Menu, MenuFunctions


class Main:

    @classmethod
    def main(cls, config_path: Optional[Path] = None,
             timezone: pytz.BaseTzInfo = None, indent: int = 2):

        Config.load_configs(config_path=config_path)
        Database.connect_to_database()

        menu = Menu(indent=indent)

        while (user_input := int(input(menu))) != \
                MenuFunctionalities.EXIT.value:
            if user_input == \
                    MenuFunctionalities.ADD_USER.value:
                username = input("Username: ")
                MenuFunctions.add_user(
                    username=username
                )
            elif user_input == \
                    MenuFunctionalities.ADD_MOVIE.value:
                title = input("Movie title: ")
                release_date_string = input("Release date (dd-mm-YYYY): ")
                MenuFunctions.add_movie(
                    title=title, release_date_string=release_date_string,
                    timezone=timezone
                )
            elif user_input == \
                    MenuFunctionalities.WATCH_A_MOVIE.value:
                username = input("Username: ")
                title = input("Movie title: ")
                MenuFunctions.watch_movie(
                    username=username, title=title
                )
            elif user_input == \
                    MenuFunctionalities.VIEW_ALL_USERS.value:
                MenuFunctions.view_all_users(indent=2*indent)
            elif user_input == \
                    MenuFunctionalities.VIEW_UPCOMMING_MOVIES.value:
                MenuFunctions.view_upcomming_movies(
                    timezone=timezone, indent=2*indent
                )
            elif user_input == \
                    MenuFunctionalities.VIEW_ALL_MOVIES.value:
                MenuFunctions.view_all_movies(
                    timezone=timezone, indent=2*indent
                )
            elif user_input == \
                    MenuFunctionalities.VIEW_WATCHED_MOVIES.value:
                username = input("Username: ")
                MenuFunctions.view_watched_movies(
                    username=username, timezone=timezone,
                    indent=2*indent
                )
            elif user_input == \
                    MenuFunctionalities.SEARCH_MOVIE.value:
                search_term = input("Input the partial movie title: ")
                MenuFunctions.search_movie(
                    search_term=search_term, timezone=timezone,
                    indent=2*indent
                )
            else:
                print("Invalid input please try again.")


if __name__ == "__main__":
    indent = 2

    timezone = pytz.timezone("Iran")

    Main.main(timezone=timezone, indent=indent)
