#pragma once

namespace duplicate {
    template<typename T>
    void eliminate_if_duplicate(std::vector<T>* vector, int index);
	
    template<typename T>
    void eliminate_duplicates(std::vector<T>* vector) {
        for (int index = 0; index < vector->size(); index++) {
            eliminate_if_duplicate(vector, index);
        }
    }

    template<typename T>
    void eliminate_if_duplicate(std::vector<T>* vector, int index) {
        while (std::count(vector->begin(), vector->end(), vector->at(index)) > 1) {
            vector->at(index) = std::rand() % 20;
        }
    }
	
	extern inline void func();
}