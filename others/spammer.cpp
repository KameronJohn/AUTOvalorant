#include <windows.h>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include "./base.h"
int spamming()
    {
        key_press("C",800);
        // std::cout << "C" << std::endl;
        // key_press("]",225);
        // std::cout << "]" << std::endl;
        click(1280,720);
        Sleep(50);
        key_press("F",900);
        // std::cout << "F" << std::endl;
    }
void spam_purchase()
{
    for (int i = 0; i<5; i++)
    {
        click(644,425);
        // double_click(644, 425);
        // double_click(644, 425);
        Sleep(100);
        key_press("G",100);
        double_click(616, 261);
        double_click(616, 261);
        Sleep(100);
    }
/*     for (int i = 0; i<4; i++)
    {
        Sleep(100);
        click(616, 600);
    }
    Sleep(100); */
}
int main()
{
    std::cout << "Press F4 to quit\nPress F7 to spam abilities\nPress F8 to spam purchase" << std::endl;
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
                    
                    if (elapsed.count() > 29)
                    {
                        std::cout << "Time limit exceeded!" << std::endl;
                        break;
                    }
                }
                std::cout << "ENDED" << std::endl;
        }
        /* if detected '1' is pressed (global) */
        if (GetAsyncKeyState(VK_F8) & 0x8000)
        {
            // Sleep(1000);
            key_press("B",500);
            auto start = std::chrono::steady_clock::now(); // Get the current time
            for (int i = 0; true; i++)
                {
                    spam_purchase();
                    auto end = std::chrono::steady_clock::now(); // Get the current time again
                    auto elapsed = std::chrono::duration_cast<std::chrono::seconds>(end - start); // Calculate the elapsed time
                    if (elapsed.count() > 29)
                    {
                        std::cout << "Time limit exceeded!" << std::endl;
                        break;
                    }
                    /* if detected '1' is pressed (global) */
                    if (GetAsyncKeyState('2') & 0x8000)
                    {
                        break;
                    }
                }
            std::cout << "ENDED" << std::endl;
        }
        if (GetAsyncKeyState(VK_F4) & 0x8000)
        {
           return 0;
        }
        /* if detected '1' is pressed (global)*/
        /* if (GetAsyncKeyState('1') & 0x8000)
        {
            
            
        } */
    }

    return 0;
    
    }