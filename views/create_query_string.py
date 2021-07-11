from .parse_date_arguments import parse_dates_arguments
from werkzeug.exceptions import BadRequest

QUERY_BEGINNING = """SELECT EXTRACT('week' FROM datetime) as week_nr, count(*) trips_am FROM public."TRIPS" """
DATES_BASE_FILTER = "WHERE datetime between '{date_from}' AND '{date_to}'"
POLYGON_BASE_FILTER = """ AND st_contains(st_geomfromtext(
'polygon(({lon1} {lat1}, {lon1} {lat2}, {lon2} {lat2}, {lon2} {lat1}, {lon1} {lat1}))', 4326), 
origin_coord )"""
REGION_FILTER = " AND REGION = '{region}'"

GROUPING = " GROUP BY EXTRACT('week' FROM datetime)"

def create_query_string(args):
    ##Get dates for query
    date_from, date_to = parse_dates_arguments(args)

    ##build string
    dates_filter = DATES_BASE_FILTER.format(date_from=date_from, date_to=date_to)

    ##Search for bbox argument which should be passed as lon,lat,lon,lat
    if 'bbox' in args.keys():
        bbox = args["bbox"].split(",")
        bbox_filter = POLYGON_BASE_FILTER.format(lon1=bbox[0], lat1=bbox[1], lon2=bbox[2], lat2=bbox[3])
        return QUERY_BEGINNING + dates_filter + bbox_filter + GROUPING
    ##Otherwise look for region
    elif 'region' in args.keys():
        region_filter = REGION_FILTER.format(region=args["region"])
        return QUERY_BEGINNING + dates_filter + region_filter + GROUPING
    else:
        raise BadRequest("Either bbox or region must be passed")


