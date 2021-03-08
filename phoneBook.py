import os
import json


class PhoneBook:
    def __init__(self, name=None, number=None):
        self.name = name
        self.number = number
        self.storage_file = "phoneNumber.json"
        self.save_new_number = {
            "name": name,
            "PhoneNumber": number
        }

    def save_number_to_json(self):
        try:
            if os.path.exists(self.storage_file):
                # if the file exists, then first load the json data into
                # a dictionary, make  and then append whatever you have to append and then dump it again to json
                with open(self.storage_file, "r") as file:
                    try:
                        phone_book = json.load(file)
                    except Exception as e:
                        print("Error!! Got %s on json.load()" % e)

                # Check if the data is of type dict, if so then convert it into a list to enable an append to it
                if type(phone_book) is dict:
                    phone_book = [phone_book]

                phone_book.append(self.save_new_number)
                with open(self.storage_file, "w") as file1:
                    json.dump(phone_book, file1, indent=4)
                    print("Contact saved!!")

            else:
                with open(self.storage_file, "w") as file2:
                    json.dump(self.save_new_number, file2, indent=4)
                    print("Contact saved!!")

        except Exception as e1:
            print("Error!! Got %s as error" % e1)

    def delete_number_from_phone_book(self):
        # This operation is only possible when the file exists in the path given
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "r") as file3:
                data = json.load(file3)

            # Check for the type of the loaded data
            if type(data) is dict:
                data = [data]

            for i in data:
                if i["name"] == self.name or i["PhoneNumber"] == self.number:
                    get_index = data.index(i)
                    data.pop(get_index)
                    print("Contact Deleted!!")
            else:
                print("It doesn't exist")

            # update the information after deleting the contact
            with open(self.storage_file, "w") as file31:
                try:
                    json.dump(data, file31, indent=4)

                except Exception as e:
                    print("Error!! occurred")
        else:
            print("Sorry!! The phoneBook is empty")

    def updating_the_given_number(self, new_name=None, new_number=None):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "r") as file4:
                database = json.load(file4)

            if type(database) is dict:
                database = [database]

            if new_name is None and new_number is not None:
                for i in database:
                    if i["name"] == self.name or i["PhoneNumber"] == self.number:
                        i["PhoneNumber"] = new_number
                        print("Contact updated")
                else:
                    pass
            elif new_name is not None and new_number is not None:
                for i in database:
                    if i["name"] == self.name or i["PhoneNumber"] == self.number:
                        i["name"] = new_name
                        i["PhoneNumber"] = new_number
                        print("Contacted updated")
                else:
                    pass
            # If both are None then we have nothing to change or update
            elif new_name is None and new_number is None:
                pass

        else:
            print("File doesn't exist")