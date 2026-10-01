from flask import Flask, render_template_string, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# ============================================================
# DỮ LIỆU MENU
# ============================================================

MENU = [
    # ================= CÀ PHÊ VIỆT NAM =================
    {
        "id": 1,
        "name": "Cà phê đen đá",
        "category": "Cà phê Việt",
        "price": 25000,
        "description": "Cà phê Robusta đậm đà, pha phin truyền thống và dùng với đá.",
        "image": "https://images.unsplash.com/photo-1512568400610-62da28bc8a13?w=700"
    },
    {
        "id": 2,
        "name": "Cà phê sữa đá",
        "category": "Cà phê Việt",
        "price": 30000,
        "description": "Cà phê phin kết hợp sữa đặc, vị đậm đà và béo ngọt.",
        "image": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=700"
    },
    {
        "id": 3,
        "name": "Bạc xỉu",
        "category": "Cà phê Việt",
        "price": 32000,
        "description": "Sữa nhiều, cà phê vừa phải, thích hợp cho người không uống cà phê quá đậm.",
        "image": "https://images.unsplash.com/photo-1572449043416-55f4685c9bb7?w=700"
    },
    {
        "id": 4,
        "name": "Cà phê trứng",
        "category": "Cà phê Việt",
        "price": 45000,
        "description": "Cà phê kết hợp lớp kem trứng béo mịn theo phong cách Hà Nội.",
        "image": "https://images.unsplash.com/photo-1570968915860-54d5c301fa9f?w=700"
    },
    {
        "id": 5,
        "name": "Cà phê muối",
        "category": "Cà phê Việt",
        "price": 40000,
        "description": "Cà phê đậm đà kết hợp lớp kem muối mặn nhẹ, béo và thơm.",
        "image": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=700"
    },

    # ================= CÀ PHÊ QUỐC TẾ =================
    {
        "id": 6,
        "name": "Espresso",
        "category": "Cà phê Quốc tế",
        "price": 40000,
        "description": "Cà phê Espresso kiểu Ý với hương thơm mạnh và vị đậm.",
        "image": "https://images.unsplash.com/photo-1510707577719-ae7c14805e3a?w=700"
    },
    {
        "id": 7,
        "name": "Americano",
        "category": "Cà phê Quốc tế",
        "price": 40000,
        "description": "Espresso pha thêm nước nóng tạo nên hương vị nhẹ nhàng hơn.",
        "image": "https://images.unsplash.com/photo-1551030173-122aabc4489c?w=700"
    },
    {
        "id": 8,
        "name": "Cappuccino",
        "category": "Cà phê Quốc tế",
        "price": 50000,
        "description": "Espresso kết hợp sữa nóng và lớp bọt sữa mịn.",
        "image": "https://images.unsplash.com/photo-1534778101976-62847782c213?w=700"
    },
    {
        "id": 9,
        "name": "Latte",
        "category": "Cà phê Quốc tế",
        "price": 50000,
        "description": "Cà phê Espresso hòa quyện cùng sữa nóng, vị nhẹ và béo.",
        "image": "https://images.unsplash.com/photo-1561882468-9110e03e0f78?w=700"
    },
    {
        "id": 10,
        "name": "Mocha",
        "category": "Cà phê Quốc tế",
        "price": 55000,
        "description": "Sự kết hợp giữa Espresso, chocolate và sữa.",
        "image": "https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=700"
    },
    {
        "id": 11,
        "name": "Caramel Macchiato",
        "category": "Cà phê Quốc tế",
        "price": 55000,
        "description": "Cà phê sữa với caramel thơm ngọt.",
        "image": "https://images.unsplash.com/photo-1485808191679-5f86510681a2?w=700"
    },

    # ================= TRÀ & NƯỚC =================
    {
        "id": 12,
        "name": "Trà đào cam sả",
        "category": "Trà & Nước",
        "price": 40000,
        "description": "Trà đào thơm mát kết hợp cam và sả.",
        "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=700"
    },
    {
        "id": 13,
        "name": "Trà chanh mật ong",
        "category": "Trà & Nước",
        "price": 35000,
        "description": "Vị chua nhẹ của chanh hòa cùng mật ong ngọt dịu.",
        "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=700"
    },
    {
        "id": 14,
        "name": "Matcha Latte",
        "category": "Trà & Nước",
        "price": 50000,
        "description": "Matcha thơm nhẹ kết hợp sữa tươi.",
        "image": "https://images.unsplash.com/photo-1515823064-d6e0c04616a7?w=700"
    },
    {
        "id": 15,
        "name": "Chocolate đá xay",
        "category": "Trà & Nước",
        "price": 50000,
        "description": "Chocolate xay lạnh, béo và thơm.",
        "image": "https://images.unsplash.com/photo-1577805947697-89e18249d767?w=700"
    },

    # ================= KEM & TRÁNG MIỆNG =================
    {
        "id": 16,
        "name": "Kem Vanilla",
        "category": "Kem & Tráng miệng",
        "price": 30000,
        "description": "Kem vanilla mềm mịn, thơm nhẹ.",
        "image": "https://images.unsplash.com/photo-1570197788417-0e82375c9371?w=700"
    },
    {
        "id": 17,
        "name": "Kem Chocolate",
        "category": "Kem & Tráng miệng",
        "price": 30000,
        "description": "Kem chocolate đậm vị, thích hợp cho người yêu chocolate.",
        "image": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=700"
    },
    {
        "id": 18,
        "name": "Kem dâu",
        "category": "Kem & Tráng miệng",
        "price": 32000,
        "description": "Kem dâu thơm ngọt, màu sắc bắt mắt.",
        "image": "https://images.unsplash.com/photo-1497034825429-c343d7c6a68f?w=700"
    },
    {
        "id": 19,
        "name": "Affogato",
        "category": "Kem & Tráng miệng",
        "price": 55000,
        "description": "Kem vanilla kết hợp Espresso nóng theo phong cách Ý.",
        "image": "https://images.unsplash.com/photo-1551024601-bec78aea704b?w=700"
    },
    {
        "id": 20,
        "name": "Bánh Tiramisu",
        "category": "Kem & Tráng miệng",
        "price": 45000,
        "description": "Bánh Tiramisu mềm, thơm cà phê và cacao.",
        "image": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=700"
    },
    {
        "id": 21,
        "name": "Bánh Cheesecake",
        "category": "Kem & Tráng miệng",
        "price": 45000,
        "description": "Cheesecake mềm mịn, vị béo nhẹ.",
        "image": "https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=700"
    }
]

