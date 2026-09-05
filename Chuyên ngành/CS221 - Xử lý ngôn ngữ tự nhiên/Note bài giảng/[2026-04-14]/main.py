from PIL import Image
import numpy as np
from matplotlib.colors import rgb_to_hsv, hsv_to_rgb

def change_image_tone(
    input_path,
    output_path,
    hue_shift=0.0,
    saturation_scale=1.0,
    value_scale=1.0,
    gray_darken=0.65,          # < 1.0 thì chữ xám sẽ đậm hơn
    gray_sat_threshold=0.08,   # màu có saturation thấp sẽ được xem là gần xám
    gray_value_min=0.25,       # tránh vùng quá tối
    gray_value_max=0.88        # tránh bắt nền trắng
):
    # Đọc ảnh
    img = Image.open(input_path).convert("RGB")
    arr = np.array(img).astype(np.float32) / 255.0

    # RGB -> HSV
    hsv = rgb_to_hsv(arr)

    # Thay đổi sắc độ tổng thể nếu cần
    hsv[..., 0] = (hsv[..., 0] + hue_shift) % 1.0
    hsv[..., 1] = np.clip(hsv[..., 1] * saturation_scale, 0, 1)
    hsv[..., 2] = np.clip(hsv[..., 2] * value_scale, 0, 1)

    # Chọn vùng màu xám: saturation thấp, độ sáng nằm trong khoảng hợp lý
    gray_mask = (
        (hsv[..., 1] < gray_sat_threshold) &
        (hsv[..., 2] > gray_value_min) &
        (hsv[..., 2] < gray_value_max)
    )

    # Làm chữ xám đậm hơn bằng cách giảm value
    hsv[..., 2][gray_mask] = np.clip(hsv[..., 2][gray_mask] * gray_darken, 0, 1)

    # HSV -> RGB
    new_arr = (hsv_to_rgb(hsv) * 255).astype(np.uint8)
    new_img = Image.fromarray(new_arr)
    new_img.save(output_path)

# input_path = "./minh_hoa_tich_luy_xac_suat_top_p.png"
# input_path = "./minh_hoa_cat_duoi_top_k_sampling.png"
input_path = "./img/hinh_dang_phan_phoi_thay_doi_theo_ngu_canh.png"
output_path = input_path[:-4] + "_modified.png"

change_image_tone(
    input_path,
    output_path,
    hue_shift=0.0,
    saturation_scale=1.0,
    value_scale=1.0,
    gray_darken=0.70
)

print("Đã lưu ảnh mới.")