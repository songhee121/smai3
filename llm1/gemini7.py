from io import BytesIO
import requests
from PIL import Image
from myllm.MyAPI import geminiModel

def test(prompt, img):
    model = geminiModel()
    response = model.generate_content([prompt, img])
    print(response.text)

    response = model.generate_content(prompt)
    print(response.text)

if __name__ == '__main__':
    image_url = "https://www.ccbk.co.kr/m/static/images/main/visual0.png"
    response_image = requests.get(image_url)
    img = Image.open(BytesIO(response_image.content))

    prompt="이 이미지의 성분을 알려줘"
    test(prompt, img)