import urllib

from myllm.MyAPI import openAiModel

def test(prompt):
    openModel = openAiModel()
    response = openModel.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    ) #이미지를 주는게 아니라 url정보
    image_url = response.data[0].url
    print(image_url)
    imgName="img/whitecat.png"
    urllib.request.urlretrieve(image_url, imgName)

if __name__ == '__main__':
    prompt="이쁜 흰색 샴 고양이 사진 만들어줘"
    test(prompt)