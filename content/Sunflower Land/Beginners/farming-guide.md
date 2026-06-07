---
created: 2026-05-31
publish: true
related_to:
  - harvesting
  - seasons
  - crops
  - fruits
  - composters
  - greenhouse
  - crop-machine
source:
  - https://wiki.sfl.world/en/mechanics/harvesting
  - https://wiki.sfl.world/en/mechanics/seasons
status: expanded
title: Farming Guide — Hướng dẫn Canh tác
updated: 2026-06-T7 | 23:26
---

The foundation của mọi farming game chính là farming! Sunflower Land cung cấp dynamic system để trồng crops, fruits và các produce khác. Hầu như mọi thứ đều bắt đầu từ đất, và nhiều game mechanics kết hợp để tối đa hóa fertility của land bạn.

---

## Crops

Crops là plants được trồng trong **Crop Plots**. Bạn có vài plots khi bắt đầu và sẽ có thêm khi expand. Bất kỳ crop plot nào cũng trồng được bất kỳ seed nào, miễn là đúng season.

Seeds mua từ **Farmer's Market** trên home island. Khi chọn seed, nó xuất hiện trên quick-select bar (góc phải màn hình). **Không có confirmation khi plant** — hãy chắc chắn bạn đặt đúng seed! Không thể destroy/remove seed sau khi đã plant.

Timer hiển thị số đếm ngược trên plot. Tắt được qua: Game Options → General Settings → Preferences → Timers.

### Harvest Security (CAPTCHA)

Đôi khi harvest crop sẽ không ra sản phẩm ngay — một blue bar xuất hiện và bạn cần click lại. Một CAPTCHA-like challenge hiện ra (tap chest hoặc chọn goblin). Đây là cơ chế chống bot.

- **Thành công:** Bonus 1-3 seeds cho crop vừa harvest
- **Thất bại:** Lock game 5 phút

**Harvest Security sẽ ngừng xuất hiện khi đủ cả 3:**
1. Bumpkin level 60
2. Active VIP status
3. Face verification tại Retreat

### Crop Types (Phân loại cây trồng)

Crops chia làm 3 loại chính dựa trên thời gian thu hoạch. Việc phân loại này rất quan trọng vì nó quyết định các hiệu ứng từ kỹ năng chuyên biệt:

*   **Acre Farm**: Tăng sản lượng Advanced Crops +1, nhưng giảm sản lượng Basic & Medium Crops -0.5.
*   **Hectare Farm**: Tăng sản lượng Basic & Medium Crops +1, nhưng giảm sản lượng Advanced Crops -0.5.
*   **Strong Roots**: Giảm 10% thời gian sinh trưởng của Advanced Crops.

#### 1. Basic Crops (Thời gian sinh trưởng $\le$ 30 phút)

| Tên Seed | Giá mua (Coins) | Thời gian | Cấp yêu cầu (Bumpkin) | Thu hoạch | Giá bán (Coins) |
|---|---|---|---|---|---|
| **Sunflower Seed** | 0.01 | 1 phút | 1 | Sunflower | 0.02 |
| **Potato Seed** | 0.10 | 5 phút | 1 | Potato | 0.14 |
| **Rhubarb Seed** | 0.15 | 10 phút | 1 | Rhubarb | 0.24 |
| **Pumpkin Seed** | 0.20 | 30 phút | 2 | Pumpkin | 0.40 |
| **Zucchini Seed** | 0.20 | 30 phút | 2 | Zucchini | 0.40 |

#### 2. Medium Crops (Thời gian sinh trưởng từ 1 giờ đến 12 giờ)

