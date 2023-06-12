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
        Sleep(2000);
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
    // std::cout << "halo" << std::endl;
    // Simulate pressing and releasing the "B" key
    key_press("B",1000);
     /* will only run in the first time */
    if (num_loop == 0){
        if (shield == 1) {
            //buy sheild
            click(1916, 380);
            Sleep(250);
        }
        if (abilities == 1) {
            for (int a = 0; a < 3; a++) {
                Point points[3] = {
                    {974, 1176},
                    {1467, 1176},
                    {1959, 1189}
                };
                for (int i = 0; i < 3; i++) {
                    click(points[i].x,points[i].y);
                    Sleep(250);
                }
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
    if (drop == 1){
        // buy vandal
        key_press("G",500);
    }
    return;
}
int random_sleep()
    {
        // Seed the random number generator
        std::srand(std::time(nullptr));
        
        // Generate a random number between 500 and 2500
        // generate a random number between 500 and 2500
        int num = random_number(250,500);
        // int num = std::rand() % 2001 + 500;
        Sleep(num);
        return num;
    }
int main(int argc, char* argv[])
// int main(int argc, char* argv[])
{

    /* declare parameters */
    int drop = std::stoi(argv[2]);
    int shield = std::stoi(argv[3]);
    int abilities = std::stoi(argv[4]);
    int abilities1 = 1;
    int abilities2 = 1;
    int abilities3 = 1;
    int abilities4 = 1;
    try {
        // Code that may throw an exception
        abilities1 = std::stoi(argv[5]);
        abilities2 = std::stoi(argv[6]);
        abilities3 = std::stoi(argv[7]);
        abilities4 = std::stoi(argv[8]);
    }
    catch (...) {
        // Code to handle any type of exception
    }

    // int drop = 1;
    // int shield = 1;
    // int abilities = 1;
    int print_parameters = std::stoi(argv[1]);
    if (print_parameters == 0){
        std::cout << "input: " << "-drop-" << drop << "-shield-" << shield << "-abilities-"  << abilities << std::endl;
        std::cout << "abilities1: " << abilities1 << "-abilities2-" << abilities2 << "-abilities3-"  << abilities3 << std::endl;
    }
    
    // std::cout << shield << std::endl;
    // std::cout << abilities << std::endl;
    // Seed the random number generatorwaw
    std::srand(std::time(nullptr));

    // std::cout << "sleeping" << std::endl;
    Sleep(1000);
    // std::cout << "starting" << std::endl;
    key_press("6",500);

    //create an array of number
    // char aqrr[] = {'A','D','W','A','D','A','D','W','S'};
    std::string aqrr[] = {"A","D","W","A","D","A","D","W","S"};
    for (int i = 0; i < 5; i++)
    {
        
        // Select a random element from the array
        int number = rand() % 10;
        //select key
        int num = random_sleep();
        // std::cout << "hi" << std::endl;6AA
        int ran_slp_time = random_number(2000,1000);
        // afk_hotkey_press(aqrr[number],aqrr[number],ran_slp_time);
        key_press(aqrr[number],num,ran_slp_time);
        // random_sleep();
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
        // std::cout << "looping" << std::endl;
        buy_for_team(drop,shield,abilities,i);
    }
    if (abilities == 1){
        /* first: 1 = click, 2 = double tap key */
        /* second: loop times */
        use_abilities("C",abilities1,1);
        use_abilities("V",abilities2,1);
        use_abilities("E",abilities3,1);
        use_abilities("X",abilities4,1);
    }
    return 0;
    
    }