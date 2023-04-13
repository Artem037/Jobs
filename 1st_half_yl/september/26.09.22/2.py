def numbers(nums):
    nums1 = ''.join([i for i in nums if i.isdigit()])
    a = 0
    b = 0
    try:
        for i in nums:
            if i not in '+()-1234567890 ' and not i == '\t':
                raise Exception
        if not (nums.lstrip().startswith('+7') or nums.lstrip().startswith('8')):
            raise Exception
        for i in nums:
            if i == '(':
                if not a:
                    a = 1
                else:
                    raise Exception
            elif i == ')':
                if not b:
                    b = 1
                else:
                    raise Exception
                if a != 1:
                    raise Exception
        if a != b:
            raise Exception
        if nums.find('--') != -1:
            raise Exception
        if nums.find('-') != -1:
            if nums.index('-') in [0, len(nums) - 1]:
                raise Exception
        if len(nums1) != 11:
            raise Exception
    except Exception:
        return 'error'
    if nums1[0] == '8':
        nums1 = nums1[1:]
        return '+7' + nums1
    return '+' + nums1


print(numbers(input()))
