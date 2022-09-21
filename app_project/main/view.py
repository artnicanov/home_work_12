from flask import Blueprint, render_template, request
from app_project.functions import get_posts_by_word

# создаем блюпринт
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

# вьюшка для главной страницы
@main_blueprint.route('/')
def main_page():
	return render_template('index.html')

# вьюшка для поиска
@main_blueprint.route('/search/')
def search_page():
	search_query = request.args.get('s') # получаем значение из адресной строки через args
	try:
		posts = get_posts_by_word(search_query) # передаем функции, которая ищет слова значени полученное выше
	except FileNotFoundError:
		return "Файл не найден"

	return render_template("post_list.html", query=search_query, posts=posts) # передаем в шаблон результаты поиска
