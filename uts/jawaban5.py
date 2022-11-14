class Time():
    def __init__(self):
        self._hours = 0
        self._minutes = 0
        self._seconds = 0

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, v):
        if v >= 0 and v <= 24:
            self._hours = v
    
    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, v):
        if v >= 0 and v <= 60:
            self._minutes = v
    
    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, v):
        if v >= 0 and v <= 60:
            self._seconds = v

t = Time()
t.hours = int(input('Masukkan jam: '))
t.minutes = int(input('Masukkan menit: '))
t.seconds = int(input('Masukkan detik: '))
print(t.hours, ':', t.minutes, ':', t.seconds)