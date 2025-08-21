from myllm.MyAPI import geminiModel

def geminiTxt(txt):
    model = geminiModel()
    response = model.generate_content(txt)
    return(response.text)