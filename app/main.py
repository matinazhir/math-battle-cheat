from selenium import webdriver
from selenium.webdriver.common.by import By
from sympy import *
import time

# Import values from links module
from links import game_link, browser_directory, your_score

# Specify the path to the Edge WebDriver executable
edge_driver_path = browser_directory

# Set up Edge options
options = webdriver.EdgeOptions()
options.binary_location = browser_directory  # Path to Edge browser executable

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

# Start the game
driver.find_element(By.ID, "button_correct").click()

# Main loop to solve equations
while True:
    try:
        # Check if the game is running or not
        game_is_run = driver.find_elements(By.CLASS_NAME, "page_wrap in_game")

        # Extract values from the webpage
        x = driver.find_element(By.ID, "task_x").text
        task_op = driver.find_element(By.ID, "task_op").text
        y = driver.find_element(By.ID, "task_y").text
        eq = driver.find_element(By.ID, "task_res").text
        score = driver.find_element(By.ID, "score_value").text

        # Construct the solution string
        op = operators.get(task_op)
        solution = x + op + y

        # Check the score value and perform actions accordingly
        if score != your_score:
            # Click on the "correct" answer if the solution is correct
            if sympify(solution) == int(eq):
                correct()
            else:
                wrong()
        else:
            # Click on the "wrong" answer to exit
            if sympify(solution) == int(eq):
                wrong()
            else:
                correct()
    except (SyntaxError, TypeError, ValueError):
        time.sleep(3)
        print("\nThe Game is Over!")
        break

# Close the WebDriver
driver.quit()