# ============================================================
# NHẬN XÉT KHÁCH HÀNG
# ============================================================

reviews = [
    {
        "name": "Nguyễn Minh",
        "rating": 5,
        "comment": "Cà phê ngon, giá hợp lý và nhân viên rất thân thiện.",
        "date": "01/10/2026"
    },
    {
        "name": "Hoàng Anh",
        "rating": 4,
        "comment": "Không gian đẹp, đồ uống khá ngon. Mình thích cà phê sữa đá.",
        "date": "01/10/2026"
    },
    {
        "name": "Thu Trang",
        "rating": 5,
        "comment": "Kem và bánh rất ngon, sẽ quay lại lần sau.",
        "date": "01/10/2026"
    }
]


# ============================================================
# HỖ TRỢ
# ============================================================

def format_money(number):
    return f"{number:,.0f} VNĐ"


# ============================================================
# TRANG CHỦ
# ============================================================

@app.route("/")
def home():
    category = request.args.get("category", "Tất cả")
    search = request.args.get("search", "").lower()

    filtered_menu = MENU

    if category != "Tất cả":
        filtered_menu = [
            item for item in filtered_menu
            if item["category"] == category
        ]

    if search:
        filtered_menu = [
            item for item in filtered_menu
            if search in item["name"].lower()
            or search in item["description"].lower()
        ]

    categories = [
        "Tất cả",
        "Cà phê Việt",
        "Cà phê Quốc tế",
        "Trà & Nước",
        "Kem & Tráng miệng"
    ]

    return render_template_string(
        TEMPLATE,
        menu=filtered_menu,
        categories=categories,
        selected_category=category,
        search=search,
        reviews=reviews,
        format_money=format_money
    )


# ============================================================
# THANH TOÁN
# ============================================================

@app.route("/checkout", methods=["POST"])
def checkout():

    order_items = []

    total = 0

    for item in MENU:
        quantity = request.form.get(
            f"quantity_{item['id']}",
            0,
            type=int
        )

        if quantity > 0:
            subtotal = item["price"] * quantity

            order_items.append({
                "name": item["name"],
                "quantity": quantity,
                "price": item["price"],
                "subtotal": subtotal
            })

            total += subtotal

    customer_name = request.form.get(
        "customer_name",
        "Khách hàng"
    )

    payment_method = request.form.get(
        "payment_method",
        "Tiền mặt"
    )

    return render_template_string(
        CHECKOUT_TEMPLATE,
        order_items=order_items,
        total=total,
        customer_name=customer_name,
        payment_method=payment_method,
        format_money=format_money
    )


# ============================================================
# NHẬN XÉT
# ============================================================

@app.route("/review", methods=["POST"])
def add_review():

    name = request.form.get("name", "").strip()
    rating = request.form.get("rating", 5, type=int)
    comment = request.form.get("comment", "").strip()

    if name and comment:

        reviews.insert(
            0,
            {
                "name": name,
                "rating": max(1, min(5, rating)),
                "comment": comment,
                "date": datetime.now().strftime("%d/%m/%Y")
            }
        )

    return redirect(url_for("home"))


