# Ni Haixia Tianji — I-Ching & Ziwei Doushu Knowledge System

> **天纪 (Tianji)** = The Celestial Realm — Ni Haixia's complete curriculum on I-Ching (易经), Ziwei Doushu (紫微斗数, Purple Star Astrology), Feng Shui (风水), and divination.

倪海厦天纪·命理风水知识系统 — 易经、紫微斗数、阳宅风水24课完整知识库。

## What's Inside

**10 reference files (653 KB)** + 4 compiled ancient text translations:

| Module | Contents | Files |
|--------|----------|-------|
| **Tian Dao (天道)** | Ziwei Doushu astrology: stars, palaces, four transformations | `tiandao.md`, `tiandao-original.md` |
| **Ren Dao (人道)** | 64 hexagrams philosophy: life wisdom from I-Ching | `rendao.md`, `rendao-64gua.md`, `rendao-print.md` (315KB) |
| **Di Dao (地道)** | Yangzhai Feng Shui: 64 geomancy patterns | `dimai.md`, `dimai-print.md` |
| **Tianji-Renji Link** | Cross-reference: star signs → body constitution, health insights | `tianji-renji-link.md` |
| **Study Notes** | 527 screenshot evidence index | `study-notes.md` (115KB) |

## Three Ways to Use

### 1. Hermes Skill

Place in `~/.hermes/skills/nihaisha-tianji/` for [Hermes Agent](https://hermes-agent.nousresearch.com).

### 2. MCP Server

```json
{
  "mcpServers": {
    "nihaisha-tianji": {
      "command": "python3",
      "args": ["/path/to/nihaisha-tianji/api_server.py"],
      "env": {
        "PORT": "8834"
      }
    }
  }
}
```

Call:
```
query_tianji(keyword="紫微", module="all", top_k=5)
```

### 3. REST API

```bash
# Query Tianji knowledge
curl -X POST http://localhost:8834/api/query \
  -H "Content-Type: application/json" \
  -d '{"keyword":"紫微","module":"all","top_k":5}'

# Health check
curl http://localhost:8834/health
```

## Quick Start

```bash
pip install fastapi uvicorn
cd nihaisha-tianji
python3 -m uvicorn api_server:app --host 0.0.0.0 --port 8834
```

## Tianji ↔ Renji Connection

This system is designed to work with [nihaisha-renji](https://github.com/jonhnsonzz/nihaisha-renji):

| Tianji | Renji Connection | Use Case |
|--------|-----------------|----------|
| Ming palace stars | Constitutional tendency | Disease predisposition |
| Health palace | Corresponding organ diseases | Diagnosis reference |
| Transformation taboos | Weak organ systems | Health maintenance |
| Yin-Yang / Five Elements | Ba Gang pattern identification | Philosophical foundation |

## Safety Notice

> ⚠️ This system is an **educational tool** for studying Chinese metaphysics. All outputs are based on course materials. **Does NOT constitute fortune-telling, professional divination, or decision-making advice.**

## Related Projects

- [nihaisha-renji](https://github.com/jonhnsonzz/nihaisha-renji) — Ni Haixia Renji: TCM diagnosis knowledge system

## License

Educational use only. Content copyright belongs to the original course materials.
