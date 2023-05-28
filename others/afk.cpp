#include <windows.h>
#include <iostream>
#include <cstdlib>
#include <ctime>
void buy_for_team()
{
    // Simulate pressing and releasing the "B" key
    keybd_event('B', 0, 0, 0); // Press the key
    keybd_event('B', 0, KEYEVENTF_KEYUP, 0); // Release the key
    Sleep(500);
    // Set the cursor position
    int x = 0;
    int y = 0;
    POINT cursorPos;
    GetCursorPos(&cursorPos);
    x = cursorPos.x;
    int new_y = cursorPos.y + 200; // move 200 pixels down
    SetCursorPos(x, new_y);
    Sleep(500);

    // Perform a left click
    mouse_event(MOUSEEVENTF_LEFTDOWN, x, y, 0, 0);
    mouse_event(MOUSEEVENTF_LEFTUP, x, y, 0, 0);
    Sleep(500);

    // move to original position
    SetCursorPos(x, y);

    // Simulate pressing and releasing the "B" key
    keybd_event('B', 0, 0, 0); // Press the key
    keybd_event('B', 0, KEYEVENTF_KEYUP, 0); // Release the key
    Sleep(500);

    // Simulate pressing and releasing the "G" key
    keybd_event('G', 0, 0, 0); // Press the key
    keybd_event('G', 0, KEYEVENTF_KEYUP, 0); // Release the key
    Sleep(500);
    return;
}
int random_sleep()
    {
        // Seed the random number generator
        std::srand(std::time(nullptr));
        
        // Generate a random number between 500 and 2500
        // generate a random number between 500 and 2500
        int num = std::rand() % (2500 - 500 + 1) + 500;
        // int num = std::rand() % 2001 + 500;
        Sleep(num);
        return num;
    }
int main()
{
    INPUT input;
    ZeroMemory(&input, sizeof(input));
    input.type = INPUT_KEYBOARD;
    // Seed the random number generatorwaw
    std::srand(std::time(nullptr));

    std::cout << "sleeping" << std::endl;
    Sleep(2000);
    std::cout << "starting" << std::endl;

    while (true)
    {
        //create an array of number
        const int VK_ARRAY[] = { VK_SPACE, 'A', 'W', 'D', 'S' };
        //iterate through the array of numbers
        for (int i = 0; i < 3; i++)
        {

            // Select a random element from the array
            int index = std::rand() % 5;
            //select key
            input.ki.wVk = VK_ARRAY[i];
            input.ki.dwFlags = 0;
            SendInput(1, &input, sizeof(INPUT));
            int num = random_sleep();
            input.ki.dwFlags = KEYEVENTF_KEYUP;
            SendInput(1, &input, sizeof(INPUT));
            std::cout << "pressed: " << VK_ARRAY[i] << " for: "<< num << 's'<< std::endl;
            random_sleep();
        }
        buy_for_team();
        buy_for_team();
    }

    return 0;
    
    }