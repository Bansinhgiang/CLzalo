<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Game Tài Xỉu Chẵn Lẻ</title>
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f2f2f2;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #F2C2FF;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
        }
        h1 {
            text-align: center;
            color: #e85d0a;
            margin-bottom: 20px;
            font-size: 26px;
        }
        .button {
            background-color: #F5A2D9;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            transition: all 0.3s ease;
            margin: 5px;
        }
        .button:hover {
            background-color: #e84393;
            transform: scale(1.05);
        }
        .section-box {
            display: none;
            padding: 20px;
            border-left: 5px solid #F5A2D9;
            margin-top: 20px;
            background-color: #f9f9f9;
            border-radius: 12px;
        }
        .alert, .rules {
            background-color: #ffcc00;
            color: #333;
            padding: 10px;
            margin-bottom: 20px;
            border-radius: 5px;
            text-align: center;
        }
        .rules {
            background-color: #f8d7da;
            color: #721c24;
        }
        .contact-support {
            text-align: center;
            margin-top: 20px;
            font-size: 16px;
            color: #333;
        }
        .contact-support a {
            color: #007bff;
            text-decoration: none;
            font-weight: bold;
        }
        .contact-support a:hover {
            text-decoration: underline;
        }
        .history-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        .history-table th, .history-table td {
            border: 1px solid #e0e0e0;
            padding: 10px;
            text-align: center;
        }
        .history-table th {
            background-color: #F5A2D9;
            color: #fff;
        }
    </style>
    <script>
        function showSection(sectionId) {
            var sections = document.getElementsByClassName('section-box');
            for (var i = 0; i < sections.length; i++) {
                sections[i].style.display = 'none';
            }
            document.getElementById(sectionId).style.display = 'block';
        }

        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(function() {
                alert("Đã sao chép số: " + text);
            }, function(err) {
                console.error('Không thể sao chép: ', err);
            });
        }
    </script>
</head>
<body>
    <div class="container">
        <h1>ZALO365.VIN - Đỉnh Cao Chẵn Lẻ</h1>
        
        <div class="alert">💡 Lưu ý: Hãy đảm bảo bạn đọc kỹ hướng dẫn chơi trước khi tham gia.</div>
        
        <div class="rules">
            <strong>Quy định xử lý lỗi:</strong>
            <ol>
                <li>Inbox telegram duy nhất @ Admin không nhắn tin trước.</li>
                <li>Sai nội dung/Quên nội dung hoàn 90% gốc.</li>
                <li>Sai hạn mức hoàn 50% gốc (dưới 20k không hoàn).</li>
                <li>Giao dịch vào số full 50 lần GD/h hoặc hết hạn mức 40M đã OFF hoàn 100% gốc (tối đa 30p).</li>
                <li>Tuyệt đối không được đánh chồng bill.</li>
                <li>Tải app Zalopay về để chơi.</li>
                <li>Chỉ áp dụng với bill thắng trong 30 phút.</li>
            </ol>
            <p>Khi bạn bỏ qua chú ý này, đồng nghĩa với việc bạn đã đọc và chấp nhận những điều đó!</p>
        </div>

        <div class="button" onclick="showSection('chan-le-instructions')">🎲 Chẵn Lẻ</div>
        <div class="button" onclick="showSection('tai-xiu-instructions')">🎲 Tài Xỉu</div>
        <div class="button" onclick="showSection('chan-le2-instructions')">🎲 Chẵn Lẻ 2</div>
        <div class="button" onclick="showSection('tai-xiu2-instructions')">🎲 Tài Xỉu 2</div>
        <div class="button" onclick="showSection('promotion')">🎉 Khuyến Mãi</div>
        <div class="button" onclick="showSection('transaction-check')">🔍 Kiểm Tra Giao Dịch</div>
        <div class="button" onclick="showSection('zalopay-status')">💳 Trạng Thái ZaloPay</div>

        <div id="chan-le-instructions" class="section-box">
            <h2>Cách Chơi Chẵn Lẻ</h2>
            <p>- Chẵn Lẻ tính kết quả bằng số cuối mã giao dịch.</p>
            <p>- Đặt cược:</p>
            <ul>
                <li>Chọn số tiền cược tối thiểu 10k.</li>
                <li>KHÔNG CẦN GHI NỘI DUNG
