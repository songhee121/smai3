from myllm.MyAPI import makeMsg, openAiModel, openAiModelArg

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

if __name__ == '__main__':
    prompt="아주 이쁜 흰색 고양이 사진 만들어줘"
    test(prompt)