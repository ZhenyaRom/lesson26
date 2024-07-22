import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __lt__(self, other):
        return self.age < other

    def __repr__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        for i in self.users:
            if i.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        user = User(nickname, password, age)
        self.users.append(user)
        self.current_user = user

    def log_in(self, nickname, password):
        for i in self.users:
            if i.nickname == nickname and hash(i.password) == hash(password):
                self.current_user = i

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, search):
        rezult_search = []
        for i in self.videos:
            j = i.title.lower()
            if j.find(search.lower()) != (-1):
                rezult_search.append(i.title)
        return rezult_search

    def watch_video(self, video_name):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for i in self.videos:
            if i.title == video_name:
                if i.adult_mode == True and self.current_user < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                while i.time_now < i.duration:
                    i.time_now += 1
                    print(i.time_now, end=' ')
                    time.sleep(1)
                print('Конец видео')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
