import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

username = "sumitpsr1"
access_key = "BrXSnGz3MGQwW8KSdABCbursKmdAURzPuiJ54kRsLvvqFCod9B"  


class FirstSampleTest(unittest.TestCase):
    # driver = webdriver.Chrome()
    # Generate capabilites from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case and
    def setUp(self):
        # capabilities =
        #     # options = Options()
        #     options.browser_version = "86.0"
        #     options.platform_name = "Windows 10"
        #     lt_options = {};
        #     lt_options["browserName"]: "Chrome",
        #     lt_options["username"] = "sumitpsr1";
        #     lt_options["accessKey"] = "BrXSnGz3MGQwW8KSdABCbursKmdAURzPuiJ54kRsLvvqFCod9B";
        #     lt_options["visual"] = True;
        #     lt_options["video"] = True;
        #     lt_options["network"] = True;
        #     lt_options["project"] = "Automation-LT";
        #     lt_options["name"] = "LambdaTest";
        #     lt_options['build'] = "v1.0";
        #     lt_options["w3c"] = True;
        #     lt_options["plugin"] = "python-python";
        #     options.set_capability('LT:Options', lt_options);
        #     },
        #     {
        options = Options()
        options.browser_version = "87.0"
        options.platform_name = "macOS Sierra"
        lt_options = {};
        # lt_options["browserName"]: "MS Edge",
        lt_options["username"] = "sumitpsr1";
        lt_options["accessKey"] = "BrXSnGz3MGQwW8KSdABCbursKmdAURzPuiJ54kRsLvvqFCod9B";
        lt_options["visual"] = True;
        lt_options["video"] = True;
        lt_options["network"] = True;
        lt_options["project"] = "Automation-LT";
        lt_options["name"] = "LambdaTest";
        lt_options['build'] = "v1.0";
        lt_options["w3c"] = True;
        lt_options["plugin"] = "python-python";
        lt_options["platformName"] = "macOS Sierra";
        lt_options["browserName"] = "Microsoft Edge";
        options.set_capability('LT:Options', lt_options);
        
        #     }
        # ]

        # desired_caps = {
        #     'LT:Options': {
        #         # "build": "Python Demo",  # Change your build name here
        #         "name": "LambdaTest",  # Change your test name here
        #         "platformName": "Windows 10",
        #         "selenium_version": "4.0.0",
        #         "console": 'true',  # Enable or disable console logs
        #         "network": 'true',  # Enable or disable network logs
        #         "plugin": "python-pytest",
        #         "tunnel": True
        #         #Enable Smart UI Project
        #         #"smartUI.project": "<Project Name>"
        #     },
        #     "browserName": "Chrome",
        #     "browserVersion": "86",
        # }

        # Steps to run Smart UI project (https://beta-smartui.lambdatest.com/)
        # Step - 1 : Change the hub URL to @beta-smartui-hub.lambdatest.com/wd/hub
        # Step - 2 : Add "smartUI.project": "<Project Name>" as a capability above
        # Step - 3 : Run "driver.execute_script("smartui.takeScreenshot")" command wherever you need to take a screenshot 
        # Note: for additional capabilities navigate to https://www.lambdatest.com/support/docs/test-settings-options/
        self.driver = webdriver.Remote(
            command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key),
            options=options)

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

    # """ You can write the test cases here """
    def test_demo_site(self):

        # try:
        driver = self.driver
        driver.implicitly_wait(20)
        # driver.set_page_load_timeout(30)
        driver.maximize_window()

        # Url
        # print('Loading URL')
        driver.get("https://www.lambdatest.com")
        element = driver.find_element(By.XPATH, "(//a[text()='See All Integrations'])")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2.5)
        link = element.get_attribute('href')
        # print(link)

        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(link)
        print(driver.window_handles[1])

        title = driver.current_url
        assert title == 'https://www.lambdatest.com/integrations'
        driver.close()

        # # Let's click on a element
        # driver.find_element(By.NAME, "li1").click()
        # location = driver.find_element(By.NAME, "li2")
        # location.click()
        # print("Clicked on the second element")

        #Take Smart UI screenshot
        #driver.execute_script("smartui.takeScreenshot")

        # Let's add a checkbox
        # driver.find_element(By.ID, "sampletodotext").send_keys("LambdaTest")
        # add_button = driver.find_element(By.ID, "addbutton")
        # add_button.click()
        # print("Added LambdaTest checkbox")

        # # print the heading
        # search = driver.find_element(By.CSS_SELECTOR, ".container h2")
        # assert search.is_displayed(), "heading is not displayed"
        # print(search.text)
        # search.click()
        # driver.implicitly_wait(3)

        # # Let's download the invoice
        # heading = driver.find_element(By.CSS_SELECTOR, ".container h2")
        # if heading.is_displayed():
        #     heading.click()
        #     driver.execute_script("lambda-status=passed")
        #     print("Tests are run successfully!")
        # else:
        #     driver.execute_script("lambda-status=failed")


if __name__ == "__main__":
    unittest.main()