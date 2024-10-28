import subprocess
import random
import string
import sys

def generate_random_input(length):
    """Generate a random string of specified length."""
    chars = string.ascii_letters + string.digits + string.punctuation + ' \n\t'
    return ''.join(random.choice(chars) for _ in range(length))

def fuzz(java_class, iterations=1000, max_input_length=100):
    """Fuzz the specified Java class.

    Args:
        java_class (str): Name of the compiled Java class.
        iterations (int): Number of fuzzing iterations.
        max_input_length (int): Maximum length of random input strings.
    """
    for i in range(iterations):
        # Generate random input
        input_length = random.randint(1, max_input_length)
        random_input = generate_random_input(input_length)
        print(f"Iteration {i+1}: Testing with input length {input_length}")

        try:
            # Run the Java program with the random input
            process = subprocess.Popen(
                ['java', java_class],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = process.communicate(input=random_input.encode(), timeout=5)

            # Check for exceptions or errors
            if process.returncode != 0 or stderr:
                print(f"Potential issue detected in iteration {i+1}!")
                print(f"Input: {repr(random_input)}")
                print(f"Return code: {process.returncode}")
                print(f"Standard Error: {stderr.decode()}")
                print('-' * 50)

        except subprocess.TimeoutExpired:
            process.kill()
            print(f"Timeout occurred in iteration {i+1}!")
            print(f"Input: {repr(random_input)}")
            print('-' * 50)

if __name__ == "__main__":
    # Replace 'YourJavaProgram' with your Java class name
    java_class_name = 'YourJavaProgram'
    fuzz(java_class_name)

