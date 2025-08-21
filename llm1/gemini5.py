from myllm.MyAPI import geminiModel

def test(prompt):
    model = geminiModel()

    response = model.generate_content(prompt)
    print(response.text)

if __name__ == '__main__':
    question = input("질문하세요: ")

    prompt = f"'{question}'에 대해 설명해 줘."

    test(prompt)
