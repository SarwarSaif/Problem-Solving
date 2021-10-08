# Problem link: https://www.hackerrank.com/challenges/maximize-it/problem
from itertools import product
if __name__ == '__main__':
    K, M = map(int, input().split(" "))
    N = (list(map(int, input().split()))[1:] for _ in range(K))
    # Create Cartesian Product of all the lists in N
    car_pro = product(*N) # return tuples
    # Find maximum squared mod from each tuple in cartesian product
    # use map to iterate over each tuple in car_pro and then apply the squared mod function
    result = map(lambda x: sum(i**2 for i in x)%M, car_pro)
    print(max(result))