VD: Bạn đặt Chẵn 50.000. Hãy chuyển số tiền: 50012 (12 là MÃ)
VD: Bạn đặt Lẻ 50.000. Hãy chuyển số tiền: 50011 (11 là MÃ).</li>
                <li>Chẵn ( 2, 4, 6, 8) và Lẻ (1, 3, 5, 7).</li>
                <li>Chuyển tiền vào tài khoản:</li>
                <li class="phone-number" onclick="copyToClipboard('0582310730')">0582310730</li>
                <li class="phone-number" onclick="copyToClipboard('0528938310')">0528938310</li>
            </ul>
            <p>[  12 ]  2 - 4 - 6 - 8  x2.5</p>
            <p>[  11 ] 1 - 3 - 5 - 7  x2.5</p>
            <p>TIỀN THẮNG = TIỀN CƯỢC x 2.5</p>
        </div>

        <div id="tai-xiu-instructions" class="section-box">
            <h2>Cách Chơi Tài Xỉu</h2>
            <p>- Tài Xỉu tính kết quả bằng số cuối mã giao dịch.</p>
            <p>- Đặt cược:</p>
            <ul>
                <li>Chọn số tiền cược tối thiểu 10k.</li>
                <li>KHÔNG CẦN GHI NỘI DUNG
VD: Bạn đặt Tài 50.000. Hãy chuyển số tiền: 50014 (14 là MÃ)
VD: Bạn đặt Xỉu 50.000. Hãy chuyển số tiền: 50013 (13 là MÃ).</li>
                <li>Chọn giữa Tài (6-8) và Xỉu (2-5).</li>
                <li>Chuyển tiền vào tài khoản:</li>
                <li class="phone-number" onclick="copyToClipboard('0582310730')">0582310730</li>
                <li class="phone-number" onclick="copyToClipboard('0528938310')">0528938310</li>
            </ul>
            <p>[  13 ]  5 - 6 - 7 - 8  x2.5</p>
            <p>[  14 ]  1 - 2 - 3 - 4  x2.5</p>
            <p>TIỀN THẮNG = TIỀN CƯỢC x 2.5</p>
        </div>
        
        <div id="chan-le2-instructions" class="section-box">
            <h2>Cách Chơi Chẵn Lẻ 2</h2>
            <p>- Chẵn Lẻ 2 tính kết quả bằng số cuối mã giao dịch.</p>
            <p>- Đặt cược:</p><ul>
                <li>Chọn số tiền cược tối thiểu 10k.</li>
                <li>KHÔNG CẦN GHI NỘI DUNG
VD: Bạn đặt Chẵn 50.000. Hãy chuyển số tiền: 50012 (12 là MÃ)
VD: Bạn đặt Lẻ 50.000. Hãy chuyển số tiền: 50011 (11 là MÃ).</li>
                <li>Chẵn ( 2, 4, 6, 8) và Lẻ (1, 3, 5, 7).</li>
                <li>Chuyển tiền vào tài khoản:</li>
                <li class="phone-number" onclick="copyToClipboard('0582310730')">0582310730</li>
                <li class="phone-number" onclick="copyToClipboard('0528938310')">0528938310</li>
            </ul>
            <p>[  12 ]  2 - 4 - 6 - 8  x2.5</p>
            <p>[  11 ] 1 - 3 - 5 - 7  x2.5</p>
            <p>TIỀN THẮNG = TIỀN CƯỢC x 2.5</p>
        </div>

        <div id="tai-xiu2-instructions" class="section-box">
            <h2>Cách Chơi Tài Xỉu 2</h2>
            <p>- Tài Xỉu 2 tính kết quả bằng số cuối mã giao dịch.</p>
            <p>- Đặt cược:</p>
            <ul>
                <li>Chọn số tiền cược tối thiểu 10k.</li>
                <li>KHÔNG CẦN GHI NỘI DUNG
