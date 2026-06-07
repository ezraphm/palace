---
publish: true
source: https://wiki.sfl.world/en/mechanics/harvesting
status: extracted
title: Thu hoạch (Harvesting)
---

## Crops và Fruits

Nền tảng của mọi game nông trại chính là nông trại! Sunflower Land cung cấp một cách năng động và thú vị để trồng cây (Crops), trái cây (Fruits) và các nông sản khác. Hầu như mọi thứ đều bắt đầu từ mặt đất, và nhiều cơ chế game phối hợp với nhau để tối đa hóa độ phì nhiêu của đất đai bạn.

### Crops (Cây trồng)

**23 loại** cây trồng, chia 3 nhóm dựa trên thời gian thu hoạch (code `isBasicCrop`, `isMediumCrop`, `isAdvancedCrop`):

| Crop | Sell Price | Hạt giống | Giá hạt | Thời gian | Level | Nhóm |
|------|-----------|-----------|---------|-----------|-------|------|
| Sunflower | 0.02 | Sunflower Seed | 0.01 | 1m | 1 | Basic |
| Potato | 0.14 | Potato Seed | 0.1 | 5m | 1 | Basic |
| Rhubarb | 0.24 | Rhubarb Seed | 0.15 | 10m | 1 | Basic |
| Pumpkin | 0.4 | Pumpkin Seed | 0.2 | 30m | 2 | Basic |
| Zucchini | 0.4 | Zucchini Seed | 0.2 | 30m | 2 | Basic |
| Carrot | 0.8 | Carrot Seed | 0.5 | 1h | 2 | Medium |
| Yam | 0.8 | Yam Seed | 0.5 | 1h | 2 | Medium |
| Cabbage | 1.5 | Cabbage Seed | 1 | 2h | 3 | Medium |
| Broccoli | 1.5 | Broccoli Seed | 1 | 2h | 3 | Medium |
| Soybean | 2.3 | Soybean Seed | 1.5 | 3h | 3 | Medium |
| Beetroot | 2.8 | Beetroot Seed | 2 | 4h | 3 | Medium |
| Pepper | 3 | Pepper Seed | 2 | 4h | 3 | Medium |
| Cauliflower | 4.25 | Cauliflower Seed | 3 | 8h | 4 | Medium |
| Parsnip | 6.5 | Parsnip Seed | 5 | 12h | 4 | Medium |
| Eggplant | 8 | Eggplant Seed | 6 | 16h | 5 | Advanced |
| Corn | 9 | Corn Seed | 7 | 20h | 5 | Advanced |
| Onion | 10 | Onion Seed | 7 | 20h | 5 | Advanced |
| Radish | 9.5 | Radish Seed | 7 | 24h | 5 | Advanced |
| Wheat | 7 | Wheat Seed | 5 | 24h | 5 | Advanced |
| Turnip | 8 | Turnip Seed | 5 | 24h | 6 | Advanced |
| Kale | 10 | Kale Seed | 7 | 36h | 7 | Advanced |
| Artichoke | 12 | Artichoke Seed | 7 | 36h | 8 | Advanced |
| Barley | 12 | Barley Seed | 10 | 48h | 14 | Advanced |

> **Crop categories trong code:** Basic = harvestSeconds ≤ 30m (Pumpkin threshold). Advanced = harvestSeconds ≥ 16h (Eggplant threshold). Medium = còn lại.
> **Overnight crop:** Radish (24h), Wheat (24h), Turnip (24h), Kale (36h), Artichoke (36h), Barley (48h) — có category riêng "Overnight Crop".

### Seasonal Availability

| Mùa | Crops | Fruits | Flowers | Greenhouse |
|-----|-------|--------|---------|------------|
| 🌸 Spring | Sunflower, Rhubarb, Carrot, Cabbage, Soybean, Corn, Wheat, Kale, Barley | Tomato, Blueberry, Orange | Sunpetal, Bloom, Lily, Lavender | Rice, Olive, Grape |
| ☀️ Summer | Sunflower, Potato, Zucchini, Pepper, Beetroot, Cauliflower, Eggplant, Radish, Wheat | Lemon, Orange, Banana | Sunpetal, Bloom, Lily, Gladiolus | Rice, Olive, Grape |
| 🍂 Autumn | Potato, Pumpkin, Carrot, Yam, Broccoli, Soybean, Wheat, Barley, Artichoke | Tomato, Apple, Banana | Sunpetal, Bloom, Lily, Clover | Rice, Olive, Grape |
| ❄️ Winter | Potato, Cabbage, Beetroot, Cauliflower, Parsnip, Onion, Turnip, Wheat, Kale | Lemon, Blueberry, Apple | Sunpetal, Bloom, Lily, Edelweiss | Rice, Olive, Grape |

