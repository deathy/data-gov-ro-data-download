import json
import requests
import os
import urllib
import requests.exceptions

download_folder = 'downloads/'


def main():
    packages = requests.get("http://data.gov.ro/api/3/action/package_list").json()
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    with open(download_folder + 'package_list.json', "w", encoding="utf8") as f:
        f.write(json.dumps(packages))
    print("Found " + str(len(packages['result'])) + " datasets")
    for package in packages['result']:
        print("Downloading dataset: " + package)
        package_folder = download_folder + package
        if not os.path.exists(package_folder):
            os.makedirs(package_folder)
        dataset = requests.get("http://data.gov.ro/api/3/action/package_show?id=" + package).json()
        package_desc_json_file = package_folder + "/" + "package_desc.json"
        if not os.path.exists(package_desc_json_file):
            with open(package_desc_json_file, "w", encoding="utf8") as f:
                f.write(json.dumps(dataset))
            if dataset['success']:
                for resource in dataset['result']['resources']:
                    try:
                        r = requests.get(resource['url'], stream=True)
                        with open(package_folder + "/" + os.path.basename(urllib.request.url2pathname(r.url)),
                                  'wb') as f:
                            for chunk in r.iter_content(chunk_size=1024 * 1024):
                                if chunk:
                                    f.write(chunk)
                                    f.flush()
                    except requests.exceptions.ConnectionError:
                        print("Error retrieving URL: " + resource['url'])
                    except OSError:
                        print("Error retrieving URL: " + resource['url'])
        else:
            print("Skipping already downloaded: " + package_desc_json_file)


if __name__ == '__main__':
    main()
