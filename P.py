def rightmost_set_bit(n):
    """
    Returns the rightmost set bit of a given number.

    Args:
        n (int): The input number.

    Returns:
        int: The rightmost set bit.
    """
    return n & -n
num = int(input("Enter a number: "))
print("Rightmost set bit:", rightmost_set_bit(num))