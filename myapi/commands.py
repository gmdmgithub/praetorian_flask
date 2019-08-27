import click
from flask.cli import with_appcontext

from .models import User
from .extensions import guard, db

@click.command(name="create_db")
@with_appcontext
def create_db():
    db.create_all()

@click.command(name='create_users')
@with_appcontext
def create_users():
    db.create_all()
    db.session.add(User(
        username='Alex',
        password=guard.hash_password('alex123'),
    ))
    db.session.add(User(
        username='Walter',
        password=guard.hash_password('walter123'),
        roles='admin'
    ))
    db.session.add(User(
        username='Adam',
        password=guard.hash_password('adam123'),
        roles='operator'
    ))
    db.session.add(User(
        username='John',
        password=guard.hash_password('john123'),
        roles='operator,admin'
    ))
    db.session.commit()

