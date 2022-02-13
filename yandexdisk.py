import requests
from pprint import pprint    


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_upload_link(self, path_to_file):
        '''запросить место для загрузки файла на яндекс диск'''
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-Type': 'application/json', 
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {"path": path_to_file, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        # pprint(response.json())
        return response.json()

    def upload(self, path_to_file, filename):
        '''загрузка файлана яндекс диск'''
        link_dict = self._get_upload_link(path_to_file=path_to_file)
        href = link_dict.get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")    

if __name__ == '__main__':
    path_to_file = "txt.txt" ,"txt2.txt"
    token = "..."
    uploader = YaUploader(token)
    for file in path_to_file:
        result = uploader.upload("Загрузки/" + file, file)
pprint(result)