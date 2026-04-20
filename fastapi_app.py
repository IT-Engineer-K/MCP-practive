from fastapi import FastAPI
app = FastAPI()

academic_background = [
    {
        "学校名": "ホーチミン日本人学校",
        "入学年": 2013,
        "卒業年": 2015,
    },
    {
        "学校名": "三鷹中央学園三鷹市立第三小学校",
        "入学年": 2015,
        "卒業年": 2017,
    },
    {
        "学校名": "小金井市立小金井第一中学校",
        "入学年": 2017,
        "卒業年": 2020,
    },
    {
        "学校名": "武蔵野大学高等学校",
        "学部": "本科",
        "入学年": 2020,
        "卒業年": 2023,
    },
    {
        "学校名": "東京電機大学",
        
        "学部": "システムデザイン工学部情報",
        "学科": "情報システムデザイン学科",
        "入学年": 2023,
        "卒業年": 2027,
    }
]

@app.get("/get_name")
def read_name():
    return {"name": "船原滉樹"}

@app.get("/get_history")
def read_root():
    return {"history": academic_background}

@app.get("/get_history/{school_name}")
def read_school_history(school_name: str):
    for school in academic_background:
        if school["学校名"] == school_name:
            return {"school": school}
    return {"error": "School not found"}