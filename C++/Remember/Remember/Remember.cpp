// Remember.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <list>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <new>
#include <bitset>

#include "duplicates.h"
#include "sorts.h"

using duplicate::eliminate_duplicates;
using duplicate::func;

template<typename T>
void print_vector(std::vector<T> vector);

std::vector<int> generate_randint_vector(int size, int limit = RAND_MAX);


struct Some {
    int i;
    float f;
    bool b;
};


class MyClass {
public:
    static int varInt;
    static float varFloat;
    double varDouble;
};

int MyClass::varInt = 1;
float MyClass::varFloat = 2.0;


template<class C>
void funcTemp(C cls) {
    std::cout << C::varInt << ", " << C::varFloat;
}

int* funcPtr() {
    int* a = new int;
    std::cout <<  a << ", ";
    return a;
}

template<class T>
void print(T arg) {
    std::cout << arg << std::endl;
}


int main() {



    /*
    int size = 3;
    int* p = (int*)std::malloc(size * sizeof(int));

    for (int index = 0; index < size; index++) {
        p[index] = index + 1;
    }

    p[0] = 65535;
    p[1] = 65535;
    p[2] = 65535;

    auto p1 = (int*)((std::uint64_t)p + 1);
    auto p2 = (int*)((std::uint64_t)p + 2);
    auto p3 = (std::uint8_t*)((std::uint64_t)p + 3);
    auto p4 = (std::uint8_t*)((std::uint64_t)p + 4);
    auto p5 = (std::uint8_t*)((std::uint64_t)p + 5);
    //*p1 = 21;
    //*p2 = 1;
    //*p3 = 0;
    //*p4 = 0;
    //*p5 = 0;
    std::bitset<32> x(*p2);
    print(x);
    print(p1);
    print(p2);
    int a[2] = { 1, 2 };
    */


    /*
    func();

    std::vector<int> vector = generate_randint_vector(20, 20);
    print_vector(vector);

    eliminate_duplicates(&vector);
    print_vector(vector);
    */

    //MyClass my = MyClass();
    //funcTemp(my);
    
    //int *a = funcPtr();
    //std::cout << a;
    //delete a;

    /*/
    auto vector = std::vector<int>(10);
    vector = { 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 };
    sorts::combosort(vector.begin(), vector.end());

    for (auto el : vector) {
        std::cout << el << ", ";
    }
    std::cout << std::endl;

    auto var = new int(3);
    std::cout << *var;
    //sorts::combosort();
    */
    
}



std::vector<int> generate_randint_vector(int size, int limit) {
    std::vector<int> vector = std::vector<int>(size);

    for (int count = 0; count < size; count++) {
        vector.at(count) = std::rand() % limit;
    }

    return vector;

}

template<typename T>
void print_vector(std::vector<T> vector) {
    std::cout << "Vector: ";
    for (int index = 0; index < vector.size(); index++) {
        std::cout << vector.at(index) << " ";
    }

    std::cout << std::endl;
}
