import yaml
import requests


class LoadTestRules:
    @staticmethod
    def return_rules():
        with open(r'test_case.yml') as file_:
            test_case = yaml.load(file_, Loader=yaml.FullLoader)
            return test_case


def test_custom_api():
    rules = LoadTestRules.return_rules()
    for k, v in rules.items():
        print(f"⚙️ Executing : {k}")
        method = v.get('method')
        url = v.get('url')
        print(f"Test case :{k} -- {url} -- {method}")
        if method == 'GET':
            # Todo
            result = requests.get(url)
            assert v.get('status_code') == result.status_code, f"Status of Test Case➡️{k} = Failed"
            print(f"Status of Test Case➡️{k} = Passed")

        if method == 'POST':
            # Todo
            result = requests.post(url, data=v.get('payload'))
            assert v.get('status_code') == result.status_code, f"Status of Test Case➡️{k} = Failed"
            print(f"Status of Test Case➡️{k} = Passed")

        if method == 'DELETE':
            # Todo
            result = requests.delete(url)
            assert v.get('status_code') == result.status_code, f"Status of Test Case➡️{k} = Failed"
            print(f"Status of Test Case➡️{k} = Passed")


if __name__ == '__main__':
    test_rules = test_custom_api()

