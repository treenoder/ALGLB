SI = {
    "tera": 12,
    "giga": 9,
    "mega": 6,
    "kilo": 3,
    "deci": -1,
    "centi": -2,
    "milli": -3,
    "micro": -6,
    "nano": -9,
}


def solution(length: str) -> int:
    if length == "meter":
        return 0

    clean_length = length.replace("meter^", "")
    dim = 1
    if "2" in clean_length:
        dim = 2
    elif "3" in clean_length:
        dim = 3
    clean_length = clean_length.replace("2", "").replace("3", "")

    total_exponent = 0
    for prefix, power in SI.items():
        if prefix in clean_length:
            total_exponent += clean_length.count(prefix) * power

    return total_exponent * dim


def main():
    length = input()
    result = solution(length)
    print(result)


if __name__ == "__main__":
    main()
