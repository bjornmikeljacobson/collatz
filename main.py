import time
import itertools
import cmd
from contextlib import contextmanager
import sys
import os


cli = cmd.Cmd()


@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout


def convergence_finder(inner_a1):
    inner_count1 = 0
    inner_complete_index = 0
    inner_power_3 = 0
    inner_power_2 = 0
    inner_b1 = inner_a1[:]
    for _ in itertools.count():
        inner_count1 += 1
        if inner_b1 == "1" or inner_b1 == "":
            print("      no proof of convergence for numbers ending in: " + inner_a1 + "\n")
            return inner_a1
        inner_b2 = inner_b1 + "0"  # to 3x we double it and it initial value, this step doubles b1
        inner_b3 = binary_add(inner_b1, inner_b2)
        inner_b3 = binary_add(inner_b3, "1")  # b3 is now next even
        inner_b3 = inner_b3[-len(inner_b1):]
        inner_power_3 += 1
        while inner_b3[-1] == "0":  # removing all leading zeros makes it odd
            inner_b3 = inner_b3[:-1]
            inner_power_2 += 1
            if inner_b3 == "1" or inner_b3 == "":
                break
        if 3 ** inner_power_3 / 2 ** inner_power_2 < 1 and inner_complete_index == 0:
            inner_complete_index = inner_count1
            print("      length a1                        " + str(len(inner_a1)))
            print("      collatz complete for strings ending in: " + inner_a1)
            print("      iterations to reduce:            " + str(inner_complete_index))
            print("      power ratio:                     " + str(round(3 ** inner_power_3 / 2 ** inner_power_2, 5)))
            print("      powers:                          " + "3^" + str(inner_power_3) + " , 2^" + str(inner_power_2))
            print("")
            return
        inner_b1 = inner_b3[:]


def binary_add(a, c):
    max_len = max(len(a), len(c))
    a = a.zfill(max_len)
    c = c.zfill(max_len)

    # Initialize the result
    result = ''

    # Initialize the carry
    carry = 0

    # Traverse the string
    for t in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[t] == '1' else 0
        r += 1 if c[t] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result

        # Compute the carry.
        carry = 0 if r < 2 else 1

    if carry != 0:
        result = '1' + result

    return result.zfill(max_len)


# n = input()

# binary_collatz(n, 0, 0, n, 0, 0, 0)

# n = int(input())
# b = input()
# t1 = input()
# t2 = input()

# previous_odd(n)

# collatz(n)

dict1 = {1: "00", 2: "01", 3: "10", 4: "11"}

with open(r"C:\Users\bjorn\PycharmProjects\collatz\venv\out_file.txt", "w") as file1:

    start_time = time.time()

    a1 = "111"
    proof_ratio = .75
    count1 = 0
    max_b1_length = 0
    complete_index = 0
    power_3 = 0
    power_2 = 0
    reduce_set = set()
    reduce_list = []
    non_converge_list = []
    temp_list = []
    b = 0

    for x in itertools.count():
        if len(a1) <= 30:
            if a1[-1:] == "1":
                count1 = 0
                max_b1_length = 0
                complete_index = 0
                power_3 = 0
                power_2 = 0
                b1 = a1[:]
                b4 = a1[:]
                reduce_list = list(reduce_set)
                match = False
                for j in range(len(reduce_list)):
                    if a1[-len(reduce_list[j]):] == reduce_list[j]:
                        match = True
                        break
                if match:
                    a1 = binary_add(a1, "100")
                    continue
                else:
                    for i in itertools.count():
                        count2 = count1 + 1
                        if len(b1) > max_b1_length:
                            max_b1_length2 = len(b1)
                        else:
                            max_b1_length2 = max_b1_length
                        if b1 == "1" or b1 == "":
                            print("no proof of convergence for numbers ending in: " + b4 + "\n")
                            non_converge_list.append(a1)
                            print(non_converge_list)
                            while non_converge_list:
                                for k in non_converge_list:
                                    if b:
                                        b -= 1
                                        continue
                                    for g in range(1, 5):
                                        print("      convergence finder #" + str(g))
                                        file1.write("      convergence finder #" + str(g) + "\n")
                                        if convergence_finder(dict1[g] + k) is not None:
                                            with suppress_stdout():
                                                temp_list.append(convergence_finder(dict1[g] + k))
                                    print("temp list: " + str(temp_list))
                                    file1.write("temp list: " + str(temp_list) + "\n")
                                    if temp_list:
                                        b = len(temp_list)-1
                                        for y in temp_list:
                                            non_converge_list.insert(0, y)
                                        non_converge_list.remove(k)
                                        temp_list = []
                                    # print("non-converge_list:")
                                    # cli.columnize(non_converge_list, displaywidth=80)
                                    # print("non_converge_list length:" + str(len(non_converge_list)))
                                    # print("")
                                    # file1.write("non_converge_list: " + str(non_converge_list) + "\n\n")
                                # print(non_converge_list)
                            a1 = binary_add(a1, "100")
                            break
                        b2 = b1 + "0"  # to 3x we double it and it initial value, this step doubles b1
                        b3 = binary_add(b1, b2)
                        b3 = binary_add(b3, "1")  # b3 is now next even
                        b3 = b3[-len(b1):]
                        power_3 += 1
                        while b3[-1] == "0":  # removing all leading zeros makes it odd
                            b3 = b3[:-1]
                            power_2 += 1
                            if b3 == "1" or b3 == "":
                                break
                        if (3 ** power_3 / 2 ** power_2) < 1:
                            complete_index = count2
                            print("length a1                        " + str(len(a1)))
                            print("collatz complete for strings ending in: " + b4)
                            print("iterations to reduce:            " + str(complete_index))
                            print("power ratio:                     " + str(round(3 ** power_3 / 2 ** power_2, 5)))
                            print("powers:                          " + "3^" + str(power_3) + " , 2^" + str(power_2))
                            reduce_set.add(a1)
                            proof_ratio += 1/2**len(a1)
                            print("proof ratio:                     " + str(proof_ratio))

                            file1.write("length a1                        " + str(len(a1)) + "\n")
                            file1.write("collatz complete for strings ending in: " + b4 + "\n")
                            file1.write("iterations to reduce:            " + str(complete_index) + "\n")
                            file1.write("power ratio:                     " + str(round(3 ** power_3 / 2 ** power_2, 5))
                                        + "\n")
                            file1.write("powers:                          " + "3^" + str(power_3) + " , 2^" +
                                        str(power_2) + "\n")
                            file1.write("proof ratio:                     " + str(proof_ratio) + "\n")
                            a1 = binary_add(a1, "10")
                            break
                        b1 = b3[:]
                        count1 += 1
            else:
                a1 = binary_add(a1, "100")
        else:
            print(proof_ratio)
            print("power ratio:                     " + str(round(3 ** power_3 / 2 ** power_2, 5)))
            break


# collatz_binary_functions.binary_collatz(b, 0, 0, b, 0, 0, 0)

# binary_add(t1, t2)

print("--- %s seconds ---" % (time.time() - start_time))
