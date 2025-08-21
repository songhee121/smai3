from myllm.MyAPI import geminiModel

def test(txt):
    model = geminiModel()

    response = model.generate_content(txt)
    return(response.text)

if __name__ == '__main__':
    while True:
        txt= input('질문을 입력하세요(나가기:q)')
        if txt=="q":
            print('종료합니다')
            break
        result=test(txt)
        print(result)