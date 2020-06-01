
BILLION = 1000000000
MILLION = 1000000
THOUSAND = 1000
HUNDRED = 100
TWENTY = 20
TEN = 10


def number_to_words(num):
    # divide number in group of billions
    if num >= BILLION:
        billions = num // BILLION
        remainder = num % BILLION
        return number_to_words(billions) + (" Billions" if billions > 1 else " Billion") + \
               ("" if remainder == 0 else " " + number_to_words(remainder))

    if num >= MILLION:
        millions = num // MILLION
        remainder = num % MILLION
        return number_to_words(millions) + (" Millions" if millions > 1 else " Million") + \
               ("" if remainder == 0 else " " + number_to_words(remainder))

    if num >= THOUSAND:
        thousands = num // THOUSAND
        remainder = num % THOUSAND
        return number_to_words(thousands) + (" Thousands" if thousands > 1 else " Thousand") + \
               ("" if remainder == 0 else " " + number_to_words(remainder))

    if num >= HUNDRED:
        hundreds = num // HUNDRED
        remainder = num % HUNDRED
        return number_to_words(hundreds) + (" Hundreds" if hundreds > 1 else " Hundred") + \
               ("" if remainder == 0 else " " + number_to_words(remainder))

    if num >= TWENTY:
        twenty_or_plus = num // TEN
        remainder = num % TEN
        string = (  "Twenty" if twenty_or_plus == 2 else
                    "Thirty" if twenty_or_plus == 3 else
                    "Forty" if twenty_or_plus == 4 else
                    "Fifty" if twenty_or_plus == 5 else
                    "Sixty" if twenty_or_plus == 6 else
                    "Seventy" if twenty_or_plus == 7 else
                    "Eighty" if twenty_or_plus == 8 else
                    "Ninety" if twenty_or_plus == 9 else
                    ""
                    )

        if string == "":
            raise ValueError("Invalid number " + str(num))

        return string + ("" if remainder == 0 else " " + number_to_words(remainder))

    string = (
        "Zero" if num == 0 else
        "One" if num == 1 else
        "Two" if num == 2 else
        "Three" if num == 3 else
        "Four" if num == 4 else
        "Five" if num == 5 else
        "Six" if num == 6 else
        "Seven" if num == 7 else
        "Eight" if num == 8 else
        "Nine" if num == 9 else
        "Ten" if num == 10 else
        "Eleven" if num == 11 else
        "Twelve" if num == 12 else
        "Thirteen" if num == 13 else
        "Fourteen" if num == 14 else
        "Fifteen" if num == 15 else
        "Sixteen" if num == 16 else
        "Seventeen" if num == 17 else
        "Eighteen" if num == 18 else
        "Nineteen" if num == 19 else
        ""
    )

    if string == "":
        raise ValueError("Invalid number " + str(num))

    return string


if __name__ == "__main__":

    while True:
        print("Type number (Q to exit) and press enter:")
        num_str = input()
        if num_str == "Q":
            # print("Thanks for using number to words app")
            break
        num = int(num_str)
        print(number_to_words(num))
