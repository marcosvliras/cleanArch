from src.data.use_cases import UserFinder
from src.infra.db.repositories.users_repository import UserRepository
from src.infra.db.settings.connection import SessionLocal
from src.presentation.controllers.user_finder_controller import \
    UserFinderController


def user_finder_composer():
    user_repository = UserRepository(SessionLocal)
    user_finder = UserFinder(user_repository)
    controller = UserFinderController(user_finder)

    return controller.handle