# ============================================================
# HTML GIAO DIỆN
# ============================================================

TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>Minh Quân Coffee</title>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f7f2ec;
    color: #34251f;
}

header {
    background: linear-gradient(
        135deg,
        #3b2117,
        #74462c
    );

    color: white;
    padding: 35px 20px;
    text-align: center;
}

header h1 {
    margin: 0;
    font-size: 38px;
}

header p {
    font-size: 17px;
}

.container {
    max-width: 1200px;
    margin: auto;
    padding: 20px;
}

.search-box {
    background: white;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    box-shadow: 0 3px 12px #0001;
}

.search-box input {
    width: 70%;
    padding: 13px;
    border: 1px solid #ddd;
    border-radius: 8px;
}

.search-box button {
    padding: 13px 20px;
    border: none;
    border-radius: 8px;
    background: #6b3e26;
    color: white;
    cursor: pointer;
}

.categories {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-bottom: 25px;
}

.category {
    text-decoration: none;
    background: white;
    color: #5c3522;
    padding: 10px 16px;
    border-radius: 20px;
    box-shadow: 0 2px 7px #0001;
}

.category.active {
    background: #6b3e26;
    color: white;
}

.menu {
    display: grid;
    grid-template-columns:
        repeat(auto-fit, minmax(260px, 1fr));

    gap: 20px;
}

.card {
    background: white;
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 4px 15px #0002;
    transition: 0.2s;
}

.card:hover {
    transform: translateY(-5px);
}

.card img {
    width: 100%;
    height: 210px;
    object-fit: cover;
}

.card-content {
    padding: 18px;
}

.card h3 {
    margin-top: 0;
    color: #4a281b;
}

.description {
    color: #777;
    min-height: 48px;
}

.price {
    font-size: 21px;
    font-weight: bold;
    color: #b45f24;
}

.quantity {
    width: 70px;
    padding: 9px;
    margin-top: 10px;
    border: 1px solid #ddd;
    border-radius: 7px;
}

.checkout {
    background: white;
    margin-top: 35px;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 3px 15px #0001;
}

.checkout input,
.checkout select {
    width: 100%;
    padding: 12px;
    margin: 7px 0 15px;
    border: 1px solid #ddd;
    border-radius: 7px;
}

.checkout button {
    width: 100%;
    padding: 15px;
    background: #5c321f;
    color: white;
    border: none;
    border-radius: 9px;
    font-size: 17px;
    cursor: pointer;
}

.review-section {
    margin-top: 40px;
}

.review {
    background: white;
    padding: 20px;
    margin-bottom: 15px;
    border-radius: 15px;
    box-shadow: 0 2px 10px #0001;
}

.stars {
    color: #f5a623;
    font-size: 20px;
}

.review-form {
    background: white;
    padding: 25px;
    border-radius: 15px;
}

.review-form input,
.review-form textarea,
.review-form select {
    width: 100%;
    padding: 12px;
    margin: 8px 0 15px;
    border: 1px solid #ddd;
    border-radius: 7px;
}

.review-form textarea {
    height: 100px;
}

.review-form button {
    background: #6b3e26;
    color: white;
    padding: 12px 25px;
    border: none;
    border-radius: 7px;
    cursor: pointer;
}

footer {
    background: #302019;
    color: white;
    text-align: center;
    padding: 30px;
    margin-top: 50px;
}

@media(max-width:600px) {

    header h1 {
        font-size: 28px;
    }

    .search-box input {
        width: 100%;
        margin-bottom: 10px;
    }

    .search-box button {
        width: 100%;
    }

}

</style>

</head>

<body>

<header>

<h1>☕ MINH QUÂN COFFEE</h1>

<p>
Cà phê Việt Nam & Quốc tế -
Đồ uống & Kem tráng miệng
</p>

</header>


<div class="container">


<!-- TÌM KIẾM -->

<div class="search-box">

<form method="GET">

<input
type="text"
name="search"
placeholder="🔎 Tìm tên món..."
value="{{ search }}"
>

<button type="submit">
Tìm kiếm
</button>

</form>

</div>


<!-- DANH MỤC -->

<div class="categories">

{% for category in categories %}

<a
class="category
{% if selected_category == category %}
active
{% endif %}"
href="/?category={{ category }}"
>
{{ category }}
</a>

{% endfor %}

</div>


<h2>☕ MENU CỦA QUÁN</h2>


<form method="POST" action="/checkout">


<div class="menu">

{% for item in menu %}

<div class="card">

