# encoding=utf-8
# 装饰器...面向切面。


def log1(func):
    def wrapper(*arg, **kw):
        print 'call %s : ' % func.__name__
        func(*arg, **kw)
    return wrapper


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print '2016-08-30'


now()
