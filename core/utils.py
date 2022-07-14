# core/utils

#routines to for compact date display in admin records.

def compact_dow_datetime(self, obj):
    return obj.datetime.strftime("%a %m/%d/%y %I:%M %p")


def compact_datetime(self, obj):
    return obj.datetime.strftime("%m/%d/%y %I:%M %p")


def compact_dow_date(self, obj):
    return obj.datetime.strftime("%a %m/%d/%y %I:%M %p")


def compact_date(self, obj):
    return obj.datetime.strftime("%m/%d/%y")
