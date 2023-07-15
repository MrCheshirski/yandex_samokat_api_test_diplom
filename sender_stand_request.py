import configuration
import requests
import data


def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=data.order_body)  # тут тело



def get_order_track(order_track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + "?t=" + str(order_track_number)) # передача параметра t в запросе
