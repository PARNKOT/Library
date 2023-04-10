# DECORATOR
# Print all function arguments
def DEBUG_args(function):
    def wrapper(*args, **kwargs):
        print('-'*15, 'DEBUG information', '-'*16)
        print(f'function has {len(args)} arguments:\n', *args)
        print(f'function has {len(kwargs)} key arguments:')
        for key, value in kwargs.items():
            print(f'{key}: {value}')
        print('-' * 50)

        function(*args, **kwargs)
    return wrapper
