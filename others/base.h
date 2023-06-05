#include <iostream>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <Windows.h>
#include <string>

void key_press(std::string input_key, int sleep_time)
{
    INPUT input = { 0 };
    input.type = INPUT_KEYBOARD;
    input.ki.wVk = static_cast<WORD>(input_key[0]);
    input.ki.dwFlags = 0;

    SendInput(1, &input, sizeof(INPUT));
    input.ki.dwFlags = KEYEVENTF_KEYUP;
    SendInput(1, &input, sizeof(INPUT));

    Sleep(sleep_time);
    /* int virtual_key_code = MapVirtualKey(input_key[0], MAPVK_VK_TO_VSC);
    BYTE ability_byte = virtual_key_code;
    keybd_event(ability_byte, 0, 0, 0); // Press the key
    keybd_event(ability_byte, 0, KEYEVENTF_KEYUP, 0); // Release the key */
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

