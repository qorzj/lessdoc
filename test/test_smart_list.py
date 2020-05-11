from unittest import TestCase
from api.util.smart_list import SmartList


class TestSmartList(TestCase):
    def test_find(self):
        array = SmartList()
        array.append({'id': 1, 'name': 'Alice'})
        array.append({'id': 2, 'name': 'Bob'})
        array.append({'id': 3, 'name': 'Carry'})
        obj = array.find(lambda x: x['name'] == 'Bob')
        self.assertDictEqual(obj, {'id': 2, 'name': 'Bob'})
        try:
            array.find(lambda x: x['name'] == 'none')
            self.fail()
        except IndexError:
            pass
