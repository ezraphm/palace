---
description: Cơ chế chăn nuôi — chickens, sheep, cows, cho ăn, XP, cấp độ, ngủ, vuốt
  ve, bệnh tật, tiền thưởng, đột biến và skills chuyên môn hóa.
publish: true
source: https://wiki.sfl.world/en/mechanics/animals
tags:
- game-mechanics
- sunflower-land
- animals
- chickens
- sheep
- cows
title: Animals
---

Hãy tạm nghỉ trồng trọt để làm công việc chăn nuôi! Tuy nhiên, bạn sẽ cần các sản phẩm từ farm của mình nếu muốn nhận được lợi ích tối đa từ mỗi con vật.

Sunflower Land rất hào phóng trong việc cho phép người chơi mới tiếp cận các tính năng, nhưng chăn nuôi là một tính năng mà hầu hết người chơi có kinh nghiệm khuyên bạn NÊN CHỜ trước khi bắt đầu. Tất cả động vật đều yêu cầu một lượng lớn thức ăn, và trừ khi bạn có một kho dự trữ lớn, chúng sẽ ăn sạch mọi thứ trên farm và đảo nhà của bạn trước khi bạn kịp nhận ra.

Bạn có thể tìm thấy tất cả các số liệu cứng về chăn nuôi tại [https://sfl.world/info/animals](https://sfl.world/info/animals)

## Kiến thức Cơ bản về Động vật

Có hai công trình nuôi nhốt động vật: **Hen House** (chickens) và **Barn** (sheep và cows cùng nhau). Mặc định cả hai công trình đều có 10 chỗ. Động vật không già đi và không thể chết do bị bỏ đói hay thiếu chăm sóc.

### Animal Stats

| Animal | Mua giá | Level yêu cầu | Công trình | Kích thước ô | Sản phẩm |
|--------|---------|--------------|------------|-------------|---------|
| 🐔 Chicken | 50 coins | 6 | Hen House | 2×2 | Egg, Feather |
| 🐄 Cow | 100 coins | 14 | Barn | 2×2 | Milk, Leather |
| 🐑 Sheep | 120 coins | 18 | Barn | 2×2 | Wool (Merino) |

### XP Required per Level

| Level | Chicken | Cow | Sheep |
|-------|---------|-----|-------|
| 0→1 | 60 | 180 | 120 |
| 1→2 | 120 | 360 | 240 |
| 2→3 | 240 | 720 | 480 |
| 3→4 | 360 | 1,080 | 720 |
| 4→5 | 480 | 1,440 | 960 |
| 5→6 | 660 | 1,980 | 1,320 |
| 6→7 | 840 | 2,520 | 1,680 |
| 7→8 | 1,020 | 3,060 | 2,040 |
| 8→9 | 1,200 | 3,600 | 2,400 |
| 9→10 | 1,440 | 4,320 | 2,880 |
| 10→11 | 1,680 | 5,040 | 3,360 |
| 11→12 | 1,920 | 5,760 | 3,840 |
| 12→13 | 2,160 | 6,480 | 4,320 |
| 13→14 | 2,400 | 7,200 | 4,800 |
| 14→15 | 2,720 | 8,160 | 5,440 |
| **Total** | **17,520** | **52,560** | **35,040** |

> Cow cần gần gấp 3 XP của Chicken để lên cấp 15. Sheep cần gấp đôi.

### Mua một con vật

Nhấp vào biểu tượng túi/cửa hàng ở góc trên bên phải của công trình. Mỗi sinh vật tốn Coins ban đầu. Bạn có thể mua nhiều con tùy theo dung lượng (Capacity) hiển thị ở cuối giao diện.

### Cho động vật ăn

Mỗi con vật đều cần thức ăn để kiếm kinh nghiệm và lên cấp. Khi đạt một cấp mới, chúng sẽ sản xuất ra một tài nguyên và đi ngủ. Một con vật đang thức và muốn ăn sẽ hiển thị biểu tượng phía trên đầu với loại thức ăn cụ thể mà nó mong muốn.

Năm loại thức ăn:
- **Kernel Blend** - 1x Corn
- **Hay** - 1x Wheat
- **NutriBarley** - 1x Barley
- **Mixed Grain** - 1x Corn, 1x Wheat, 1x Barley (3x Kale với skill Kale Mix)
- **Omnifeed** - 1x Gem

Tất cả thức ăn được làm tại **Feeder Machine** ở đỉnh công trình. Thức ăn được lưu vào inventory sau khi Mix; nhấp vào thức ăn trong cửa sổ Machine sẽ đưa nó lên đầu thanh active bar. Thức ăn bạn muốn phải ở vị trí đầu tiên khi bạn chạm vào con vật.

Bạn có thể cho ăn bất kỳ thức ăn nào ở bất kỳ giai đoạn nào. Tuy nhiên, cho ăn đúng loại thức ăn hiển thị trên đầu con vật sẽ cho **lượng XP tối đa**. Bất kỳ thức ăn nào khác chỉ cho **một nửa XP** mỗi lần cho ăn.

Thức ăn được cấu trúc theo **"gói" (packs)**. Mỗi con vật yêu cầu một lượng thức ăn khác nhau phải được cho cùng lúc:
- **Chickens** yêu cầu 1 đơn vị thức ăn mỗi gói
- **Sheep** yêu cầu 3 đơn vị mỗi gói
- **Cows** yêu cầu 5 đơn vị mỗi gói

Mỗi cấp độ yêu cầu số lượng gói khác nhau.

**Omnifeed** là một loại thức ăn "wildcard" đặc biệt mang lại sự hài lòng hoàn toàn bất kể loại thức ăn mà con vật đang yêu cầu. Tùy vào giá tài nguyên, Omnifeed có thể rẻ hơn Mixed Grain, đặc biệt khi bạn có thể mua Gem trực tiếp bằng FLOWER từ việc bán Milk và Leather.

### XP và Cấp độ

Một con vật thức cho đến khi thanh XP đầy, sau đó nó sẽ sản xuất và đi ngủ. Mỗi gói thức ăn lấp đầy thanh XP một lượng nhất định, và **phần dư không bị mất**. Ví dụ: nếu nó có 90/100 XP và bạn cho ăn gói worth 20 XP, nó sẽ có 10/100 XP sau đó.

Mỗi loại động vật cần thức ăn khác nhau ở các cấp khác nhau, nhưng cấu trúc hiện tại là giống nhau cho cả ba loại.

**Cấp độ tối đa hiện tại là 15.** Động vật cấp cao sản xuất nhiều tài nguyên nhất nhưng cũng cần nhiều thức ăn nhất, vì vậy bạn phải cân nhắc khi nào nên cho ăn và khi nào nên bán.

### Ngủ và Vuốt ve (Sleep and Petting)

Sau khi con vật đi ngủ, bạn phải chờ một lúc để nó lấy lại sức. Tuy nhiên, định kỳ khi đang ngủ, con vật sẽ yêu cầu bạn chú ý. Một biểu tượng sẽ xuất hiện với một trong ba công cụ: **Bàn tay vuốt ve (Petting Hand)**, **Bàn chải (Brush)**, hoặc **Hộp nhạc (Music Box)**. Cả ba đều có thể chế tạo tại Workbench trên đảo nhà.

Khoảng thời gian cho mỗi lần vuốt ve được tính bằng tổng thời gian ngủ (sản xuất) chia cho 3. Bộ hẹn giờ chỉ reset khi bạn vuốt ve con vật.

Bạn không cần chọn đúng công cụ khi con vật ngủ. Nếu bạn có đúng công cụ nó yêu cầu, nó sẽ tự động được sử dụng khi chạm. Nếu không có, bạn sẽ không mất gì. Vuốt ve chỉ mang lại **thưởng thêm, không có hình phạt**.

Vuốt ve sẽ cho con vật **bonus XP** tùy theo công cụ sử dụng, nghĩa là nó sẽ cần ít thức ăn hơn khi thức dậy — điều này cực kỳ quan trọng với động vật cấp cao. thậm chí có thể lên cấp trong lúc ngủ, khiến nó sản xuất ngay khi thức dậy rồi lại đi ngủ.

Nếu bạn cần thêm trứng ngay, bạn có thể dùng **Doll** phù hợp để đánh thức con vật, cho phép cho ăn lại và nhận thêm sản phẩm. Loại Doll cần thiết hiển thị tại sfl.world hoặc khi chạm vào con vật. **Động vật cấp 15 không thể đánh thức bằng Doll.**

### Spice Boosts (Tăng cường gia vị)

Sau khi xây dựng **Aging Shed**, bạn có thể tạo hai vật phẩm ảnh hưởng đến động vật:
- **Salt Lick** — tăng sản lượng 5%
- **Honey Treat** — giảm thức ăn cần thiết mỗi gói 25%

Mỗi vật phẩm kéo dài **3 chu kỳ thu hoạch**, và chỉ có thể áp dụng **một trong hai** cho mỗi con vật, không thể dùng cả hai.

### Bệnh tật (Sickness)

Định kỳ động vật sẽ bị bệnh, hiển thị biểu tượng phía trên đầu. Động vật bệnh **giảm một nửa sản lượng** khi lên cấp, và bệnh **có thể lây lan**: mỗi con vật bệnh làm tăng nguy cơ con vật khác bị bệnh mỗi ngày. Bạn phải chữa trị càng sớm càng tốt.

Thuốc chữa bệnh là **Barn Delight**, được pha từ **Lemons và Honey** tại Feeder Machine.

Nếu không có tiền thuốc, bạn có thể bán con vật bị bệnh, nhưng chỉ nhận được **75% giá trị bounty** so với con vật khỏe mạnh.

### Bán và Tiền thưởng (Selling and Bounties)

Khi con Bò bắt đầu yêu cầu Mixed Grain, bạn biết đã đến lúc bán nó. Tại cùng menu mua động vật, bạn có thể bán. Mỗi công trình có **Bounty Board riêng**:
- Có thể bán tối đa 10 chickens, hoặc 5 cows và 5 sheep
- Phải đạt cấp độ yêu cầu (số bounty tăng theo cấp công trình)
- Ba loại bounty: **Coins**, **Chapter Tickets**, và **Chỉ Gems** (chỉ xuất hiện trong Auction Week hoặc tuần giữa các Chapter)

Con vật **phải đang thức** để bán. Nếu bị bệnh, chỉ nhận được **75% bounty** (làm tròn xuống).

> **Mẹo:** Động vật cấp cao cần nhiều thức ăn hơn cấp thấp. Kiểm tra [https://sfl.world/boost/](https://sfl.world/boost/) (nhập farm ID) để xem output cụ thể và quyết định có nên đẩy cow lên cấp 11 hay bán nó.

### Nâng cấp Công trình (Building Upgrades)

Mỗi công trình có thể nâng cấp để chứa thêm động vật. Yêu cầu và lợi ích hiển thị tại nút **Upgrade** góc trên bên trái mỗi công trình. Xem trước tại [https://sfl.world/info/animals](https://sfl.world/info/animals).

Mỗi công trình có thể chứa **tối đa 15 động vật** khi nâng cấp đầy đủ. Nếu cần thêm:
- **Barn Blueprint** — mở rộng thêm chỗ cho sheep/cows
- **Chicken Coop** — mở rộng thêm chỗ cho chickens

### Động vật Đột biến (Mutant Animals)

Đôi khi khi thu thập tài nguyên sau khi cho ăn, bạn có thể nhận được **mutant animal hiếm**. Chúng được xác định ngẫu nhiên theo Chapter hiện tại. Càng nuôi nhiều động vật, càng có nhiều cơ hội gặp mutant.

- **Rooster** (có trên marketplace) — **gấp đôi cơ hội** tìm mutant Chicken
- Hiện tại **không có vật phẩm nào** tăng cơ hội mutant Sheep hoặc Cow
- Mỗi mutant animal có **boost mạnh**, có thể dùng hoặc bán trên marketplace sau khi Chapter kết thúc

> Cơ hội rất nhỏ — nhiều người chơi từ khi tính năng animals ra mắt chưa bao giờ gặp mutant.

### Kỹ năng Chuyên môn hóa (Specialization Skills)

Chăn nuôi không hiệu quả nếu không có boost phù hợp. Cách tốt nhất để giảm chi phí và tăng sản lượng là **chọn một loại động vật** và tối ưu kỹ năng cho nó.

#### Các kỹ năng chung quan trọng:
- **Acre Farm crops** — tăng +1 cho tất cả cây trồng Advanced (Corn, Wheat, Barley)
- **Kale Mix** — thay thế Mixed Grain bằng 3x Kale (có thể đắt hơn và Kale chỉ trồng được 2 tuần/tháng)
- **Chonky Feed** — mỗi gói thức ăn cho **2x XP** nhưng kích thước gói **tăng 50%** (tiết kiệm thức ăn tổng thể, especially at higher levels)
- **Healthy Livestock** — khiến bệnh tật trở nên hiếm
- **Alternative Medicine** — giảm chi phí Barn Delight

#### Chicken Specialist
| Kỹ năng | Hiệu ứng |
|---|---|
| Fine Fibers | +0.1 Feather |
| Double Bale | +0.4 Egg total với Bale |
| Featherweight | +0.35 Feather, -0.1 Leather & Merino Wool |
| Abundant Harvest | +0.2 Egg |
| Clucky Grazing | 25% ít thức ăn hơn mỗi gói, 50% nhiều hơn cho hai loại kia |

#### Sheep Specialist
| Kỹ năng | Hiệu ứng |
|---|---|
| Fine Fibers | +0.1 Merino Wool |
| Bale Economy | +0.2 Wool |
| Double Bale | Thêm +0.2 Wool với Bale |
| Abundant Harvest | +0.2 Wool |
| Merino Whisperer | +0.35 Merino, -0.1 Leather & Feather |
| Sheepwise Diet | 25% ít thức ăn hơn mỗi gói, 50% nhiều hơn cho hai loại kia |

#### Cow Specialist
| Kỹ năng | Hiệu ứng |
|---|---|
| Fine Fibers | +0.1 Leather |
| Bale Economy | +0.2 Milk |
| Double Bale | Thêm +0.2 Milk với Bale |
| Abundant Harvest | +0.2 Milk |
| Leathercraft Mastery | +0.35 Leather, -0.1 Merino & Feather |
| Cow-Smart Nutrition | 25% ít thức ăn hơn mỗi gói, 50% nhiều hơn cho hai loại kia |
| Chonky Feed | 2x XP/gói, +50% kích thước gói (khuyến nghị cho Cows do nhu cầu thức ăn cao) |

> **Lưu ý:** Với các nhóm kỹ năng có bonus và penalty cùng nhau, bạn có thể lấy cả hai và đạt lợi nhuận ròng (ví dụ: Hectare và Acre Farm). Nhưng với animals, con số không hiệu quả như vậy. Chọn một loại động vật và tập trung kỹ năng sẽ luôn tốt hơn.

### Vật phẩm NFT

Nhiều vật phẩm hỗ trợ chăn nuôi, nhiều loại rất đắt. Các vật phẩm Gold Cow/Sheep/Egg cho phép cho ăn miễn phí nhưng vượt ngân sách hầu hết người chơi.

Một số vật phẩm giá phải chăng hơn:
- **Speed Chicken** — -10% thời gian sản xuất Egg (chickens thức dậy nhanh hơn, cho ăn thường xuyên hơn)
- **Fat Chicken** — -10% thức ăn cần thiết cho Chicken
- **Rich Chicken** — +0.1 Egg
- **Summer Chicken** — Chickens không bị bệnh vào mùa hè
- **Frozen Cow** — Cows không bị bệnh vào mùa đông
- **Nurse Sheep** — Sheep không bị bệnh vào mùa hè
- **White Sheep Onesie** — +0.25 Wool

Tìm kiếm tên động vật hoặc tài nguyên ("chicken", "egg", v.v.) trên marketplace để cập nhật danh sách mới nhất.

---

> **Gợi ý chiến lược:** Nếu muốn nguồn Eggs ổn định cho nấu ăn, chọn Chicken. Nếu muốn cung cấp Wool cho người làm Doll và người đi cua, chọn Sheep. Nếu muốn thử thách với nông trại bò sữa — cung cấp Milk cho thức ăn cao cấp và Leather cho Doll và dầu khoan — hãy nắm lấy cơ hội với Cow.
