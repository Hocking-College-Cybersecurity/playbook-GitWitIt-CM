import math, random, re, sys

# Optional features
HAS_SYMPY = True
HAS_MPL = True
try:
    import sympy as sp
except Exception as e:
    HAS_SYMPY = False
    sp = None

try:
    import matplotlib.pyplot as plt
except Exception as e:
    HAS_MPL = False
    plt = None

def parse_convert_args(expr):
    """
    Robustly parse convert(value, from_unit, to_unit)
    Returns (value: float, from_unit: str, to_unit: str) or raises ValueError.
    """
    # Accept things like:
    # convert(10, cm, inch)
    # convert(10, "cm", "inch")
    # convert(  10.5  , 'cm' ,  inch )
    m = re.match(r'convert\s*\(\s*([^\s,]+(?:\.[^\s,]+)?)\s*,\s*([\'"]?[A-Za-z°]+[\'"]?)\s*,\s*([\'"]?[A-Za-z°]+[\'"]?)\s*\)\s*$', expr, re.IGNORECASE)
    if not m:
        raise ValueError("Bad format. Use: convert(value, from_unit, to_unit)\nExample: convert(10, cm, inch) or convert(10, \"cm\", \"inch\")")
    val_str, from_u_raw, to_u_raw = m.groups()
    try:
        val = float(val_str)
    except:
        raise ValueError(f"Can't parse value: {val_str}")
    # strip quotes if present and lowercase
    from_u = from_u_raw.strip().strip("'\"").lower()
    to_u = to_u_raw.strip().strip("'\"").lower()
    return val, from_u, to_u

