from distutils.core import setup, Extension

setup(name="helloworld", version="1.0.1",
      ext_modules=[
          Extension('helloworld', ['Hello_C.c'])
        ]
      )
