#include <opencv2/opencv.hpp>
#include <string>
using namespace cv;
int main(){
VideoCapture capture(0);
int key;
int i=0;    //图片数
int j=0;    //视频数
char pName[100];//图片文件名
char vName[100];//视频文件名    
while(1){ 
    Mat Frame;
    namedWindow("摄像头");
    capture>>Frame;
    if((key=waitKey(5))!=-1){
        if(key=='p'){ 
            sprintf(pName,"photo/%d.jpg",i);
            imwrite(pName, Frame);  
            while(key==waitKey(5)&&waitKey(5)==-1);
            i++;
        }
        if(key=='v'){
            destroyWindow("摄像头");
            sprintf(vName,"video/%d.avi",j);    
            VideoWriter writer(vName, CV_FOURCC('M', 'J', 'P', 'G'), 25.0, Size(640, 480));
            do{   
            capture>>Frame;
            writer<<Frame;
            imshow("录像",Frame);
            }while(key==waitKey(5)&&waitKey(5)==-1);
            j++;
            destroyWindow("录像");
        }
    }
    imshow("摄像头",Frame);
    waitKey(10);
    }
return 0;
}
// #include <iostream>
 
// #include <opencv2/opencv.hpp>
// using namespace cv;
// int main(int arg, char** args) {
// 	std::cout << "aa" << std::endl;
 
//     std::string img = "openCV/test.jpg";
//     Mat srcImage = imread(img);
//     if (!srcImage.data) {
//         return 1;
//     }
//     imshow("srcImage", srcImage);
//     cvWaitKey(0);
//     return 0;
// }
