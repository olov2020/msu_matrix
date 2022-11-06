while True:
    print('Enter any number for choosing function:')
    print('1 for pasting one string into another')
    print('2 for calculating function')
    print('3 for counting how many times one string if included in another')
    print('4 for calculating sum of nums that less than mean')
    print('5 for finding the day of the week with its date\n')
    print('To exit program enter -1\n')

    checker = input()

    if checker == '-1':
        print('\nProgram has been finished')
        break

    elif checker == '1':
        s1 = input('\nEnter first string: ')
        s2 = input('Enter second string: ')
        check = 0
        ind = 4
        try:
            tmp = s1[ind - 1]
            print(s1[:ind] + s2 + s1[ind:])
        except IndexError:
            print('\nFirst string is too small, enter it again')
            while True:
                s1 = input('Enter first string: ')
                s2 = input('Enter second string: ')
                ind = 4
                try:
                    tmp = s1[ind - 1]
                    print(s1[:ind] + s2 + s1[ind:])
                    break
                except IndexError:
                    print('\nFirst string is too small, enter it again')
        print('Program worked correctly\n')

    elif checker == '2':
        print('\nNow enter some data to calculate function: f(x) = x^3 + 3log(-(x+2)/6) - 2^x - sqrt(x^2-3x+17)')
        start_input = input('Enter start of D(x): ')
        end_input = input('Enter end of D(x): ')
        step_input = input('Enter step of D(x): ')
        start, end, step = 0, 0, 0
        try:
            start = float(start_input)
            end = float(end_input)
            step = float(step_input)
        except ValueError:
            print('\nEnter your data again, input must contain only nums')
            while True:
                start_input = input('Enter start of D(x): ')
                end_input = input('Enter end of D(x): ')
                step_input = input('Enter step of D(x): ')
                try:
                    start = float(start_input)
                    end = float(end_input)
                    step = float(step_input)
                    break
                except ValueError:
                    print('\nEnter your data again, input must contain only nums')

        while start > end or end > -2 or step <= 0:
            print('\nEnter your data with some conditions: start <= end, end <= -2, stop > 0')
            start_input = input('Enter start of D(x): ')
            end_input = input('Enter end of D(x): ')
            step_input = input('Enter step of D(x): ')
            try:
                start = float(start_input)
                end = float(end_input)
                step = float(step_input)
            except ValueError:
                print('\nEnter your data again, input must contain only nums')
                while True:
                    start_input = input('Enter start of D(x): ')
                    end_input = input('Enter end of D(x): ')
                    step_input = input('Enter step of D(x): ')
                    try:
                        start = float(start_input)
                        end = float(end_input)
                        step = float(step_input)
                        break
                    except ValueError:
                        print('\nEnter your data again, input must contain only nums')

        while start <= end:
            import math

            print(f'x = {start}\n'
                  f'y = {start ** 3 + 3 * math.log(-(start + 2) / 6) - 2 ** start - math.sqrt(start ** 2 - 3 * start + 17)}')
            start += step
        print('Program worked correctly\n')

    elif checker == '3':
        s1 = input('\nEnter first string: ')
        s2 = input('Enter second string: ')

        ans = 0
        for i in range(len(s2) - len(s1) + 1):
            if s2[i:i + len(s1)] == s1:
                ans += 1
        print(f'First string is included {ans} times into second')
        print('Program worked correctly\n')

    elif checker == '4':
        n_input = input('\nEnter integer: ')
        n = 0
        try:
            n = int(n_input)
        except ValueError:
            print()
            while True:
                n_input = input('Enter integer: ')
                try:
                    n = int(n_input)
                    break
                except ValueError:
                    print()
        while n <= 0:
            print('\nInteger must be > 0')
            n_input = input('Enter integer: ')
            try:
                n = int(n_input)
            except ValueError:
                print()
                while True:
                    n_input = input('Enter integer: ')
                    try:
                        n = int(n_input)
                        break
                    except ValueError:
                        print()
        s = input(f'Enter string of {n} numbers with any separator: ')
        sr = 0
        ans = 0
        tmp = ''
        check = 1
        for i in s:
            if i == '-':
                check = -1
            else:
                if i.isdigit():
                    tmp += i
                else:
                    sr += int(tmp) * check
                    check = 1
                    tmp = ''
        if len(tmp) != 0:
            sr += int(tmp) * check
        tmp = ''
        sr /= n
        for i in s:
            if i == '-':
                check = -1
            else:
                if i.isdigit():
                    tmp += i
                else:
                    a = int(tmp) * check
                    check = 1
                    tmp = ''
                    if a < sr:
                        ans += a
        if len(tmp) != 0:
            a = int(tmp)
            tmp = ''
            if a < sr:
                ans += a
        print(f'Sum of nums less than mean ({sr}) is {ans}')
        print('Program worked correctly\n')

    elif checker == '5':
        s = input('\nEnter date in format dd.mm.yyyy: ')
        import re

        pattern = r'(\d{2}|\d{1})\.(\d{2}|\d{1})\.((160[1-9])|(16[1-9][0-9])|(1700))'
        day, month, year = 0, 0, 0
        check = False
        if not re.fullmatch(pattern, s):
            check = True
        else:
            day, month, year = map(int, s.split('.'))
            if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and (
                    day < 1 or day > 31):
                check = True
            if (month == 4 or month == 6 or month == 9 or month == 11) and (day < 1 or day > 30):
                check = True
            if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) and month == 2 and (day < 1 or day > 29):
                check = True
            if not (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) and month == 2 and (day < 1 or day > 28):
                check = True
            if year < 1601 or year > 1700:
                check = True
            if month < 1 or month > 12:
                check = True
        while not re.fullmatch(pattern, s) or check:
            s = input('\nEnter correct date of 17-th century in format dd.mm.yyyy: ')
            check = False

            if not re.fullmatch(pattern, s):
                check = True
            else:
                day, month, year = map(int, s.split('.'))
                if (
                        month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10
                        or month == 12) and (
                        day < 1 or day > 31):
                    check = True
                if (month == 4 or month == 6 or month == 9 or month == 11) and (day < 1 or day > 30):
                    check = True
                if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) and month == 2 and (day < 1 or day > 29):
                    check = True
                if not (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) and month == 2 and (day < 1 or day > 28):
                    check = True
                if year < 1601 or year > 1700:
                    check = True
                if month < 1 or month > 12:
                    check = True

        ans = ''
        ans_ind = 0
        month_id = 0
        year_id = 0

        if month == 1 or month == 10:
            month_id = 1
        elif month == 5:
            month_id = 2
        elif month == 8:
            month_id = 3
        elif month == 2 or month == 3 or month == 11:
            month_id = 4
        elif month == 6:
            month_id = 5
        elif month == 12 or month == 9:
            month_id = 6
        elif month == 4 or month == 7:
            month_id = 0

        year_id = (6 + year % 100 + (year % 100) // 4) % 7
        if year == 1700:
            year_id = (4 + year % 100 + (year % 100) // 4) % 7

        check_year = 0
        if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) and month <= 2:
            check_year = 1
        ans_ind = (day + month_id + year_id - check_year) % 7
        if ans_ind == 0:
            ans = 'Saturday'
        elif ans_ind == 1:
            ans = 'Sunday'
        elif ans_ind == 2:
            ans = 'Monday'
        elif ans_ind == 3:
            ans = 'Tuesday'
        elif ans_ind == 4:
            ans = 'Wednesday'
        elif ans_ind == 5:
            ans = 'Thursday'
        elif ans_ind == 6:
            ans = 'Friday'
        print(f'Date {s} was {ans}')
        print('Program worked correctly\n')
