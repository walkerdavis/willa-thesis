import textract

from functions.remove_all_quote_types                       import remove_all_quote_types

def get_article_str(article_fp):

    return remove_all_quote_types(str(textract.process(article_fp)).lower())