#include <Windows.h>
#include <iostream>

int main(int argc, char* argv[])
{
    // std::cout << "halo" << std::endl;
    // Check that the correct number of arguments were passed
    if (argc != 5)
    {
        std::cerr << "Usage: " << argv[0] << " pos1_x pos1_y pos2_x pos2_y" << std::endl;
        return 1;
    }

    // Parse the x and y coordinates from the arguments
    int pos1_x = std::stoi(argv[1]);
    int pos1_y = std::stoi(argv[2]);
    if (pos1_x == 999 && pos1_y == 999)
    {
        std::cout << "test run done" << std::endl;
        return 0;
    }
    int pos2_x = std::stoi(argv[3]);
    int pos2_y = std::stoi(argv[4]);

    // Print the x and y coordinates to the console
    // std::cout << "pos1_x = " << pos1_x << std::endl;
    // std::cout << "pos1_y = " << pos1_y << std::endl;
    // std::cout << "pos2_x = " << pos2_x << std::endl;
    // std::cout << "pos2_y = " << pos2_y << std::endl;



    // Define the two coordinates to move to
    POINT coords[] = {
        {pos1_x, pos1_y},
        {pos2_x, pos2_y}
    };
    int numCoords = sizeof(coords) / sizeof(coords[0]);

    // Get the current tick count
    DWORD startTick = GetTickCount();

    // Loop 10 times and move to each coordinate in turn
    for (int i = 0; i < 10000000; i++)
    {
        for (int j = 0; j < numCoords; j++)
        {
            // Check if 4 seconds have elapsed
            if (GetTickCount() - startTick > 2500)
            {
                // std::cout << "Breaking loop" << std::endl;
                return 0;
            }

            // Move the mouse to the current coordinate
            SetCursorPos(coords[j].x, coords[j].y);

            //Simulate a left mouse button click
            mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);
            mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0);

            // Wait for a short period to avoid moving too quickly
            Sleep(30);
        }
    }

    return 0;
}