from yandex_testing_lesson import is_palindrome


def test_reverse():
    test_data = (
        (12344321, True),
        ('abcddcba', True),
        ('', False),
        ('aba', True),
        ('a', True),
        ('1]3553]1', True),
        ('abbaaa', False),
        (129301, False),
        ('57291', False),
        ('a73ffsj', False),
        ('a[]]sd', False),
        ('aaaooooaaa', True))

    for input_s, correct_output_s in test_data:
        try:
            output_s = is_palindrome(input_s)
        except Exception:
            print('NO')
            return
        else:
            if output_s != correct_output_s:
                print('NO')
                return
    print('YES')


test_reverse()
