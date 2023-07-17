#include "./base.h"
void spam_purchase()
{
    for (int i = 0; i<5; i++)
    {
        double_click(644, 425);
        Sleep(100);
        key_press("G",100);
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
    while (true)
    {
        /* if detected '1' is pressed (global) */
        if (GetAsyncKeyState(VK_F7) & 0x8000)
        {
            // Sleep(1000);
            key_press("B",500);
            auto start = std::chrono::steady_clock::now(); // Get the current time
            for (int i = 0; true; i++)
                {
                    spam_purchase();
                    auto end = std::chrono::steady_clock::now(); // Get the current time again
                    auto elapsed = std::chrono::duration_cast<std::chrono::seconds>(end - start); // Calculate the elapsed time
                    if (elapsed.count() > 20)
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
    }
}