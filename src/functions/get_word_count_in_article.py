

def get_word_count_in_article(article_str, word_list):
    num_w_instances     =   0
    for w in word_list:
        # need to search with using neighboring characters
        # terms like 'eu' may show up in bigger words like 'bleu cheese' (bad example, but worth avoiding)

        # words are generally surrounded by spaces
        num_w_instances += article_str.count(' ' + w + ' ')
        article_str.replace(' ' + w + ' ', '')

        # or a space and a period
        num_w_instances += article_str.count(' ' + w + '.')
        article_str.replace(' ' + w + '.', '')

        # maybe period first?
        num_w_instances += article_str.count('.' + w + ' ')
        article_str.replace('.' + w + ' ', '')

        num_w_instances += article_str.count('.' + w + '.')
        article_str.replace('.' + w + '.', '')

    return num_w_instances