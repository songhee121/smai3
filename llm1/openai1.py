from myllm.MyAPI import openAiModel, openAiModelArg, makeMsg



def test():
    model= openAiModel()
    response= openAiModelArg("gpt-4o",makeMsg("친구", "잠실 카페 프랜차이즈 빼고 추천"))
    print(response)

if __name__ == '__main__':
    test()