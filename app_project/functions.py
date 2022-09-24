import json

def load_post():
	"""загружаем посты из файла"""
	with open('posts.json', encoding='utf-8') as file:
		return json.load(file)

def get_posts_by_word(word):
	"""находим пост по слову в строке поиска"""
	result= []
	for post in load_post():
		if word.lower() in post['content'].lower():
			result.append(post)
	return result

def save_picture(picture):
	"""сохраняем картинку"""
	filename = picture.filename
	path = f'./uploads/images/{filename}' # по этому пути сохраняем и показываем картинку
	picture.save(path)
	return path

def add_post(post):
	"""добавляет пост в файлик и возвращает его для показа на странице"""
	posts = load_post()  # здесь у нас список словарей
	posts.append(post)  # добавляем в него наш пост
	save_posts_to_json(posts) # вызываем функцию, которая запишет файл с новым постом
	return post # функция должна обязательно возвращать пердаваемый ее пост для отображения на странице шаблона "пост добавлен"

def save_posts_to_json(posts, path='posts.json'):
	"""сохраняем пост"""
	with open(path, "w", encoding='utf-8') as file: # открываем файл на запись и записываем  его уже с новым постом
# ensure_ascii=False для того чтобы распозналась киррилица, indent=4 это отступ, для того чтобы файл оставался в читабельном виде
		json.dump(posts, file, ensure_ascii=False, indent=4)