> **Greenhouse crops** (Rice, Olive, Grape) available 4 mùa, không bị ảnh hưởng bởi season.

Thuật ngữ "Crops" đề cập đến các loại cây được trồng trong Crop Plots (ô cây trồng). Bạn sẽ có một vài ô này trong trang trại khi bắt đầu game và sẽ kiếm thêm khi bạn mở rộng (expand). Bất kỳ Crop Plot nào cũng có thể trồng bất kỳ loại hạt giống (seed) nào, miễn là nó đang trong mùa vụ hiện tại. Tất cả cây trồng đều bắt đầu từ hạt giống, bạn có thể mua tại Farmer's Market trên Home Island của mình.

Khi bạn chọn một hạt giống từ Market hoặc từ Inventory Basket, nó sẽ xuất hiện ở đầu thanh chọn nhanh (quick-select bar) ở bên phải màn hình. Đây là ba vật phẩm bạn đã chọn gần đây nhất và bạn có thể chọn một trong hai vật phẩm còn lại để thay thế lựa chọn đang hoạt động ở trên cùng. Không có xác nhận khi bạn trồng hạt giống, vì vậy hãy chắc chắn rằng bạn đang đặt đúng hạt vào đúng chỗ! Cũng không có cách nào để phá hủy hoặc loại bỏ hạt giống khỏi một ô sau khi đã trồng. Ngay cả khi bạn sử dụng công cụ farm designer (bàn tay) để loại bỏ ô khỏi trang trại, nó sẽ giữ lại hạt giống đang phát triển trong inventory và tiếp tục phát triển sau khi bạn đặt lại ô.

Sau khi bạn trồng hạt giống, một con số sẽ xuất hiện trên ô với thời gian còn lại cho đến khi thu hoạch (được làm tròn), và một thanh màu xanh lá để thể hiện theo cách khác. Các bộ đếm thời gian này có thể được tắt qua Game Options → General Settings → Preferences → Timers, nếu bạn muốn. Bạn cũng có thể chạm hoặc di chuột qua ô để xem thời gian cụ thể đến từng phút hoặc giây.

### Harvest Security (Bảo mật Thu hoạch)

Đôi khi khi bạn thu hoạch cây trồng, bạn sẽ không nhận được sản phẩm ngay lập tức — một thanh màu xanh xuất hiện bên dưới nó và bạn sẽ cần nhấp vào cây trồng lần thứ hai. Một cửa sổ bật lên yêu cầu bạn thực hiện một thử thách giống CAPTCHA đơn giản, chẳng hạn như chạm vào rương (chest) trên cánh đồng hoặc chọn Goblins giữa những thứ màu xanh khác. Đừng lo lắng, điều này hoàn toàn bình thường và là một phần trong nỗ lực liên tục của game nhằm chống lại bot và các hành vi xấu khác.

Sau khi giải được câu đố, bạn sẽ nhận được thêm 1-3 hạt giống cho loại cây bạn vừa thu hoạch, rất hữu ích cho các loại hạt đắt tiền. Nếu bạn thất bại trong việc giải câu đố bằng cách nhấp vào sai phần tử, bạn sẽ bị khóa game trong 5 phút. Hãy nghỉ ngơi trước khi quay lại nông trại!

Nếu các cửa sổ bật lên thu hoạch này bắt đầu gây khó chịu, đừng lo lắng. Một khi bạn đáp ứng tất cả các tiêu chí sau, chúng sẽ ngừng xuất hiện (và bạn vẫn sẽ nhận được hạt giống bonus định kỳ!):
- Đạt cấp Bumpkin level 60
- Có VIP status đang hoạt động
- Hoàn tất face verification tại Retreat

### Loại Crops (Crop Type)

Crops được chia thành ba loại: **Basic**, **Medium** và **Advanced**.