| Tên Seed | Giá mua (Coins) | Thời gian | Cấp yêu cầu (Bumpkin) | Thu hoạch | Giá bán (Coins) |
|---|---|---|---|---|---|
| **Carrot Seed** | 0.50 | 1 giờ | 2 | Carrot | 0.80 |
| **Yam Seed** | 0.50 | 1 giờ | 2 | Yam | 0.80 |
| **Cabbage Seed** | 1.00 | 2 giờ | 3 | Cabbage | 1.50 |
| **Broccoli Seed** | 1.00 | 2 giờ | 3 | Broccoli | 1.50 |
| **Soybean Seed** | 1.50 | 3 giờ | 3 | Soybean | 2.30 |
| **Beetroot Seed** | 2.00 | 4 giờ | 3 | Beetroot | 2.80 |
| **Pepper Seed** | 2.00 | 4 giờ | 3 | Pepper | 3.00 |
| **Cauliflower Seed** | 3.00 | 8 giờ | 4 | Cauliflower | 4.25 |
| **Parsnip Seed** | 5.00 | 12 giờ | 4 | Parsnip | 6.50 |

#### 3. Advanced Crops (Thời gian sinh trưởng $\ge$ 16 giờ)

| Tên Seed | Giá mua (Coins) | Thời gian | Cấp yêu cầu (Bumpkin) | Thu hoạch | Giá bán (Coins) |
|---|---|---|---|---|---|
| **Eggplant Seed** | 6.00 | 16 giờ | 5 | Eggplant | 8.00 |
| **Corn Seed** | 7.00 | 20 giờ | 5 | Corn | 9.00 |
| **Onion Seed** | 7.00 | 20 giờ | 5 | Onion | 10.00 |
| **Radish Seed** | 7.00 | 24 giờ | 5 | Radish | 9.50 |
| **Wheat Seed** | 5.00 | 24 giờ | 5 | Wheat | 7.00 |
| **Turnip Seed** | 5.00 | 24 giờ | 6 | Turnip | 8.00 |
| **Kale Seed** | 7.00 | 36 giờ | 7 | Kale | 10.00 |
| **Artichoke Seed** | 7.00 | 36 giờ | 8 | Artichoke | 12.00 |
| **Barley Seed** | 10.00 | 48 giờ | 14 | Barley | 12.00 |

---

### Plot Fertility (Water Well)

Khi expand, một số Crop Plots bị grayed out và không dùng được. Xây **Water Well** từ Workbench để cấp fertility. Nâng cấp well đến max level 4 khi có thêm plots.

> Xem requirements: https://sfl.world/info/const/#BUILDINGS

Well trước đây không upgradeable (phải đặt nhiều wells). Nếu còn extra well, bán tại Garbo.

---

### Fertilizers

Fertilizer có thể applied trong khi crop đang phát triển. **Chỉ 1 fertilizer per plot, 1 lần per harvest.**

| Fertilizer | Effect | Nguồn |
|------------|--------|-------|
| **Sprout Mix** | +0.2 yield | Compost Bin |
| **Rapid Root** | −50% remaining time | Premium Composter |
| **Sproutroot Surprise** | −50% time + +0.2 yield | Aging Shed (kết hợp) |

> **Tip:** Dùng Rapid Root ngay sau khi plant. Không thể apply fertilizer lên crop đã fully grown.

**Mass-apply skills:**
- **Sprout Surge:** Thêm Sprout Mix vào tất cả plots chưa có fertilizer
- **Root Rocket:** Tương tự cho Rapid Root

---

### Bee Swarm

Khi Beehive đạt 100%, harvest có **10% chance** tạo Bee Swarm (+0.2 yield cho crops hiện tại). Stack được với fertilizer và bee swarms sau đó.

| Skill | Effect |
|-------|--------|
| **Pollen Power Up** | Boost → +0.3 |
| **Bee Collective** | +20% swarm chance |

---

### Scarecrows

Ba items có thể craft để boost crop outputs. Ảnh hưởng crops trong **3x3 grid** bên dưới (glowing square). Range có thể tăng lên **7x7** với skill.

| Scarecrow | Effect | Skill Upgrade |
|-----------|--------|---------------|
| **Basic Scarecrow** | Basic −20% growth time | Chonky Scarecrow (−10% thêm + range) |
| **Scary Mike** | Medium +0.2 yield | Horror Mike (+0.3 + range) |
| **Laurie the Chuckle Crow** | Advanced +0.2 yield | Laurie's Gains (+0.3 + range) |

