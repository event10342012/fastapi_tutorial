from unittest.mock import MagicMock
from unittest import TestCase


class TestPhone(TestCase):
    def test_call(self):
        phone = Iphone()
        phone.call = MagicMock()
        leo = People('Leo', phone)
        leo.hi()
        assert phone.call.called
