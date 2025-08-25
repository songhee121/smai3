from langchain.agents import load_tools, initialize_agent, AgentType
from MyLCH import getOpenAI, getGenAI

if __name__ == '__main__':
    openllm = getOpenAI()
    genllm=getGenAI()

    #chat Gpt에 질문, wikipedia 기반
    tools = load_tools(['wikipedia'], llm=openllm)

    agent = initialize_agent(
        tools,
        openllm,
        agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION, #위키피디아에 내 정보 저장하지 않음
        verbose = False #결과 화면에 출력
    )
    txt = '귀멸의 칼날:무한성 개봉날짜? 개봉한지 얼마나 지났어?'
    print(agent.run(txt))