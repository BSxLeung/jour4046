import requests
import os
import pandas as pd


class REST:

    # Constructor
    def __init__(self, action, link):
        self.action = action
        self.headers = {"Authorization": "Bearer keyuKJ1mneZ37iBCR"}
        self.link = link

# get Action
    def exec(self, dataset=None, record_id="1", params=None):
        self.dataset = dataset
        self.record_id = record_id
        if self.action == "retriveall":
            return self.retriveall(params)
        elif self.action == "retriveone":
            return self.retriveone(self.record_id)
        elif self.action == "update":
            return self.update(self.dataset)
        elif self.action == "delete":
            return self.delete(self.record_id)
        elif self.action == "add":
            return self.add(self.dataset)

        # not working
        # switcher = {
        #     "retriveall": self.retriveall(),
        #     "add": self.add(self.dataset),
        #     "update": self.update(self.dataset),
        #     "delete": self.delete(self.dataset, self.record_id),
        #     "retriveone": self.retriveone(self.record_id)

        # }
        # return switcher.get(self.action)

# Retrive All
    def retriveall(self, params):
        r = requests.get(
            self.link+"?sortField=_createdTime&sortDirection=desc", headers=self.headers, params=params)
        dict = r.json()
        dataset = []
        for i in dict['records']:
            dict = i['fields']
            dataset.append(dict)
        return dataset

# Retrive One
    def retriveone(self, record_id):
        link = self.link + "/" + self.record_id
        r = requests.get(link,
                         headers=self.headers)
        dict = r.json()["fields"]
        return dict

# Add
    def add(self, dataset):
        r = requests.post(self.link, json=dataset, headers=self.headers)
        message = 'Added Successfully!'
        return message

# Update
    def update(self, dataset):
        r = requests.put(self.link, json=dataset, headers=self.headers)
        print(r)
        message = 'Updated Successfully!'
        return message

# Delete
    def delete(self, record_id):
        r = requests.delete(self.link + "/" + record_id, headers=self.headers)
        message = 'Deleted Successfully!'
        return message
