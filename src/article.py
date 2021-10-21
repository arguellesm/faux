import globals

class Article:
    def __init__(self, headline='', content='', author='', topic='', source=''):
        self.date = date
        if(len(headline) < globals.HEADLINE_MAX_SIZE and headline):
            self.headline = headline
            self.ID = self.headline[0:3] + "-" + self.date.strftime("%-d%-m%-y%-H%-M%-S")
        else:
            if(not headline):
                raise ValueError('Headline cannot be empty')
            else:
                raise ValueError('Headline cannot be larger than ' + str(globals.HEADLINE_MAX_SIZE))
        
        if(author and globals.AUTHOR_MAX_LENGHT > len(author) > 0):
            self.author = author
        else:
            if(not author):
                raise ValueError('Author cannot be None')
            else:
                raise ValueError('Author cannot be larger than ' + str(globals.AUTHOR_MAX_LENGHT))

        if(content and len(content) > 0):
            self.content = content
        else:
            raise ValueError('Content cannot be None')
        if(topic and len(topic) > 0):
            self.topic = topic
        else:
            raise ValueError('Topic cannot be None')
        if(origin and len(origin) > 0):
            self.origin = origin
        else:
            raise ValueError('Origin cannot be None')

    # getter functions
    def author(self):
        return self.author
    
    def content(self):
        return self.content

    def origin(self):
        return self.origin

    def topic(self):
        return self.topic

    def headline(self):
        return self.headline
    
    def ID(self):
        return self.ID