- **Basic Crops** phát triển nhanh, từ 1-30 phút. Chúng được thiết kế cho lối chơi năng động hơn, liên tục thu hoạch và trồng lại, và thực sự có thể mang lại lợi nhuận cao hơn so với cây trồng phát triển chậm. Kỹ năng (Skill) **Young Farmer** tăng sản lượng của chúng thêm +0.1.
- **Medium Crops** nằm ở giữa, mất từ 1-12 giờ cho mỗi lần thu hoạch. Chúng đóng vai trò quan trọng trong nhiều công thức và sản phẩm. Kỹ năng **Experienced Farmer** tăng sản lượng Medium thêm +0.1.
- **Advanced Crops** mất nhiều thời gian nhất, từ 16-48 giờ trước khi trưởng thành. Tốt nhất nên trồng qua đêm hoặc khi bạn sẽ rời game một thời gian dài. Kỹ năng **Old Farmer** tăng sản lượng Advanced thêm +0.1. Kỹ năng **Strong Roots** giảm thời gian phát triển dài của chúng đi 10%.

Có hai kỹ năng chuyên môn hóa: **Acre Farm** và **Hectare Farm**:
- **Acre Farm** tăng sản lượng của Advanced Crops thêm +1, trong khi giảm Basic và Medium đi -0.5.
- **Hectare Farm** tăng Basic và Medium thêm +1 và giảm Advanced đi -0.5.

Chọn cả hai kỹ năng này sẽ cân bằng thành +0.5 cho tất cả các loại cây trồng, nhưng chọn cái này thay vì cái kia có thể dẫn đến những cú tăng sản lượng và lợi nhuận nghiêm trọng. Bạn có thể xem loại cây trồng tại Farmer's Market bằng cách chọn nó trong tab Buy hoặc tab Guide. Hạt giống được sắp xếp trong inventory của bạn theo thứ tự loại.

### Plot Fertility (Water Well)

Khi bạn mở rộng trang trại và có thêm Crop Plots, bạn sẽ thấy một số ô bị mờ đi và không thể sử dụng. Đã đến lúc xây dựng Water Well! Tìm trong workbench và đặt nó ở đâu đó trong trang trại của bạn. Nó không cần phải ở gần các ô trồng trọt. Khi bạn tiếp tục mở rộng, bạn sẽ cần nâng cấp giếng, tối đa cấp 4. Bạn có thể xem các yêu cầu nâng cấp giếng tại https://sfl.world/info/const/#BUILDINGS

Trước đây, Water Well không thể nâng cấp, thay vào đó bạn phải đặt nhiều giếng trong trang trại để xử lý nhiều cây trồng hơn. Nếu bạn vẫn còn một cái giếng thừa, hãy đến gặp Garbo để ông ấy lấy nó đi.

### Fertilizers

Cây trồng phát triển tốt hơn với một chút yêu thương và chăm sóc, và bạn có thể giúp cây phát triển trước khi nó sẵn sàng. Fertilizers có thể được áp dụng trong khi cây đang phát triển.

- **Sprout Mix** tăng sản lượng thêm +0.2 cố định.
- **Rapid Root** giảm 50% thời gian phát triển còn lại. Vì lý do đó, tốt nhất nên sử dụng Rapid Root ngay khi bạn trồng cây, hoặc trên một ô trống mà bạn sắp trồng.
- Bạn chỉ có thể áp dụng một loại Fertilizer cho một ô và chỉ một lần mỗi vụ thu hoạch.
- Bạn có thể áp dụng Fertilizer cho một ô trống và nó sẽ tăng cường cho vụ cây trồng tiếp theo trong ô đó.
- Bạn không thể áp dụng bất kỳ Fertilizer nào cho cây đã trưởng thành hoàn toàn.

Bạn có thể kết hợp hiệu ứng của hai loại Fertilizer cây trồng tại Aging Shed; **Sproutroot Surprise** giảm thời gian phát triển 50% và thêm +0.2 vào sản lượng cùng một lúc.

Mặc dù bạn không thể thu hoạch tất cả các ô cùng một lúc nếu không có vật phẩm đặc biệt, nhưng có một cách để bón phân hàng loạt. Kỹ năng **Sprout Surge** thêm Sprout Mix vào tất cả Crop Plots trên trang trại của bạn chưa có Fertilizer, trong khi **Root Rocket** làm điều tương tự với Rapid Root.

### Bee Swarm

Nếu bạn may mắn nhận được pollination celebration từ Beehive, phần thưởng sẽ được áp dụng trên bất kỳ loại Fertilizer nào bạn đã thêm và sẽ cộng dồn với các đợt Bee Swarm tiếp theo. Hãy chọn kỹ năng **Pollen Power Up** để tăng boost lên +0.3 và **Bee Collective** để tăng cơ hội xảy ra Bee Swarm thêm 20%.

### Scarecrows

