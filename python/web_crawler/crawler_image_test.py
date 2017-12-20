# crawler picture with pretending browser
import urllib.request, socket, re, sys, os

# save file path
target_path = ".\\crawler_images_douban"  #target_path = ".\\crawler_images_csdn"
# target url that needs to crawler
target_url = "https://www.douban.com/" #target_url = "http://www.csdn.net/"
req_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'
}

def get_file_local_path(file_path):
    file_name = os.path.split(file_path)[1]
    return os.path.join(target_path, file_name)

def start_crawler():
    #create dir if not exist
    if not os.path.isdir(target_path):
        os.mkdir(target_path)

    req = urllib.request.Request(url = target_url, headers = req_headers)
    res = urllib.request.urlopen(req)
    data = res.read()

    for link, t in set(re.findall(r'(https:[\S]*?(jpg|png|gif))', str(data))):
        print(link)
        try:
            urllib.request.urlretrieve(link, get_file_local_path(link))
        except:
            print('crawler failed')

# start to crawler
if __name__ == '__main__':
    start_crawler()
    #urllib.request.urlretrieve('http://www.getuikit.net/docs/images/bg_teaser.svg', 'test.svg')