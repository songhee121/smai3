from myllm.MyAPI import openAiModelArg, makeMsg


def test(prompt):
    modelName="gpt-4o"
    msg=makeMsg("반말로 대답해", prompt)
    result = openAiModelArg(modelName, msg)
    print(result)

if __name__ == '__main__':
    prompt="SK하이닉스에 대해서 알려줘"
    test(prompt)
