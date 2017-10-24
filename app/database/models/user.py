
from edmunds.database.model import relationship, backref
from edmunds.auth.models.usermixin import UserMixin
from app.database.models.role import Role
from app.database.models.userroles import UserRolesTable
from edmunds.database.model import Model


class User(Model, UserMixin):
    """
    User Model
    """

    # __tablename__ = 'user'
    # __bind_key__ = 'users_database'

    roles = relationship(Role, backref=backref('users', lazy='dynamic'), secondary=UserRolesTable)
