from functions.remove_all_quote_types                       import remove_all_quote_types

def convert_raw_txt_to_list(filepath):

    words   =   None

    with open(filepath) as f:
        words = f.readlines()

    words = [w.strip('\n') for w in words]
    words = [w.lower() for w in words]

    for i, w in enumerate(words):
        if words[i][-1] ==  ' ':
            words[i]    =   words[i][:-1]

        words[i]        =   remove_all_quote_types(words[i])

    words.sort()

    grouped_list    =   []
    inds_to_ignore  =   []

    for i, w in enumerate(words):

        if i < len(words) - 1:
            if i not in inds_to_ignore:
                cur_word    =   words[i]
                next_word   =   words[i + 1]
                # group single and plural duplicates 
                if (next_word[-1] == 's') & (cur_word == next_word[:-1]):
                    grouped_list.append([cur_word, next_word])
                    inds_to_ignore.append(i + 1)
                # group single and plural duplicates 
                elif cur_word   ==  next_word:
                    inds_to_ignore.append(i + 1)
                # group cases with and without hyphens
                elif (cur_word == next_word.replace('-', ' ')) or (cur_word == next_word.replace(' ', '-')):
                    grouped_list.append([cur_word, next_word])
                    inds_to_ignore.append(i + 1)
                # check words with periods to see if there are instances without them
                elif ('.' in cur_word):
                    grouped_list.append([cur_word, cur_word.replace('.', '')])
                else:
                    grouped_list.append([cur_word])

    return grouped_list