def round_value(value, places):
    places = 10**places
    return round(value * places) / places