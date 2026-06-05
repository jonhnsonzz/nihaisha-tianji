# 倪海厦天纪·命理风水知识系统

> **天纪** = 倪海厦命理风水教学体系，涵盖易经、紫微斗数、阳宅风水24课完整知识库。

🇨🇳 中文说明 | [English Version](README.md)

## 内容概览

**10个引用文件（653KB）** + 4份古文编译：

| 模块 | 内容 | 文件 |
|:----|:----|:----|
| **天道** | 紫微斗数命盘、星辰、四化、十二宫 | `tiandao.md` + 全文原文 |
| **人道** | 64卦处世哲学、易经智慧 | `rendao.md` + 64卦详解 + 可打印全文 |
| **地道** | 阳宅风水64局、地脉 | `dimai.md` + 可打印版 |
| **天纪-人纪关联** | 命宫→脏腑、星性→体质、化忌→养生 | 关联图谱 |
| **学习笔记** | 527张截图证据索引 | 板书/命盘/风水图 |

## 三种使用方式

### 1. Hermes Skill

放到 `~/.hermes/skills/nihaisha-tianji/` 即可。

### 2. MCP Server

```json
{
  "mcpServers": {
    "nihaisha-tianji": {
      "command": "python3",
      "args": ["绝对路径/nihaisha-tianji/api_server.py"],
      "env": {
        "PORT": "8834"
      }
    }
  }
}
```

调用：
```
query_tianji(keyword="紫微", module="all", top_k=5)
```

### 3. REST API

```bash
curl -X POST http://localhost:8834/api/query \
  -H "Content-Type: application/json" \
  -d '{"keyword":"紫微","module":"all","top_k":5}'
```

## 天纪↔人纪联动

本系统与[人纪系统](https://github.com/jonhnsonzz/nihaisha-renji)可联动使用：

| 天纪 | 人纪关联 | 应用 |
|:----|:--------|:----|
| 命宫星辰 | 先天体质倾向 | 判断易患疾病 |
| 疾厄宫 | 对应脏腑疾病 | 辨证参考 |
| 化忌宫位 | 薄弱脏腑 | 养生方向 |
| 阴阳五行 | 八纲辨证基础 | 中医理论根基 |

## 安全声明

> ⚠️ 本系统为传统文化**学习辅助工具**。所有输出基于课程原文。
> **不提供命运预测、不替代专业命理师、不作为重大决策依据。**

## 相关项目

- [nihaisha-renji](https://github.com/jonhnsonzz/nihaisha-renji) — 倪海厦人纪：中医辨证知识系统
