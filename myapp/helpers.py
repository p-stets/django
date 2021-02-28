from mysite.settings import OPERATOR_CODES


def codes_regexp(codes_list=OPERATOR_CODES, additional_digits_count=7):
    '''
    Takes a list of mobile codes as "codes_list" argument
    Takes number of numbers that can go after code as "additional_digits_count"
    Returns regex to catch cell number.
    '''
    for el in list(enumerate(codes_list[:-1])):
        codes_list[el[0]] = el[1] + '|'
    regex_list = ''.join(x for x in codes_list)
    phone_regex = f'^0({regex_list})\\d{{{additional_digits_count}}}/$'
    return phone_regex
