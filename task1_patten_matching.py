import re


def validate(validator:list,patterns:list):
    try:
        allowed = []
        count=0
        for n,pat in enumerate(patterns):
            for val in validator:
                if val not in allowed:
                    match = re.fullmatch(pat,val)
                    if match != None:
                        allowed.append(val)
        print(f"Allowed Patter from the given list are \n{allowed}\n Total number of validation numbers {len(validator)} and allowed numbers {len(allowed)}")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    validator = ["2124567890",
                "212-456-7890",
                "(212)456-7890",
                "(212)-456-7890",
                "212.456.7890",
                "212 456 7890",
                "+12124567890",
                "+1 212.456.7890",
                "+212-456-7890",
                "1-212-456-7890"]

    patterns = ["^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]\d{4}$",
                "^\+\d{3}[\-]?\d{3}[\-]?\d{4,5}$",
                "\d{10}",
                "\d{1,2}?[\-]\d{3}[\-]\d{3}[\-]\d{4}"]


    validate(validator,patterns)