from tree_sitter import Language

Language.build_library(
    # Store the library in a `build` directory
    "build/my-languages.so",
    # Include the languages you need
    ["vendor/tree-sitter-python"],
)

