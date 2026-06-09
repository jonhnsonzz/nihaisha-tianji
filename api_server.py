"""天纪API服务 — 端口8834"""
import subprocess, os, json
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="倪海厦天纪查询API")

class Query(BaseModel):
    keyword: str
    module: str = "all"  # tiandao, rendao, dimai, all
    top_k: int = 5

@app.post("/api/query")
def tianji_query(q: Query):
    kw = q.keyword.strip()
    if not kw:
        return {"code": 400, "message": "请输入关键词"}
    
    tianji_dir = os.path.expanduser("~/.hermes/skills/nihaisha-tianji/references")
    results = []
    
    if os.path.exists(tianji_dir):
        try:
            if q.module == "all":
                out = subprocess.run(["grep", "-ril", kw, tianji_dir], capture_output=True, text=True, timeout=15)
                matched = [f for f in out.stdout.strip().split("\n") if f.strip()][:q.top_k]
            else:
                fpath = os.path.join(tianji_dir, f"{q.module}.md")
                if os.path.exists(fpath):
                    out = subprocess.run(["grep", "-il", kw, fpath], capture_output=True, text=True, timeout=10)
                    matched = [fpath] if out.stdout.strip() else []
                else:
                    matched = []
            
            for fname in matched:
                basename = os.path.basename(fname).replace(".md", "")
                size = os.path.getsize(fname) if os.path.exists(fname) else 0
                try:
                    prev = subprocess.run(["grep", "-i", kw, fname], capture_output=True, text=True, timeout=5)
                    lines = [l.strip() for l in prev.stdout.split("\n") if l.strip()][:3]
                except:
                    lines = []
                results.append({"module": basename, "size_kb": round(size/1024, 1), "match_count": len(lines), "preview": lines})
        except Exception as e:
            return {"code": 500, "message": str(e)}
    
    return {
        "code": 0,
        "data": {
            "query": kw,
            "module": q.module,
            "total": len(results),
            "results": results
        },
        "disclaimer": "仅限传统文化学习用途"
    }

@app.get("/health")
def health():
    return {"status": "ok", "service": "nihaisha-tianji-api"}
