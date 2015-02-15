import datetime

class Validate():

    @staticmethod
    def is_int(string):
        try:
            int(string)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_decimal(string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_date(string, date_format=None):
        if date_format:
            try:
                datetime.datetime.strptime(string, date_format)
                return True
            except ValueError:
                return False
        try:
            datetime.datetime.strptime(string, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    @staticmethod
    def is_time(string):
        try:
            datetime.datetime.strptime(string, '%H:%M:%S')
            return True
        except ValueError:
            try:
                datetime.datetime.strptime(string, '%H:%M')
                return True
            except ValueError:
                return False

    @staticmethod
    def is_datetime(string, date_format=None):
        if date_format:
            try:
                datetime.datetime.strptime(string, date_format)
                return True
            except ValueError:
                return False
        else:
            try:
                datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
                return True
            except ValueError:
                try:
                    datetime.datetime.strptime(string, "%Y-%m-%d %H")
                    return True
                except ValueError:
                    try:
                        datetime.datetime.strptime(string, "%Y-%m-%d %H:%M")
                        return True
                    except ValueError:
                        return False