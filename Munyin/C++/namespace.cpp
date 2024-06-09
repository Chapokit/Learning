#include <iostream>

namespace first{
    int x = 1;
}

namespace second{
    int x = 2;
}


// int main() {
//     using namespace first;


//     std::cout << second::x;
//     std::cout << x;

//     return 0;
// }
int main() {
    using namespace std;

    string name = "Bro";

    std::cout << "Hello " << name;

    return 0;
}