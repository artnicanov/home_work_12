from flask import Blueprint, render_template, request
from app_project.functions import get_posts_by_word

# создаем блюпринт, передаем ему имя и папку с шаблонами, чтобы потом можно было их брать для вьюшек
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

# вьюшка для главной страницы
@main_blueprint.route('/')
def main_page():
	return render_template('index.html') # просто возвращаем готовый шаблон

# вьюшка для поиска
@main_blueprint.route('/search/')
def search_page():
	search_query = request.args.get('s') # получаем значение из адресной строки через args
	try:
		posts = get_posts_by_word(search_query) # передаем функции, которая ищет слова, значение полученное строкой выше
	except FileNotFoundError:
		return "Файл не найден"

	# передаем в шаблон название и результаты поиска как переменные
	return render_template("post_list.html", query=search_query, posts=posts)