<img
src="{{ item.image }}"
alt="{{ item.name }}"
loading="lazy"
>

<div class="card-content">

<h3>{{ item.name }}</h3>

<p class="description">
{{ item.description }}
</p>

<p class="price">
{{ format_money(item.price) }}
</p>

<label>
Số lượng:
</label>

<input
class="quantity"
type="number"
name="quantity_{{ item.id }}"
value="0"
min="0"
>

</div>

</div>

{% endfor %}

</div>


<!-- THÔNG TIN KHÁCH -->

<div class="checkout">

<h2>🛒 Đặt món & Thanh toán</h2>

<label>
Tên khách hàng
</label>

<input
type="text"
name="customer_name"
placeholder="Nhập tên của bạn"
required
>


<label>
Phương thức thanh toán
</label>

<select name="payment_method">

<option>Tiền mặt</option>

<option>Chuyển khoản ngân hàng</option>

<option>Thanh toán tại quầy</option>

</select>


<button type="submit">
🧾 TÍNH TIỀN & THANH TOÁN
</button>

</div>

</form>


<!-- NHẬN XÉT -->

<div class="review-section">

<h2>⭐ Khách hàng nhận xét</h2>


{% for review in reviews %}

<div class="review">

<h3>{{ review.name }}</h3>

<div class="stars">

{% for i in range(review.rating) %}
★
{% endfor %}

</div>

<p>
{{ review.comment }}
</p>

<small>
{{ review.date }}
</small>

</div>

{% endfor %}


<h2>✍️ Viết nhận xét về quán</h2>

<div class="review-form">

<form method="POST" action="/review">

<label>
Tên của bạn
</label>

<input
type="text"
name="name"
placeholder="Nhập tên"
required
>


<label>
Đánh giá
</label>

<select name="rating">

<option value="5">★★★★★ - Rất tuyệt vời</option>
<option value="4">★★★★ - Tốt</option>
<option value="3">★★★ - Bình thường</option>
<option value="2">★★ - Chưa tốt</option>
<option value="1">★ - Cần cải thiện</option>

</select>


<label>
Nhận xét
</label>

<textarea
name="comment"
placeholder="Hãy chia sẻ cảm nhận của bạn..."
required
></textarea>


<button type="submit">
Gửi nhận xét
</button>

</form>

</div>

</div>

</div>


<footer>

<h3>☕ MINH QUÂN COFFEE</h3>

<p>
Cà phê ngon - Giá hợp lý - Phục vụ thân thiện
</p>

<p>
© 2026 Minh Quân Coffee
</p>

</footer>

</body>

</html>
"""


# ============================================================
# TRANG THANH TOÁN
# ============================================================

CHECKOUT_TEMPLATE = """

<!DOCTYPE html>

<html lang="vi">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>Hóa đơn - Minh Quân Coffee</title>

<style>

body {
    font-family: Arial;
    background: #f5efe8;
    margin: 0;
}

.invoice {
    max-width: 700px;
    margin: 40px auto;
    background: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 5px 20px #0002;
}

h1 {
    text-align: center;
    color: #5c321f;
}

.customer {
    background: #f7f1eb;
    padding: 15px;
    border-radius: 10px;
}

.item {
    display: flex;
    justify-content: space-between;
    padding: 12px 0;
    border-bottom: 1px solid #ddd;
}

.total {
    text-align: right;
    font-size: 24px;
    font-weight: bold;
    color: #b34e1e;
    margin-top: 20px;
}

.success {
    text-align: center;
    color: #268a48;
    font-size: 18px;
}

.back {
    display: block;
    text-align: center;
    background: #5c321f;
    color: white;
    padding: 13px;
    text-decoration: none;
    border-radius: 8px;
    margin-top: 25px;
}

</style>

</head>

<body>

<div class="invoice">

<h1>☕ MINH QUÂN COFFEE</h1>

<p class="success">
✅ Đơn hàng đã được tiếp nhận!
</p>


<div class="customer">

<p>
<strong>Khách hàng:</strong>
{{ customer_name }}
</p>

<p>
<strong>Thanh toán:</strong>
{{ payment_method }}
</p>

</div>


<h2>🧾 Hóa đơn</h2>


{% if order_items %}

{% for item in order_items %}

<div class="item">

<span>

{{ item.name }}

<br>

x {{ item.quantity }}

</span>

<strong>

{{ format_money(item.subtotal) }}

</strong>

</div>

{% endfor %}


<div class="total">

Tổng cộng:
{{ format_money(total) }}

</div>


{% else %}

<p>
Bạn chưa chọn món nào.
</p>

{% endif %}


<a class="back" href="/">
← Quay lại menu
</a>


</div>

</body>

</html>

"""


# ============================================================
# CHẠY APP
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
)
