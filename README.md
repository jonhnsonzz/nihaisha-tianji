# 🌌 倪海厦天纪 · 命理风水知识系统

<div align="center">

**Ni Haixia Tianji — I-Ching, Ziwei Doushu & Feng Shui Knowledge System**

[![GitHub stars](https://img.shields.io/github/stars/jonhnsonzz/nihaisha-tianji?style=flat-square)](https://github.com/jonhnsonzz/nihaisha-tianji)
[![License](https://img.shields.io/badge/License-Educational-blue?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-green?style=flat-square)](api_server.py)
[![MCP Server](https://img.shields.io/badge/MCP-Server-purple?style=flat-square)](mcp.json)

> 基于倪海厦天纪24课完整转录，涵盖**天道（紫微斗数）· 人道（64卦）· 地道（阳宅风水）** 三大系统。
> **天纪 = 命相卜** — 10个引用文件 + 527张截图证据。

[中文](#) | [English](#)

</div>

---

## 🌟 Features

- **🌸 天道（紫微斗数）** — 命盘十二宫、星辰、四化、大限，含全文原文（68KB）
- **📜 人道（64卦）** — 易经64卦处世哲学详解，含可打印全文（315KB）
- **🏠 地道（阳宅风水）** — 阳宅64局、地脉方位
- **🖼️ 527张截图证据** — 板书/命盘/风水图精确定位到课次
- **🔄 天纪-人纪联动** — 命宫→脏腑、星性→体质、化忌→养生（配合人纪项目）
- **🔥 天纪↔人纪关联图谱** — 完整的十二宫→脏腑、主星→体质对照表

## 📦 What's Inside

### 三才系统

| 系统 | 内容 | 文件 | 大小 |
|:----|:----|:----|:----:|
| **天道** | 紫微斗数命盘、十四主星、四化、十二宫 | `tiandao.md` + `tiandao-original.md` | 78KB |
| **人道** | 64卦处世哲学、易经智慧 | `rendao.md` + `rendao-64gua.md` + `rendao-print.md` | 350KB |
| **地道** | 阳宅风水64局、地脉剖析 | `dimai.md` + `dimai-print.md` | 10KB |

### 目录结构

```
nihaisha-tianji/
├── SKILL.md                  # Hermes Agent Skill
├── mcp.json                  # MCP Server 配置
├── api_server.py             # REST API 服务
├── references/               # 📚 知识库（10文件，653KB）
│   ├── index.md              # 三才系统导航
│   ├── tiandao.md            # 天道：紫微斗数
│   ├── tiandao-original.md   # 天道全文原文
│   ├── rendao.md             # 人道：64卦
│   ├── rendao-64gua.md       # 64卦详解
│   ├── rendao-print.md       # 人道可打印全文
│   ├── dimai.md              # 地道：阳宅风水
│   ├── dimai-print.md        # 地脉打印版
│   ├── study-notes.md        # 学习笔记+527张截图索引
│   └── tianji-renji-link.md  # 🔄 天纪-人纪关联图谱
├── compiled/                 # 古文编译解读
│   ├── 64卦图解古文编译与专家解读.md
│   ├── 天机道古文编译与专家解读.md
│   ├── 人间道古文编译与专家解读.md
│   └── 地脉道古文编译与专家解读.md
├── README.md                 # 本文档
└── README_CN.md              # 中文版
```

## 🚀 Quick Start

### Option 1: REST API

```bash
pip install fastapi uvicorn
cd nihaisha-tianji
python3 -m uvicorn api_server:app --host 0.0.0.0 --port 8834
```

查询示例：
```bash
curl -X POST http://localhost:8834/api/query \
  -H "Content-Type: application/json" \
  -d '{"keyword":"紫微","module":"all","top_k":3}'
```

**示例输出：**
```json
{
  "code": 0,
  "data": {
    "query": "紫微",
    "total": 2,
    "results": [
      {"module": "index", "size_kb": 3.2, "match_count": 3, "preview": [...]},
      {"module": "tiandao", "size_kb": 10.1, "match_count": 5, "preview": [...]}
    ]
  }
}
```

### Option 2: MCP Server

```json
{
  "mcpServers": {
    "nihaisha-tianji": {
      "command": "python3",
      "args": ["/path/to/nihaisha-tianji/api_server.py"],
      "env": {"PORT": "8834"}
    }
  }
}
```

调用方式：
```
query_tianji(keyword="乾卦", module="rendao", top_k=5)
```

### Option 3: Hermes Skill

```bash
cp -r nihaisha-tianji ~/.hermes/skills/nihaisha-tianji
```

## 🔗 Tianji ↔ Renji Connection

本系统与 [nihaisha-renji](https://github.com/jonhnsonzz/nihaisha-renji)（人纪·中医辨证系统）共享关联知识图谱：

| Tianji → | Renji → | Application |
|----------|---------|-------------|
| Ming Palace Stars | Constitutional tendency | Disease predisposition |
| Health Palace | Corresponding organ diseases | Diagnosis reference |
| Transformation Taboos | Weak organ systems | Health maintenance direction |
| Yin-Yang / Five Elements | Eight-Principle pattern ID | Philosophical foundation |

See `references/tianji-renji-link.md` for the complete mapping.

## ⚠️ Safety Notice

> This system is an **educational tool** for studying Chinese metaphysics. All outputs are based on course materials.
> **Does NOT constitute fortune-telling, professional divination, or decision-making advice.**

## 📊 Project Stats

- **引用文件**: 10个
- **总大小**: 653 KB
- **课程数量**: 24课
- **截图证据**: 527张
| **API价格**: 开放平台定价
- **代码语言**: Python 3.8+

## 🤝 Contributing

PRs and Issues are welcome!

## 📄 License

Educational use only. Content copyright belongs to the original course materials.

## 📬 Related Projects

- [nihaisha-renji](https://github.com/jonhnsonzz/nihaisha-renji) — Ni Haixia Renji: TCM Diagnosis Knowledge System
