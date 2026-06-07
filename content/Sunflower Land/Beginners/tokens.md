---
publish: true
source: https://wiki.sfl.world/en/home/tokens
title: Tokens — Tiền tệ & Token
updated: 2026-05-31T17:50
belongs_to:
  - "[[beginners-index]]"
  - "[[how-to-start]]"
---

# Tokens — Hệ thống Tiền tệ Sunflower Land

Sunflower Land có nhiều loại tiền tệ khác nhau, mỗi loại phục vụ mục đích riêng. Dưới đây là tổng quan đầy đủ.

---

## 🔷 $FLOWER

**FLOWER** là token **ERC-20 đa chuỗi, do cộng đồng sở hữu**, dùng trong tất cả khía cạnh cao cấp của Sunflower Land.

| Thuộc tính | Giá trị |
|------------|---------|
| **Loại** | ERC-20 |
| **Mạng chính** | BASE (hiện tại) |
| **Contract** | `0x3e12b9d6a4d12cd9b4a6d613872d0eb32f68b380` |
| **Giao dịch** | Uniswap (base) |
| **Công dụng** | Mua Gems, premium items, governance, trading |

### 🛒 Cách mua FLOWER

1. Truy cập [Uniswap](https://app.uniswap.org/swap?chain=base&inputCurrency=0x3e12b9d6a4d12cd9b4a6d613872d0eb32f68b380&outputCurrency=0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913&value=1&field=input)
2. Kết nối wallet (MetaMask, Sequence...)
3. Swap USDC → FLOWER trên mạng **BASE**

### 🏦 Cách nạp FLOWER vào game

1. Mở giao diện Currency ở góc trên bên phải 💎
2. Gửi FLOWER đến địa chỉ được cung cấp (địa chỉ mới mỗi lần)

> **⚠ Cảnh báo:** Chỉ nạp FLOWER vào địa chỉ được cấp trên mạng **BASE**. Luôn double-check address & network. Địa chỉ có thể thay đổi mỗi lần.
>
> **Lưu ý:** Chỉ tài khoản đã xác minh mới có thể rút tiền.

---

## 🪙 Coins

| Thuộc tính | Giá trị |
|------------|---------|
| **Loại** | In-game (không thể giao dịch) |
| **Kiếm bằng** | Bán crops, deliveries, chores, sự kiện |
| **Công dụng** | Mua tools, seeds, buildings từ NPC |

**Cách kiếm hiệu quả:** Bán cây trồng cho [[Betty]] trên Home Island.

---

## 💎 Gems

| Thuộc tính | Giá trị |
|------------|---------|
| **Loại** | Premium in-game (không thể giao dịch) |
| **Mua bằng** | Fiat (thẻ/ngân hàng) hoặc $FLOWER |
| **Công dụng chính** | Restock shops |
| **Công dụng khác** | Speed up cooking/crafting, pet food, feed animals, mua craft-ables từ blacksmith |

### Các mức Restock bằng Gems

| Loại Restock | Cost (Gems) | Shop | NPC | Items |
|-------------|-------------|------|-----|-------|
| **Market Restock** | 15 | Betty's Market | Betty | Crops, fruits, flowers, greenhouse seeds |
| **Workbench Restock** | 10 | Workbench | Blacksmith | All tools (axes, pickaxes, rods, salt rakes...) |
| **Digging Restock** | 5 | Jafar's Treasure Shop | Jafar | Sand Shovels, Sand Drills |
| **Full Restock** | 20 | Any shop | Any | Tất cả (seeds + tools + digging) |

> Full Restock (20 Gems) tiết kiệm nhất — nếu mua riêng lẻ hết 15+10+5 = 30 Gems.

**Lưu ý kỹ thuật:**
- **NPC Restock** (15/10/5 Gems): Dùng `Math.max(INITIAL_STOCK, current_stock)` — nếu stock hiện tại **cao hơn** giới hạn, nó **giữ nguyên** (không bị reset xuống). Chỉ bổ sung nếu thấp hơn.
- **Full Restock** (20 Gems): Reset toàn bộ stock về `INITIAL_STOCK`, trừ các hạt giống hoa đặc biệt (Duskberry, Lunara, Celestine) được giữ nguyên stock dư.

---

## 🎟️ Chapter Tickets

| Thuộc tính | Giá trị |
|------------|---------|
| **Loại** | Token sự kiện (theo Chapter) |
| **Kiếm bằng** | [[Chapter Race]] |
| **Công dụng** | [[Megastore]], [[Auctions]] |
| **Hết hạn** | Cuối mỗi Chapter (3 tháng) — gần như vô giá trị |

> Vé Chapter không dùng hết có thể bán cho [[Garbo]] với giá rất rẻ bằng Coins.

---

## 💕 Love Charms

| Thuộc tính | Giá trị |
|------------|---------|
| **Loại** | Token sự kiện (Love Island) |
| **Kiếm bằng** | Nhiều nguồn khác nhau |
| **Công dụng** | Đổi quà tại [[Mystery Island]] |
| **Prize đặc biệt** | Pet Egg: 10,000 Love Charms |

---

## 💸 Thuế & Phí

### Withdrawal Tax (Thuế rút FLOWER)

Áp dụng cho FLOWER kiếm được từ **deliveries**. FLOWER từ market đã bị đánh thuế trước đó.

| Số lượng rút | Thuế rút (thường) | Petal Island+ |
|-------------|-------------------|---------------|
| Dưới 10 FLOWER | 30% | 27.5% |
| Dưới 100 FLOWER | 25% | 22.5% |
| Dưới 1,000 FLOWER | 20% | 17.5% |
| Dưới 5,000 FLOWER | 15% | 12.5% |
| Trên 5,000 FLOWER | 10% | 7.5% |

> **Petal Island+** giảm thêm 2.5% thuế rút so với mức thường.

### 🔥 Market Tax (Thuế bán resources)

Khi **bán** resources (không phải mua), mỗi island có mức thuế khác nhau. **VIP giảm một nửa thuế.**

| Island | Tên | Thuế (không VIP) | Thuế (có VIP) |
|--------|-----|------------------|---------------|
| 1 | Basic Tutorial Island | Không được bán | — |
| 2 | Petal Paradise | 50% | 25% |
| 3 | Desert | 20% | 10% |
| 4 | Volcano | 15% | 7.5% |

> **Lưu ý:** Buying (mua) **không** bị ảnh hưởng bởi Market Tax. Chỉ áp dụng cho selling.

---

## So sánh nhanh

| Token | Giao dịch được? | On-chain? | Cách kiếm chính |
|-------|----------------|-----------|-----------------|
| **Coins** | ❌ | ❌ | Bán crops, deliveries |
| **Gems** | ❌ | ❌ | Mua bằng FLOWER/Fiat |
| **$FLOWER** | ✅ ERC-20 | ✅ BASE | Market, deliveries |
| **Chapter Tickets** | ❌ | ❌ | Chapter Race |
| **Love Charms** | ❌ | ❌ | Sự kiện |

---

> **Xem thêm:** [[how-to-start]] | [[beginners-guide]] | [[wallets]] | [[stock-limits]] | [[beginners-index]]
