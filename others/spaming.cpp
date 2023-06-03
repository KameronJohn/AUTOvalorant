#include <windows.h>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <chrono>

int spamming()
    {
        INPUT input;
        ZeroMemory(&input, sizeof(input));
        input.type = INPUT_KEYBOARD;
        //create an array of number
        const int VK_ARRAY[] = {'E', 'C'};
        //iterate through the array of numbers
        //select key
        input.ki.wVk = 'C';
        input.ki.dwFlags = 0;
        SendInput(1, &input, sizeof(INPUT));
        input.ki.dwFlags = KEYEVENTF_KEYUP;
        SendInput(1, &input, sizeof(INPUT));
        // std::cout << "pressed: " << VK_ARRAY[i] << " for: "<< num << 's'<< std::endl;
        Sleep(800);
        
        /* press ] key */
        input.ki.wScan = MapVirtualKey(VK_OEM_6, MAPVK_VK_TO_VSC);
        input.ki.time = 0;
        input.ki.dwExtraInfo = 0;
        input.ki.wVk = 0;
        input.ki.dwFlags = KEYEVENTF_SCANCODE;
        SendInput(1, &input, sizeof(INPUT));
        input.ki.dwFlags = KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP;
        SendInput(1, &input, sizeof(INPUT));
        
        /* press ] key */
        Sleep(425);
        //select key
        input.ki.wVk = 'F';
        input.ki.dwFlags = 0;
        SendInput(1, &input, sizeof(INPUT));
        input.ki.dwFlags = KEYEVENTF_KEYUP;
        SendInput(1, &input, sizeof(INPUT));
        Sleep(1000);
    }
int main()
{
    std::cout << "Press 1 to spam" << std::endl;
    while (true)
    {
        auto start = std::chrono::steady_clock::now(); // Get the current time
        if (GetAsyncKeyState('1') & 0x8000)
        {
            
            for (int i = 0; true; i++)
            {
                spamming();
                auto end = std::chrono::steady_clock::now(); // Get the current time again
                auto elapsed = std::chrono::duration_cast<std::chrono::seconds>(end - start); // Calculate the elapsed time
                
                if (elapsed.count() > 20)
                {
                    std::cout << "Time limit exceeded!" << std::endl;
                    break;
                }
            }
            std::cout << "ENDED" << std::endl;
            
        }
    }

    return 0;
    
    }