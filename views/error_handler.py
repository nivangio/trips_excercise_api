import traceback
from functools import wraps
from werkzeug.exceptions import BadRequest

def error_handler(f):
    @wraps(f)
    def applicator(*args, **kwargs):
        try:
            return f(*args,**kwargs)
        except BadRequest as e:
            return {"reason": e.description}, e.code

        except Exception as e:
            traceback.print_exc()
            return {"reason": e.args[0]}, 500
    return applicator