> AOE có thể overlap giữa các scarecrow, nhưng không thể cả 3 affect cùng 1 area.

---

## Fruits

Fruit Patches mở khóa khi upgrade lên **Petal Island** (Petal Paradise). Fruit seeds mua từ Market, tốn hơn crop seeds nhưng **multiple harvests per seed**.

1. Plant fruit seed → produce sau thời gian
2. Harvest → timer restart (replenishing)
3. Sau số harvests nhất định → plant chết (stick/stump)
4. Dùng Axe để chop → nhận 1 Wood → plot trống

> **Biết số harvests còn lại:** https://sfl.world/map/ (nhập Farm ID)

**Quick Select:** Click/tap fruit patch → popup seeds khả dụng. Tắt qua: Game Options → General Settings → Preferences → Quick Select.

**Fruit skills:**

| Skill | Effect |
|-------|--------|
| **No Axe No Worries** | Clear dead plots không cần Axe (0 Wood) |
| **Fruity Woody** | +1 Wood từ cleared plots |
| **Cả 2** | +1 Wood, không dùng Axe |

### Fruit Types

| Type | Fruits | Time | Skills |
|------|--------|------|--------|
| **Basic** | Tomato, Lemon | 2–4h | Zesty Vibes (+1 yield, −0.25 others) |
| **Medium** | Blueberry, Orange | 6–8h | Short Pickings (−25% time, +10% others) |
| **Advanced** | Apple, Banana | 12h | Long Pickings (−25% time, +10% others) |

**Moon Berries** (tháng): Celestine (Basic), Lunara (Medium), Duskberry (Advanced). Nhiều boosts apply cho cả 3.

**Seasonality:** 3/6 fruits mỗi season. 1 fruit valid cho season kế tiếp (vd: Orange Spring→Summer, Apple Autumn→Winter).

### Fruit Fertilizer

| Fertilizer | Effect | Nguồn |
|------------|--------|-------|
| **Fruitful Blend** | +0.1 per harvest (1 lần cho lifecycle) | Turbo Composter |
| **Turbofruit Mix** | +0.1 + −20% growth time | Aging Shed |
| **Fruitful Bounty** (skill) | Double Fruitful Blend → +0.2 | |
| **Blend-Tastic** (skill) | Apply Fruitful Blend all plots | |

### Immortal Pear & Macaw

| Item | Effect | Skill |
|------|--------|-------|
| **Immortal Pear** | +2 harvests per plot (không ảnh hưởng Moon Berries) | Pear Turbocharge → +4 |
| **Macaw** | +0.2 yield all fruit patches | Loyal Macaw → +0.4 |

> Cả 2 có thể đặt anywhere (kể cả trong house).

---

## Composters

Ba composters từ Workbench. Cần resources (crops, fruit, eggs) thay đổi theo season. Requirements: https://sfl.world/info/const/#SEASON_COMPOST_REQUIREMENTS

| Composter | Input | Output | Skill |
|-----------|-------|--------|-------|
| **Compost Bin** | Basic + Medium crops | Sprout Mix + Earthworms | Efficient Bin (+5 fertilizer) |
| **Turbo Composter** | Medium + Advanced crops | Fruitful Blend + Grubs | Turbo Charged (+5 Fruitful Blend) |
| **Premium Composter** | Expensive fruits + Eggs | Rapid Root + Red Wigglers | Premium Worms (+10 Rapid Root) |

**Boost mechanics:**
- Speed up composter: thêm Eggs = −2h (<2h = complete ngay)
- **Feathery Business** (skill): dùng Feathers thay Eggs (x2 số lượng)
- **Composting Bonanza** (skill): boost time → 3h (resource cost x2)

**Specialize output:**

| Skill | Effect |
|-------|--------|
| **Composting Revamp** | +5 fertilizer, −2 worm (có thể 0 worms) |
| **Composting Overhaul** | +2 worm, fertilizer unchanged |

---

## Greenhouse

