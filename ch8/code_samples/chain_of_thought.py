import ast


def validate_no_bugs_in_source_code(sc: str) -> None:
    validate_syntax(sc)
    validate_compilation(sc)
    validate_reoroducibility_across_runs(sc)


def validate_syntax(sc: str) -> None:
    try:
        ast.parse(sc)
    except SyntaxError:
        raise ValueError("Syntax error in source code")
    

def validate_compilation(sc: str) -> None:
    try:
        compile(sc, "<string>", "exec")
    except Exception:
        raise ValueError("Compilation error in source code")
    

def validate_reoroducibility_across_runs(sc: str) -> None:
    res1 = exec(sc)
    res2 = exec(sc)
    if res1 != res2:
        raise ValueError("Non-deterministic source code")
