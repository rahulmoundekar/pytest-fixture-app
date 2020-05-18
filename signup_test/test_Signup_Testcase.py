import pytest


@pytest.yield_fixture()
def setUp():
    print("First your want to navigate singup page")
    yield
    print("close all resources")


def test_signup_by_gmail(setUp):
    print('signup using gmail account')


def test_signup_by_official_mail(setUp):
    print('signup using official account')
