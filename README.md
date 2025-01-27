# Comwatt Python Client (Legacy)

## Overview

The Comwatt Python Client (Legacy) is a Python library that provides a convenient way to interact with the legacy Comwatt API (`go.comwatt.com/api`). It allows you to authenticate users, retrieve authenticated user information, and access owner, box, product, device, and statistical data.

Please note that this client is intended for devices below gen4 and uses the deprecated `go.comwatt.com`. If you're looking for the client compatible with gen4 devices and the `energy.comwatt.com`, please refer to the [python-comwatt-client](https://github.com/MateoGreil/python-comwatt-client).

## Features

The client currently supports the following methods:

- `authenticate(self, username, password)`: Authenticates a user with the provided username and password.
- `get_authenticated_user(self)`: Retrieves information about the authenticated user.
- `get_owner_details(self, owner_id)`: Retrieves information about the owner's details.
- `get_box_details(self, macAddress)`: Retrieves information about the box's details.
- `get_products(self)`: Retrieves information about the products.
- `get_devices(self, indepbox_id)`: Retrieves a list of devices for the specified box.
- `get_networkstats(self, indepbox_id, level="HOUR", measure_kind="QUANTITY", start=datetime.now(), end=datetime.now())`: Retrieves a list of network statistics for the specified box.
- `get_devices_stats(self, device_id, measure_kind="QUANTITY", measure_type_id="1", level="HOUR", start=datetime.now(), end=datetime.now())`: Retrieves a list of device statistics for the specified device.

## Installation

You can install the Comwatt Python Client (Legacy) using pip. Run the following command:

```
pip install comwatt-client-legacy
```

## Usage

Here's a simple example of how to use the Comwatt Python Client (Legacy):

```python
from comwatt.client import ComwattClient
from datetime import datetime, timedelta

# Create a Comwatt client instance
client = ComwattClient()

# Authenticate the user
client.authenticate('username', 'password')

# Get information about the authenticated user
user_info = client.get_authenticated_user()
print(user_info)

# Get owner details
owner_id = user_info['id']
owner_details = client.get_owner_details(owner_id)
print(owner_details)

# Get box details
macAddress = owner_details[0]['macAddress']
box_details = client.get_box_details(macAddress)
print(box_details)

# Get products
products = client.get_products()
print(products)

# Get devices for a specific box
indepbox_id = box_details['id']
devices = client.get_devices(indepbox_id)
print(devices)

# Get network statistics for a specific box
start_date = datetime.now() - timedelta(days=7)
end_date = datetime.now()
networkstats = client.get_networkstats(indepbox_id, start=start_date, end=end_date)
print(networkstats)

# Get device statistics for a specific device
device_id = devices[0]['id']
devices_stats = client.get_devices_stats(device_id, start=start_date, end=end_date)
print(devices_stats)
```

Make sure to replace `'username'` and `'password'` with the actual values for your Comwatt account.

## Contributing

Contributions to the Comwatt Python Client (Legacy) are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on the GitHub repository.
