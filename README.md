<p align="center">
  <img src="https://www.uit.edu.vn/sites/vi/files/banner_uit_0.png" title="avatar_UIT">
</p>

<h1 align="center"> CS338 - NHẬN DẠNG </h1>
<h1 align="center"> ĐỒ ÁN CUỐI KỲ: PHÂN LOẠI CÁC LOẠI THỰC VẬT ĐÔNG NAM Á (KAGGLE)</h1>

## Giảng viên hỗ trợ:
    Ths. Đỗ Văn Tiến - tiendv@uit.edu.vn
## Mô tả bài toán
Input: Một bức ảnh một loại thực vật 

Output: Tên loại thực vật đó

Tập dữ liệu sử dụng [Bali26](https://www.kaggle.com/competitions/classification-of-plants-of-southeast-asia/data) là bộ dữ liệu dành riêng cho ngành ethnobotany, nghiên cứu về sự tương tác giữa con người và thực vật. Đây là bộ dữ liệu hình ảnh được thu thập
trên đảo Bali vào năm 2020 (và sửa đổi vào năm 2021) bởi các cư dân địa phương cùng với Cơ quan nghiên cứu và Đổi mới Quốc gia Indonesia. 

Metric đánh giá: Accuracy
## Kết quả
Accuracy đạt 1.0 trên tập private test. Team [UIT_A_H_H_N](https://www.kaggle.com/competitions/classification-of-plants-of-southeast-asia/leaderboard)
đạt hạng 4 chung cuộc

## Thành viên thực 
| STT | Họ tên | MSSV | E-mail | Github |
| :---: | --- | --- | --- | --- |
| 1 | Đỗ Nguyễn Hoàng Huy | 19521603 | 19521603@gm.uit.edu.vn | [Al3xDo](https://github.com/Al3xDo) |
| 2 | Trần Gia Nghĩa | 19521901 | 19521901@gm.uit.edu.vn | [SoulOfWindTGN](https://github.com/SoulOfWindTGN) |
| 3 | Hồ Mỹ Hạnh | 19521470 | 19521470@gm.uit.edu.vn | [homyhanh](https://github.com/homyhanh) |
| 4 | Nguyễn Thị Thúy An | 19521183 | 19521183@gm.uit.edu.vn | [UIT-19521183](https://github.com/UIT-19521183) |

## [Notebook](https://github.com/SoulOfWindTGN/Pattern_Recognition_Demo/tree/main/notebooks)
- [Swin Transformer for train](https://github.com/SoulOfWindTGN/Pattern_Recognition_Demo/blob/main/notebooks/SwinTransformerTrain.ipynb)
- [Swin Transformer for test](https://github.com/SoulOfWindTGN/Pattern_Recognition_Demo/blob/main/notebooks/SwinTransformerTest.ipynb)
- [MobileNet](https://github.com/SoulOfWindTGN/Pattern_Recognition_Demo/blob/main/notebooks/mobilenet.ipynb)
- [VGG16](https://github.com/SoulOfWindTGN/Pattern_Recognition_Demo/blob/main/notebooks/vgg-baseline.ipynb)
- [Color Histogram + HOG +LBP](https://github.com/SoulOfWindTGN/Pattern_Recognition_Demo/blob/main/notebooks/ColorHistogram_HOG_LBP.ipynb)
- [Color histogram + Hu Moments + Haralick Texture](https://github.com/SoulOfWindTGN/Pattern_Recognition_Demo/blob/main/notebooks/Color_histogram_Hu_Moments__Haralick_Texture.ipynb)
## Respository
- [Swin Transformer](https://github.com/SoulOfWindTGN/Swin-Transformer)
## Demo
### Instalation
#### Docker
`docker-compose up`
#### Manual (window)
`cd server && python pip install -r requirements.txt
make server`

`make client`

#### Diagram
<img src="https://github.com/Al3xDo/Pattern_Recognition_Demo/blob/main/Doc/PT_demo.png" width="100%">
<br/>
<img src="https://github.com/Al3xDo/Pattern_Recognition_Demo/blob/main/Doc/PT_demo-Page-2.png" width="100%">
<br/>
<img src="https://github.com/Al3xDo/Pattern_Recognition_Demo/blob/main/Doc/demo.png" width="100%">
<br/>
### Website Sreenshot
<img src="https://github.com/Al3xDo/Pattern_Recognition_Demo/blob/main/Doc/test.png" width="100%">
