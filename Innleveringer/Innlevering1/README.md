## Innlevering 1 IN2010

How to run the program:
python3 oppg1.py inputs/eksempel_input


### Author:
Philip Elias Fleischer (philipef@ifi.uio.no)




## Pseudocode for balanced_print_tree

    Procedure balanced_print_tree(array)
    #Assumptions: sorted and indexable array
        low <- 0
        high <- len(array) - 1

        procedure _print_midpoint(low, high)
            if low > high then
                return
            midpoint <- (low + high) / 2
            print(array[midpoint])
            _print_midpoint(midpoin + 1, high)  #right sub-array
            _print_midpoint(low, midpoint - 1)  #Left sub-array
        _print(low, high)




## Pseudodcode for balanced_print_tree_pq

    Procedure balanced_print_tree_pq(array)
        low <- 0
        high <- len(array) - 1
        heap <- []
        seq_number <- 0

        Procedure _heap_push(low, high)
            if low <= high then
                seq_number <- seq_number + 1
                heap.push(heap, (-seq_number, low, high))
    
        _heap_push(low, high)

        while heap is not empty do
            pop heap values of the top with heappop()
            midpoint <- (low + high) / 2
            print(array[midpoint])
            _heap_push(low, mid - 1)    #Left sub-array
            _heap_push(mid + 1, high)   #right sub-array

