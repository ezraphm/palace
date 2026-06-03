---
created: 2025-05-30
description: Chi tiết về cách hoạt động của các SFT cụ thể trong trò chơi, bao gồm
  phân tích mã nguồn.
publish: true
source: https://wiki.sfl.world/en/sfts/Details
tags:
- sfts
- sunflower-land
- wiki
- faq
- game-mechanics
title: SFT Details
---

## Green Amulet
"Theo những gì tôi biết, Green Amulet có 10% tỷ lệ kích hoạt" — iSPANK

Green Amulet có **10% cơ hội** kích hoạt đòn đánh chí mạng nhân sản lượng lên **10 lần**.

Trò chơi sử dụng bộ sinh số giả ngẫu nhiên (prng) được gieo bởi farmId, itemId và một bộ đếm:

```typescript
export function prngChance({
  farmId,
  itemId,
  counter,
  chance,
  criticalHitName,
}: {
  farmId: number;
  itemId: number;
  counter: number;
  chance: number;
  criticalHitName: CriticalHitName;
}) {
  const prngValue = prng({ farmId, itemId, counter, criticalHitName });
  return prngValue * 100 < chance;
}
```

Cách sử dụng (bên trong một khối điều kiện lớn hơn):

```typescript
const criticalDrop = (criticalHitName: CriticalHitName, chance: number) =>
    prngChance({ ...prngArgs, itemId, chance, criticalHitName });

if (
  isWearableActive({ name: "Green Amulet", game }) &&
  criticalDrop("Green Amulet", 10)
) {
  amount *= 10;
  boostsUsed.push({ name: "Green Amulet", value: "x10" });
}
```
