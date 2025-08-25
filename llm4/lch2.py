from langchain.model_laboratory import ModelLaboratory
from MyLCH import getOpenAI, getGenAI

if __name__ == '__main__':
    openllm = getOpenAI()
    genllm=getGenAI()

    model_lab = ModelLaboratory.from_llms([openllm, genllm])
    model_lab.compare('귀멸의 칼날:무한성 개봉날짜? 개봉한지 얼마나 지났어')