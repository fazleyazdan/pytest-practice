import pytest 
import unittest.mock as mock
import source.mock_service as mock_service

@mock.patch("source.mock_service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Kamran"
    user_name = mock_service.get_user_from_db(1)
    assert user_name == "Kamran"
    
    
    
    