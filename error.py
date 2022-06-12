# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass

class AlphaError(Error):
    """Raised when the input value is not a letter"""
    pass

class OffGridError(Error):
    """Raised when the rover will fall off the grid"""
    pass

class CrashError(Error):
    """Raised when the rover will crash into another rover"""
    pass

#Exception classes used by the Distutils implementation classes


class DistutilsError (Exception):
    """The root of all Distutils evil."""
    pass

class DistutilsPlatformError (DistutilsError):
    """We don't know how to do something on the current platform (but
    we do know how to do it on some platform) -- eg. trying to compile
    C files on a platform not supported by a CCompiler subclass."""
    pass

class DistutilsExecError (DistutilsError):
    """Any problems executing an external program (such as the C
    compiler, when compiling C files)."""
    pass

# Exception classes used by the CCompiler implementation classes

class CCompilerError (Exception):
    """Some compile/link operation failed."""

class PreprocessError (CCompilerError):
    """Failure to preprocess one or more C/C++ files."""

class CompileError (CCompilerError):
    """Failure to compile one or more C/C++ source files."""

class LibError (CCompilerError):
    """Failure to create a static library from one or more C/C++ object
    files."""

class LinkError (CCompilerError):
    """Failure to link one or more C/C++ object files into an executable
    or shared library file."""

class UnknownFileError (CCompilerError):
    """Attempt to process an unknown file type."""
