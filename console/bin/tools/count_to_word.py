def main(count):
    words = ["null", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    output = []
    str_count = str(count)
    for x in str_count:
        output.append(words[int(x)])
    return output