Có ba vật phẩm bạn có thể chế tạo (Crafting) để trực tiếp tăng sản lượng cây trồng, và rất đáng để đầu tư. Mỗi Scarecrow chỉ ảnh hưởng đến cây trồng trong lưới 3x3 ngay bên dưới nó, như được hiển thị bằng hình vuông phát sáng khi đặt nó. Phạm vi này có thể được tăng lên 7x7 với kỹ năng dành riêng cho từng Scarecrow.

- **Basic Scarecrow** giảm thêm 20% thời gian phát triển của Basic Crops vốn đã nhanh. Kỹ năng **Chonky Scarecrow** tăng phạm vi và giảm thêm 10% thời gian phát triển.
- **Scary Mike** làm Medium Crops sợ hãi để tăng thêm +0.2 sản lượng. Kỹ năng **Horror Mike** tăng phạm vi ảnh hưởng và tăng boost lên +0.3.
- **Laurie the Chuckle Crow** canh gác Advanced Crops, tăng sản lượng thêm +0.2. Chi điểm kỹ năng vào **Laurie's Gains** tăng phạm vi và boost lên +0.3.

Điều quan trọng cần lưu ý là vùng ảnh hưởng của các Scarecrow có thể chồng lấn, nghĩa là boost sẽ được áp dụng cho nhiều loại cây trồng trong phạm vi của chúng. Tuy nhiên, ngay cả khi tất cả được xếp thành một hàng và phạm vi được tăng lên, bạn không thể có cả ba ảnh hưởng đến cùng một khu vực.

### Fruit (Trái cây)

**9 loại** trái cây trồng trên Fruit Patch (mở khóa tại Petal Paradise), cộng thêm **Grape** (Greenhouse):

| Fruit | Sell Price | Seed | Giá hạt | Thời gian/lần | Level | Bush? | Loại |
|-------|-----------|------|---------|---------------|-------|-------|------|
| Tomato | 2 | Tomato Seed | 5 | 2h | 13 | ✅ | Basic |
| Lemon | 6 | Lemon Seed | 15 | 4h | 12 | ❌ | Basic |
| Blueberry | 12 | Blueberry Seed | 30 | 6h | 13 | ✅ | Medium |
| Orange | 18 | Orange Seed | 50 | 8h | 14 | ❌ | Medium |
| Apple | 25 | Apple Seed | 70 | 12h | 15 | ❌ | Advanced |
| Banana | 25 | Banana Plant | 70 | 12h | 16 | ✅ | Advanced |
| Celestine 🌙 | 200 | Celestine Seed | 300 | 6h | 12 | ✅ | Full Moon |
| Lunara 🌙 | 500 | Lunara Seed | 750 | 12h | 12 | ✅ | Full Moon |
| Duskberry 🌙 | 1000 | Duskberry Seed | 1250 | 24h | 12 | ✅ | Full Moon |

> **Full Moon Fruits** (Celestine, Lunara, Duskberry) — chỉ available trong sự kiện Full Moon. Cố định 6 harvests mỗi seed, không bị ảnh hưởng bởi Immortal Pear.
> **isBush** = cây bụi (không cần Axe để dọn? Cần verify).

Fruit Patches được mở khóa khi bạn nâng cấp hòn đảo lên Petal Paradise và chúng rất đáng để đầu tư thời gian. Hạt giống trái cây (Fruit Seeds) có sẵn tại Market cùng với hạt giống cây trồng, tùy theo mùa hiện tại. Chúng đắt hơn một chút so với hạt giống cây trồng, nhưng như bạn có thể thấy từ mô tả, bạn sẽ thu hoạch được nhiều lần từ mỗi hạt.

Sau khi trồng hạt giống trái cây, nó sẽ mất thời gian như được liệt kê để tạo ra một lần thu hoạch. Sau khi thu hoạch, bộ đếm thời gian sẽ khởi động lại và phát triển một quả khác (replenishing). Bạn phải thu hoạch trái cây trước khi một quả khác bắt đầu phát triển, vì vậy hãy để mắt đến chúng.

Khi số lần thu hoạch đã đạt đến giới hạn, cây trái sẽ chết và biến thành một cây gậy hoặc gốc cây. Bạn cần có Axe để chặt nó và đưa ô trở về trạng thái trống trước khi có thể trồng hạt khác. Đổi lại, bạn sẽ nhận được 1 Wood. Chọn kỹ năng **No Axe No Worries** để có thể dọn sạch các ô đã chết mà không cần Axe, nhưng không nhận được Wood. Hoặc chọn **Fruity Woody** để tăng lượng Wood nhận được thêm +1. Chọn cả hai cho bạn +1 Wood mà không cần dùng Axe.

