from selenium import webdriver                          # Loads Selenium WebDriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By             # Loads .BY
import time

URL = f"https://www.simplyrecipes.com/trinidadian-macaroni-pie-recipe-6830792"  # Macro holding scraping target URL
RECIPE_TITLE = "recipe-block__header_1-0"               # ElementID for name of dish on SimplyRecipes (SR) recipe page
RECIPE_INFO = "recipe-block__meta_1-0"                  # ElementID for prep time, cook time, combined time, and servings on SR recipe page
INGREDIENTS = "section--ingredients_1-0"                # ElementID for ingredient list on SR recipe page
METHOD = "section--instructions_1-0"                    # ElementID for cooking instructions on SR recipe page
PATH = "/usr/local/bin/chromedriver"                    # Filepath for Selenium Chromedriver
SPACER = f"\n\n ------------------------------- \n"     # Visual spacer for terminal output
END = f"\n\n --------------END--------------"           # Visual spacer for terminal output, notates end of program output

driver = webdriver.Chrome(PATH)                         # assigns Chromedriver

driver.get(URL)                                         # Passes URL to Chromedriver
recipe_title = driver.find_element(By.ID, RECIPE_TITLE)  # Retrieves name of dish from SR recipe page
recipe_info = driver.find_element(By.ID, RECIPE_INFO)    # Retrieves prep time, cook time, combined time, and servings from SR recipe page
ingredients = driver.find_element(By.ID, INGREDIENTS)    # Retrieves ingredient list from SR recipe page
method = driver.find_element(By.ID, METHOD)              # Retrieves cooking instructions from SR recipe page
print(recipe_title.text + SPACER)                       # Prints retrieved name of dish
print(recipe_info.text + SPACER)                        # Prints retrieved prep time, cook time, combined time, and servings
print(ingredients.text + SPACER)                        # Prints retrieved ingredient list
print(method.text + END)                                # Prints retrieved cooking instructions

driver.quit()                                           # Halts Chromedriver. Pretty self-explanatory
