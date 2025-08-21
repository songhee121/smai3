import urllib
from myllm.MyAPI import makeMsg, openAiModel, openAiModelArg

def test(prompt):
    openModel = openAiModel()
    response = openModel.images.edit(
        model="dall-e-2",
        prompt=prompt,
        size="1024x1024",
        n=1,
        image=open("img/sample.png", "rb"),#Read Binary
        mask=open("img/sample-mask.png","rb")
    ) #이미지를 주는게 아니라 url정보
    image_url = response.data[0].url
    print(image_url)
    urllib.request.urlretrieve(image_url, "img/sample2.png")

if __name__ == '__main__':
    prompt="나무를 넣어줘"
    test(prompt)