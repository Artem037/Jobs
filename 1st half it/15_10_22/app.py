from flask import Flask, render_template, url_for, request, redirect, abort
from forms.link_forms import LinkForm, LinkFormSearch
import sqlalchemy
from sqlalchemy import and_, desc, asc
from data.__models import Link, SqlBase, association_links, Category
from sqlalchemy.orm import sessionmaker
# from flask_migrate import Higrate
import urllib.parse
from flask_paginate import Pagination, get_page_parameter
from flask import session as sess_client
import datetime
import alembic

app = Flask(__name__)
app.config['SECRET_KEY'] = 'protect_my_kvantorium'
app.config['SQALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres@localhost:5439/my_app"
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)

engine = sqlalchemy.create_engine(app.config['SQALCHEMY_DATABASE_URI'], echo=False)

# создание таблиц
SqlBase.metadata.create_all(engine)
# Привязка метаданных класса sqlbase к engine
SqlBase.metadata.bind = engine

Session = sessionmaker(bind=engine)
session = Session()


# migrate = Higrate(app, engine)


@app.route('/set_sort')
def set_sort():
    sess_client['sort_order'] = request.args.get('order', 'desc')
    print(request.environ)
    path = request.environ.get('HTTP_REFERER')
    if path:
        return redirect(path)
    else:
        return redirect('/')


@app.route("/", methods=['GET', 'POST'])
def links():
    report_msg = None
    search_form = LinkFormSearch()

    cat_arr = session.query(Category).all()
    cat_selected = []

    links = []

    pagination = None

    if request.method == 'GET':
        # print(links)

        page = request.args.get(get_page_parameter(), type=int, default=1)

        limit = 2
        total = session.query(Link).count()

        offset = (page - 1) * limit

        order = sess_client.get('sort_order', 'desc')

        if order == 'asc':
            links = session.query(Link).order_by(asc(Link.id)).offset(offset).limit(limit).all()
        elif order:
            links = session.query(Link).order_by(desc(Link.id)).offset(offset).limit(limit).all()

        pagination = Pagination(page=page, per_page=limit, total=total,
                                record_name='links',
                                css_framework='foundation')

    # links = session.query(Link).all()
    elif request.method == 'POST':
        search_values = [(key, val) for key, val in search_form.data.items() if
                         key in ['link', 'title', 'comment', 'category'] and val.strip()]

        cat_id_selected = request.form.getlist('category')

        if cat_id_selected:
            cat_selected = session.query(Category).filter(Category.name.in_(cat_id_selected)).all()
            print(1)
            links = session.query(Link).join(Link.categories).filter(Category.name.in_(cat_id_selected)).all()
        if search_values:
            print(2)
            links = session.query(Link).join(Link.categories).filter(
                and_(*(getattr(Link, field).like(f'%{value}%') for field, value in search_values))).all()
            print(links)
        if not search_values:
            report_msg = 'Не заданы условия поиска'
    return render_template('links.html', links=links, search_form=search_form, report_msg=report_msg,
                           pagination=pagination,
                           categories=cat_arr, cat_selected=cat_selected, order=order)


@app.route('/link_add', methods=['POST', 'GET'])
@app.route('/link_edit/<int:link_id>', methods=['POST', 'GET'])
def links_manage(link_id=None):
    link_form = LinkForm()
    cat_selected = []
    cat_arr = session.query(Category).all()

    if request.method == 'GET' and link_id:
        link = session.query(Link).filter(Link.id == link_id).first()
        if link:
            link_form.link.data = link.link
            link_form.title.data = link.title
            link_form.comment.data = link.comment
            cat_selected = link.categories
            print(cat_selected)
        else:
            abort(404)

    if request.method == 'POST':
        cat_id_selected = request.form.getlist('category')
        if link_form.validate_on_submit():
            if link_id:
                # изменение данных ссылки в БД
                link = session.query(Link).filter(Link.id == link_id).first()
                if link:
                    link.link = urllib.parse.unquote(link_form.link.data)
                    link.title = link_form.title.data
                    link.comment = link_form.comment.data
                    link.categories.clear()
                else:
                    abort(404)
            else:
                # Добавление данных ссылки к бд
                link = Link(
                    link=urllib.parse.unquote(link_form.link.data),
                    title=link_form.title.data,
                    comment=link_form.comment.data)
                session.add(link)
            if cat_id_selected:
                cat_selected = session.query(Category).filter(Category.id.in_(cat_id_selected))
                link.categories.extend(cat_selected)
            session.commit()
            return redirect('/')
    return render_template('link_add.html', categories=cat_arr, link_id=link_id, cat_selected=cat_selected,
                           link_form=link_form)


@app.route('/link_delete/<int:link_id>')
def link_delete(link_id):
    link = session.query(Link).filter(Link.id == link_id).first()
    if link:
        session.delete(link)
        session.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/get_title', methods=['POST', 'GET'])
def get_title():
    # для метода гет
    link = request.args.get('link')
    btn_text = request.args.get('btn_id')

    # для метода пост
    # request.form.get('link')
    # content_type = request.headers.get('Content-Type')
    return 'Заголовок страницы'
    # return '', 204 если ничего не надо отправлять


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
