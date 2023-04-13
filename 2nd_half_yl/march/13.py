from yandex_testing_lesson import is_prime


def test_is_prime():
    check = True
    test_data = (
        (3, True),
        (11, True),
        (7, True),
        (4, False),
        (6, False))
    try:
        is_prime(1)
        is_prime(-4)
        is_prime(0)
    except ValueError or TypeError:
        check = False
    if check:
        return 'NO'
    for input_s, correct_output_s in test_data:
        output_s = is_prime(input_s)
        if output_s != correct_output_s:
            return 'NO'
    return 'YES'


print(test_is_prime())
