from conans import ConanFile, CMake

class MQTT_CPP(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "boost_test@1.67.0@bincrafters/stable", "boost_beast@1.67.0@bincrafters/stable", "OpenSSL@1.1.1@conan/stable"
    options = {"build_examples" : [True, False], "build_tests": [True, False], "use_tls" : [True, False], "use_ws" : [True, False], "use_str_check" : [True, False]}
    default_options = {"build_examples": False, "build_tests" : False, "use_tls" : True, "use_ws" : False, "use_str_check" : True}
    exports_sources = "tests*", "include*", "src*", "CMakeLists.txt"
    generators = "cmake", "ycm"

    def build(self):
        cmake = CMake(self)
        cmake.definitions["MQTT_NO_TLS"] = "Off" if self.options.use_tls else "On"
        cmake.definitions["MQTT_USE_WS"] = "On" if self.options.use_ws else "Off"
        cmake.definitions["MQTT_USE_STR_CHECK"] = "On" if self.options.use_tls else "Off"
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy(pattern="*.h", dst="include", src="include")
        self.copy(pattern="*.hpp", dst="include", src="include")

    def package_info(self):
        self.cpp_info.header_only()
