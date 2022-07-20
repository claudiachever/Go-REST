import requests

class Rest:
base_url= 'https://gorest.co.in'
token= '95a03b743fd8b0968ccd1df6df1ae0d87bee1292c9fc91e917dd5b8669e4395e'


    def get(self, resource, **kwargs):
        headers = {}
        url = self.base_url + '/' + resource

        if self.token:
            headers['Authorization'] = 'Bearer ' + self.token

        if 'options' in kwargs.keys():
            options = kwargs['options']
            if options['query']:
                url += '?'
                for key in options['query'].keys():
                    if options['query'][key]:
                        url += f"{key}={options['query'][key]}&"

        response = requests.get(url, headers=headers)
        return response.json()


    def post(self, resource, data):
        headers = {}
        url = self.base_url + '/' + resource
        if self.token:
            headers['Authorization'] = 'Bearer ' + self.token
        print(f'POST - {url}')
        print(f"DATA - {data}")
        response = requests.post(url, data, headers=headers)
        if response.status_code < 300:
            response = response.json()
            for key in response.keys():
                print(f"{key}: {response[key]}")
        else:
            print(f'Got stats code: {response.status_code}')


    def patch(self, resource, target, data):
        headers = {}
        url = self.base_url + '/' + resource + '/' + str(target)
        if self.token:
            headers['Authorization'] = 'Bearer ' + self.token
        response = requests.patch(url, data, headers=headers)
        return response.json()
