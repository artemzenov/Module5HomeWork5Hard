from ..user.user import User
from time import sleep


class UrTube:

    def __init__(self):
        self.users = list()
        self.videos = list()
        self.current_user = None

    def __str__(self):
        return (f'Список пользователей: {self.users}\n'
                f'Список видео: {self.videos}\n'
                f'Текущий пользователь: {self.current_user}\n')

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, word_search):
        result_search = list()
        for video in self.videos:
            if word_search.lower() in video.title.lower():
                result_search.append(video.title)
        return result_search

    def watch_video(self, title_film):
        if self.current_user:
            for video in self.videos:
                if title_film == video.title:
                    if self.current_user.age >= 18:
                        for num_sec in range(video.time_now, video.duration + 1):
                            print(num_sec, end=' ')
                            sleep(1)
                        else:
                            video.time_now = 0
                            print(f'Конец видео')
                    else:
                        print(f'Вам нет 18 лет, пожалуйста покиньте страницу')
                    break
            # else:
            #     print(f'Видео "{title_film}" не найдено')
        else:
            print(f'Войдите в аккаунт, чтобы смотреть видео')

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {user.nickname} уже существует')
                break
        else:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.log_out()
                self.current_user = user
                break

    def log_out(self):
        self.current_user = None