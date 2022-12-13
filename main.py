import address_parser


def main():
    args = address_parser.parse_args()
    address_str = args.s
    result = address_parser.parse(address_str)
    address_parser.pprint(result)
    return address_parser


if __name__ == '__main__':
    main()
