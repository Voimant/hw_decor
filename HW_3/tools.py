import time


def logger(old_function):
    def new_function(*args, **kwargs):
        do_func = old_function(*args, **kwargs)
        with open('main.log', 'a', encoding='utf-8') as file_obj:
            result_time = time.ctime()
            file_obj.write(result_time)
            file_obj.write(f'Вызвана функция {old_function} аргументы *args={args}, **kwargs={kwargs}\n\n')
            file_obj.write(f'Результат функции: {do_func}\n\n')

        return do_func

    return new_function


def logger2(path):
    def _logger2(old_function):
        def new_function(*args, **kwargs):
            do_func = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as file_obj:
                result_time = time.ctime()
                file_obj.write(result_time)
                file_obj.write(f'Вызвана функция {old_function} аргументы *args={args}, **kwargs={kwargs}\n\n')
                file_obj.write(f'Результат функции: {do_func}\n\n')

            return do_func

        return new_function

    return _logger2


