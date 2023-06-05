#include <windows.h>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include "./base.h"
int spamming()
    {
        key_press("C",800);
        std::cout << "C" << std::endl;
        // key_press("]",225);
        // std::cout << "]" << std::endl;
        click(1280,720);
        Sleep(50);
        key_press("F",900);
        std::cout << "F" << std::endl;
    }
int main()
{
    while (true)
    {
        /* if '1' is input */
        if (GetAsyncKeyState(VK_F7) & 0x8000)
        {
            auto start = std::chrono::steady_clock::now(); // Get the current time
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
        
        /* if detected '1' is pressed (global) */
        /* if (GetAsyncKeyState('1') & 0x8000)
        {
            
            
        } */
    }

    return 0;
    
    }