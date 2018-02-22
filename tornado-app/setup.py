from setuptools import setup, find_packages

requires = [
    'tornado',
    'tornado-sqlalchemy',
    'psycopg2'
]

setup(
    name='tornado-app',
    version='0.0',
    description='A To-Do List built with Tornado',
    author='Kayra',
    author_email='Kayra@test.com',
    keywords='web tornado',
    packages=find_packages(),
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'serve_app = todo:main',
            'init_db = todo.scripts.initialise_db:main',
        ]
    }
)
