// Remember.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <list>
#include <vector>
#include <stdlib.h>
#include <algorithm>

#include "duplicates.h"

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


int main() {

    /*
    func();

    std::vector<int> vector = generate_randint_vector(20, 20);
    print_vector(vector);

    eliminate_duplicates(&vector);
    print_vector(vector);
    */

    //MyClass my = MyClass();
    //funcTemp(my);

    int a = 10;
    bool* b;
    b = (bool*)&a;
    std::cout << "a: " << &a << std::endl;
    std::cout << "b: " << b-1 << ", " << (int)(*(b-1));
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
