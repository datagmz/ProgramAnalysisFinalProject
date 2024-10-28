import jpype
import jpype.imports
import random
import string
import sys

def generate_random_input(length):
    """Generate a random string of specified length."""
    chars = string.ascii_letters + string.digits + string.punctuation + ' \n\t'
    return ''.join(random.choice(chars) for _ in range(length))

def fuzz_java_function(java_class_path, java_class_name, java_method_name, iterations=1000, max_input_length=100):
    """Fuzz a specific Java method.

    Args:
        java_class_path (str): Path to the directory containing the Java class files.
        java_class_name (str): Name of the Java class containing the method.
        java_method_name (str): Name of the method to fuzz.
        iterations (int): Number of fuzzing iterations.
        max_input_length (int): Maximum length of random input strings.
    """
    # Start the JVM
    if not jpype.isJVMStarted():
        jpype.startJVM(classpath=[java_class_path])

    # Import the Java class
    JavaClass = jpype.JClass(java_class_name)

    for i in range(iterations):
        # Generate random input
        input_length = random.randint(1, max_input_length)
        random_input = generate_random_input(input_length)
        print(f"Iteration {i+1}: Testing with input length {input_length}")

        try:
            # Call the Java method with the random input
            java_instance = JavaClass()
            method = getattr(java_instance, java_method_name)
            result = method(random_input)
            # Optionally, you can print or log the result
            # print(f"Result: {result}")

        except Exception as e:
            print(f"Exception detected in iteration {i+1}!")
            print(f"Input: {repr(random_input)}")
            print(f"Exception: {e}")
            print('-' * 50)

    # Shutdown the JVM
    jpype.shutdownJVM()

if __name__ == "__main__":
    # Update these variables with your Java class information
    java_class_path = './'  # Directory containing your Java class files
    java_class_name = 'YourJavaClass'  # Replace with your Java class name
    java_method_name = 'yourMethod'  # Replace with the method you want to fuzz

    fuzz_java_function(java_class_path, java_class_name, java_method_name)