def ultra_calc():
    allowed = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    allowed.update({
        "rand": random.random,
        "randint": random.randint,
        "abs": abs,
        "complex": complex,
    })
    if HAS_SYMPY:
        allowed.update({"sp": sp})
    memory = {}
    last = None
    history = []
    mem_value = 0

    # conversion factors (multiplicative)
    units = {
        ("cm", "inch"): 0.39370078740157477,
        ("inch", "cm"): 2.54,
        ("m", "ft"): 3.280839895013123,
        ("ft", "m"): 0.3048,
        ("kg", "lb"): 2.2046226218487757,
        ("lb", "kg"): 0.45359237,
        ("km", "mile"): 0.621371192237334,
        ("mile", "km"): 1.609344,
    }

    print("🧮 Ultra Python Calculator (robust)")
    print("Optional features: SymPy =", HAS_SYMPY, "| Matplotlib =", HAS_MPL)
    print("Commands: quit | history | vars | convert(v, from, to) | (plot/diff/solve if sympy/mpl installed)")
    print("Examples: convert(10, cm, inch)   convert(5, 'inch', 'cm')\n")

    while True:
        try:
            expr = input(">> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nexiting.")
            break
        if not expr:
            continue

        if expr.lower() in ("quit", "exit"):
            break
        if expr == "history":
            for i, h in enumerate(history[-20:], start=1):
                print(f"{i}: {h}")
            continue
        if expr == "vars":
            for k, v in memory.items():
                print(f"{k} = {v}")
            continue
        if expr.startswith("convert"):
            try:
                val, from_u, to_u = parse_convert_args(expr)
                key = (from_u, to_u)
                if key in units:
                    result = val * units[key]
                    last = result
                    history.append(f"{expr} = {result}")
                    print(f"{val} {from_u} = {result} {to_u}")
                else:
                    # temperature special handling
                    if (from_u, to_u) in (("c", "f"), ("celsius", "fahrenheit"), ("°c","°f")):
                        # C -> F : F = C*9/5 + 32
                        result = val * 9/5 + 32
                        last = result
                        history.append(f"{expr} = {result}")
                        print(f"{val} {from_u} = {result} {to_u}")
                    elif (from_u, to_u) in (("f", "c"), ("fahrenheit", "celsius"), ("°f","°c")):
                        result = (val - 32) * 5/9
                        last = result
                        history.append(f"{expr} = {result}")
                        print(f"{val} {from_u} = {result} {to_u}")
                    elif (from_u, to_u) in (("c","k"),("celsius","kelvin")):
                        result = val + 273.15
                        last = result
                        history.append(f"{expr} = {result}")
                        print(f"{val} {from_u} = {result} {to_u}")
                    elif (from_u, to_u) in (("k","c"),("kelvin","celsius")):
                        result = val - 273.15
                        last = result
                        history.append(f"{expr} = {result}")
                        print(f"{val} {from_u} = {result} {to_u}")
                    else:
                        print("Unsupported conversion pair. Supported examples: cm↔inch, m↔ft, kg↔lb, km↔mile, c↔f, c↔k")
                continue
            except Exception as e:
                print("Conversion error:", e)
                continue

        # If sympy plotting/diff/solve requested but not available, give message
        if expr.startswith("plot("):
            if not (HAS_SYMPY and HAS_MPL):
                print("Plotting requires sympy and matplotlib. Install them (`pip install sympy matplotlib`) to use plot().")
                continue
            # else, let the plot code in SymPy branch below handle it

        if expr.startswith("diff(") or expr.startswith("solve("):
            if not HAS_SYMPY:
                print("Symbolic features require sympy. Install it (`pip install sympy`) to use diff()/solve().")
                continue

        # Plot/diff/solve implemented if sympy present
        if HAS_SYMPY and expr.startswith("plot(") and expr.endswith(")"):
            try:
                # expected: plot(formula, [x1,x2])
                args = expr[5:-1].split(",[", 1)
                if len(args) != 2:
                    raise ValueError("Use: plot(formula, [x1,x2]) e.g. plot(sin(x), [0, 6.28])")
                formula = args[0].strip()
                rng = args[1].strip(" []")
                x1, x2 = map(float, rng.split(","))
                x = sp.Symbol('x')
                f = sp.sympify(formula, {"sin": sp.sin, "cos": sp.cos, "pi": sp.pi, "e": sp.E})
                fx = sp.lambdify(x, f, "math")
                X = [x1 + i * (x2 - x1) / 400 for i in range(401)]
                Y = [fx(val) for val in X]
                plt.plot(X, Y)
                plt.title(formula)
                plt.grid(True)
                plt.show()
            except Exception as e:
                print("Plot error:", e)
            continue

        if HAS_SYMPY and expr.startswith("diff(") and expr.endswith(")"):
            try:
                args = expr[5:-1].split(",")
                func = args[0].strip()
                var = args[1].strip()
                x = sp.Symbol(var)
                d = sp.diff(sp.sympify(func), x)
                print(f"d/d{var} of {func} = {d}")
                history.append(f"{expr} = {d}")
            except Exception as e:
                print("Diff error:", e)
            continue

        if HAS_SYMPY and expr.startswith("solve(") and expr.endswith(")"):
            try:
                args = expr[6:-1].split(",")
                func = args[0].strip()
                var = args[1].strip()
                x = sp.Symbol(var)
                sol = sp.solve(sp.sympify(func), x)
                print(f"Solutions for {func}=0: {sol}")
                history.append(f"{expr} = {sol}")
            except Exception as e:
                print("Solve error:", e)
            continue

        # Normal calculation or assignment
        try:
            if "=" in expr:
                var, val = expr.split("=", 1)
                var = var.strip()
                val = val.strip()
                result = eval(val, {"__builtins__": None}, {**allowed, **memory, "_": last, "mem": mem_value})
                memory[var] = result
                last = result
                history.append(f"{var} = {result}")
                print(f"{var} = {result}")
            else:
                result = eval(expr, {"__builtins__": None}, {**allowed, **memory, "_": last, "mem": mem_value})
                last = result
                history.append(f"{expr} = {result}")
                print("= ", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    ultra_calc()
