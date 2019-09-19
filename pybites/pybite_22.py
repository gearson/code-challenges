#%%
from functools import wraps

#%%

def make_html(argument):
    def decorator(function):
        def wrapper():
            return f'<{argument}>{function()}</{argument}>'
        return wrapper
    return decorator

#%%
@make_html('strong')
@make_html('p')
def get_text(text='I code with PyBites'):
    return text

get_text()

#%%
