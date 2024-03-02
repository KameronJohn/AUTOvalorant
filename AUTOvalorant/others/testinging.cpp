#include <windows.h>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include "./base.h"

void clickMouse(int x, int y, int numClicks)
{
    // Set the cursor position
    SetCursorPos(x, y);

    // Perform multiple mouse clicks
    for (int i = 0; i < numClicks; i++)
    {
        // Simulate the mouse click
        mouse_event(MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_LEFTUP, x, y, 0, 0);

        // Add a small delay between clicks (optional)
        Sleep(500);
    }
}

int main()
{
    int x = 1594; // Specify x-coordinate
    int y = 965; // Specify y-coordinate
    int numClicks = 5; // Specify number of clicks
    Sleep(2000);
    std::cout << "CLICKING" << std::endl;
    clickMouse(x, y, numClicks);
    return 0;
}