from conans import ConanFile, CMake, tools


class OpensubdivConan(ConanFile):
    name = "OpenSubdiv"
    version = "3.3.0"
    license = "https://github.com/PixarAnimationStudios/OpenSubdiv/blob/master/LICENSE.txt"
    url = "https://github.com/thomthom/conan-opensubdiv"
    description = "An Open-Source subdivision surface library. "
    settings = "os", "compiler", "build_type", "arch"
    # options = {"shared": [True, False]}
    # TODO: Apart from `static`, these options are not hooked up yet.
    options = {
        "dx": [True, False],
        "clew": [True, False],
        "cuda": [True, False],
        "omp": [True, False],
        "opencl": [True, False],
        "opengl": [True, False],
        "ptex": [True, False],
        "tbb": [True, False],
        "static": [True, False],
    }
    default_options = \
        "dx=False", \
        "clew=False", \
        "cuda=False", \
        "omp=False", \
        "opencl=False", \
        "opengl=False", \
        "ptex=False", \
        "tbb=False", \
        "static=True"
    generators = "cmake"

    def config(self):
        # OpenSubdiv controls /MT vs MD via the MSVC_STATIC_CRT flag.
        # NOTE: https://github.com/conan-io/conan/issues/475
        self.settings.compiler["Visual Studio"].remove("runtime")

    def source(self):
        self.run("git clone https://github.com/PixarAnimationStudios/OpenSubdiv.git")
        self.run("cd OpenSubdiv && git checkout v3_3_0")

    # http://blog.conan.io/2017/03/07/Supporting-Different-C-C++-Package-Paradigms-with-conan.html
    # def build_id(self):
    #     self.info_build.settings.build_type = "Any"

    def build(self):
        cmake = CMake(self)

        # TODO: This should probably be part of `conan install`.
        if self.settings.os == "Macos":
            # http://conanio.readthedocs.io/en/latest/integrations/cmake/cmake_multi_generator.html
            # > The CMAKE_BUILD_TYPE default, if not specified is Debug.
            cmake.definitions["CMAKE_OSX_DEPLOYMENT_TARGET"] = "10.8"
            cmake.definitions["CMAKE_C_STANDARD"] = 11
            cmake.definitions["CMAKE_CXX_STANDARD"] = 11
            cmake.definitions["CMAKE_CXX_FLAGS"] ="-std=c++11 -stdlib=libc++"

        cmake.definitions["NO_EXAMPLES"] = 1
        cmake.definitions["NO_TUTORIALS"] = 1
        cmake.definitions["NO_REGRESSION"] = 1
        cmake.definitions["NO_PTEX"] = int(not self.options.ptex)
        cmake.definitions["NO_DOC"] = 1
        cmake.definitions["NO_OMP"] = int(not self.options.omp)
        cmake.definitions["NO_TBB"] = int(not self.options.tbb)
        cmake.definitions["NO_CUDA"] = int(not self.options.cuda)
        cmake.definitions["NO_OPENCL"] = int(not self.options.opencl)
        cmake.definitions["NO_OPENGL"] = int(not self.options.opengl)
        cmake.definitions["NO_DX"] = int(not self.options.dx)
        cmake.definitions["NO_CLEW"] = int(not self.options.clew)
        cmake.definitions["MSVC_STATIC_CRT"] = int(bool(self.options.static))

        cmake.configure(source_dir="%s/OpenSubdiv" % self.source_folder)
        cmake.build()

    def package(self):
        self.copy("opensubdiv/*.h", dst="include", src="OpenSubdiv")
        self.copy("*.lib", dst="lib", src="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["osdCPU"]
