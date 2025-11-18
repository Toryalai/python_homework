# Write your code here.

# Task 1: Hello
def hello():
    return "Hello!"

# Task 2: Greet with a Formatted String
def greet(name):
    return "Hello, " + name +"!"

# Task 3: Calculator
def calc(a, b, op="multiply"):
    try:
        match op:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return "Unknown operation!"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except Exception:
        return "You can't multiply those values!"

# Task 4: Data Type Conversion
def data_type_conversion(value, type_name):
    try:
        match type_name:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
            case _:
                return f"Unknown data type: {type_name}"
    except Exception:
        return f"You can't convert {value} into a {type_name}."

# Task 5: Grading System, Using *args
def grade(*args):
    try:
        avg = sum(args) / len(args)

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    except Exception:
        return "Invalid data was provided."

# Task 6: Use a For Loop with a Range
def repeat(text, count):
    result = ""
    for _ in range(count):
        result += text
    return result

# Task 7: Student Scores, Using **kwargs
def student_scores(mode, **kwargs):
    if mode == "mean":
        # Calculate average of all scores
        return sum(kwargs.values()) / len(kwargs)

    elif mode == "best":
        # Find student with highest score
        best_student = max(kwargs, key=kwargs.get)
        return best_student

    else:
        return "Invalid mode"

# Task 8: Titleize, with String and List Operations
def titleize(text):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    
    # Split it to words
    words = text.split()
    
    for i, word in enumerate(words):
        
        # capitalize first and last words
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        else:
            if word.lower() in little_words:
                words[i] = word.lower()
            else:
                words[i] = word.capitalize()

    return " ".join(words)

# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    result = ""
    for char in secret:
        if char in guess:
            result += char
        else:
            result += "_"
    return result

# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(text):
    vowels = "aeiou"
    
    def convert_word(word):
        # If the string starts with a vowel (aeiou)
        if word[0] in vowels:
            return word + "ay"
        
        # If the string starts with one or several consonants, they are moved to the end and "ay" is tacked on after them
        if word.startswith("qu"):
            return word[2:] + "quay"
        
        # "qu" is a special case, as both of them get moved to the end of the word, as if they were one consonant letter.
        index = 0
        while index < len(word) and word[index] not in vowels:

            if index + 1 < len(word) and word[index:index+2] == "qu":
                index += 2
                break
            index += 1
        
        return word[index:] + word[:index] + "ay"
    
    words = text.split()
    converted = [convert_word(word) for word in words]
    
    return " ".join(converted)
