class Post:

    def __init__(self,
                 pk=0,
                 poster_avatar='',
                 pic='',
                 content='',
                 views_count=0,
                 likes_count=0,
                 poster_name=''
                 ):

        self.pk = pk
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content
        self.views_count = views_count
        self.likes_count = likes_count
        self.poster_name = poster_name

    def __repr__(self):
        return f"post " \
               f"{self.pk}" \
               f"{self.poster_avatar}" \
               f"{self.pic}" \
               f"{self.content}" \
               f"{self.views_count}" \
               f"{self.likes_count}" \
               f"{self.poster_name}" \
               f")"


    def as_dict(self):
        dict_data = {
            'pk':self.pk,
            'poster_avatar':self.poster_avatar,
            'pic':self.pic,
            'content':self.content,
            'views_count':self.views_count,
            'likes_count':self.likes_count,
            'poster_name':self.poster_name
        }
        return dict_data