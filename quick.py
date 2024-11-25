def permutate_custom(input: int):
    output = []

    # very cool preallocaton stuff
    input_string = str(input)
    length = len(input_string)
    used = [False] * length
    current_perm = []

    def recurse():
        # append finished permutations
        if len(current_perm) == length:
            output.append("".join(current_perm))
            return

        # index iteration
        for i in range(length):
            if not used[i]:
                # set digit used to true and append it
                used[i] = True
                current_perm.append(input_string[i])
                
                recurse()

                # only executed after finished permutations, marks next i as available again
                used[i] = False
                current_perm.pop()

    # call the recursion until it returns because everything has been used
    recurse()
    
    for line in output:
        print(line)

permutate_custom(123)