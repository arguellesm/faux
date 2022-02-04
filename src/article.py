from src import globals, blacklists
import itertools
import pickle
import os.path



class ArticleValueError(ValueError):
    """
    Article creation value error.
    """
    pass

class ArticleDependencyError(ModuleNotFoundError):
    """
    Missing dependencies error.
    """
    pass

class CantLoadContentModelError(FileNotFoundError):
    """
    Content model loading errors.
    """
    pass

class ContentModelError(Exception):
    """
    Content model parameter errors.
    """
    pass



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
            raise ArticleValueError('An article must include a headline or content')

        if(len(headline) < globals.HEADLINE_MAX_SIZE):
            self._headline = headline
        else:
            raise ArticleValueError('Headline cannot be larger than {}'.format(globals.HEADLINE_MAX_SIZE))
        
        if(globals.AUTHOR_MAX_LENGHT > len(author)):
            self._author = author
        else:
            raise ArticleValueError('Author cannot be larger than {}'.format(globals.AUTHOR_MAX_LENGHT))

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
        Returns the author, source and content score indicating
        how misleading the article is.
        """

        author_score = self.rate_author()
        source_score = self.rate_source()
        content_score = self.rate_content()

        return author_score, source_score, content_score


    def rate_author(self):
        """
        Checks whether the author is listed as untrustworthy.
        """

        if self.author and self.author in blacklists.UNTRUSTED_AUTHORS:
            author_score = blacklists.UNTRUSTED_AUTHORS[self.author]
        else:
            author_score = 0

        return author_score


    def rate_source(self):
        """
        Checks whether the source is listed as untrustworthy.
        """
        
        if self.source and self.source in blacklists.UNTRUSTED_SOURCES:
            source_score = blacklists.UNTRUSTED_SOURCES[self.source]
        else:
            source_score = 0

        return source_score


    def rate_content(self, debug=False):
        """
        Evaluates the likeliness of the content being fake.

        Parameters
        ----------
        debug : bool, default=False
            Will load a missing model for test purposes.

        Raises
        ------
        ArticleDependencyError
            Missing model dependencies.
        CantLoadContentModelError
            Couldn't load model.
        ContentModelError
            Model parameter error.
        """
        
        if debug:
            filename = os.path.dirname(__file__)+globals.DUMMY_MODEL_PATH
        else:
            filename = os.path.dirname(__file__)+globals.MODEL_PATH
        
        try:
            with open(filename, 'rb') as f:
                model = pickle.load(f)
        except FileNotFoundError as e:
            raise(CantLoadContentModelError('Unable to load {}: {}'.format(filename, e)))
        except ModuleNotFoundError as e:
            raise(ArticleDependencyError('Missing module: {}'.format(e)))

        try:
            content_score = model.predict_proba([self.content])[0][0]
        except Exception as e:
            raise(ContentModelError('Wrong parameter: {}'.format(e)))

        return content_score