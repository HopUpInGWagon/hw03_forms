import datetime

annum = int(datetime.datetime.today().year)


def year(request):
    """Добавляет переменную с текущим годом."""
    return {
        'year': annum
    }
