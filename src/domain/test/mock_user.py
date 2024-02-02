from faker import Faker
from src.domain.models import Users

faker = Faker()


def mock_users() -> Users:
    """Mocking Users"""

    return Users(id=faker.string.numeric(), name=faker.name(), password=faker.name())
