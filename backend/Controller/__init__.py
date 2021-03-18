import pickle, os

REGULATE_PATH = "./models"
label_encode = ["Công nghệ", "Du lịch", "Giáo dục", "Giải trí", "Kinh doanh", "Nhịp sống", "Phim ảnh", "Pháp luật", "Sống trẻ", "Sức khỏe", "Thế giới", "Thể thao", "Thời sự", "Thời trang", "Xe", "Xuất bản", "Âm nhạc", "Ẩm thực"]
nb_model = pickle.load(open(os.path.join(REGULATE_PATH, "model.pkl"), 'rb'))