VD: Bạn đặt Tài 50.000. Hãy chuyển số tiền: 50014 (14 là MÃ)
VD: Bạn đặt Xỉu 50.000. Hãy chuyển số tiền: 50013 (13 là MÃ).</li>
                <li>Chọn giữa Tài (6-8) và Xỉu (2-5).</li>
                <li>Chuyển tiền vào tài khoản:</li>
                <li class="phone-number" onclick="copyToClipboard('0582310730')">0582310730</li>
                <li class="phone-number" onclick="copyToClipboard('0528938310')">0528938310</li>
            </ul>
            <p>[  13 ]  5 - 6 - 7 - 8  x2.5</p>
            <p>[  14 ]  1 - 2 - 3 - 4  x2.5</p>
            <p>TIỀN THẮNG = TIỀN CƯỢC x 2.5</p>
        </div>

        <div id="promotion" class="section-box">
            <h2>Khuyến Mãi</h2>
            <p>Chương trình khuyến mãi hấp dẫn sẽ được cập nhật thường xuyên. Hãy theo dõi để không bỏ lỡ cơ hội!</p>
        </div>

        <div id="transaction-check" class="section-box">
            <h2>Kiểm Tra Giao Dịch</h2>
            <p>Để kiểm tra giao dịch của bạn, vui lòng liên hệ với Admin.</p>
        </div>

        <div id="zalopay-status" class="section-box">
            <h2>Trạng Thái ZaloPay</h2>
            <p>Để kiểm tra trạng thái tài khoản ZaloPay, vui lòng liên hệ với Admin.</p>
        </div>

        <h2>Lịch Sử Thắng</h2>
        <p>Làm mới sau 10 giây</p>
        <table class="history-table">
            <thead>
                <tr>
                    <th>Số Người Chơi</th>
                    <th>Tiền Đặt</th>
                    <th>Tiền Thắng</th>
                    <th>Nội Dung</th>
                    <th>Trạng Thái</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>****1574</td>
                    <td>100.012 VND</td>
                    <td>230.028 VND</td>
                    <td>12</td>
                    <td>Thắng</td>
                </tr>
                <tr>
                    <td>****1574</td>
                    <td>70.011 VND</td>
                    <td>161.025 VND</td>
                    <td>11</td>
                    <td>Thắng</td>
                </tr>
                <tr>
                    <td>****1574</td>
                    <td>50.011 VND</td>
                    <td>115.025 VND</td>
                    <td>11</td>
                    <td>Thắng</td>
                </tr>
                <tr>
                    <td>****1574</td>
                    <td>100.011 VND</td>
                    <td>230.025 VND</td>
                    <td>11</td>
                    <td>Thắng</td>
                </tr>
                <tr>
                    <td>****1574</td>
                    <td>60.012 VND</td>
                    <td>138.028 VND</td>
                    <td>12</td>
                    <td>Thắng</td>
                </tr>
                <tr>
                    <td>****1574</td>
                    <td>70.012 VND</td>
                    <td>161.028 VND</td>
                    <td>12</td>
                    <td>Thắng</td>
                </tr>
                <tr>
                    <td>****1574</td>
                    <td>60.011 VND</td>
                    <td>138.025 VND</td>
                    <td>11</td>
                    <td>Thắng</td>
                </tr>
                <tr>
                    <td>****1574</td>
                    <td>300.012 VND</td>
                    <td>690.028 VND</td>
                    <td>12</td>
                    <td>Thắng</td>
                </tr>
                <tr>
                    <td>****1574</td>
                    <td>160.011 VND</td>
                    <td>368.025 VND</td>
                    <td>11</td>
                    <td>Thắng</td>
                </tr>
                <tr>
                    <td>****1574</td>
                    <td>70.011 VND</td>
                    <td>161.025 VND</td>
                    <td>11</td>
                    <td>Thắng</td>
                </tr>
            </tbody>
        </table>

        <div class="contact-support">
            <p>💬 Liên hệ hỗ trợ: <a href="https://t.me/ZALO365">Telegram</a></p>
        </div>
    </div>
</body>
</html>