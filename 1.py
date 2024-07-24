# You are given an array of integers and an integer k. Your task is to select k elements from the array such that their sum is maximized

def max_sum_elements(arr, k):
    arr.sort(reverse=True)
    return sum(arr[:k])