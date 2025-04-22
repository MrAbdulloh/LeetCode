def minMovesToSeat(seats: list[int], students: list[int]) -> int:
    seats.sort()
    students.sort()
    total = 0
    for i, j in zip(students, seats):
        total += abs(i - j)
    return total


# seats = [3, 1, 5]
# students = [2, 7, 4]

# seats = [4,1,5,9]
# students = [1,3,2,6]
seats = [2, 2, 6, 6]
students = [1, 3, 2, 6]
print(minMovesToSeat(seats, students))
