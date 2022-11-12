--- Tìm optimal subset dựa vào tương quan giữa các input features ---

A. PEARSON CORRELATION
Loại bỏ những em có corr quá cao -> threshhold.

B. TƯƠNG QUAN PHI TUYẾN TÍNH (SU) - CATEGORICAL/DISCRETE DATA
(I) Irrelevant, (II) Weakly relevant and redundant feature, (III) Weakly relevant and non - redundant feature, (IV) Strongly relevant 
Giữ lại [(III), (IV)] = optimal subset

C. VẤN ĐỀ:
[1]: Xét tương quan giữa indicators multi-components so với single-component ?
[2]: Giá và các chỉ báo thông thường xu hướng thay đổi khá bám sát nhau => hiển nhiên tương quan tuyến tính cao
[3]: Xét tương quan phi tuyến tính:
Tất cả feature input đều là continuous data, việc chuyển tất cả -> discrete data để tìm correlation có là hợp lí ? (Thông thường khi input có cả continuous và discrete mới làm như thế)
Khi -> discrete = cách phân đoạn giá trị, các khoảng giá trị và giá trị tối đa nên đặt nhw nào ?

Hướng làm tạm thời: Xét tương quan trong 1 khoảng timestamp sẽ chọn được giá trị tối đa, còn khoảng giá trị có thể đặt tùy chỉnh(ví dụ chia thành 10 khoảng).

----
UPDATE:
test su trên 5 tập discrete_data với độ chia (10/20/50/99/999)

Long infor
Close price; SMA; EMA; K,D,J; EMA
Short infor: ADX; Close - Open : Biến động tuyệt đối; Trung bình giá nến = (close - open) / (high - low)  -> tổng biến động trong nến.

