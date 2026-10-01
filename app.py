import streamlit as st
from datetime import datetime

# ============================================================
# MINH QUÂN COFFEE - ỨNG DỤNG QUÁN CÀ PHÊ BẰNG STREAMLIT
# Chạy: streamlit run app.py
# ============================================================

st.set_page_config(
    page_title="Minh Quân Coffee",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# GIAO DIỆN
# ============================================================
st.markdown("""
<style>
.stApp {
    background: #f7f2ec;
}

.hero {
    background: linear-gradient(135deg, #3b2117, #7a4a2d);
    color: white;
    padding: 35px 20px;
    border-radius: 22px;
    text-align: center;
    margin-bottom: 25px;
}

.hero h1 {
    margin: 0;
    font-size: 42px;
}

.hero p {
    margin-top: 10px;
    font-size: 18px;
}

.price {
    color: #b45f24;
    font-size: 21px;
    font-weight: bold;
}

.review-card {
    background: white;
    padding: 18px;
    border-radius: 15px;
    margin: 10px 0;
    border: 1px solid #eaded3;
}

.total-card {
    background: #fff5e9;
    padding: 20px;
    border-radius: 15px;
    border: 2px solid #d6a16f;
}

.info-card {
    background: white;
    padding: 18px;
    border-radius: 15px;
    border: 1px solid #eaded3;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# HÀM
# ============================================================
def money(value):
    return f"{value:,.0f} VNĐ"


def star_text(rating):
    return "★" * rating + "☆" * (5 - rating)


# ============================================================
# MENU
# ============================================================
MENU = [
    # ---------------- CÀ PHÊ VIỆT ----------------
    {
        "id": 1,
        "name": "Cà phê đen đá",
        "category": "Cà phê Việt",
        "price": 25000,
        "description": "Cà phê phin Việt Nam đậm đà, thơm và sảng khoái.",
        "image": "https://images.unsplash.com/photo-1512568400610-62da28bc8a13?w=900"
    },
    {
        "id": 2,
        "name": "Cà phê sữa đá",
        "category": "Cà phê Việt",
        "price": 30000,
        "description": "Cà phê phin kết hợp sữa đặc, vị béo ngọt vừa phải.",
        "image": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=900"
    },
    {
        "id": 3,
        "name": "Bạc xỉu",
        "category": "Cà phê Việt",
        "price": 32000,
        "description": "Nhiều sữa, cà phê nhẹ, phù hợp với nhiều khách hàng.",
        "image": "https://images.unsplash.com/photo-1572449043416-55f4685c9bb7?w=900"
    },
    {
        "id": 4,
        "name": "Cà phê trứng",
        "category": "Cà phê Việt",
        "price": 45000,
        "description": "Cà phê thơm kết hợp lớp kem trứng béo mịn.",
        "image": "https://images.unsplash.com/photo-1570968915860-54d5c301fa9f?w=900"
    },
    {
        "id": 5,
        "name": "Cà phê muối",
        "category": "Cà phê Việt",
        "price": 40000,
        "description": "Cà phê đậm vị kết hợp lớp kem muối béo nhẹ.",
        "image": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=900"
    },
    {
        "id": 6,
        "name": "Cà phê dừa",
        "category": "Cà phê Việt",
        "price": 45000,
        "description": "Cà phê kết hợp vị dừa thơm béo, mát lạnh.",
        "image": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=900"
    },

    # ---------------- CÀ PHÊ QUỐC TẾ ----------------
    {
        "id": 7,
        "name": "Espresso",
        "category": "Cà phê Quốc tế",
        "price": 40000,
        "description": "Espresso phong cách Ý, đậm đà và thơm.",
        "image": "https://images.unsplash.com/photo-1510707577719-ae7c14805e3a?w=900"
    },
    {
        "id": 8,
        "name": "Americano",
        "category": "Cà phê Quốc tế",
        "price": 40000,
        "description": "Espresso pha cùng nước, vị nhẹ và dễ uống.",
        "image": "https://images.unsplash.com/photo-1551030173-122aabc4489c?w=900"
    },
    {
        "id": 9,
        "name": "Cappuccino",
        "category": "Cà phê Quốc tế",
        "price": 50000,
        "description": "Espresso, sữa nóng và lớp bọt sữa mịn.",
        "image": "https://images.unsplash.com/photo-1534778101976-62847782c213?w=900"
    },
    {
        "id": 10,
        "name": "Latte",
        "category": "Cà phê Quốc tế",
        "price": 50000,
        "description": "Espresso kết hợp sữa, vị dịu và béo.",
        "image": "https://images.unsplash.com/photo-1561882468-9110e03e0f78?w=900"
    },
    {
        "id": 11,
        "name": "Mocha",
        "category": "Cà phê Quốc tế",
        "price": 55000,
        "description": "Sự kết hợp giữa cà phê, chocolate và sữa.",
        "image": "https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=900"
    },
    {
        "id": 12,
        "name": "Caramel Macchiato",
        "category": "Cà phê Quốc tế",
        "price": 55000,
        "description": "Cà phê sữa thơm cùng caramel ngọt dịu.",
        "image": "https://images.unsplash.com/photo-1485808191679-5f86510681a2?w=900"
    },
    {
        "id": 13,
        "name": "Flat White",
        "category": "Cà phê Quốc tế",
        "price": 50000,
        "description": "Espresso cùng sữa nóng, vị cà phê rõ và mượt.",
        "image": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=900"
    },

    # ---------------- TRÀ & NƯỚC ----------------
    {
        "id": 14,
        "name": "Trà đào cam sả",
        "category": "Trà & Nước",
        "price": 40000,
        "description": "Trà đào thanh mát kết hợp cam và sả.",
        "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=900"
    },
    {
        "id": 15,
        "name": "Trà chanh mật ong",
        "category": "Trà & Nước",
        "price": 35000,
        "description": "Chanh tươi và mật ong, vị chua ngọt dễ uống.",
        "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=900"
    },
    {
        "id": 16,
        "name": "Matcha Latte",
        "category": "Trà & Nước",
        "price": 50000,
        "description": "Matcha thơm nhẹ kết hợp sữa.",
        "image": "https://images.unsplash.com/photo-1515823064-d6e0c04616a7?w=900"
    },
    {
        "id": 17,
        "name": "Chocolate đá xay",
        "category": "Trà & Nước",
        "price": 50000,
        "description": "Chocolate xay lạnh, béo và thơm.",
        "image": "https://images.unsplash.com/photo-1577805947697-89e18249d767?w=900"
    },
    {
        "id": 18,
        "name": "Trà sữa truyền thống",
        "category": "Trà & Nước",
        "price": 35000,
        "description": "Trà sữa thơm béo, phù hợp với nhiều độ tuổi.",
        "image": "https://images.unsplash.com/photo-1558857563-b371033873b8?w=900"
    },

    # ---------------- KEM & TRÁNG MIỆNG ----------------
    {
        "id": 19,
        "name": "Kem Vanilla",
        "category": "Kem & Tráng miệng",
        "price": 30000,
        "description": "Kem vanilla mềm mịn, thơm nhẹ.",
        "image": "https://images.unsplash.com/photo-1570197788417-0e82375c9371?w=900"
    },
    {
        "id": 20,
        "name": "Kem Chocolate",
        "category": "Kem & Tráng miệng",
        "price": 30000,
        "description": "Kem chocolate đậm vị, thơm ngon.",
        "image": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=900"
    },
    {
        "id": 21,
        "name": "Kem dâu",
        "category": "Kem & Tráng miệng",
        "price": 32000,
        "description": "Kem dâu thơm ngọt, màu sắc bắt mắt.",
        "image": "https://images.unsplash.com/photo-1497034825429-c343d7c6a68f?w=900"
    },
    {
        "id": 22,
        "name": "Kem Cookies",
        "category": "Kem & Tráng miệng",
        "price": 35000,
        "description": "Kem sữa kết hợp vụn bánh cookies giòn thơm.",
        "image": "https://images.unsplash.com/photo-1567206563064-6f60f40a2b57?w=900"
    },
    {
        "id": 23,
        "name": "Affogato",
        "category": "Kem & Tráng miệng",
        "price": 55000,
        "description": "Kem vanilla kết hợp Espresso nóng kiểu Ý.",
        "image": "https://images.unsplash.com/photo-1551024601-bec78aea704b?w=900"
    },
    {
        "id": 24,
        "name": "Tiramisu",
        "category": "Kem & Tráng miệng",
        "price": 45000,
        "description": "Bánh Tiramisu mềm, thơm cà phê và cacao.",
        "image": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=900"
    },
    {
        "id": 25,
        "name": "Cheesecake",
        "category": "Kem & Tráng miệng",
        "price": 45000,
        "description": "Bánh phô mai mềm mịn, béo nhẹ.",
        "image": "https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=900"
    },
]


# ============================================================
# SESSION STATE
# ============================================================
if "cart" not in st.session_state:
    st.session_state.cart = {}

if "reviews" not in st.session_state:
    st.session_state.reviews = [
        {
            "name": "Nguyễn Minh",
            "rating": 5,
            "comment": "Cà phê ngon, giá hợp lý và nhân viên thân thiện.",
            "date": "01/10/2026"
        },
        {
            "name": "Hoàng Anh",
            "rating": 4,
            "comment": "Không gian đẹp, đồ uống khá ngon.",
            "date": "01/10/2026"
        },
        {
            "name": "Thu Trang",
            "rating": 5,
            "comment": "Kem và bánh rất ngon, sẽ quay lại.",
            "date": "01/10/2026"
        }
    ]


# ============================================================
# HEADER
# ============================================================
st.markdown("""
<div class="hero">
    <h1>☕ MINH QUÂN COFFEE</h1>
    <p>Cà phê Việt Nam • Cà phê Quốc tế • Trà • Kem • Tráng miệng</p>
</div>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR - TÌM KIẾM / LỌC
# ============================================================
with st.sidebar:
    st.header("🔎 Tìm kiếm món")

    search = st.text_input(
        "Tên món",
        placeholder="Ví dụ: Latte, Kem..."
    )

    category = st.selectbox(
        "Danh mục",
        [
            "Tất cả",
            "Cà phê Việt",
            "Cà phê Quốc tế",
            "Trà & Nước",
            "Kem & Tráng miệng"
        ]
    )

    st.markdown("---")
    st.subheader("💡 Giá cả")
    st.write(
        "Menu được xây dựng với nhiều mức giá "
        "từ 25.000 - 55.000 VNĐ, phù hợp với "
        "học sinh, sinh viên, người đi làm và gia đình."
    )


# ============================================================
# LỌC MENU
# ============================================================
filtered_menu = MENU[:]

if category != "Tất cả":
    filtered_menu = [
        item for item in filtered_menu
        if item["category"] == category
    ]

if search.strip():
    keyword = search.strip().lower()
    filtered_menu = [
        item for item in filtered_menu
        if keyword in item["name"].lower()
        or keyword in item["description"].lower()
    ]


# ============================================================
# HIỂN THỊ MENU
# ============================================================
st.header("🍽️ MENU QUÁN")

if not filtered_menu:
    st.warning("Không tìm thấy món phù hợp.")
else:
    for start in range(0, len(filtered_menu), 3):
        row = filtered_menu[start:start + 3]
        columns = st.columns(3)

        for column, item in zip(columns, row):
            with column:
                st.image(
                    item["image"],
                    use_container_width=True
                )

                st.subheader(item["name"])
                st.caption(item["category"])
                st.write(item["description"])

                st.markdown(
                    f'<div class="price">{money(item["price"])}</div>',
                    unsafe_allow_html=True
                )

                current = st.session_state.cart.get(
                    item["id"], 0
                )

                quantity = st.number_input(
                    "Số lượng",
                    min_value=0,
                    max_value=50,
                    value=current,
                    step=1,
                    key=f"qty_{item['id']}"
                )

                if quantity > 0:
                    st.session_state.cart[item["id"]] = quantity
                else:
                    st.session_state.cart.pop(item["id"], None)

                st.divider()


# ============================================================
# GIỎ HÀNG & TÍNH TIỀN
# ============================================================
st.header("🛒 GIỎ HÀNG & TÍNH TIỀN")

cart_items = []
total = 0

for item in MENU:
    quantity = st.session_state.cart.get(item["id"], 0)

    if quantity > 0:
        subtotal = item["price"] * quantity
        total += subtotal

        cart_items.append(
            {
                "name": item["name"],
                "quantity": quantity,
                "price": item["price"],
                "subtotal": subtotal
            }
        )


if cart_items:
    for item in cart_items:
        col1, col2, col3 = st.columns([5, 2, 3])

        with col1:
            st.write(f"**{item['name']}**")

        with col2:
            st.write(f"x {item['quantity']}")

        with col3:
            st.write(f"**{money(item['subtotal'])}**")

    st.markdown(
        f"""
        <div class="total-card">
            <h2>💰 TỔNG CỘNG: {money(total)}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("👤 Thông tin khách hàng")

    customer_name = st.text_input(
        "Tên khách hàng",
        placeholder="Nhập tên khách hàng"
    )

    phone = st.text_input(
        "Số điện thoại",
        placeholder="Nhập số điện thoại"
    )

    payment = st.selectbox(
        "💳 Phương thức thanh toán",
        [
            "Tiền mặt",
            "Chuyển khoản ngân hàng",
            "Thanh toán tại quầy"
        ]
    )

    note = st.text_area(
        "📝 Ghi chú",
        placeholder="Ví dụ: ít đá, ít ngọt..."
    )

    if st.button(
        "✅ XÁC NHẬN ĐẶT HÀNG",
        type="primary",
        use_container_width=True
    ):
        if not customer_name.strip():
            st.warning("Vui lòng nhập tên khách hàng.")
        else:
            st.success(
                f"Đặt hàng thành công! Xin chào {customer_name}."
            )

            st.write(f"**Tổng tiền:** {money(total)}")
            st.write(f"**Phương thức:** {payment}")

            if phone.strip():
                st.write(f"**Số điện thoại:** {phone}")

            if note.strip():
                st.write(f"**Ghi chú:** {note}")

            st.info(
                "☕ Quán cảm ơn bạn đã mua hàng. "
                "Chúc bạn có một ngày thật vui!"
            )

            # Xóa giỏ hàng sau khi đặt hàng
            st.session_state.cart = {}

else:
    st.info(
        "🛍️ Giỏ hàng đang trống. "
        "Hãy chọn số lượng món ở phần MENU."
    )


# ============================================================
# NHẬN XÉT
# ============================================================
st.markdown("---")
st.header("⭐ NHẬN XÉT CỦA KHÁCH HÀNG")

for review in st.session_state.reviews:
    st.markdown(
        f"""
        <div class="review-card">
            <b>👤 {review["name"]}</b>
            <div style="color:#f2a900;font-size:22px">
                {star_text(review["rating"])}
            </div>
            <p>{review["comment"]}</p>
            <small>📅 {review["date"]}</small>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FORM GỬI NHẬN XÉT
# ============================================================
st.subheader("✍️ Viết nhận xét về quán")

with st.form("review_form"):
    review_name = st.text_input(
        "Tên của bạn",
        placeholder="Nhập tên"
    )

    review_rating = st.slider(
        "Đánh giá",
        min_value=1,
        max_value=5,
        value=5
    )

    review_comment = st.text_area(
        "Nội dung nhận xét",
        placeholder="Hãy chia sẻ cảm nhận của bạn..."
    )

    submit_review = st.form_submit_button(
        "⭐ GỬI NHẬN XÉT"
    )

    if submit_review:
        if (
            not review_name.strip()
            or not review_comment.strip()
        ):
            st.warning(
                "Vui lòng nhập tên và nội dung nhận xét."
            )
        else:
            st.session_state.reviews.insert(
                0,
                {
                    "name": review_name.strip(),
                    "rating": review_rating,
                    "comment": review_comment.strip(),
                    "date": datetime.now().strftime("%d/%m/%Y")
                }
            )

            st.success(
                "Cảm ơn bạn đã đánh giá Minh Quân Coffee! ❤️"
            )

            st.rerun()


# ============================================================
# FOOTER
# ============================================================
st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;padding:20px">
        <h3>☕ MINH QUÂN COFFEE</h3>
        <p>Cà phê ngon • Giá hợp lý • Phục vụ thân thiện</p>
        <small>© 2026 Minh Quân Coffee</small>
    </div>
    """,
    unsafe_allow_html=True
  )
