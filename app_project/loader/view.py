from flask import Blueprint, render_template, request
from app_project.functions import save_picture, save_posts_to_json, add_post

# создаем блюпринт, передаем ему имя и папку с шаблонами, чтобы потом можно было их брать для вьюшек
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

# вьюшка для показа формы загрузки, обрабатывается метод GET
@loader_blueprint.route('/post')
def post_form():
	return render_template('post_form.html')

# вьюшка для самой загрузки картинки и поста, обрабатывается метод POST
@loader_blueprint.route('/post', methods=['POST'])
def add_post_page():
	picture = request.files.get('picture') # атрибут name у картинки
	content = request.form.get('content') # атрибут name у формы

	if not picture or not content:
		return "не картинка или текст"
	if picture.filename.split('.')[-1] not in ['jpg', 'png']: # делим название файла по точке и берем вторую часть через[-1]
		return 'неверное расширение файла'
	try:
		picture_path = '/' + save_picture(picture) # по этому пути сохраняем и показываем картинку
	except FileNotFoundError:
		return "Файл не найден"
	post = add_post({'pic': picture_path, "content": content})

	# передаем в шаблон название и добавленный пост как переменную
	return render_template('post_uploaded.html', post=post)
