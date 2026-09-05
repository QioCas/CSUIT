file http.pcapng
1. Thời gian phản hồi HTTP cho yêu cầu GET ở gói tin thứ 4 là bao lâu?
2. Có bao nhiêu gói tin SYN?
3. Tên của đối tượng HTTP lớn nhất đã được tải về là gì?
4. Mất bao lâu để tải xuống favicon.ico (bao gồm TCP connection setup/teardown)?
5. Gói tin số 131 là spurious retransmission. Gói tin nào trước đó nào đã gây ra "spurious" cho nó?
file sniff.pcapng
Kịch bản: file pcap này được lấy từ máy tính của Luciafer, cô ta đang cố gắng hack máy tính của ai đó, do đó các bạn hãy phân tích sâu hơn file pcap này để xem thử hành vi của Luciafer. Có thể tham khảo các gợi ý tìm kiếm sau:
1. Đầu tiên cô ta hình như có vẻ đang search một tên của ai đó ( có thể là nạn nhân), hãy tìm tên của nạn nhân này
2. Lucifer có vẻ đã hack thành công máy ai đó, sau đó cô ta làm gì tiếp theo
3. Sau khi tấn công thành công, lucifer tải 1 tập tin để sau đó chạy trên máy nạn nhân để giữ kết nối, tập tin ấy tên gì.
4. Ai đó trong công ty cảnh báo với luciafer rằng cô ta bị theo dõi "Stay away from ..", hãy tìm thử gói tin và nội dung họ trao đổi với nhau
