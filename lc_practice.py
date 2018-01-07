# List comprehension basic guideline:
# [expression for item in list if condition]


def identity(nums):
    """Identity:

    Given a list of numbers, write a list comprehension that produces a copy of the list.

        >>> identity([1, 2, 3, 4, 5])
        [1, 2, 3, 4, 5]

        >>> identity([])
        []
    """
    return [num for num in nums]



def doubled(nums):
    """Doubled:

    Given a list of numbers, write a list comprehension that produces a list of each number doubled.

        >>> doubled([1, 2, 3, 4, 5])
        [2, 4, 6, 8, 10]

        >>> doubled([-2, 2, -10, 10])
        [-4, 4, -20, 20]
    """
    return [num * 2 for num in nums]



def squared(nums):
    """Squared:

    Given a list of numbers, write a list comprehension that produces a list of the squares of each number.

        >>> squared([1, 2, 3, 4, 5])
        [1, 4, 9, 16, 25]

        >>> squared([-2, 2, -10, 10])
        [4, 4, 100, 100]
    """
    return [num ** 2 for num in nums]



def evens(nums):
    """Evens:

    Given a list of numbers, write a list comprehension that produces a list of only the even numbers in that list.

        >>> evens([1, 2, 3, 4, 5])
        [2, 4]

        >>> evens([1, 3, 5])
        []

        >>> evens([-2, -4, -7])
        [-2, -4]
    """
    return [num for num in nums if num % 2 == 0]



def odds(nums):
    """Odds:

    Given a list of numbers, write a list comprehension that produces a list of only the odd numbers in that list.

        >>> odds([1, 2, 3, 4, 5])
        [1, 3, 5]

        >>> odds([2, 4, 6])
        []

        >>> odds([-2, -4, -7])
        [-7]
    """
    return [num for num in nums if num % 2 != 0]



def positives(nums):
    """Positives:

    Given a list of numbers, write a list comprehension that produces a list of only the positive numbers in that list.

        >>> positives([-2, -1, 0, 1, 2])
        [1, 2]
    """
    return [num for num in nums if num > 0]



def selective_stringify_nums(nums):
    """Selectively stringify nums:

    Given a list of numbers, write a list comprehension that produces a list of strings of each number that is divisible by 5.

        >>> selective_stringify_nums([25, 91, 22, -7, -20])
        ['25', '-20']
    """
    return [str(num) for num in nums if num % 5 == 0]



def words_not_the(sentence):
    """Words not 'the'

    Given a sentence, produce a list of the lengths of each word in the sentence, but only if the word is not 'the'.

        >>> words_not_the('the quick brown fox jumps over the lazy dog')
        [5, 5, 3, 5, 4, 4, 3]
    """
    return [len(word) for word in sentence.split() if word != "the"]



def vowels(word):
    """Vowels:

    Given a string representing a word, write a list comprehension that produces a list of all the vowels in that word.

        >>> vowels('mathematics')
        ['a', 'e', 'a', 'i']
    """
    vowel_set = {'a','e','i','o','u'}
    return [char for char in word if char in vowel_set]



def vowels_set(word):
    """Vowels set:

    Given a string representing a word, write a set comprehension that produces a set of all the vowels in that word.

        >>> vowels_set('mathematics')
        set(['a', 'i', 'e'])
    """
    vowel_set = {'a','e','i','o','u'}
    return {char for char in word if char in vowel_set}



def disemvowel(sentence):
    """Disemvowel:

    Given a sentence, return the sentence with all vowels removed.

        >>> disemvowel('the quick brown fox jumps over the lazy dog')
        'th qck brwn fx jmps vr th lzy dg'
    """
    vowel_set = {'a','e','i','o','u'}
    chars = [char for char in sentence if char not in vowel_set]
    return "".join(chars)



def wiggle_numbers(nums):
    """Wiggle numbers:

    Given a list of numbers, return the list with all even numbers doubled, and all odd numbers turned negative.

        >>> wiggle_numbers([72, 26, 79, 70, 20, 68, 43, -71, 71, -2])
        [144, 52, -79, 140, 40, 136, -43, 71, -71, -4]
    """
    return [num * 2 if num % 2 == 0 else num * -1 for num in nums]



def encrypt_lol(sentence):
    """Encrypt lol:

    Given a sentence, return the sentence with all its letter transposed by 1 in the alphabet, but only if the letter is a-y.

        >>> encrypt_lol('the quick brown fox jumps over the lazy dog')
        'uif rvjdl cspxo gpy kvnqt pwfs uif mbzz eph'
    """
    ascii_nums = range(97, 122)
    chars = [chr(ord(char) + 1) if ord(char) in ascii_nums else char for char in sentence]
    return "".join(chars)




# STOP HERE! You solved everything!
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print '\n*** ALL TESTS PASSED!\n'
