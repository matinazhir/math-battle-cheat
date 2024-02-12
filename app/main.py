from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from sympy import *
import time
from link import game_link


# Specify the path to the Edge WebDriver executable
edge_driver_path = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'

# Set up Edge options
options = webdriver.EdgeOptions()
options.binary_location = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'  # Path to Edge browser executable

# Create a new Edge driver instance
driver = webdriver.Edge(options=options)

# Open the desired webpage
driver.get(game_link)

# Function to click on the "correct" button
def correct():
    driver.find_element(By.ID, "button_correct").click()

# Function to click on the "wrong" button
def wrong():
    driver.find_element(By.ID, "button_wrong").click()

# Dictionary mapping operators
operators = {'+': '+', '–': '-', '×': '*', '/': '/'}

driver.find_element(By.ID, "button_correct").click()

# Main loop to solve equations
while True:
    try:
        # Explicitly wait for the elements to be present
        wait = WebDriverWait(driver, 10)
        x_element = wait.until(EC.visibility_of_element_located((By.ID, "task_x")))
        task_op_element = wait.until(EC.visibility_of_element_located((By.ID, "task_op")))
        y_element = wait.until(EC.visibility_of_element_located((By.ID, "task_y")))
        eq_element = wait.until(EC.visibility_of_element_located((By.ID, "task_res")))
        
        # Extract values from the webpage
        x = x_element.text
        task_op = task_op_element.text
        y = y_element.text
        eq = eq_element.text
        
        # Check if any of the extracted values are empty
        if not all((x, task_op, y, eq)):
            time.sleep(5)
            print("Error: One or more values are empty")
            break
        
        # Construct the solution string
        op = operators.get(task_op)
        
        # Check if the operator is valid
        if op is None:
            print(f"Error: Operator '{task_op}' not found in operators dictionary")
            break
        
        solution = x + op + y
        
        # Evaluate the solution using Sympy and compare with expected result
        if sympify(solution) == int(eq):
            correct()  # Click on the "correct" button if the solution is correct
        else:
            wrong()    # Click on the "wrong" button if the solution is incorrect
    
    except TimeoutException:
        print("TimeoutException: Element not found within the specified time frame")
        break
