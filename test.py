import sys, json
import requests
import re


def format_dictionary(data):
    modified_data = {
        "id": data["id"],
        "job title": data["title"],
        "noc": "",
        "company": data["company"],
        "location": data["location"],
        "review rate": "",
        "link": data["company_url"],
        "job type": data["type"],
        "language": "",
        "salary estimate": "",
        "date posting": data["created_at"],
        "job posting website": "Github Jobs",
        "preferable work experience": "",
        "preferable educational background": "",
        "preferable programming language": "",
        "preferable certificate": "",
        "key qualifications": "",
        "key requirements": "",
        "number of views": "",
        "number of applications": ""
    }
    # print(modified_data)
    return modified_data


def write_json(modified_data):
    with open('github_jobs.json', 'w') as json_file:
        json.dump(modified_data, json_file)


def main():
    # url = "https://jobs.github.com/positions.json?description=python&full_time=true&location=sf"
    # url = "https://jobs.github.com/positions.json?utf8=%E2%9C%93&description=software+developer&location="
    modified_data_list = []
    i = 1
    j = 0
    while True:
        url = "https://jobs.github.com/positions.json?description=software+developer&location=&page=" + str(i)
        i = int(i) + 1
        #try:
        resp = requests.get(url)
        data = resp.json()
        for posting in data:
            j += 1
            modified_data_list.append(format_dictionary(posting))
            if posting == data[-1]:
                break
        if i == 3:
            break
        write_json(modified_data_list)


if __name__ == "__main__":
    main()
