{
    "targets": [
        {
            "target_name": "tree_sitter_context_predicate_binding",
            
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "src"
            ],
            
            "sources": [
                "src/parser.c",
                "src/binding.cc"
            ],
            
            "cflags_c": [
                "-std=c99"
            ]
        }
    ]
}