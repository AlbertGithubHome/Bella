solution "main"
  configurations { "Debug", "Release" } 
  location "../../code"

  includedirs {
    "../../code/share",
    "../../code/share/utilities",
    "../../code/utilities",
  }

  defines{"OS_WINDOWS","_DEBUG","WIN32","_WINDOWS","_LIB","MY_CMD","_STANDALONE","_OPENALLFUNCTION","NO_DIRECT_X","_USE_32BIT_TIME_T"}
  language "C++"

  project "main"
    location "../../code/main"
    kind "ConsoleApp"
    files { "../../code/main/**.h", "../../code/main/**.cpp"}
    links {}
    libdirs{"../../code/share/library/debug"}
    targetdir "../../bin"
    debugdir "../../bin"
      configuration "Debug"
        defines { "DEBUG" }
        flags { "Symbols" }
      configuration "Release"
        defines { "NDEBUG" }
        flags { "Optimize" }

  project "utilities"
    location "../../code/utilities"
    kind "StaticLib"
    files { "../../code/utilities/**.h", "../../code/utilities/**.cpp"}
    targetdir "../../code/share/library/debug"
    targetname "utilities"
      configuration "Debug"
        flags { "Symbols","FatalWarnings" }
      configuration "Release"
        defines { "NDEBUG" }
        flags { "Optimize", "FatalWarnings"}

  project "share"
    location "../../code/share"
    kind "StaticLib"
    files { "../../code/share/**.h"}
    targetdir "../../code/share/library/debug"
    targetname "share"
      configuration "Debug"
        flags { "Symbols" }
      configuration "Release"
        defines { "NDEBUG" }
        flags { "Optimize" }