Game không chỉ cho bạn biết còn bao nhiêu lần thu hoạch trên mỗi cây trái. Tuy nhiên, nếu bạn thực sự muốn biết, bạn có thể tìm hiểu tại https://sfl.world/map/ (Nhập Farm ID của bạn).

### Quick Select

Khi bạn nhấp hoặc chạm vào một Fruit Patch và không có hạt giống trái cây trong thanh quick-select, bạn sẽ được hiển thị một popup các hạt giống hiện có sẵn cho ô đó. Chọn một hạt sẽ trồng nó trong ô đó và đặt nó làm vật phẩm được chọn hiện tại (ngay cả khi bạn chọn kỹ năng No Axe No Worries). Bạn có thể tắt tính năng này trong Game Options → General Settings → Preferences → Quick Select. Dọn sạch một ô đã hết sẽ khiến Axe trở thành vật phẩm hiện tại của bạn, vì vậy bạn sẽ cần quick-select lại để tiếp tục trồng.

### Loại Fruit

Game không phân chia mỗi loại trái cây thành các loại như đối với Crops, nhưng có thể thấy các nhóm rõ ràng.

- **Cơ bản:** Tomatoes và Lemons, mất 2-4 giờ để tạo ra một lần thu hoạch. Kỹ năng **Zesty Vibes** tăng sản lượng của chúng thêm +1, trong khi giảm bốn loại còn lại đi -0.25. Kỹ năng **Crime Fruit** cũng tăng số lượng stock tại chợ cho cả hai loại thêm +10.
- **Trung bình:** Blueberries và Oranges, mất 6-8 giờ mỗi lần. Kỹ năng **Short Pickings** giảm 25% thời gian phát triển của chúng, nhưng tăng 10% thời gian phát triển của tất cả các loại khác.
- **Cao cấp:** Apples và Bananas, mất 12 giờ giữa mỗi lần thu hoạch. Kỹ năng **Long Pickings** làm tương tự cho hai loại này, giảm 25% với cái giá là tất cả các loại trái cây khác chậm hơn 10%.

Ba trong sáu loại trái cây có thể được trồng mỗi mùa và một loại luôn có hiệu lực cho mùa tiếp theo mùa hiện tại. Ví dụ: Oranges phát triển từ mùa xuân đến mùa hè, trong khi Apples có hiệu lực từ mùa thu đến hết mùa đông. Hãy sử dụng thực tế này khi lên kế hoạch cho vườn cây ăn trái của bạn để đảm bảo sản lượng tối đa.

Ngoài ra, "Moon Berries" hàng tháng gồm **Celestine** (Basic), **Lunara** (Medium) và **Duskberry** (Advanced) thuộc một loại riêng. Nhiều boost và bonus cho trái cây cũng áp dụng cho ba loại này.

### Fertilizer cho Trái cây

Fertilizer chính cho trái cây là **Fruitful Blend**, được tạo tại Turbo Composter. Nó sẽ tăng sản lượng của mỗi lần thu hoạch trên một cây thêm +0.1. Nó không cần được áp dụng lại cho đến khi cây chết và một cây mới được trồng. Kỹ năng **Fruitful Bounty** tăng gấp đôi hiệu ứng của Fertilizer này, tạo tổng boost +0.2 cho mỗi lần thu hoạch.

Kỹ năng **Blend-Tastic** cho phép bạn áp dụng Fruitful Blend Fertilizer vào mọi Fruit Patch cùng một lúc, rất hữu ích để đảm bảo mọi ô đều đã được xử lý.

Tại Aging Shed, bạn có thể kết hợp Fruitful Blend với Rapid Root để tạo **Turbofruit Mix**, tăng sản lượng thêm +0.1 và giảm 20% thời gian phát triển của mỗi lần thu hoạch trong vòng đời của cây. Các kỹ năng cho Fruitful Bounty không ảnh hưởng đến Turbofruit Mix.

### Pear và Macaw

Bạn có thể chế tạo (Crafting) một vật phẩm tại workbench gọi là **Immortal Pear**, khi đặt trong trang trại sẽ tăng số lần thu hoạch trên mỗi ô thêm +2. Điều này chỉ xảy ra với trái cây bạn trồng sau khi đặt nó, không phải trái cây đang phát triển. Kỹ năng **Pear Turbocharge** tăng gấp đôi hiệu ứng của vật phẩm này, tổng cộng +4 lần thu hoạch mỗi ô. Bonus của Pear không ảnh hưởng đến ba loại Moon Berries — chúng cố định ở 6 lần thu hoạch mỗi hạt.

