import urllib
from bs4 import BeautifulSoup
import time

# start url.organization page
base_url = "https://github.com/orgs/alibaba/people?page="


def check_end(content):
    return b"no public members" in content


def extract_person_url(content):
    soup = BeautifulSoup(content, 'html.parser')
    urls = list(map(lambda x: "https://github.com" + x["href"], soup.select("a.css-truncate-target.f4")))
    return urls


def extract_email(url):
    try:
        u = urllib.request.URLopener()
        u.addheader('Cookie','')
        content = u.open(url).read()
        soup = BeautifulSoup(content, 'html.parser')
        v = soup.select("a.u-email")
        email = None
        if len(v) > 0:
            email = v[0].text
        return email
    except Exception as e:
        print("error ")
        print(e)
        return None


def main():
    user_list = []
    for i in range(1,100):
        print("page " + str(i))
        content = urllib.request.urlopen(base_url + str(i)).read()
        if check_end(content):
            break
            user_list += extract_person_url(content)
    print(user_list)
    for i in user_list:
        email = extract_email(i)
        if email is not None:
            print(email)
        time.sleep(1)


if __name__ == '__main__':
    main()


