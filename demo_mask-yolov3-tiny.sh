export DARKNET=../../darknet
export PRJ_PATH=../2_objDetect/mask

cd $DARKNET
./darknet detector demo \
$PRJ_PATH/mask.data \
$PRJ_PATH/yolov3-tiny.cfg \
$PRJ_PATH/backup/yolov3-tiny.backup \
-c 1 -thresh .4
