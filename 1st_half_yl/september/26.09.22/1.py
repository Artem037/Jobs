def numbers(nums):
    a = 0
    b = 0
    for i in nums:
        if i not in '+()-1234567890 ' and not i == '\t':
            return 'error'
    nums1 = ''.join([i for i in nums if i.isdigit()])
    if not (nums.lstrip().startswith('+7') or nums.lstrip().startswith('8')):
        return 'error'
    for i in nums:
        if i == '(':
            if not a:
                a = 1
            else:
                return 'error'
        elif i == ')':
            if not b:
                b = 1
            else:
                return 'error'
            if a != 1:
                return 'error'
    if a != b:
        return 'error'
    if nums.find('--') != -1:
        return 'error'
    if nums.find('-') != -1:
        if nums.index('-') in [0, len(nums) - 1]:
            return 'error'
    if len(nums1) != 11:
        return 'error'
    if nums1[0] == '8':
        nums1 = nums1[1:]
        return '+7' + nums1
    return '+' + nums1


print(numbers(input()))
