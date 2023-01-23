from django.shortcuts import render
import datetime
from datetime import date
from datetime import datetime, timedelta
from datetime import time
from .models import *
from datetime import datetime
from calendar import monthrange

def take_days():
    current_year = datetime.now().year
    month = 1
    days = monthrange(current_year, month)[1]
    return days


def report_view_today(request):

    # if request.GET.get('period'):
    #     period = request.GET.get('period')
    # else:
    #     period = '1'
    # if period == '1':
    #     start = datetime.combine(date.today() - timedelta(days=1), time(17, 30, 00)) # Вчера вечер
    #     finish = datetime.combine(date.today(), time(8, 30, 00)) # сегодня утро
    #     period_str = '17:30 - 8:30'
    # elif period == '2':
    #     start = datetime.combine(date.today(), time(8, 30, 00)) # Сегодня утро
    #     finish = datetime.combine(date.today(), time(17, 30, 00)) # Сегодня вечер
    #     period_str = '8:30 - 17:30'

    # drivers = Driver.objects.all()
    data_dr = {}
    days = []
    for i in range(1, take_days()+1):
        days.append(str(i) if i > 9 else "0" + str(i))

    data_dr["columns"] = ["Аналитика"] + days



    #
    # for driver in drivers:
    #     orders = driver.get_open_orders_detalis(start, finish)
    #     if not orders:
    #         continue
    #     data = []
    #
    #     for inx, row in enumerate(orders):
    #         # if order.date_dev != datetime.date.today():
    #         #     continue
    #         f = {'num': inx + 1,
    #              'date_dev': row.order.date_dev,
    #              'district': row.order.client.district,
    #              'address': row.order.client,
    #              'phone_number': row.order.client.phone_number,
    #              'position': row.position,
    #              'quantity': row.quantity,
    #              'amount': row.amount,
    #              'comment': row.order.comment if row.order.comment != None else '' ,
    #              'period_str': period_str ,
    #              }
    #         data.append(f)
    #     key = driver.name
    #     data_dr[key] = data
    #
    # # Теперь для незаполненных водителей
    # orders = TabluarOrders.objects.filter(order__client__driver=None,  order__date__gte=start, order__date__lte=finish).order_by('order__client__district')
    # # orders = TabluarOrders.objects.filter(order__client__driver=None).order_by('order__client__district')
    # if not orders:
    #     return render(request,'report_today.html',{'data' : data_dr})
    # for inx, row in enumerate(orders):
    #     # if order.date_dev != datetime.date.today():
    #     #     continue
    #     f = {'num': inx + 1,
    #          'date_dev': row.order.date_dev,
    #          'district': row.order.client.district,
    #          'address': row.order.client,
    #          'phone_number': row.order.client.phone_number,
    #          'position': row.position,
    #          'quantity': row.quantity,
    #          'amount': row.amount,
    #          'comment': row.order.comment if row.order.comment != None else '',
    #          'period_str': period_str,
    #          }
    #     data.append(f)
    # # key = driver.name +' '+ datetime.date.today().strftime('%d.%m')
    # key = "Не установлен"
    # data_dr[key] = data
    return render(request,'report_today.html',{'data' : data_dr})
