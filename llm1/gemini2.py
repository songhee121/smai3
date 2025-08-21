from PIL import Image
from myllm.MyAPI import geminiModel

def test():
    img=Image.open("img/doyoungking.jpg")

    model = geminiModel()
    response = model.generate_content(["제시한 이미지의 남자 이름과 그에 대해 한국어로 설명해", img])
    print(response.text)

if __name__ == '__main__':
    test()