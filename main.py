from fastapi import FastAPI
from gpt_researcher import GPTResearcher

app = FastAPI()

@app.get("/report/{report_type}")
async def get_report(report_type: str, query: str):
    researcher = GPTResearcher(query, report_type)
    report = await researcher.run()
    return {"report": report}