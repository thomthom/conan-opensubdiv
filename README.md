# Conan Package for OpenSubdiv

Work in progress. Currently set up for CPU evaluation only. Testing on Windows (MSVC) and Xcode.

## References

http://graphics.pixar.com/opensubdiv/docs/intro.html
https://github.com/PixarAnimationStudios/OpenSubdiv

## Example Usage

```shell
mkdir build && cd build
```

### Windows

http://conanio.readthedocs.io/en/latest/reference/generators/visualstudiomulti.html

```shell
conan install .. -g visual_studio_multi -s arch=x86 -s build_type=Debug --build missing
conan install .. -g visual_studio_multi -s arch=x86_64 -s build_type=Debug --build missing
conan install .. -g visual_studio_multi -s arch=x86 -s build_type=Release --build missing
conan install .. -g visual_studio_multi -s arch=x86_64 -s build_type=Release --build missing

```

### OSX

http://conanio.readthedocs.io/en/latest/reference/generators/xcode.html

**TODO:** Update this example once Xcode is tested.

```shell
conan install .. -g xcode -s arch=x86 -s build_type=Debug
conan install .. -g xcode -s arch=x86_64 -s build_type=Debug
conan install .. -g xcode -s arch=x86 -s build_type=Release
conan install .. -g xcode -s arch=x86_64 -s build_type=Release
```

