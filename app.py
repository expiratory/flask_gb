from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'header': 'Добро пожаловать на домашнюю страницу нашего интернет магазина!',
        'text': 'Здесь вы можете очень удачно совершить покупки по ужасно выгодным ценам с большими скидками!'
    }
    return render_template('index.html', **context)


@app.route('/clothes/')
def clothes():
    context = {
        'title': 'Одежда',
        'items': [
            {
                'title': 'Модная мужская парка',
                'description': 'Очень теплая и удобная, а главное легкая, черного цвета, 20 века',
                'image': url_for('.static', filename='clothes.png')
            },
            {
                'title': 'Красивая женская курточка',
                'description': 'Она настолько красивая, что все будут от вас просто без ума',
                'image': url_for('.static', filename='clothes2.jpg')
            }
        ]
    }
    return render_template('categories.html', **context)


@app.route('/shoes/')
def shoes():
    context = {
        'title': 'Обувь',
        'items': [
            {
                'title': 'Тяги Бархатные',
                'description': 'Ну ты сам посмотри, что за тяги такие бархатные! Надо брать!',
                'image': url_for('.static', filename='shoes.jpg')
            },
            {
                'title': 'Красные макасины',
                'description': 'Классика 2010-2012 годов. А классика никогда не стареет.',
                'image': url_for('.static', filename='shoes2.jpg')
            }
        ]
    }
    return render_template('categories.html', **context)


@app.route('/bags/')
def bags():
    context = {
        'title': 'Сумки и рюкзаки',
        'items': [
            {
                'title': 'Сумка-бананка',
                'description': 'Сделает тебя либо модным, либо кондуктором, как повезет',
                'image': url_for('.static', filename='bag.jpg')
            },
            {
                'title': 'Рюкзак Доры',
                'description': 'Карта в сделку не входила',
                'image': url_for('.static', filename='bag2.jpg')
            }
        ]
    }
    return render_template('categories.html', **context)
