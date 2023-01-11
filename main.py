import requests
from bs4 import BeautifulSoup
import shutil
import cv2

image_urls = []
website_urls = ["https://cusat.ac.in/chem.php", "https://cusat.ac.in/biotech.php", "https://cusat.ac.in/maths.php",  #list of urls you need to take images from

                "https://cusat.ac.in/physics.php"
    ,

                "https://cusat.ac.in/stats.php"
    ,

                "https://cusat.ac.in/cis.php"
    ,

                "https://cusat.ac.in/sls.php"
    ,

                "https://cusat.ac.in/ciprs.php"
    ,

                "http://dpe.cusat.ac.in/"
    ,

                "http://welfarecusat.in/"
    ,

                "https://cusat.ac.in/tejas.php"
    ,

                "https://cusat.ac.in/acarr.php"
    ,

                "https://cusat.ac.in/cam.php"
    ,

                "https://cusat.ac.in/cirm.php"
    ,

                "https://cusat.ac.in/cns.php"
    ,

                "https://cusat.ac.in/c-sis.php"
    ,

                "https://cusat.ac.in/csseip.php"
    ,

                "https://cusat.ac.in/cittic.php"
    ,

                "https://cusat.ac.in/ncpor.php"
    ,

                "https://cusat.ac.in/ddukk.php"
    ,

                "https://cusat.ac.in/ciprs.php"
    ,

                "https://cusat.ac.in/iucnd.php"
    ,

                "https://cusat.ac.in/icrep.php"
    ,

                "https://cusat.ac.in/cbs.php"
    ,

                "https://cusat.ac.in/ncaah.php"
    ,

                "https://cusat.ac.in/stic.php"
    ,

                "https://cusat.ac.in/ugcsct.php"
    ,

                "https://cusat.ac.in/wsc.php"
                ]
count = 0
for i in range(28):
    response = requests.get(website_urls[i])
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find('body').find_all('img')

    # --- loop ---

    data = []
    i = 0

    for img in images:
        url = img.get('src')
        url = "https://cusat.ac.in/" + url     #as my src of images lack "http...." you can avoid this!

        if url:  # skip `url` with `None`
            try:
                response = requests.get(url, stream=True)
                i += 1
                url = url.rsplit('?', 1)[0]  # remove ?opt=20 after filename
                ext = url.rsplit('.', 1)[-1]  # .png, .jpg, .jpeg
                filename = f'{i}.{ext}'

                with open(filename, 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)

                image = cv2.imread(filename)
                height, width = image.shape[:2]

                data.append({
                    'url': url,
                    'path': filename,
                    'width': width,
                    'height': height,
                })

            except Exception as ex:
                print('Could not download: ', url)
                print('Exception:', ex)

        print('---')
    # --- after loop ---

    all_sorted = sorted(data, key=lambda x: x['width'], reverse=True)

    for item in all_sorted[:1]:
        print(count, 'first', item['width'], item['url'])
        count = count + 1
        image_urls.append(item['url'])

for i in range(28):
    print(image_urls[i])
