from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the jQuery UI droppable page
url = "https://www.jqueryui.com/droppable/"
driver.get(url)

# Switch to the iframe where the droppable elements are located
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'demo-frame'))

try:
    # Locate the draggable and droppable elements
    draggable = driver.find_element(By.ID, 'draggable')
    droppable = driver.find_element(By.ID, 'droppable')

    # Use ActionChains to perform drag and drop
    action_chains = ActionChains(driver)
    action_chains.drag_and_drop(draggable, droppable).perform()

    # Verify if the drop was successful
    drop_text = droppable.text
    assert drop_text == 'Dropped!', f"Actual drop text: {drop_text}"
    print("Drag and drop successful!")

finally:
    # Close the browser
    driver.quit()