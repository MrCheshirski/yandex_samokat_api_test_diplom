import sender_stand_request
def get_track_number():
    order_track_number = sender_stand_request.post_new_order()
    return order_track_number.json()["track"]


def test_get_order_track_number():
    order_track_number = get_track_number()
    response = sender_stand_request.get_order_track(order_track_number)
    assert response.status_code == 200