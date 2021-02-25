from mysite.settings import OPERATOR_CODES


class Cell(object):

    @staticmethod
    def codes_regexp(codes_list=OPERATOR_CODES, additional_digits_count=7):
        for el in list(enumerate(codes_list[:-1])):
            codes_list[el[0]] = el[1] + '|'
        regex_list = ''.join(x for x in codes_list)
        return f'^0({regex_list})\\d{{{additional_digits_count}}}/$'
