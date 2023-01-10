#!/usr/bin/python3
"""

Module with pascal_triangle.

"""


if __name__ == "__main__":

    def pascal_triangle(n):
        """Method  that returns a list of lists of integers
        representing the Pascal’s triangle of n.

        Args:
            n (int): number of integers to be used.
        """
        list1 = []
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                list1.append(j)
        return list1
