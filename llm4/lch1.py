from langchain_core.prompts import PromptTemplate


def test(txt):
    template=f'{txt}를 홍보하기 위한 문구 만들어줘?'
    prompt=PromptTemplate(
        input_variables=['txt'],
        template= template
    )
    prompt.format(txt=txt)

if __name__ == '__main__':
    test('카메라')