"""About: A program to find the value of a postfix expression. Variables are one or more
characters each. We might have some integer numbers as part of the expression.
Sample I/O:
    Enter a postfix expression with a $ at the end:
    20 jerry 45 + tom - * $
    Enter the value of jerry: 10
    Enter the value of tom: 5
    Expression's value is 1000
"""
word_container = []
stack = []

def main():
    expression = input("Enter a postfix expression with a $ at the end: \n   ")

    """ Separate each token by empty space into a list """
    word_container = expression.split(" ") 
    
    """ Convert and restore all word inputs into digits"""
    iterator = 0
    for word in word_container:

        """ if word is +, -, /, or * then ignore and don't replace"""
        if word.isdigit() or word == '+' or word == '-' or word == '*' or word == '/' or word == "$": 
            iterator += 1
            continue
        else:
            replacement = input('\t Enter the value of ' + word + ": ")
            word_container[iterator] = replacement
        iterator += 1
    
    """ Postfix Algebra """   
    total = 0
    for word in word_container:
        match word:
            case "+":
                total = int(stack[len(stack) - 2]) + int(stack[len(stack) - 1])
                for x in range(2):
                    stack.pop()
                stack.append(total)
                continue
            case "-":
                total = int(stack[len(stack) - 2]) - int(stack[len(stack) - 1])
                for x in range(2):
                    stack.pop()
                stack.append(total)
                continue
            case "*":

                total = int(stack[len(stack) - 2]) * int(stack[len(stack) - 1])
                for x in range(2):
                    stack.pop()
                stack.append(total)
                continue
            case "/":
                total = int(stack[len(stack) - 2]) / int(stack[len(stack) - 1])
                for x in range(2):
                    stack.pop()
                stack.append(total)
                continue
            case "$":
                break
            case default:
                stack.append(word)
    print("\t\t Expression's value is " + str(total))

if __name__ == '__main__':
    main()