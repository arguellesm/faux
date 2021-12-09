from src import globals, blacklists
import itertools
import pickle
import os.path


class Article:
    """
    Class which contains all the data from an article.

    Parameters
    ----------
    headline : str, default=''
        Article's headline.
    author : str, default=''
        Person who wrote the article.
    content : str, default=''
        Content of the article.
    topic : str, default=''
        Subject of the article.
    source : str, default=''
        Where the article comes from.
    """

    id_iter = itertools.count()

    def __init__(self, headline='', author='', content='', topic='', source=''):
        """
        Constructor of Article

        Raises
        ------
        ValueError
            Headline or author is not valid.

        """
        if not headline and not content:
            raise ValueError('An article must include a headline or content')

        if(len(headline) < globals.HEADLINE_MAX_SIZE):
            self._headline = headline
        else:
            raise ValueError('Headline cannot be larger than ' + str(globals.HEADLINE_MAX_SIZE))
        
        if(globals.AUTHOR_MAX_LENGHT > len(author)):
            self._author = author
        else:
            raise ValueError('Author cannot be larger than ' + str(globals.AUTHOR_MAX_LENGHT))

        self._id = next(Article.id_iter)
        self._content = content
        self._topic = topic
        self._source = source

    @property
    def author(self):
        """
        Returns the author of the article.
        """
        return self._author
    
    @property
    def content(self):
        """
        Returns the content of the article.
        """
        return self._content

    @property
    def source(self):
        """
        Returns the source of the article.
        """
        return self._source

    @property
    def topic(self):
        """
        Returns the topic of the article.
        """
        return self._topic

    @property
    def headline(self):
        """
        Returns the headline of the article.
        """
        return self._headline
    
    @property
    def id(self):
        """
        Returns the id of the article.
        """
        return self._id

    def predict(self):
        """
        Returns how misleading the article is.
        """

        author_score = 0
        source_score = 0

        # check author
        if self.author and self.author in blacklists.UNTRUSTED_AUTHORS:
            author_score = 1

        # check source
        if self.source and self.source in backlists.UNTRUSTED_SOURCES:
            source_score = 1

        # check content
        with open(os.path.dirname(__file__)+globals.MODEL_PATH, 'rb') as f:
            file = f
        
        model = pickle.load(file) 
        content_score = model.predict_proba([self.content])[0][0]

        return author_score, source_score, content_score
