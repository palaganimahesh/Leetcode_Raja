"""
Statement
Given an array, colors, which contains a combination of the following three elements:

0 -- (representing red)

1 -- (representing white)

2 -- (representing blue)
Sort the array in place so that the elements of the same color are adjacent, with the colors in the order of red, white, and blue. To improve your problem-solving skills, do not utilize the built-in sort function.
"""

def sort_colors(colors):
    # Initialize the start, current, and end pointers
    start, current, end = 0, 0, len(colors) - 1

    # Iterate through the list until the current pointer exceeds the end pointer
    while current <= end:
        if colors[current] == 0:
            # If the current element is 0, swap it with the element at the start pointer
            colors[start], colors[current] = colors[current], colors[start]
            # Move both the start and current pointers one position forward
            current += 1
            start += 1

        elif colors[current] == 1:
            # If the current element is 1, just move the current pointer one position forward
            current += 1

        else:
            # If the current element is 2, swap it with the element at the end pointer
            colors[current], colors[end] = colors[end], colors[current]
            # Move the end pointer one position backward
            end -= 1
    return colors

# Driver code
def main():
    inputs = [[0, 1, 0], [1, 1, 0, 2], [2, 1, 1, 0, 0], [2, 2, 2, 0, 1, 0], [2, 1, 1, 0, 1, 0, 2]]

    # Iterate over the inputs and print the sorted array for each
    for i in range(len(inputs)):
        colors=inputs[i]
        print(i + 1, ".\tcolors:", colors)
        sort_colors(colors)
        print("\n\tThe sorted array is:", colors)
        print("-" * 100)

if __name__ == "__main__":
    main()