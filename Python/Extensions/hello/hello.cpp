#include "boost/python/module.hpp"
#include "boost/python/list.hpp"
#include "boost/python/class.hpp"
#include "boost/python/def.hpp"


std::string get_hello_function()
{
    return "Hello world!";
}


class hello_class
{
    public:
        hello_class(std::string message) : _message(message) {}

        boost::python::list as_list(int count) {
            boost::python::list res;

            for (int i = 0; i < count; ++i) {
                res.append(_message);
            }
            return res;
        }

    private:
        std::string _message;
};

BOOST_PYTHON_MODULE(hello)
{
    boost::python::def("get_hello", get_hello_function);

    boost::python::class_<hello_class>("Hello", boost::python::init<std::string>())
        .def("as_list", &hello_class::as_list);
}