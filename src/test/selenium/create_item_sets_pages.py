import monolithic
import time
import unittest


class TestCreateItemSetsPage(monolithic.MonolithicTest):
    def step_01_go_to_the_create_item_sets_page(self):
        self.login()
        button = self.browser.find_element_by_xpath(
            "//a[.='Create Item Sets']")
        button.click()
        time.sleep(2)
        self.assertCurrentUrl(self.domain+'admin/lab/itemsets/create')

    def step_02_find_all_fields(self):
        self.currentUrl = self.domain+'admin/lab/itemsets/create'
        self.title = 'monitor'
        self.attribute = 'Color'
        self.value = 'Black'
        self.item_set_title = self.browser.find_element_by_name("title")
        self.attribute_name = self.browser.find_element_by_name(
            "attributes.0.key")
        self.attribute_value = self.browser.find_element_by_name(
            "attributes.0.defaultValue")
        self.createbutton = self.browser.find_element_by_xpath(
            "//button[.='Create Itemset']")

    def step_03_check_if_in_the_same_page_after_empty_button_click(self):
        self.createbutton.click()
        time.sleep(1)
        self.assertCurrentUrl(self.currentUrl)

    def step_04_fill_data(self):
        self.item_set_title.send_keys(self.title)
        self.attribute_name.send_keys(self.attribute)
        self.attribute_value.send_keys(self.value)

    def step_05_clear_data(self):
        self.clearInputField(self.item_set_title)
        self.clearInputField(self.attribute_name)
        self.clearInputField(self.attribute_value)

    def step_06_fill_only_itemset_title_and_submit(self):
        self.item_set_title.send_keys(self.title)
        self.createbutton.click()
        time.sleep(1)
        self.assertCurrentUrl(self.currentUrl)

    def step_07_fill_only_attribute_name_and_submit(self):
        self.clearInputField(self.item_set_title)
        self.attribute_name.send_keys(self.attribute)
        self.createbutton.click()
        time.sleep(1)
        self.assertCurrentUrl(self.currentUrl)

    def step_08_fill_only_attribute_value_and_submit(self):
        self.clearInputField(self.attribute_name)
        self.attribute_value.send_keys(self.value)
        self.createbutton.click()
        time.sleep(1)
        self.assertCurrentUrl(self.currentUrl)

    def step_09_create_itemset_success(self):
        self.clearInputField(self.attribute_value)
        self.item_set_title.send_keys(self.title)
        self.attribute_name.send_keys(self.attribute)
        self.attribute_value.send_keys(self.value)
        self.createbutton.click()                       # TODO :Check for not working
        time.sleep(2)
        element = self.browser.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/main/div[1]/div/div[2]/div/div/div/div/div/div[2]')
        expected = "Item set '"+self.title+"' was created successfully."
        self.assertElementText(expected, element)

    def step_10_go_to_view_itemsets_page(self):
        button = self.browser.find_element_by_xpath("//a[.='View Item Sets']")
        button.click()
        time.sleep(1)
        self.assertCurrentUrl(self.domain+'admin/itemset/list')

    def step_11_click_refresh_button_and_check_itemsets(self):
        refresh = self.browser.find_element_by_xpath(
            "//button[@title='Refresh Tokens List']")
        refresh.click()
        time.sleep(2)
        data = self.browser.find_elements_by_tag_name("td")
        self.assertIn(self.title, [each.text.lower() for each in data])

    def step_12_check_search_bar(self):
        self.search_input = self.browser.find_element_by_xpath(
            '//input[@placeholder="Search"]')
        self.search_input.send_keys(self.title)
        element = self.browser.find_element_by_xpath(
            "//td[.='Monitor']")
        self.assertEqual(element.text.lower(), self.title)
        time.sleep(1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
