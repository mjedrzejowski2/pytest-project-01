import pytest
import source.service as service
import unittest.mock as mock
import requests

#Wpisujemy sciezke do funkcji ktora ma byc mockowana
@mock.patch("source.service.get_user_from_db")
#Random name => moze być dowolna nazwa
def test_get_user_from_db(random_name):
    #Jezeli w tej funkcji wywołamy funckje random_name, zawsze bedzie miala wartosc return_value
    random_name.return_value = "Mocked Alice"
    #Wywołujemy prawdziwa funkcje, ale tak naprawde to jest mockowana
    user_name = service.get_user_from_db(1)

    assert user_name == "Mocked Alice"



@mock.patch("requests.get")
def test_get_users(mock_get):
    #Tworzymy imitacje odpowiedzi od API
    mock_response = mock.Mock()
    #.status_code is property, musimy ustawić atrybuty by dobrze odwzorywał odpowiedź API
    mock_response.status_code = 200
    #.json is function dlatego dajemu mu return_value, tak samo tutaj
    mock_response.json.return_value = {"id": 1, "name":"John Doe"}

    #Dopiero po zdefiniowaniu możemy zdefiniowac do argumentu mock_get
    mock_get.return_value = mock_response
    data = service.get_users()
    assert data == {"id":1, "name": "John Doe"}


# Parametryzacja i mockowanie
@pytest.mark.parametrize("status_code, json_data, raises_exception", [(200, {"id": 1, "name":"John Doe"}, False),
                                                                      (404, None, True)
])
@mock.patch("requests.get")
def test_get_users2(mock_get, status_code, json_data, raises_exception):
    #Tworzymy nowy obiektu typu Mock
    mock_response = mock.Mock()
    mock_response.status_code = status_code
    mock_response.json.return_value = json_data
    
    mock_get.return_value = mock_response

    if raises_exception:
        with pytest.raises(requests.HTTPError):
            service.get_users()
    else:
            data = service.get_users()
            assert data == json_data
