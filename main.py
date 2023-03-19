# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks,
    # create the output pairs
    time = 0
    threads = []
    for i in range(m):
        if i < n:
            threads.append([i, int(data[i])])
            output.append([i, 0])
        else:
            lowest_index = 0
            for j in range(len(threads)):
                if threads[j][1] < threads[lowest_index][1]:
                    lowest_index = j
            output.append([threads[lowest_index][0], threads[lowest_index][1]])
            threads[lowest_index][1] += int(data[i])

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(list(input().split()))

    # TODO: create the function
    result = parallel_processing(n, m, data)
    
    # TODO: print out the results, each pair in it's own line
    for pair in result:
        print(pair[0], pair[1])



if __name__ == "__main__":
    main()