class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self. duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return (f'Название видео: {self.title}\n'
                f'Продолжительность видео: {self.duration}\n'
                f'Секунда остановки видео: {self.time_now}\n'
                f'Ограничение по возрасту: {self.adult_mode}\n')