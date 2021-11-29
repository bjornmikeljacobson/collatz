import time
import itertools
# import collatz_functions
import collatz_binary_functions


# n = int(input())
# b = input()
# t1 = input()
# t2 = input()

# previous_odd(n)

# collatz(n)


with open(r"C:\Users\bjorn\PycharmProjects\collatz\venv\out_file.txt"
          r"", "w") as file1:

    start_time = time.time()

    a1 = "011"
    proof_ratio = .75
    count1 = 0
    max_b1_length = 0
    complete_index = 0
    power_3 = 0
    power_2 = 0
    reduce_set = set()
    reduce_list = []

    for x in itertools.count():
        if len(a1) <= 30:
            if a1[-2:] == "11":
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
                    a1 = collatz_binary_functions.binary_add(a1, "100")
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
                            a1 = collatz_binary_functions.binary_add(a1, "100")
                            break
                        b2 = b1 + "0"  # to 3x we double it and it initial value, this step doubles b1
                        b3 = collatz_binary_functions.binary_add(b1, b2)
                        b3 = collatz_binary_functions.binary_add(b3, "1")  # b3 is now next even
                        # print(b3)
                        b3 = b3[-len(b1):]
                        # print("b3 shortened: " + b3)
                        power_3 += 1
                        while b3[-1] == "0":  # removing all leading zeros makes it odd
                            b3 = b3[:-1]
                            power_2 += 1
                            if b3 == "1" or b3 == "":
                                break
                        # print("b3 zeros removed:" + b3)
                        if 3 ** power_3 / 2 ** power_2 < 1 and complete_index == 0:
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
                            file1.write("\n")
                            a1 = collatz_binary_functions.binary_add(a1, "100")
                            break
                        b1 = b3[:]
                        count1 += 1
            else:
                a1 = collatz_binary_functions.binary_add(a1, "100")
        else:
            print("proof ratio:                     " + str(proof_ratio) + "\n")
            break

file1.write("proof ratio:                     " + str(proof_ratio) + "\n")
file1.write(str(reduce_set))

# collatz_binary_functions.binary_collatz(b, 0, 0, b, 0, 0, 0)

# binary_add(t1, t2)

print("--- %s seconds ---" % (time.time() - start_time))
