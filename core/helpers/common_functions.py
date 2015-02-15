__author__ = 'domagoj'


class CommonFunctions:

    @staticmethod
    def trunc(num, digits):
        sp = str(num).split('.')
        # return "" '.'.join(sp[0], sp[:digits])
        return str(sp[0]) + "." + str(sp[1][:digits])