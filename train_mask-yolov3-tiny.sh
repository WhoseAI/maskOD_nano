export DARKNET=<full_Path_of_darknet>
export PRJ_PATH=<full_Path_of_Project>

cd $DARKNET
time ./darknet detector train \
$PRJ_PATH/mask.data \
$PRJ_PATH/yolov3-tiny.cfg \
darknet53.conv.74
