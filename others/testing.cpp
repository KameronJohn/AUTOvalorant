#include <iostream>
using namespace std;

int main() {
    int num = 0;
    char key;

    while(true) {
        cout << num << endl;
        num++;

        // Check if there is user input
        if (cin.peek() != '\n') {
            // Read and discard input
            cin >> key;
            continue;
        }

        // Otherwise, wait for user input
        key = getchar();
        if (key == '\n') {
            break;
        }
    }

    return 0;
}