from setuptools import setup, find_packages


base_requires = [
    # core
    'pyramid==1.10.4',
    'tet==0.3.2',

    # DB
    'SQLAlchemy==1.3.10',
    'zope.sqlalchemy==1.2',
    'psycopg2-binary==2.8.4',
    'alembic==1.2.1',
    'pyramid-tm==2.3',
    'pyramid-retry==2.1',
    'transaction==2.4.0',

    # task queue
    # 'huey==2.1.3',
    # 'redis==3.4.1',

    # others
    'waitress==2.0.0',
    'pyramid-jwt==1.4.1',
    'marshmallow==3.2.2',
    'fire==0.2.1',
    'sentry-sdk==0.14.2',

    # this is actually not required but some model is pickling incorrectly
    # 'dill==0.3.1.1',
    'numpy == 1.17.3',
]

test_requires = [
    'pytest==5.2.2',
    'pytest-cov==2.8.1',
    'pytest-mock==1.12.1',
    'WebTest==2.0.33',
    'freezegun==0.3.12',
]

dev_requires = [
    'pyramid-debugtoolbar==4.5',
    'pyramid-ipython==0.2',
    'pre-commit==1.20.0',
    'flake8==3.7.9',
    'fabric==2.5.0',
    'patchwork==1.0.1',
] + test_requires


setup(
    name='better_factory',
    version='0.1',
    description='Better factory',
    packages=find_packages(),
    include_package_data=True,
    install_requires=base_requires,
    message_extractors={
        'better_factory': [
            ('**.py', 'python', None),
        ],
    },
    extras_require={
        'dev': dev_requires,
    },
    entry_points={
        'paste.app_factory': [
            'main = better_factory.main:main'
        ],
        'console_scripts': [
            
        ],
    },
)
