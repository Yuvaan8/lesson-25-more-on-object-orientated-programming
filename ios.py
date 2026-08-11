class IOS_string:
    def __init__(self):
        self.str = ''
    def get_string(self):
        self.str = input('Enter string:')
    def print_string(self):
        print('result is:', self.str.upper())
str1 = IOS_string()
str1.get_string()
str1.print_string()