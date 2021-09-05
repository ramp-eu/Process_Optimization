from .base import Base

__all__ = [
    'Base',
]


def includeme(config):
    config.include('tet.sqlalchemy.simple')
    config.setup_sqlalchemy()
