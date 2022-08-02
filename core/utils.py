# core/utils

# routines to for compact date display in admin records.


def compact_datetime(fld, with_dow=True):
    try:
        if with_dow is True:
            return fld.astimezone().strftime("%m/%d/%y %I:%M %p")
        else:
            return fld.astimezone().strftime("%m/%d/%y %I:%M %p (%a)")
    except Exception as e:
        return "???"


def compact_date(fld,with_dow=True):
    try:
        if with_dow is True:
            return fld.strftime("%m/%d/%y (%a)")
        else:
            return fld.strftime("%m/%d/%y (%a)")
    except Exception as e:
        return "???"

