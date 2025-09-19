def main():
    r, s = map(int, input().split())
    x, y = map(int, input().split())

    # x and y are 1-indexed, convert to 0-indexed
    x -= 1
    y -= 1

    result = 0
    intersection_value = 0
    start_num = 1

    while r > 0 and s > 0:
        should_break = True

        if 0 <= x < r:
            should_break = False
            if x == 0:
                result += (start_num + s - 1) * (start_num + s) // 2 - (start_num - 1) * start_num // 2
                if intersection_value == 0 and 0 <= y < s:
                    intersection_value = start_num + y
            elif x == r - 1:
                result += (start_num + 2 * s + r - 3) * (start_num + 2 * s + r - 2) // 2 - (start_num + s + r - 2) * (start_num + s + r - 3) // 2
                if intersection_value == 0 and 0 <= y < s:
                    intersection_value = start_num + 2 * s + r - 3 - y
            else:
                result += start_num + s - 1 + x
                result += start_num + 2 * (s + r) - 4 - x
        if 0 <= y < s:
            should_break = False
            if y == s - 1:
                result += (start_num + s + r - 2) * (start_num + s + r - 1) // 2 - (start_num + s - 2) * (start_num + s - 1) // 2
                if intersection_value == 0 and 0 <= x < r:
                    intersection_value = start_num + s - 1 + x
            elif y == 0:
                result += start_num + (start_num + 2 * (s + r) - 5) * (start_num + 2 * (s + r) - 4) // 2 - (start_num + 2 * s + r - 3) * (start_num + 2 * s + r - 4) // 2
                if intersection_value == 0 and 0 <= x < r:
                    intersection_value = start_num + 2 * (r + s) - 4 - x
            else:
                result += start_num + y
                result += start_num + 2 * s + r - 3 - y

        if should_break:
            break

        x -= 1
        y -= 1
        start_num += 2 * (r + s - 2)
        r -= 2
        s -= 2

    # subtract the intersection value since it was added twice
    result -= intersection_value

    print(result)


if __name__ == "__main__":
    main()