Bạn cũng có thể chế tạo **Macaw**, tăng sản lượng của tất cả Fruit Patches thêm +0.2. Kỹ năng **Loyal Macaw** tăng boost này lên +0.4. Cả hai vật phẩm có thể được đặt ở bất cứ đâu, kể cả trong nhà bạn, để có hiệu lực.

## Composters

Các loại Fertilizer bạn cần để cải thiện trang trại đến từ Composters, một bộ ba vật phẩm bạn có thể xây dựng từ workbench. Những gì đi vào các thiết bị tuyệt vời này? Crops và Fruit, tất nhiên! (Và đôi khi là Eggs)

Mỗi Composter yêu cầu một bộ vật phẩm khác nhau thay đổi theo mùa. Phù hợp với hệ thống ba cấp, mỗi cấp yêu cầu tài nguyên cấp cao hơn khi bạn tiến lên. Bạn có thể xem danh sách đầy đủ các yêu cầu theo mùa tại https://sfl.world/info/const/#SEASON_COMPOST_REQUIREMENTS

Sau khi bạn bắt đầu nấu, một Composter có thể được tăng tốc bằng cách thêm Eggs, giảm thời gian còn lại đi 2 giờ. Nếu còn dưới 2 giờ, nó sẽ hoàn thành ngay lập tức.

Kỹ năng **Feathery Business** sẽ thay đổi boost để yêu cầu Feathers thay vì Eggs, nhưng sẽ cần gấp đôi số lượng. Kỹ năng **Composting Bonanza** sẽ tăng thời gian boost lên 3 giờ, nhưng tăng yêu cầu tài nguyên lên gấp đôi. Nếu bạn đang dùng Feathers, điều này có thể khiến việc tăng tốc trở nên quá đắt.

Nếu bạn không câu cá nhiều, bạn có thể chọn kỹ năng **Composting Revamp**, tăng sản lượng Fertilizer của mỗi đơn vị thêm +5, trong khi giảm sản lượng worm đi -2. Điều này có thể dẫn đến việc bạn không nhận được worm nào trừ khi bạn tăng chúng bằng cách khác. Ngược lại, kỹ năng **Composting Overhaul** tăng sản lượng worm thêm +2, trong khi giữ nguyên sản lượng Fertilizer.

### Compost Bin

Composter đầu tiên bạn xây dựng, nhỏ nhất và yêu cầu cây trồng đơn giản nhất, chủ yếu là Basic và một số Medium. Đổi lại, bạn sẽ nhận được Sprout Mix, cùng với một vài Earthworms để câu cá. Kỹ năng **Efficient Bin** tăng lượng Fertilizer thêm +5.

### Turbo Composter

Mặc dù có tên gọi như vậy, Composter này thực sự sản xuất Fruitful Blend, nhưng chỉ nhận Medium và Advanced Crops. Bạn cũng sẽ có được Grubs để câu cá. Kỹ năng **Turbo Charged** tăng sản lượng Fruitful Blend thêm +5.

### Premium Composter

Composter cao cấp này yêu cầu một núi Gold để xây dựng, chưa kể đến các loại trái cây đắt tiền và Eggs cần thiết để làm cho nó hoạt động. Nó sẽ cung cấp cho bạn không chỉ Rapid Root đáng thèm muốn, mà còn cả Red Wigglers, mồi câu (bait) cấp cao nhất. Kỹ năng **Premium Worms** tăng sản lượng Rapid Root thêm +10, không phải sản lượng worm, nhưng có một kỹ năng khác để tăng sản lượng đó.

## Greenhouse

### Greenhouse Crops

| Crop | Sell Price | Seed | Giá hạt | Thời gian | Level | Loại |
|------|-----------|------|---------|-----------|-------|------|
| Rice | 320 | Rice Seed | 240 | 32h | 40 | Crop |
| Olive | 400 | Olive Seed | 320 | 44h | 40 | Crop |
| Grape | 240 | Grape Seed | 160 | 12h | 40 | Fruit |

> Rice/Olive bị ảnh hưởng bởi crop growth boost. Grape KHÔNG bị ảnh hưởng bởi crop hoặc fruit growth boost — chỉ có skill **Rice and Shine** giảm thời gian.
> Cả 3 đều available 4 mùa.

