from re import search as regexsearch, sub
from datetime import timedelta, datetime
from werkzeug.exceptions import BadRequest

'''
This function parses date_from and date_to from the request. It supports both absoulte and relative
date starts
'''
def parse_dates_arguments(args):
    try:
        date_from = args["date_from"]
    except:
        raise BadRequest("date_from not passed")
    date_to = args.get("date_to", "2500-01-01")

    ##If date_from_does not match a date, assume last n period
    if regexsearch(r'^[0-9]{4}\-[0-9]{2}\-[0-9]{2}( [0-9]{2}\:[0-9]{2}:[0-9]{2})?$', date_from) is None:
        try:
            diff_obj = float(sub("[A-Za-z]","",date_from))
            diff_unit = sub("[0-9\.]","",date_from)
            timediff_obj = timedelta(**{diff_unit:diff_obj})
            date_from = datetime.strftime((datetime.utcnow() - timediff_obj), "%Y-%m-%d %H:%M:%S")
        except:
            raise BadRequest("Wrong date_from argument")

    return date_from, date_to