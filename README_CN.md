# 🌌 倪海厦天纪 · 命理风水知识系统

<div align="center">

**基于倪海厦天纪24课完整转录 — 天道（紫微斗数）· 人道（64卦）· 地道（阳宅风水）**

[![GitHub stars](https://img.shields.io/github/stars/jonhnsonzz/nihaisha-tianji?style=flat-square)](https://github.com/jonhnsonzz/nihaisha-tianji)
[![License](https://img.shields.io/badge/License-Educational-blue?style=flat-square)](LICENSE)
[![MCP Server](https://img.shields.io/badge/MCP-Server-purple?style=flat-square)](mcp.json)

> **天纪 = 命相卜** — 10个引用文件 + 527张截图证据

[中文](#) | [English](README.md)

</div>

---

## 📖 三才系统

| 系统 | 内容 | 关键文件 |
|:----|:----|:--------|
| **🌸 天道** | 紫微斗数命盘、十四主星、四化、十二宫 | `tiandao.md` + `tiandao-original.md` |
| **📜 人道** | 64卦处世哲学、易经智慧 | `rendao.md` + `rendao-64gua.md` + 可打印全文 |
| **🏠 地道** | 阳宅风水64局、地脉剖析 | `dimai.md` + `dimai-print.md` |

## 🚀 快速开始

```bash
pip install fastapi uvicorn
cd nihaisha-tianji
python3 -m uvicorn api_server:app --host 0.0.0.0 --port 8834

# 查询示例
curl -X POST http://localhost:8834/api/query \
  -H "Content-Type: application/json" \
  -d '{"keyword":"紫微","module":"all","top_k":3}'
```

## 🔗 天纪↔人纪联动

与 [人纪项目](https://github.com/jonhnsonzz/nihaisha-renji) 联动分析：

| 天纪 → | 人纪 → | 应用 |
|:-------|:-------|:-----|
| 命宫星辰 | 先天体质倾向 | 易患疾病类型 |
| 疾厄宫 | 对应脏腑疾病 | 辨证参考 |
| 化忌宫位 | 薄弱脏腑 | 养生方向 |

## ⚠️ 安全声明

本系统为传统文化**学习辅助工具**。**不提供命运预测、不替代专业命理师、不作为重大决策依据。**

## 相关项目

- [nihaisha-renji](https://github.com/jonhnsonzz/nihaisha-renji) — 倪海厦人纪：中医辨证知识系统
