import hashlib
import json
import requests
from datetime import datetime

class ComwattClient:
    """
    A client for interacting with the Comwatt API.

    Args:
        None

    Attributes:
        base_url (str): The base URL of the Comwatt API.
        session (requests.Session): The session object for making HTTP requests.

    """

    def __init__(self):
        self.base_url = 'https://go.comwatt.com/api'
        self.session = requests.Session()

    def authenticate(self, username, password):
        """
        Authenticates a user with the provided username and password.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            None

        Raises:
            Exception: If the authentication fails.

        """

        url = f'{self.base_url}/v1/authent'
        encoded_password = hashlib.sha256(f'jbjaonfusor_{password}_4acuttbuik9'.encode()).hexdigest()
        data = {'username': username, 'password': encoded_password}

        response = self.session.post(url, json=data)

        if response.status_code != 200:
            raise Exception(f'Authentication failed: {response.status_code}')

    def get_authenticated_user(self):
        """
        Retrieves information about the authenticated user.

        Args:
            None

        Returns:
            dict: Information about the authenticated user.

        Raises:
            Exception: If an error occurs while retrieving the information.

        """

        url = f'{self.base_url}/users/authenticated'

        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error retrieving authenticated user: {response.status_code}')

    def get_owner_details(self, owner_id):
        """
        Retrieves information about the owner's details.

        Args:
            owner_id (str): The ID of the owner.

        Returns:
            dict: Information about the authenticated owner.

        Raises:
            Exception: If an error occurs while retrieving the information.

        """

        url = f'{self.base_url}/api/indepboxes?ownerid={owner_id}'

        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error retrieving owner details : {response.status_code}')

    def get_box_details(self, box_id):
        """
        Retrieves information about the box's details.

        Args:
            box_id (str): The ID of the box.

        Returns:
            dict: Information about the box.

        Raises:
            Exception: If an error occurs while retrieving the information.

        """

        url = f'{self.base_url}/api/indepboxes/byMacAddress/{box_id}'

        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error retrieving box details : {response.status_code}')

    def get_products(self):
        """
        Retrieves information about the box's details.

        Args:
            none

        Returns:
            dict: Information about the authenticated user.

        Raises:
            Exception: If an error occurs while retrieving the information.

        """

        url = f'{self.base_url}/api/products/1'

        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error retrieving products : {response.status_code}')

    def get_devices(self, indepbox_id):
        """
        Retrieves a list of devices for the specified box.

        Args:
            indepbox_id (str): The ID of the box.

        Returns:
            list: A list of devices.

        Raises:
            Exception: If an error occurs while retrieving the devices.

        """

        url = f'{self.base_url}/api/devices?indepbox_id={indepbox_id}'

        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error retrieving devices: {response.status_code}')

    def get_networkstats(self, indepbox_id,
                         level="HOUR",
                         measure_kind="QUANTITY",
                         start=datetime.now(),
                         end=datetime.now()):
        """
        Retrieves a list of networkstat for the specified box.

        Args:
            level (str): The level of the networkstat ("HOUR","DAY","MONTH","YEAR","LAST_24_HOURS").
            measure_kind (str): The kind of measure of the networkstat ("FLOW","STATE","QUANTITY","VIRTUAL_QUANTITY").
            indepbox_id (str): The ID of the networkstat.
            start (datetime): The start datetime of the network
            end (datetime): The end datetime of the network

        Returns:
            list: A list of networkstat (real).
            {
                "productionFlow": 0000.000000,
                "consumptionFlow": 0000.000000,
                "networkOutput": 0000.000000,
                "networkInput": 0000.000000,
                "autonomyRate": 0000.000000,
                "autoconsumptionRate": 0000.000000,
                "networkOutputRate": 0000.000000,
                "networkInputRate": 0000.000000
            }

        Raises:
            Exception: If an error occurs while retrieving the networkstat.

        """

        url = (f'{self.base_url}/api/aggregations/networkstats?indepbox_id={indepbox_id}&'
               f'level={level}&'
               f'measure_kind={measure_kind}&'
               f'start={start}&'
               f'end={end}&'
               f'mm=')

        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error retrieving networkstats: {response.status_code}')

    def get_devices_stats(self, device_id,
                          measure_kind="VIRTUAL_QUANTITY",
                          measure_type_id="1",
                          level="HOUR",
                          start=datetime.now(),
                          end=datetime.now()):

        """
        Retrieves a list of devices_stats for the specified device.

        Args:
            level (str): The level of the devices_stats ("HOUR","DAY","MONTH","YEAR","LAST_24_HOURS").
            measure_kind (str): The kind of measure of the devices_stats ("FLOW","STATE","QUANTITY","VIRTUAL_QUANTITY").
            measure_type_id (int): The type of measure of the devices_stats
            device_id (str): The ID of the device.
            start (datetime): The start datetime of the devices_stats.
            end (datetime): The end datetime of the devices_stats.
        Returns:
            list: A list of devices_stats (real).


        Raises:
            Exception: If an error occurs while retrieving the devices_stats.
        """

        url = (f'{self.base_url}/api/aggregations/raw?device_id={device_id}&'
               f'level={level}&'
               f'measure_kind={measure_kind}&'
               f'start={start}&'
               f'end={end}&'
               f'measure_type_id={measure_type_id}&'
               f'mm=')

        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error retrieving devices_stats: {response.status_code}')
