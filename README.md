Address line parser

- [DESCRIPTION](#description)
- [SOLUTION](#solution)
- [RUN](#run)
- [OPTIONS](#options)
- [EXAMPLES](#examples)
- [TESTS](#tests)

# DESCRIPTION
An address provider returns addresses only with concatenated street names and numbers. Our own system on the other hand has separate fields for street name and street number.

**Input:** string of address

**Output:** string of street and string of street-number as JSON object

1. Write a simple program that does the task for the simplest cases, e.g.
   1. `"Winterallee 3"` -> `{"street": "Winterallee", "housenumber": "3"}`
   1. `"Musterstrasse 45"` -> `{"street": "Musterstrasse", "housenumber": "45"}`
   1. `"Blaufeldweg 123B"` -> `{"street": "Blaufeldweg", "housenumber": "123B"}`

2. Consider more complicated cases
   1. `"Am Bächle 23"` -> `{"street": "Am Bächle", "housenumber": "23"}`
   1. `"Auf der Vogelwiese 23 b"` -> `{"street": "Auf der Vogelwiese", "housenumber": "23 b"}`

3. Consider other countries (complex cases)
   1. `"4, rue de la revolution"` -> `{"street": "rue de la revolution", "housenumber": "4"}`
   1. `"200 Broadway Av"` -> `{"street": "Broadway Av", "housenumber": "200"}`
   1. `"Calle Aduana, 29"` -> `{"street": "Calle Aduana", "housenumber": "29"}`
   1. `"Calle 39 No 1540"` -> `{"street": "Calle 39", "housenumber": "No 1540"}`

# SOLUTION
It requires a Python interpreter and has been tested with version 3.8.1 and macOS. But it should be platform agnostic and run on Linux and Windows.

The application extracts the street name and house number using regular expressions and simple logic.

There have been used 3 different approaches to try to extract the corresponding address components.\
They are evaluated one at a time. When the parser matches with one of the cases for the input address line, it's not necessary 
to continue with others.

When the parser doesn't meet any of the 3 given criteria, then the algorithm moves from the end of the address string to the beginning until it meets the number. Therefore everything to the right of the number, including the number itself is supposed to be a house number.

## Case I: Regex for No/nr notion

`(?P<street>.+\d+)\s(?P<house_number>(?:No|Nr|no|nr)\.?\s?\d+\s?[a-zA-Z]?)`

It will match addresses with the following format:
- Calle 39 No 1540
- Calle 39 nr. 1540

## Case II: Trailing house number

`has_num(splitted_address[-1])`

It will match addresses with the trailing house number:
- Winterallee 3
- Musterstrasse 45
- Blaufeldweg 123B
- Am Bächle 23
- Calle Aduana, 29
- 200th century Fox Av. 1568

## Case III: Leading house number

`has_num(splitted_address[0])`

It will match addresses with the following format:
- 200 Broadway Av
- 4, rue de la revolution
- 123 W 34th St

## Case IV: House number is between characters

`for ix in reversed(range(len(splitted_address)))`

It will match addresses with the following format:
- Auf der Vogelwiese 23 b

# RUN
Clone the project executing the following command in a terminal:\
`git clone https://github.com/plahoi/address_parser.git`

Move to the project directory using:\
`cd address_parser`

Execute the following:\
`python3 main.py [OPTIONS] [ADDRESS_LINE]`

# OPTIONS
    -s   Address line to be parsed

# EXAMPLES
Parse the address "Rue des Francs, 70":\
`python3 main.py -s 'Rue des Francs, 70'`
  
Output:
```
{'street': 'Rue des Francs', 'housenumber': '70'}
```

Parse the address "Calle 39 No 1540B":\
`python3 main.py -s 'Calle 39 No 1540B'`
  
Output:
```
{'street': 'Calle 39', 'housenumber': 'No 1540B'}
```

# TESTS
To run tests, in the project directory run the following command:
```
python3 -m unittest test.test_parser
```