Greenhouse là một công trình (building) cao cấp chỉ dành cho người chơi trên Desert Island và yêu cầu một lượng lớn tài nguyên để xây dựng và sử dụng. Khi đã sẵn sàng, nó cung cấp các loại cây trồng độc đáo mà bạn không thể trồng ở bất kỳ nơi nào khác.

Greenhouse crops phát triển từ hạt giống mua từ Market. Greenhouse chỉ có bốn ô và hiện không thể mở rộng. Composter Fertilizers không thể áp dụng cho các ô Greenhouse, nhưng có hai loại có thể được tạo tại Aging Shed. Ngoài ra, sản lượng và thời gian phát triển của mỗi cây có thể được tăng hoặc giảm bởi các Skills khác nhau. Hệ thống quick-select được sử dụng trong Fruit Patches cũng hoạt động với hạt giống Greenhouse.

Cả ba loại cây đều yêu cầu Oil, phải được thêm vào máy móc của Greenhouse trước khi bạn có thể trồng hạt giống trong một ô. Oil chỉ có thể được thêm theo bội số của 5, hoặc bạn có thể đổ toàn bộ inventory của mình vào cùng một lúc. Các yêu cầu cho mỗi hạt giống được hiển thị trên màn hình nơi bạn thêm Oil và có thể bị ảnh hưởng thông qua các Skills khác nhau.

Greenhouse crops có thể được trồng trong bất kỳ mùa nào, vì đó là môi trường được bảo vệ. Sự đồng thuận giữa hầu hết người chơi là Greenhouse quá đắt để vận hành cho đến giai đoạn sau của game, nhưng nếu bạn muốn đảm bảo luôn là thành viên đóng góp cho Faction Pet của mình hoặc có thể xử lý bất kỳ Delivery nào từ bất kỳ NPC nào, bạn có thể chọn sử dụng nó bất chấp chi phí.

Vì một lý do nào đó, các boost ảnh hưởng đến thời gian phát triển của Crops sẽ tăng tốc Rice và Olives, nhưng không tăng tốc Grapes. Các boost giảm thời gian phát triển của Fruits cũng sẽ không ảnh hưởng đến Grapes. Cách thực sự duy nhất để giảm thời gian của Grapes là kỹ năng **Rice and Shine**.

## Crop Machine

Crop Machine là trạm canh tác tự động của bạn, được mở khóa trên Desert Island. Nó chạy bằng Oil, tiêu thụ Oil cho mỗi mẻ nó xử lý. Khi được cung cấp năng lượng, nó tự động trồng cây và tiếp tục hoạt động ngay cả khi bạn ngoại tuyến.

Bạn có thể xếp hàng tối đa năm mẻ, mặc dù chỉ một mẻ chạy tại một thời điểm. Mỗi loại cây có dung lượng hạt giống và thời gian phát triển riêng bên trong máy, tách biệt với các ô thông thường. Crops trồng ở đây bỏ qua mùa vụ, vì vậy bạn có thể sản xuất chúng bất cứ lúc nào. Bạn cũng có thể mua hạt giống cho mọi loại cây mà máy hỗ trợ bất cứ lúc nào, bất kể mùa vụ (chúng cũng sẽ được bao gồm trong Free Restock hàng ngày của bạn).

Các mẻ đã hoàn thành có thể được thu thập bất cứ lúc nào mà không có rủi ro mất mát hoặc bị phạt. Tuy nhiên, do cách hoạt động của crop yield bonuses, có thể đáng để chờ đợi cho đến khi sự kiện Bountiful Harvest xảy ra trước khi lấy sản phẩm từ máy. Fertilizers không thể được áp dụng cho Crop Machine dưới bất kỳ hình thức nào.

Thêm hạt giống được thực hiện theo mẻ 10, vì vậy nếu bạn có ít hơn 10 hạt cho một loại cây, bạn không thể thêm chúng. Nút All trong hộp thoại thêm hạt giống cho phép bạn thêm mọi hạt giống trong inventory, miễn là bạn có ít nhất 10 hạt. Mỗi bộ 10 hạt mất thời gian phát triển cơ bản của cây trồng để phát triển, nhưng chúng được thu hoạch và trồng lại tự động. Bạn có thể loại bỏ một gói hạt giống nếu nó không đang được xử lý tích cực.

