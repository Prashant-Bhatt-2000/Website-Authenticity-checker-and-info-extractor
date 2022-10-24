import requests


def check_url_authenticity(): 
    global url
    url = 'https://www.youtube.com/robots.txt'
    try:
        global request_url 
        request_url = requests.get(url)
        if request_url.status_code == 200:
            print("Url is authenticated")
            print(request_url.status_code)
    except:
        print("url not found")

def retrive_data():
       check_url_authenticity()
       try: 
        if request_url.status_code == 200: 
            print("ok")
            data_file = 'file.md'
            with open(data_file, 'wb') as retrive:
                retrive.write(request_url.content)

       except:
        print("| ======================================================================= |")
        print("   Data cannot be retrive. File not found / website not authenticated")
        print("| ======================================================================= |")

retrive_data()