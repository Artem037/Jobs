class Wrong_format(Exception):
    pass


class Incorrect_number_of_digits(Exception):
    pass


def numbers(nums):
    nums1 = ''.join([i for i in nums if i.isdigit()])
    a = 0
    b = 0
    try:
        for i in nums:
            if i not in '+()-1234567890 ' and not i == '\t':
                raise Wrong_format
        if not (nums.lstrip().startswith('+7') or nums.lstrip().startswith('8')):
            raise Wrong_format
        for i in nums:
            if i == '(':
                if not a:
                    a = 1
                else:
                    raise Wrong_format
            elif i == ')':
                if not b:
                    b = 1
                else:
                    raise Wrong_format
                if a != 1:
                    raise Wrong_format
        if a != b:
            raise Wrong_format
        if nums.find('--') != -1:
            raise Wrong_format
        if nums.find('-') != -1:
            if nums.index('-') in [0, len(nums) - 1]:
                raise Wrong_format
        if len(nums1) != 11:
            raise Incorrect_number_of_digits
    except Wrong_format:
        return 'неверный формат'
    except Incorrect_number_of_digits:
        return 'неверное количество цифр'
    if nums1[0] == '8':
        nums1 = nums1[1:]
        return '+7' + nums1
    return '+' + nums1


print(numbers(input()))
