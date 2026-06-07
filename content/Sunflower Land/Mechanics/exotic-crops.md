---
publish: true
source: GitHub (src/features/game/types/beans.ts)
updated: 2026-06-07
tags:
- game-mechanics
- sunflower-land
- exotic-crops
- mutant-crops
- magic-bean
- gardening
title: Exotic & Mutant Crops
---

> Exotic Crops là cây đặc biệt chỉ trồng được từ **Magic Bean** — không phải seed thường.

## Magic Bean

Chỉ có **một loại Bean** trong game:

| Item | Thời gian trồng | Nguồn |
|------|----------------|-------|
| Magic Bean | 48h (2 ngày) | Rương, sự kiện, marketplace |

> `plantSeconds: 2 * 24 * 60 * 60` = 172,800 giây = 48 tiếng.

## Exotic Crops

Exotic Crops là kết quả khi trồng Magic Bean. **Không thể trồng trực tiếp từ seed thường.**

| Exotic Crop | Sell Price | Ghi chú |
|------------|-----------|---------|
| **Black Magic** 🌑 | 32,000 | Giá trị nhất, rất hiếm |
| **Golden Helios** 🌻 | 16,000 | Biến thể vàng |
| **Chiogga** 🫘 | 8,000 | Củ cải đường tím |
| **Purple Cauliflower** 🟣 | 3,200 | Súp lơ tím |
| **Adirondack Potato** 🥔 | 2,400 | Khoai tây tím |
| **Warty Goblin Pumpkin** 🎃 | 1,600 | Bí ngô cóc |
| **White Carrot** 🥕 | 800 | Cà rốt trắng |

> Tất cả `disabled: false` — đều đã active trong game.

### Giant Fruits

Giant Fruits cũng thuộc nhóm Exotic Crop nhưng là fruits:

| Giant Fruit | Sell Price |
|-------------|-----------|
| Giant Banana 🍌 | 5,000 |
| Giant Apple 🍎 | 2,000 |
| Giant Orange 🍊 | 800 |

## Mutant Crops

Mutant Crops là cây trồng đột biến hiếm, trồng từ seed thường với tỷ lệ nhỏ:

| Mutant Crop | Base Crop | Ghi chú |
|------------|-----------|---------|
| Stellar Sunflower 🌟 | Sunflower | Sunflower đột biến |
| Potent Potato 💪 | Potato | Potato đột biến |
| Radical Radish 🔴 | Radish | Radish đột biến |

> Tỷ lệ đột biến phụ thuộc vào chapter hiện tại và các boost (NFT, collectibles).

## Chiến lược

- **Black Magic** (32,000) có sell price cao nhất — nếu drop, giữ để bán hoặc dùng trong cooking cao cấp
- Exotic crops được dùng trong deliveries và một số công thức nấu ăn đặc biệt
- Magic Bean là resource giới hạn (không mua được ở market), chỉ có từ rương và sự kiện
- Dùng Obsidian để **instant-grow** exotic crops nếu cần gấp

## Related Notes

- [[harvesting]] — crop mechanics
- [[crafting]] — dùng exotic crops làm ingredient
- [[cooking]] — công thức nấu ăn đặc biệt
