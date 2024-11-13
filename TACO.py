import os
# data.yaml

train: "C:/Users/saart/Desktop/TACO/taco-dataset-yolo-format/train/images"
val: "C:/Users/saart/Desktop/TACO/taco-dataset-yolo-format/valid/images"

nc: 18  # Number of classes
names: ['Plastic', 'Paper', 'Metal', 'Glass', 'Trash', 'Organic Waste', 'Other', 'Rubber', 'Textile', 'Carton', 'Cigarette', 'Cup', 'Food waste', 'Lid', 'Other plastic', 'Paper', 'Plastic bag', 'Bottle']

#In terminal ---> git clone https://github.com/ultralytics/yolov5.git
#In terminal ---> cd yolov5

#In terminal ---> python C:\Users\saart\Desktop\TACO\yolov5\train.py --img 640 --batch 16 --epochs 50 --data "C:\Users\saart\Desktop\TACO\taco-dataset-yolo-format\data.yaml" --weights yolov5s.pt

