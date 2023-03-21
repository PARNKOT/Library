#include "boost/python.hpp"


char const* greet() {
    return "Hello world!";
}

BOOST_PYTHON_MODULE(hello_ext)
{
    using namespace boost::python;
    def("greet", greet);
}