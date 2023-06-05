#include <windows.h>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
#include "./base.h"
struct Point {
    int x;
    int y;
    };
void use_abilities(std::string ability,int method,int loop_count){
    /* 1 = click, 2 = double tap key */
    for (int i = 0; i < loop_count; i++){
        /* pick abilities */
        key_press(ability,2000);
        /* cast abilities */
        if (method == 1){
            /* center point of the monitor */
            click(1280,720);
        }else if (method == 2){
            key_press(ability,0);
        }
        Sleep(2000);
    }
    return;
}
void buy_for_team(int drop,int shield, int abilities, int num_loop)
{
    // Simulate pressing and releasing the "B" key
    keybd_event('B', 0, 0, 0); // Press the key
    keybd_event('B', 0, KEYEVENTF_KEYUP, 0); // Release the key
    Sleep(1000);
     /* will only run in the first time */
    if (num_loop == 0){
        if (shield == 1) {
            //buy sheild
            click(1916, 380);
            Sleep(250);
        }
        if (abilities == 1) {
            Point points[3] = {
                {782, 1181},
                {1261, 1181},
                {1759, 1179}
            };
            for (int i = 0; i < 3; i++) {
                click(points[i].x,points[i].y);
                Sleep(250);
            }
        }
    }
    if (drop == 1){
        // buy vandal
        click(1212,871);
        Sleep(500);
    }

    // Simulate pressing and releasing the "B" key
    key_press("B",500);
    key_press("G",500);
    return;
}
int random_sleep()
    {
        // Seed the random number generator
        std::srand(std::time(nullptr));
        
        // Generate a random number between 500 and 2500
        // generate a random number between 500 and 2500
        int num = rand() % 1001 + 500;
        // int num = std::rand() % 2001 + 500;
        Sleep(num);
        return num;
    }
int main(int argc, char* argv[])
{
    /* declare parameters */
    int drop = std::stoi(argv[1]);
    int shield = std::stoi(argv[2]);
    int abilities = std::stoi(argv[3]);
    
    // std::cout << drop << std::endl;
    // std::cout << shield << std::endl;
    // std::cout << abilities << std::endl;
    /* declare parameters */

    INPUT input;
    ZeroMemory(&input, sizeof(input));
    input.type = INPUT_KEYBOARD;
    // Seed the random number generatorwaw
    std::srand(std::time(nullptr));

    // std::cout << "sleeping" << std::endl;
    Sleep(1000);
    // std::cout << "starting" << std::endl;
    key_press("6",500);
    //create an array of number
    const int VK_ARRAY[] = {VK_SPACE,'A', 'W', 'D'};
    for (int i = 0; i < 3; i++)
    {
        
        std::cout << "cehckl"<< std::endl;
        // Select a random element from the array
        int number = rand() % 5;
        //select key
        input.ki.wVk = VK_ARRAY[number];
        std::cout << "pressed: " << number << std::endl;
        input.ki.dwFlags = 0;
        SendInput(1, &input, sizeof(INPUT));
        int num = random_sleep();
        input.ki.dwFlags = KEYEVENTF_KEYUP;
        SendInput(1, &input, sizeof(INPUT));
        random_sleep();
    }
    // std::cout << "loop_times " << std::endl;
    int loop_times = 0;
    // std::cout << "loop_times " << loop_times << std::endl;
    if (drop == 0){
        loop_times = 1;
    }else{
        loop_times = 3;
    }
    // std::cout << "loop_times: " << loop_times << std::endl;
    for (int i = 0; i < loop_times; i ++){
        buy_for_team(drop,shield,abilities,i);
    }
    if (abilities == 1){
        /* 1 = click, 2 = double tap key */
        use_abilities("C",1,2);
        use_abilities("V",1,2);
        use_abilities("E",2,2);
        use_abilities("X",1,1);
    }
    return 0;
    
    }