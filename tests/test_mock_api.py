
import pytest
import requests
import unittest.mock as mock 
import source.mock_api as mock_api

#! NOTE : we are not mocking the actual function. here we are mocking the 'requests.get', which we are using inside the function
@mock.patch("requests.get")
def test_get_user(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id":1, "name": "Ali Khan"}
    mock_get.return_value = mock_response
    data = mock_api.get_user()
    
    assert data == {"id":1, "name": "Ali Khan"}
    

#! for API Error

@mock.patch("requests.get")
def test_get_user_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    
    with pytest.raises(requests.HTTPError):
        mock_api.get_user()
        
        

#! explanation test case 1:

"""Explanation:

Mocking requests.get: The @mock.patch("requests.get") decorator replaces the requests.get method with a mock object for the duration of the test. 
This prevents the actual HTTP request from being made.
Creating Mock Response:

mock_response = mock.Mock(): Creates a mock response object.
mock_response.status_code = 200: Sets the status_code attribute of the mock response to 200.
mock_response.json.return_value = {"id": 1, "name": "Ali Khan"}: Sets the return value of the json method to a dictionary representing the user data.
Configuring Mock requests.get:

mock_get.return_value = mock_response: Configures the mock requests.get to return the mock_response when called.
Calling get_user: Calls the get_user function, which now uses the mocked requests.get.

Assertion:
assert data == {"id": 1, "name": "Ali Khan"}: Checks that the data returned by get_user matches the expected mock data.
This test case ensures that the get_user function correctly handles a successful API response. """