def is_palindrome(teststr):
    # Your code goes here.
    #print("Input String for Palindrome check: ", teststr)

    #listing characters to remove
    removechars = '!?.,"\' '
    remchars = teststr.maketrans('','',removechars)

    # removecase and remove special character in forward
    forstr =  teststr.casefold().translate(remchars)
    #print("Corrected Input string : ", forstr)

    # reverse string, removecase and remove special character in reverse
    revinput = teststr[::-1]
    revstr = revinput.casefold().translate(remchars)
    #print("Reverse string : ", revstr)

    print("Input: ", teststr)

    #compare forward and reverse string and return true if same else false.
    if forstr == revstr:
        print("Result: ","True")
        return True

    print("Result: ","False")
    return False

total = 0
test_words = ["Hello World!","Radar","Mama?","Madam, I'm Adam.","Race car!"]
for word in test_words:
    total += is_palindrome(word)

