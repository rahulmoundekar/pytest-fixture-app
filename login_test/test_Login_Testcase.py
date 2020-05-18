import pytest


@pytest.fixture()
def setUp():
    print("First your want to navigate login page")
    yield
    print("once after close all resources")


def test_login_by_gmail(setUp):
    print('Login using gmail account')


def test_login_by_official_mail(setUp):
    print('Login using official mail id')
