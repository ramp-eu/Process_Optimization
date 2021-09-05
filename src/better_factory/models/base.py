from datetime import datetime

from sqlalchemy import Column, BigInteger, DateTime
from sqlalchemy.schema import MetaData
from sqlalchemy.ext.declarative import declarative_base

# Recommended naming convention used by Alembic, as various different database
# providers will autogenerate vastly different names making migrations more
# difficult. See: http://alembic.zzzcomputing.com/en/latest/naming.html
NAMING_CONVENTION = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}

metadata = MetaData(naming_convention=NAMING_CONVENTION)
Base = declarative_base(metadata=metadata)


class BaseModel(Base):
    __abstract__ = True
    __table_args__ = {'extend_existing': True}

    id = Column(BigInteger, primary_key=True)
    created_at = Column(
        DateTime,
        nullable=True,
        default=datetime.utcnow,
    )
    updated_at = Column(
        DateTime,
        nullable=True,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
