import httpx
import csv
from rich import print
from dotenv import load_dotenv
import json
import os

# Load environment variables
load_dotenv()

# Set API key
api_key = os.getenv("API_KEY")

# Set the headers
hs_headers = {
    "Authourization": f"Bearer {api_key}"
}

# Create a class that will have the methods to add and remove devices
class AddRemoveDevice:

    # method to call an api with a GET, POST, PATCH, or DELETE
    def _call_api(self, method, url, header, payload=None):
        allowed_methods = ["GET", "POST", "PATCH", "DELETE"]

        if method not in allowed_methods:
            raise ValueError(f"Invalid method {method} passed to call_api")
        else:
            response = httpx.request(method=method, url=url, data=payload)
            return response
    
    # method to add a device
    def add_devices(self, team_id, payload):
        url = f'https://{api_key}@api-dev.headspin.io/v0/team/{team_id}/devices/add'

        response = self._call_api("PATCH", url, hs_headers, payload)
        if response.status_code == 200:
            print("[green]Device added successfully[/green]")
            return response
        else:
            print("[red]Failed to add device[/red]")
            print(response.url)
            print(response.text)

    # method to remove a device
    def remove_devices(self, team_id, payload):
        url = f'https://{api_key}@api-dev.headspin.io/v0/team/{team_id}/devices/remove'

        response = self._call_api("DELETE", url, hs_headers, payload)
        if response.status_code == 200:
            print("[green]Device removed successfully[/green]")
            return response
        else:
            print("[red]Failed to remove device[/red]")
            print(response.url)
            print(response.text)

    def process_csv(self, csv_file):
        result = []
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            udid_dict = {}
            for row in reader:
                udid = row['team_id']
                device_address = row['device_address']
                if udid not in udid_dict:
                    udid_dict[udid] = {'device_addresses': []}
                udid_dict[udid]['device_addresses'].append(device_address)
            result = [{'UDID': udid, 'data': data} for udid, data in udid_dict.items()]
        return result


# Create main function
def main():
    # process remove list
    remove_list = AddRemoveDevice().process_csv('sample_remove_list.csv')
    print(remove_list)
    # process add list
    add_list = AddRemoveDevice().process_csv('sample_add_list.csv')
    print(add_list)

    # remove devices
    for remove in remove_list:
        team_id = remove['UDID']
        device_addresses = remove['data']
        data = json.dumps(device_addresses)
        removed = AddRemoveDevice().remove_devices(team_id, data)
        print(removed.json())

    # add devices
    for add in add_list:
        team_id = add['UDID']
        device_addresses = add['data']
        data = json.dumps(device_addresses)
        added = AddRemoveDevice().add_devices(team_id, data)
        print(added.json())


if __name__ == "__main__":
    main()
