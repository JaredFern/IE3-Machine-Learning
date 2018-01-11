import rescrape
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("http://allrecipes.com/recipes/276/desserts/cakes/?page=3#2")
assert "Cake" in driver.title
elems = driver.find_elements_by_class_name("fixed-recipe-card")
ii = 0

while ii <=2:
    for recipe in elems:
        a_tag = recipe.find_element_by_tag_name("a")
        link = a_tag.get_attribute("href")
        s = rescrape.site.AllRecipesCom(link)
        s.write("~/Recipes/")
        ii += 1

driver.close()