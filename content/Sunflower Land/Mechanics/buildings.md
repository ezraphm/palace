---
publish: true
source: GitHub (src/features/game/types/buildings.ts)
updated: 2026-06-07
tags:
- game-mechanics
- sunflower-land
- buildings
title: Buildings — Công trình
---

> Tọa độ lưới (Dimensions) cho farm planning.

## Toàn bộ Buildings

### Cooking Stations (Nhà bếp)

| Building | Level | Coins | Thời gian xây | Nguyên liệu | Kích thước |
|----------|-------|-------|---------------|-------------|-----------|
| Fire Pit | ∞ (miễn phí) | 0 | 0s (ngay) | 3 Wood + 2 Stone | 3×2 |
| Kitchen | 5 | 10 | 30m | 30 Wood + 5 Stone | 4×3 |
| Bakery | 8 | 200 | 4h | 50 Wood + 20 Stone + 5 Gold | 4×3 |
| Deli | 16 | 300 | 12h | 50 Wood + 50 Stone + 10 Gold | 4×3 |
| Smoothie Shack | 23 | 0 | 12h | 25 Wood + 25 Stone + 10 Iron | 3×2 |

> Fire Pit unlock ∞ có nghĩa build ngay từ đầu. Kitchen unlock level 5 — mở khóa sớm.

### Utility (Tiện ích)

| Building | Level | Coins | Thời gian xây | Nguyên liệu | Kích thước |
|----------|-------|-------|---------------|-------------|-----------|
| Town Center | ∞ | 0 | 30s | Không | 4×3 |
| Market | ∞ | 0 | 30s | Không | 3×2 |
| Workbench | ∞ | 5 | 1m | Không | 3×2 |
| Water Well | 2 | 100 | 5m | 5 Wood | 2×2 |
| Crafting Box | 6 | 0 | 1h | 100 Wood + 5 Stone | 3×2 |
| Toolshed | 25 | 0 | 2h | 500W + 30 Iron + 25 Gold + 100 Axe + 50 Pickaxe | 2×2 |
| Warehouse | 20 | 0 | 2h | 250W + 150S + 5000 Potato + 2000 Pumpkin + 500 Wheat + 100 Kale | 3×2 |

> Water Well có thể nâng cấp (max level 4) — không có trong file này, cần verify từ nguồn khác.
> Warehouse là building duy nhất yêu cầu crops (Potato, Pumpkin, Wheat, Kale) để xây.

### Animal Housing (Chuồng trại)

| Building | Level | Coins | Thời gian xây | Nguyên liệu | Kích thước |
|----------|-------|-------|---------------|-------------|-----------|
| Hen House | 6 | 100 | 2h | 30 Wood + 5 Iron + 5 Gold | 4×3 |
| Barn | 30 | 200 | 2h | 150 Wood + 10 Iron + 10 Gold | 4×4 |
| Pet House | 0 | 5000 | 2h | 200 Wood + 100 Stone | 3×3 |

### Composters (Ủ phân)

| Building | Level | Coins | Thời gian xây | Nguyên liệu | Kích thước |
|----------|-------|-------|---------------|-------------|-----------|
| Compost Bin | 7 | 0 | 1h | 5 Wood + 5 Stone | 2×2 |
| Turbo Composter | 12 | 0 | 2h | 50 Wood + 25 Stone | 2×2 |
| Premium Composter | 18 | 0 | 4h | 50 Gold | 2×2 |

### Housing (Nhà ở)

| Building | Level | Coins | Thời gian xây | Nguyên liệu | Kích thước |
|----------|-------|-------|---------------|-------------|-----------|
| Tent | ∞ | 20 | 1h | 50 Wood | 3×2 |
| House | ∞ | 0 | 30s | Không | 4×4 |
| Manor | ∞ | 0 | 30s | Không | 5×4 |
| Mansion | ∞ | 0 | 30s | Không | 6×5 |

> House → Manor → Mansion là upgrades. Không rõ điều kiện upgrade từ source.

### Desert Island (Endgame)

| Building | Level | Coins | Thời gian xây | Nguyên liệu | Kích thước |
|----------|-------|-------|---------------|-------------|-----------|
| Greenhouse | 46 | 4800 | 4h | 500W + 100S + 25 Crimstone + 100 Oil | 4×4 |
| Crop Machine | 35 | 8000 | 2h | 1250W + 125 Iron + 50 Crimstone | 5×4 |

> Cả hai đều yêu cầu `requiredIsland: "desert"` — chỉ xây được trên Desert Island.

### Processing

| Building | Level | Coins | Thời gian xây | Nguyên liệu | Kích thước |
|----------|-------|-------|---------------|-------------|-----------|
| Fish Market | 10 | 0 | 1h | 50 Wood + 10 Iron + 5 Gold | 3×3 |
| Aging Shed | 0 | 200 | 0s (ngay) | 30 Wood | 3×2 |

---

## Building Dimensions Map

Không gian chiếm trên farm (width × height):

```
2×2: Water Well, Toolshed, Compost Bin, Turbo Composter, Premium Composter
3×2: Market, Fire Pit, Workbench, Tent, Smoothie Shack, Warehouse, Crafting Box, Aging Shed
3×3: Fish Market, Pet House
4×3: Town Center, Kitchen, Bakery, Deli, Hen House
4×4: House, Barn, Greenhouse
5×4: Manor, Crop Machine
6×5: Mansion
```

## Related Notes

- [[harvesting]] — Water Well, Composters
- [[cooking]] — Fire Pit, Kitchen, Bakery, Deli, Smoothie Shack
- [[animals]] — Hen House, Barn
- [[crafting]] — Workbench, Crafting Box, Toolshed
- [[fishing]] — Fish Market
- [[salt-aging]] — Aging Shed
- [[skills]] — Skill trees cho từng building type
