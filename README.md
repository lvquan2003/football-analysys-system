# Football Analysis Project

## 🤝 Contributors

| **Members**                                          |                        **Email**                        |
| :--------------------------------------------------- | :-----------------------------------------------------: |
| [Đỗ Thành Nhân](https://github.com/ThanhNhan411)         | [21522400@gm.uit.edu.vn](mailto:21522400@gm.uit.edu.vn) |
| [Lê Văn Quân](https://github.com/lvquan2003) | [21522491@gm.uit.edu.vn](mailto:21522491@gm.uit.edu.vn) |
| [Đào Nam Thuận](https://github.com/daonamthuan)      | [21522649@gm.uit.edu.vn](mailto:21522649@gm.uit.edu.vn) |

## Requirements
- Python 3.x
- ultralytics
- supervision
- OpenCV
- streamlit
- NumPy
- Matplotlib
- Pandas
- gdown

## To run app
Firstly, clone this repository:
```
git clone https://github.com/lvquan2003/football-analysys-system.git
cd football-analysys-system
```
Then download our model uploaded in Google Drive using command below:
```
bash setup.sh
```
Finally, run app with streamlit:
```
streamlit run app.py
```

*Note: need to **tick in clear stub checkbox before running other videos**( (It has the effect of increasing the prediction speed for previously predicted videos so don't need if we predict other videos)*

To speed up the prediction process, you can provide the input video, output video, and the stub files here: [https://drive.google.com/drive/folders/1rBiXgezcRMo_7xAlnhaHeL5Q23FxpwaV?usp=sharing].

Please copy the stub files of the video into the corresponding folder ("stubs") to load them faster. This will reduce the processing time for videos that have already been predicted.
