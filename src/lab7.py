class clip:
    def __init__(self, Author = "Dzidzio", Song = "Pavyk", Duration = 183, Views = 40000000):
        self.clip_Author = Author
        self.clip_Song = Song
        self. clip_Duration = Duration
        self.clip_Views = Views

    def get_author(self):
        return self.clip_Author
    
    def get_song(self):
        return self.clip_Song
    
    def get_duration(self):
        return self.clip_Duration
    
    def get_views(self):
        return self.clip_Views
    
    def __repr__(self):
         return f"clip(Autor = {self.clip_Author}, Song = {self.clip_Song}, Duration = {self.clip_Duration}, Views = {self.clip_Views})"
    
    def __str__(self):
        return f"Autor:{self.clip_Author}, Song:{self.clip_Song},Dduration:{self.clip_Duration}, Views:{self.clip_Views} "
    
clip1 = clip("Travis Scott", "FE!N", "215sec", "55mil")
clip2 = clip( "Hanumankind ft. Kalmi","Big Dawgs", "234sec", "144mil")
clip3 = clip( "Arctic Monkeys", "505", "254sec", "527mil") 
print(repr(clip1))
print(clip2)
print(repr(clip2))
print(clip3)
print(repr(clip3))
            




