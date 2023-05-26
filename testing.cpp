#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

int main(int argc, char* argv[])
{
    // Load the template image
    cv::Mat templateImage = cv::imread("C:/Users/kamka/Documents/AUTOvalorant/source/play.png", cv::IMREAD_GRAYSCALE);
    if (templateImage.empty())
    {
        std::cerr << "Failed to load template image" << std::endl;
        return 1;
    }

    // Load the source image from the monitor
    cv::Mat sourceImage = cv::imread("\\\\.\\DISPLAY1", cv::IMREAD_GRAYSCALE);
    if (sourceImage.empty())
    {
        std::cerr << "Failed to load source image" << std::endl;
        return 1;
    }

    // Perform template matching
    cv::Mat result;
    cv::matchTemplate(sourceImage, templateImage, result, cv::TM_CCOEFF_NORMED);

    // Find the location of the best match
    double minVal, maxVal;
    cv::Point minLoc, maxLoc;
    cv::minMaxLoc(result, &minVal, &maxVal, &minLoc, &maxLoc);

    // Check if the template was found
    if (maxVal > 0.9)
    {
        std::cout << "Template found at location (" << maxLoc.x << ", " << maxLoc.y << ")" << std::endl;
        // Do something when the template is found
    }
    else
    {
        std::cout << "Template not found" << std::endl;
        // Do something else when the template is not found
    }

    return 0;
}