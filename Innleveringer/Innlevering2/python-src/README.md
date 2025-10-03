Assignment 2 IN2010 - Philip Elias Fleischer (philipef@ifi.uio.no)

## Experimentation answers

### Question 1 - Do the measured runtimes match Big-O expectations?

Yes, overall the sorting algorithms´ performance did match the predicted Big-O outcome.

- Insertion sort has a time complexity of O(n^2) (quadratic) for worst cases. The curve of the graph rises rapidly beyond a certain point in regard to a input number n. For nearly sorted inputs the growth flattens out considerably and in the best case it has a time complexity of O(n) (linear).
- Quicksort has an average running time of O(n\*log(n)) (it has linearithmic running times in most cases). The quicksort algorithm does however, with a opposite sorted array or nearly sorted array in combination with a not so good pivot point have O(n^2) (quadratic) time complexity.
- Mergesort has a time complexity of O(n\*log(n)) in all three cases (Best, Worst and average).
- Heapsort also has linearithmic time complexity, but is a bit slower compared to mergesort and the space complexity is also increased because heapsort is not an in-place sorting algorithm.

### Question 2 - How do comparisons and swaps correlate with runtime?

There is a strong correlation between comparisons and swaps in regards to runtime, but there are deviations. For all of the sorting algorithms more comparisons means more time used (in most cases). At the same time, memory and space usages with a similar comparison number may actually have quite differnces in the time used.

- Insertion sort tracks both comparisons and swaps closely; when the array is near sorted, both of them drop considerably and the time is reduced.
- Quicksort tracks both as well, but comparisons are a better indicator for the time prediction; bad pivots mean both comparisons and time amount increases.
- Mergesort compares quite a bit, but has a retty consistent or scalable number variance. Swaps on the other hand are high, and despite many operations, it is still fast because of the partitioning and memory usage.
- Heapsort has numerous comparisons to deal with and there is not as good memory utilization, therefore even with similar comparison counts the time complexity can be higher than mergesort.

To conclude, the comparisons and swaps are good indicators of the overall runtime, but not the whole picture. For example, mergesort and heapsort shows deviations when memory utilization algorithms and other constant factors are in play. Insertionsort and quicksort on the other hand track more directly with comparisons ans swaps counts in regard to time usage. This means that the runtime depends on not only number of operations, but also on how efficiently the algorithms are executed in practice.

### Question 3 - Which akgorithms are best when n is very small vs very large?

- Insertion sort is often best for small inputs.
- Quicksort is good, with a good pivot point, for large values of input.

### Question 4 - Which algorithms perform best across different input files?

- For random data, quicksort with a good pivot point and mergesort are the fastest.
- For nearly sorted or already sorted, insertion sort is best.
- For randomsorted files with small n: Quicksort is often best, but the other O(n\*log(n)) will also work fine.
- For randomsorted files with large n: Mergesort performs best on average compared to heapsort and quicksort that may result in some longer usage times.

To conclude: Insertion sort wins on small inputs, mergesort tends to be better on large inputs and quicksort is ofte better in practice.

### Question 5 - Any surprising findings?

Mergesort can often outperform heapsort even with more swaps, because of the memory utilization (in-place).
Mergesort has splitting and merging wich can or cannot be counted as swap moves, if they are included the swap count is really big, but it is still very fast, even though the swap count is considerably larger than that of the other sorting algorithms.
