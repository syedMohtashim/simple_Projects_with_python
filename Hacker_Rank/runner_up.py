# This program prints the runner up score 
def runner_up(arr):
    sorted_arr = sorted(arr , reverse=True)
    return print( sorted_arr[2] )
arr = [10,10,10,8,10]
runner_up(arr)