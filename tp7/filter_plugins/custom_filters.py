class FilterModule(object):
    def filters(self):
        return {
            'reverse_string': self.reverse_string
        }

    def reverse_string(self, value):
        return value[::-1]

