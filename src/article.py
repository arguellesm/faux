import globals
import itertools

class Article:
    """
    Class which contains all the data from an article

    Attributes
    ----------
    id_iter : itertools
        Iterator used to obtain an unique id

    """

    id_iter = itertools.count()

    def __init__(self, headline='', author='', content='', topic='', source=''):
        """
        Constructor of Article

        Parameters
        ------
        headline : string, default=''
        author : string, default=''
        content : string, default=''
        topic : string, default=''
        source : string, default=''

        Raises
        ------
        ValueError
            Headline or author is not valid

        """
        self._id = next(Article.id_iter)
        self._content = content
        self._topic = topic
        self._source = source
        if(len(headline) < globals.HEADLINE_MAX_SIZE):
            self._headline = headline
        else:
            raise ValueError('Headline cannot be larger than ' + str(globals.HEADLINE_MAX_SIZE))
        
        if(globals.AUTHOR_MAX_LENGHT > len(author) >= globals.INVALID):
            self._author = author
        else:
            raise ValueError('Author cannot be larger than ' + str(globals.AUTHOR_MAX_LENGHT))

    @property
    def author(self):
        """
        Returns the author of the article
        """
        return self._author
    
    @property
    def content(self):
        """
        Returns the content of the article
        """
        return self._content

    @property
    def source(self):
        """
        Returns the source of the article
        """
        return self._source

    @property
    def topic(self):
        """
        Returns the topic of the article
        """
        return self._topic

    @property
    def headline(self):
        """
        Returns the headline of the article
        """
        return self._headline
    
    @property
    def id(self):
        """
        Returns the id of the article
        """
        return self._id