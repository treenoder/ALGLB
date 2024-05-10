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
    convert_power = 0
    for prefix, power in SI.items():
        if length.startswith(prefix):
            convert_power = power + solution(length[len(prefix):])
            break

    if "^" in length:
        unit = int(length.split("^")[1])
        return convert_power * unit
    return convert_power


def main():
    length = input()
    result = solution(length)
    print(result)


if __name__ == "__main__":
    main()
