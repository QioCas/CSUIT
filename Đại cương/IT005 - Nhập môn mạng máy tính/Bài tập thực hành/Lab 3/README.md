file: udp.pcap
Câu hỏi 1: Tính checksum thủ công của các gói tin UDP có Arrival Time: Jan  1, 1970 08:00:13.398602000 +08 (ví dụ: https://stackoverflow.com/questions/1767910/checksum-calculation-for-icmpv6-in-python/1769267#1769267)
Câu hỏi 2: Có 2 người bạn truyền gói tin cho nhau thông qua udp, biết là mỗi gói tin udp truyền đi 1 kí tự, trong lúc đó có ai đó gửi thêm những gói tin không liên quan và bị đánh dấu bởi security flags, hãy cố gắng lọc các gói tin đó ra và tìm thấy nội dung được truyền đi.
file: tcp.pcap
Câu hỏi 2: Tìm gói tin tương ứng với các sự kiện sau và phân tích ( tham khảo lại slide lý thuyết về các sự kiện)

TCP sender

- Sự kiện: Nhận dữ liệu từ tầng ứng dụng

- Sự kiện: timeout

- Sự kiện: nhận được ACK

TCP Receiver: ACK generation [RFC 5681]

- Nhận được segment đúng với STT đang chờ. Tất cả segment trước đó đã được ACK.

- Nhận được segment đúng với STT đang chờ, một segment chưa được ACK.

- Nhận được segment không đúng thứ tự (STT cao hơn).

- Nhận được segment trong khoảng bị trống (giữa STT đang chờ và STT nhận được trước đó).