Bất kỳ boost nào bạn có để giảm thời gian phát triển của cây trồng đều không ảnh hưởng đến Crop Machine, ngoại trừ những boost đặc biệt nói rõ rằng chúng làm giảm thời gian sản xuất của Crop Machine. Tất cả các boost ảnh hưởng đến sản lượng của cây trồng, dù là cố định hay phần trăm, sẽ hoạt động khi thu hoạch một gói đã hoàn thành.

Oil được thêm vào với tỷ lệ cơ bản là 1 đơn vị mỗi 1 giờ. Giảm sử dụng Oil bằng Skills hoặc vật phẩm làm cho nó yêu cầu ít Oil hơn mỗi giờ. Nếu bạn thêm các gói hạt giống mất nhiều thời gian hơn thời gian chạy Oil của máy, nó sẽ không nhắc bạn thêm Oil — nó sẽ dừng lại khi hết giờ. Vì bạn không thể rút ra một bộ hạt giống đang xử lở dở, thông thường tốt hơn là xử lý các mẻ nhỏ hơn là lớn hơn, trừ khi bạn biết mình sẽ rời game trong thời gian dài.

Thông qua nâng cấp Skills, bạn có thể mở rộng dung lượng hàng đợi, giảm chi phí Oil, tăng hiệu quả và hơn thế nữa. Tuy nhiên, sự đồng thuận chung của người chơi là Crop Machine đắt để vận hành và không có lãi lắm trừ khi bạn đầu tư nhiều điểm kỹ năng vào các nâng cấp liên quan của nó.

Có SFTs tăng sản lượng cây trồng được hỗ trợ cũng có thể tạo ra sự khác biệt lớn, biến một hệ thống thường đắt đỏ thành một nguồn thu nhập nền ổn định. Ngay cả các vật phẩm cung cấp boost dựa trên cơ hội như Peeled Potato (20% cơ hội +1 potato khi thu hoạch) cũng hoạt động với máy; game chỉ đơn giản tính toán các boost này như thể bạn đã trồng từng hạt potato theo cách thủ công và tăng sản lượng của bạn tương ứng.

Do tính chất thô sơ của Crop Machine, bạn sẽ không bao giờ nhận được hạt giống bonus sau khi thu hoạch bất cứ thứ gì trong nó. Trong khi sức mạnh của Bountiful Harvest thêm +1 vào sản lượng máy của bạn, hiệu ứng tăng tốc của Sunshower không ảnh hưởng đến tốc độ xử lý.

### Seasonal Events

| Event | Icon | Effect | Prevention Item | Cost (Home Island) |
|-------|------|--------|-----------------|-------------------|
| 🌪️ Tornado | tornado | Phá hủy crops? | Tornado Pinwheel | 100 coins + 30 Wood + 5 Leather |
| 🌊 Tsunami | tsunami | ? | Mangrove | 100 coins + 30 Wood + 5 Leather |
| 🌙 Full Moon | fullMoon | Kích hoạt Full Moon Fruits (Celestine/Lunara/Duskberry) | — | — |
| ❄️ Great Freeze | greatFreeze | ? | Thermal Stone | 100 coins + 5 Stone + 5 Wool |
| 📦 Double Delivery | doubleDelivery | Gấp đôi phần thưởng Delivery | — | — |
| 🌾 Bountiful Harvest | bountifulHarvest | +1 yield mỗi crop khi thu hoạch | — | — |
| 🦗 Insect Plague | insectPlague | Phá hoại mùa màng? | Protective Pesticide | 100 coins + 30 Wood + 30 Feather |
| ☀️ Sunshower | sunshower | Tăng tốc growth? | — | — |
| 🐟 Fish Frenzy | fishFrenzy | Tăng cường câu cá | — | — |

> Island cost multipliers: Volcano ×2.5, Desert ×2, Home ×1.
> Mỗi event kéo dài 24h từ lúc triggered.
> Weather Shop items chỉ prevention — nếu không có item, bạn chịu hậu quả.

### Seasonal Guardian Items

| Guardian | Season |
|----------|--------|
| 🌸 Spring Guardian | Spring |
| ☀️ Summer Guardian | Summer |
| 🍂 Autumn Guardian | Autumn |
| ❄️ Winter Guardian | Winter |

Placeable boost items thuộc bộ sưu tập — kích hoạt bonus khi đúng mùa và đã built trong farm.

## Related Notes

- [[seeds|Hạt giống & Mùa vụ]]
- [[skills|Bumpkin Skills — Crop/Fruit skills detail]]
- [[buildings|Buildings — Composters, Greenhouse, Crop Machine]]
- [[recipes|Cooking Recipes — dùng crops/fruits làm nguyên liệu]]
