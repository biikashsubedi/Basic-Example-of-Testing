def add(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return 'Please Enter a Number!'
    except ValueError as err:
        return err