Advanced building, **Desert Island only.** 4 plots, không expand được.

**Yêu cầu:** Oil. Add Oil multiples of 5 hoặc empty all. Mỗi seed tốn Oil:

| Crop | Oil/seed |
|------|----------|
| Grape | 3 Oil |
| Rice | 4 Oil |
| Olive | 6 Oil |

**Đặc điểm:**
- Trồng được **mọi season** (protected environment)
- Composter fertilizers **không apply** được (dùng Aging Shed variants)
- Boosts growth time: ảnh hưởng Rice & Olive, **không ảnh hưởng Grape**
- Quick-select system tương tự fruit patches
- **Consensus: Greenhouse đắt, chỉ nên dùng late-game** hoặc khi cần Faction Pet / NPC deliveries

---

## Crop Machine

Automated farming station, **Desert Island unlock.** Chạy bằng Oil.

**Cơ chế:**
- Queue tối đa 5 batches (1 chạy 1 lúc)
- Mỗi crop có seed capacity + growth time riêng (khác regular plots)
- **Ignore seasons** — trồng bất kỳ lúc nào
- Seeds mua bất kỳ season (kể cả trong Free Restock)
- Fertilizers **không apply** được
- Bonus seeds sau harvest **không có** (không có Harvest Security)
- Finished batches có thể collect bất kỳ lúc (không decay)

**Adding seeds:**
- Batches of 10 (cần ≥10 seeds để add)
- "All" button = add tất cả seeds (nếu ≥10)
- Removed pack nếu không đang actively processed

**Oil:**
- Base rate: 1 unit per 1 hour
- Decrease oil usage: skills/items
- Nếu hết oil giữa chừng → machine ngừng (không thể extract partial batch)
- Nên process batches nhỏ hơn trừ khi bạn offline lâu

**Boosts:**
- **Không ảnh hưởng:** growth time decreases (trừ skills đặc biệt cho Crop Machine)
- **Có ảnh hưởng:** tất cả yield boosts (flat + percentage)
- **Bountiful Harvest:** +1 yield cho machine (làm việc)
- **Sunshower:** không ảnh hưởng speed
- Chance-based boosts (vd: Peeled Potato 20% +1) vẫn work

> **Consensus:** Crop Machine đắt, không profitable trừ khi đầu tư nhiều skill points + SFT boosts.

---

## Seasons & Weather

Mỗi **7 ngày** (Monday) season thay đổi. Mỗi season có crops/fruits riêng.

### Mùa trong năm

| Season | Đặc điểm |
|--------|----------|
| **Spring** | Cây cối xanh tươi |
| **Summer** | Nóng, một số crops đặc trưng |
| **Autumn** | Pumpkin, Yam, Parsnip |
| **Winter** | Lạnh, crops mùa đông |

**Quan trọng:** Crops/fruits **không chết** khi đổi season — tiếp tục phát triển. Chỉ không mua được seeds mới nếu không compatible. **Wheat** là crop duy nhất trồng được mọi season.

**Greenhouse & Moon Berries:** Không bị ảnh hưởng bởi season. Fish: một số loại seasonal, nhưng anchovy, tuna, red snapper, marine marvels có quanh năm.

### Calendar & Unknown Events

Sau khi upgrade lên Petal Island, calendar đồng bộ với Global Events sau **14 ngày**.

**Unknown Events:** Có thể là Positive (buff) hoặc Negative (debuff). Mua weather protection từ **Bailey** tại Plaza.

| Event | Effect |
|-------|--------|
| **Double Delivery Day** | Gấp đôi rewards từ deliveries |
| **Full Moon** | Tăng chance fish đặc biệt, mutant fish |
| **Tornado/Tsunami** | Debuff — cần shield |
| **Insect Plague** | Debuff crops |
| **Great Freeze** | Debuff — cần protection |
| **Sunshower** | Buff crops |
| **Bountiful Harvest** | +1 yield tất cả crops |
| **Fish Frenzy** | Buff fishing |

Xem thêm: [[seasons]]

---

