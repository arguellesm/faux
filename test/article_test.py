import pytest
from src.article import Article
from src.article import ArticleValueError, CantLoadContentModelError, ContentModelError    


# test article
article = Article(headline='A simple headline', content='And a very short content')


def test_can_create_object_only_headline():
    assert Article(headline='A simple headline')


def test_can_create_object_only_content():
    assert Article(content='And a very short content')


def test_cant_create_invalid_object_no_headline_nor_content():
    with pytest.raises(ArticleValueError):
        Article(author='Jane Doe', topic='health', source='NYT')


def test_cant_create_invalid_object_hempty_headline_no_content():
    with pytest.raises(ArticleValueError):
        Article(headline='')


def test_cant_create_invalid_object_hempty_content_no_headline():
    with pytest.raises(ArticleValueError):
        Article(content='')


def test_has_headline_or_content():
    assert article.headline or article.content


def test_predict_returns_three_values():
    assert len(article.predict()) == 3


def test_content_between_0_and_1():
    assert 0 <= article.rate_content() <= 1


def test_author_score_is_0():
    assert article.rate_author() == 0


def test_source_score_is_0():
    assert article.rate_source() == 0


def test_dummy_model_raises_cant_load_content_model_error_exception():
    with pytest.raises(CantLoadContentModelError):
        article.rate_content(debug=True)


def test_corrupted_article_raises_content_model_error_exception():
    article.content = 10
    with pytest.raises(ContentModelError):
        article.rate_content()