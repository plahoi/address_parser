import unittest
import json
from address_parser import parse


class TestParser(unittest.TestCase):
    def _asserter(self, expected_data, raw_data):
        for ix in range(len(raw_data)):
            with self.subTest(raw_data[ix]):
                parsed_address = parse(raw_data[ix])
                print(parsed_address, expected_data[ix])
                self.assertEqual(parsed_address, json.dumps(expected_data[ix]))

    def test_simple_addresses(self):
        addresses = ['Winterallee 3', 'Musterstrasse 45', 'Blaufeldweg 123B']
        expected_result = [
            {'street': 'Winterallee', 'housenumber': '3'},
            {'street': 'Musterstrasse', 'housenumber': '45'},
            {'street': 'Blaufeldweg', 'housenumber': '123B'},
        ]

        self._asserter(expected_result, addresses)

    def test_complicated_addresses(self):
        addresses = ['Am Bächle 23', 'Auf der Vogelwiese 23 b']
        expected_result = [
            {'street': 'Am Bächle', 'housenumber': '23'},
            {'street': 'Auf der Vogelwiese', 'housenumber': '23 b'},
        ]

        self._asserter(expected_result, addresses)

    def test_complex_addresses(self):
        addresses = ['4, rue de la revolution', '200 Broadway Av', 'Calle Aduana, 29', 'Calle 39 No 1540']
        expected_result = [
            {'street': 'rue de la revolution', 'housenumber': '4'},
            {'street': 'Broadway Av', 'housenumber': '200'},
            {'street': 'Calle Aduana', 'housenumber': '29'},
            {'street': 'Calle 39', 'housenumber': 'No 1540'},
        ]

        self._asserter(expected_result, addresses)

    def test_other_addresses(self):
        addresses = [
            'Hello world',
            'Franz-Rennefeld-Weg 8',
            '19 East  Rd',
            'Rue des Francs, 70',
            '123 W 34th St',
            'Boulevard Porfirio Díaz #58 ',
            '200th century Fox Av. 1568',
            'Calle 39 No 1540B',
            'Franz-Rennefeld-Weg 8/3',
        ]
        expected_result = [
            {'street': 'NA', 'housenumber': 'NA'},
            {'street': 'Franz-Rennefeld-Weg', 'housenumber': '8'},
            {'street': 'East Rd', 'housenumber': '19'},
            {'street': 'Rue des Francs', 'housenumber': '70'},
            {'street': 'W 34th St', 'housenumber': '123'},
            {'street': 'Boulevard Porfirio Díaz', 'housenumber': '58'},
            {'street': '200th century Fox Av.', 'housenumber': '1568'},
            {'street': 'Calle 39', 'housenumber': 'No 1540B'},
            {'street': 'Franz-Rennefeld-Weg', 'housenumber': '8/3'},
        ]

        self._asserter(expected_result, addresses)


if __name__ == '__init__':
    unittest.main()
