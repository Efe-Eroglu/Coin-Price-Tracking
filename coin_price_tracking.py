from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pyautogui


def menu():

    print("Which currency chart you want to follow. Please copy and paste the url of the chart from tradingview.")
    chart_link=input()
    return chart_link


def main(link):

    option=input("Would you like to receive notifications via Whatsapp message? ? (y/n)\n")

    if option=="y":
        wp_driver=webdriver.Chrome(ChromeDriverManager().install())
        wp_driver.set_window_position(500, 10)
        wp_driver.get("https://web.whatsapp.com/")
        input("\n--* Select the person to be notified on WhatsApp and press enter to continue.. *--\n")
    
    elif option == "n":
        print("\nContinues without whatsapp notification.\n")
        
    else:
        print("\nAnswer only one letter (y/n).\n")


    driverOptions = webdriver.ChromeOptions()
    driverOptions.add_argument("--incognito")
    driverOptions.add_argument("--headless")

    driver = webdriver.Chrome(ChromeDriverManager().install(),options=driverOptions)
    driver.get(link)

    WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]")))

    coin_name=driver.find_element(By.XPATH,"/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/span[2]").text

    currency=driver.find_element(By.XPATH,"/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[2]/span[2]").text
    
    price_path="/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]"
    
    first_price=driver.find_element(By.XPATH,price_path).text
    


    while True:
        try:
            price_text=driver.find_element(By.XPATH,price_path).text
            print(coin_name+" =>",price_text,currency)
            
            if price_text>first_price:
                first_price=price_text
                print(f"Increase [{coin_name}] => {price_text} ")

                if option=="y":
                    wp_driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p").click()
                    pyautogui.typewrite(f"Increase [{coin_name}] => {price_text} ")
                    pyautogui.press("Enter")
                    
            sleep(5)

        except Exception:
            driver.quit()
            print("Something went wrong")

main(menu())
