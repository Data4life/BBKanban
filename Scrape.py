from bs4 import BeautifulSoup as bs
import requests as r
import requests_html

def post_request(s, url, payload):
    try:
        request = s.post(url, data=payload)
        if(request.status_code == 200):
            return request
        else:
            print(r.status_codes)
    except Exception as e:
        print(e)

def get_request(s, url, addon):
    try:
        request = s.get(url + addon)
        if(request.status_code == 200):
            return request
        else:
            print(request.status_code)
    except Exception as e:
        print(e)

def main():
    print("Hello world")
    url = 'https://ttu.blackboard.com/webapps/'
    login_route = 'login/'
    courses_route = 'portal/execute/tabs/tabAction?tab_tab_group_id=_2_1'
    username = 'wyland.harris@ttu.edu' # <input id="userNameInput".....
    password = 'ytrewq123456YTREWQ' # <inpuit id="passwordInput"...
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'origin': 'https://fs.ttu.edu',
        'referer': 'https://fs.ttu.edu/adfs/ls/?wa=wsignin1.0&wtrealm=https://eraider.ttu.edu/&wctx=rm=0&id=passive&ru=%2fsignin.aspx%3fredirect%3dhttps%253A%252F%252Fwebapps.itsd.ttu.edu%252Fshim%252Fbblearn9%252Findex.php&wct=2023-03-04T20:32:29Z'
    }
    s = r.session()
    # token = s.get(url).cookies['MSISAuth']
    payload = {
        'UserName': username,
        'Password': password,
        'AuthMethod': 'FormsAuthentication',
    }

    login_req = s.post(url+login_route, headers=headers, data=payload)
    print(login_req)

    cookies = login_req.cookies

    courses_url = url+courses_route
    courses_page = s.get(courses_url, cookies=cookies, headers=headers)
    if (courses_page.status_code != 200):
        print('Bad request, recieved code:\n', courses_page.status_code)
        exit()
    
    print('Request is good')
    soup = bs(courses_page.content, 'lxml')
    courses = soup.find('ul', attrs={'class': 'portletList-img courseListing coursefakeclass '})



    # s = requests_html.HTMLSession()
    # s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    # s.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
    # s.headers['Accept-Language'] = 'en-US,en;q=0.9'
    # s.headers['Connection'] = 'keep-alive'
    # s.headers['Upgrade-Insecure-Requests'] = '1'



    # res = r.get(url)

    



    # homePage = bs(soup.content, 'lxml')
    # coursesLink = homePage.find_all('td')

    # res = get_request(s, url, courses)
    # soup = bs(res.content, 'lxml')

    temp = 1


if __name__ == '__main__':
    main()