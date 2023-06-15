#include <iostream>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <Windows.h>
#include <string>
int random_number(int start, int end)
{
    std::srand(std::time(nullptr));
    int num = rand() % start + end + 1;
    return num;
}
void key_press(std::string input_key, int sleep_time, int hold_time=0)
{
    INPUT input = { 0 };
    input.type = INPUT_KEYBOARD;
    input.ki.wVk = static_cast<WORD>(input_key[0]);
    input.ki.dwFlags = 0;
    SendInput(1, &input, sizeof(INPUT));
    Sleep(hold_time);
    input.ki.dwFlags = KEYEVENTF_KEYUP;
    SendInput(1, &input, sizeof(INPUT));

    Sleep(sleep_time);
    /* int virtual_key_code = MapVirtualKey(input_key[0], MAPVK_VK_TO_VSC);
    BYTE ability_byte = virtual_key_code;
    keybd_event(ability_byte, 0, 0, 0); // Press the key
    keybd_event(ability_byte, 0, KEYEVENTF_KEYUP, 0); // Release the key */
}
void afk_hotkey_press(WORD key1, WORD key2, DWORD sleepTime)
{
    INPUT inputs[2] = { 0 };
    inputs[0].type = INPUT_KEYBOARD;
    inputs[0].ki.wVk = key1;
    inputs[1].type = INPUT_KEYBOARD;
    inputs[1].ki.wVk = key2;

    // Press both keys down simultaneously
    SendInput(2, inputs, sizeof(INPUT));

    // Sleep for the specified amount of time
    Sleep(sleepTime);

    // Release both keys simultaneously
    inputs[0].ki.dwFlags = KEYEVENTF_KEYUP;
    inputs[1].ki.dwFlags = KEYEVENTF_KEYUP;
    SendInput(2, inputs, sizeof(INPUT));
}
void click(int x, int y){
    SetCursorPos(x, y);
    mouse_event(MOUSEEVENTF_LEFTDOWN, x, y, 0, 0);
    mouse_event(MOUSEEVENTF_LEFTUP, x, y, 0, 0);
}
void click_right(int x, int y){
    SetCursorPos(x, y);
    mouse_event(MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0);
    mouse_event(MOUSEEVENTF_RIGHTUP, x, y, 0, 0);
}
void double_click(int x, int y)
{
    SetCursorPos(x, y);
    mouse_event(MOUSEEVENTF_LEFTDOWN, x, y, 0, 0);
    mouse_event(MOUSEEVENTF_LEFTUP, x, y, 0, 0);
    Sleep(50); // Wait a short time between clicks
    SetCursorPos(x, y);
    mouse_event(MOUSEEVENTF_LEFTDOWN, x, y, 0, 0);
    mouse_event(MOUSEEVENTF_LEFTUP, x, y, 0, 0);
}
void quadra_click(int x, int y)
{
    for (int i = 0; i < 4; i++){
        SetCursorPos(x, y);
        mouse_event(MOUSEEVENTF_LEFTDOWN, x, y, 0, 0);
        mouse_event(MOUSEEVENTF_LEFTUP, x, y, 0, 0);
        Sleep(30); // Wait a short time between clicks
    }

}

