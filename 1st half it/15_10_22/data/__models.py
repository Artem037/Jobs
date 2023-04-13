from datetime import datetime
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm

SqlBase = declarative_base()


class Link(SqlBase):
    __tablename__ = 'links'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    link = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    comment = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    top = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    created_date = sqlalchemy.Column(sqlalchemy.Date,
                                     default=datetime.now().date)
    categories = orm.relation("Category", secondary="categories_to_links",
                              backref="links")


class Category(SqlBase):
    __tablename__ = 'categories'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)


association_links = sqlalchemy.Table(
    'categories_to_links', SqlBase.metadata,
    sqlalchemy.Column('link_id', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('links.id')),
    sqlalchemy.Column('category_id', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('categories.id'))
)
