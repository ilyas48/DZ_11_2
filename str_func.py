def str_in(n):
    '''

    :param n: функция принимает слово
    :return: функция возвращает слово со всеми заглавными буквами
    '''
    n_upper = n.upper()
    return n_upper


def up_first_letter(s):
    '''

    :param s: функция принимает слово
    :return: функция возвращает слово с первой заглавной буквой
    '''
    return s[0].upper() + s[1:]
