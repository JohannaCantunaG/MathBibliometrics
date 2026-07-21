import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.optimize import curve_fit

import numpy as np
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def fit_best_growth_model(
        df,
        name_column,
        models=None,
        criterion="aic",
    ):
    
    years = df["Year"].values.astype(float)
    y = df[name_column].values.astype(float)

    if models is None:
        models = ["linear", "exponential", "poly2", "poly3", "logistic"]
    
    valid_models = {"linear", "exponential", "poly2", "poly3", "logistic"}
    unknown_models = set(models) - valid_models

    if unknown_models:
        raise ValueError(f"Unknown models: {sorted(unknown_models)}")

    if criterion not in {"aic", "r2"}:
        raise ValueError("criterion must be either 'aic' or 'r2'.")

    years = np.asarray(years, dtype=float)
    y = np.asarray(y, dtype=float)
    mask = np.isfinite(years) & np.isfinite(y) & (y > 0)
    years = years[mask]
    y = y[mask]

    if len(y) < 4:
        raise ValueError("At least four valid observations are required.")

    year0 = years.min()
    t = years - year0
    t_2d = t.reshape(-1, 1)
    t_dense = np.linspace(t.min(), t.max(), 300)
    years_dense = t_dense + year0
    eps = 1e-12
    results = {}

    def aic_from_rss(rss, n, n_parameters):
        rss = max(float(rss), eps)
        return n * np.log(rss / n) + 2 * n_parameters

    def build_result(yhat, ycurve, parameters, n_parameters):
        rss = np.sum((y - yhat) ** 2)

        return {
            "r2": float(r2_score(y, yhat)),
            "aic": float(aic_from_rss(rss=rss, n=len(y), n_parameters=n_parameters)),
            "params": parameters,
            "ycurve": np.asarray(ycurve),
            "years_dense": years_dense,
        }

    if "linear" in models:
        try:
            model = LinearRegression().fit(t_2d, y)
            results["linear"] = build_result(
                yhat=model.predict(t_2d),
                ycurve=model.predict(t_dense.reshape(-1, 1)),
                parameters={"intercept": float(model.intercept_), "slope": float(model.coef_[0])},
                n_parameters=2,
            )
        except (ValueError, RuntimeError):
            pass

    if "exponential" in models:
        try:
            y_log = np.log(np.maximum(y, eps))
            model = LinearRegression().fit(t_2d, y_log)
            a = float(model.intercept_)
            b = float(model.coef_[0])
            doubling_time = np.log(2) / b if b > 0 else np.nan
            results["exponential"] = build_result(
                yhat=np.exp(model.predict(t_2d)),
                ycurve=np.exp(model.predict(t_dense.reshape(-1, 1))),
                parameters={"a": a, "b": b, 
                            "doubling_time": ( float(doubling_time)if np.isfinite(doubling_time) else np.nan)},
                n_parameters=2,
            )
        except (ValueError, RuntimeError, FloatingPointError):
            pass

    def fit_polynomial(degree):
        coefficients = np.polyfit(t, y, deg=degree)
        polynomial = np.poly1d(coefficients)

        return build_result(
            yhat=polynomial(t),
            ycurve=polynomial(t_dense),
            parameters={"degree": degree, "coefficients": coefficients.tolist()},
            n_parameters=degree + 1,
        )

    if "poly2" in models:
        try:
            results["poly2"] = fit_polynomial(2)
        except (ValueError, RuntimeError, np.linalg.LinAlgError):
            pass

    if "poly3" in models:
        try:
            results["poly3"] = fit_polynomial(3)
        except (ValueError, RuntimeError, np.linalg.LinAlgError):
            pass

    if "logistic" in models:
        try:
            def logistic(values, carrying_capacity, rate, midpoint):
                return carrying_capacity / (1.0 + np.exp(-rate * (values - midpoint)))

            initial_parameters = [y.max() * 1.2, 0.05, np.median(t)]
            bounds = ([0.0, 0.0, t.min() - 10.0], [np.inf, 5.0, t.max() + 10.0])

            parameters, _ = curve_fit(
                logistic,
                t,
                y,
                p0=initial_parameters,
                bounds=bounds,
                maxfev=20_000,
            )

            carrying_capacity, rate, midpoint = parameters
            results["logistic"] = build_result(
                yhat=logistic(t, *parameters),
                ycurve=logistic(t_dense, *parameters),
                parameters={"carrying_capacity": float(carrying_capacity),
                            "rate": float(rate),
                            "midpoint": float(midpoint)},
                n_parameters=3,
            )
        except (ValueError, RuntimeError, OverflowError):
            pass

    if not results:
        raise ValueError("None of the requested models could be fitted.")

    if criterion == "r2":
        best_name = max(results, key=lambda model_name: results[model_name]["r2"])
    else:
        best_name = min(results, key=lambda model_name: results[model_name]["aic"])

    best = {"model": best_name, **results[best_name]}

    return best, results

def fit_powerlaw_logspace(x, y):
    
    x = np.asarray(x, float)
    y = np.asarray(y, float)

    mask = np.isfinite(x) & np.isfinite(y) & (x > 0) & (y > 0)
    x = x[mask]
    y = y[mask]

    lx = np.log(x)
    ly = np.log(y)

    m, c = np.polyfit(lx, ly, 1)
    ly_hat = c + m*lx

    sse = float(np.sum((ly - ly_hat) ** 2))
    ss_tot = float(np.sum((ly - np.mean(ly)) ** 2))
    r2 = 1 - sse / ss_tot if ss_tot > 0 else np.nan

    a = float(np.exp(c))
    b = float(-m)

    return {"a": a, "b": b, "r2": r2, "sse": sse}

def find_best_two_powerlaws(freq, min_points=6):
    
    x = freq.index.values.astype(float)
    y = freq.values.astype(float)

    mask = np.isfinite(x) & np.isfinite(y) & (x > 0) & (y > 0)
    x = x[mask]
    y = y[mask]
    order = np.argsort(x)
    x = x[order]
    y = y[order]

    n = len(x)
    if n < 2 * min_points + 1:
        raise ValueError("Very few points to automatically adjust two sections.")

    best = None
    for k in range(min_points, n - min_points):
        x1, y1 = x[:k], y[:k]
        x2, y2 = x[k:], y[k:]
        fit1 = fit_powerlaw_logspace(x1, y1)
        fit2 = fit_powerlaw_logspace(x2, y2)
        total_sse = fit1["sse"] + fit2["sse"]

        if (best is None) or (total_sse < best["total_sse"]):
            best = {"k": k, "break_x": float(x[k]), "fit1": fit1, "fit2": fit2, "total_sse": float(total_sse), "x": x, "y": y}

    return best

def leimkuhler(x, a, b):
    return a * np.log(1 + b*x)

def format_equation(
        best, 
        year0, 
        decimals=2
    ):
    
    m = best["model"]
    p = best.get("params", {})
    print("-------->",p)

    if m == "linear":
        a = round(p["intercept"], decimals)
        b = round(p["slope"], decimals)
        return f"y = {a} + {b} (Year - {int(year0)})"

    if m == "exponential":
        a = round(p["a"], decimals)
        b = round(p["b"], decimals)
        A = np.exp(p["a"])
        A = round(A, decimals)
        eq1 = f"log(y) = {a} + {b} (Year - {int(year0)})"
        eq2 = f"y = {A} · exp({b} (Year - {int(year0)}))"
        T = p.get("doubling_time", np.nan)
        if np.isfinite(T):
            eq2 += f"   |   T = {round(T, decimals)} years"
        return eq1 + "\n" + eq2

    if m in ("poly2", "poly3"):
        coeffs = p["coefficients"]
        deg = p["degree"]
        terms = []
        for i, c in enumerate(coeffs):
            power = deg - i
            c = round(c, decimals)
            if power == 0:
                terms.append(f"{c}")
            elif power == 1:
                terms.append(f"{c}(Year - {year0})")
            else:
                terms.append(f"{c}(Year - {year0})^{power}")
        poly_txt = " + ".join(terms).replace("+ -", "- ")
        return f"y = {poly_txt}"

    if m == "logistic":
        K  = round(p["carrying_capacity"], decimals)
        r  = round(p["rate"], decimals)
        t0 = round(p["midpoint"], decimals)
        return f"y = {K} / (1 + exp(-{r}·((Year -{year0}) - {t0})))"

    return f"Model {m} (without equation formatting )"

def fit_forced_growth_segments(
        df,
        name_column,
        segments,
        criterion="aic",
        min_points=4,
    ):

    parts = []
    for model_name, start_year, end_year in segments:
        df_segment = df[df["Year"].between(start_year, end_year)].copy()
        if len(df_segment) < min_points:
            parts.append({
                "model": model_name,
                "years_range": (int(start_year), int(end_year)),
                "status": f"skip (<{min_points} points)",
            })
            continue

        try:
            best_segment, all_results = (
                fit_best_growth_model(
                    df=df_segment,
                    name_column=name_column,
                    models=[model_name],
                    criterion=criterion,
                )
            )

            best_segment["years_range"] = (int(start_year), int(end_year))
            best_segment["status"] = "ok"
            best_segment["df"] = df_segment
            best_segment["all_results"] = all_results
            parts.append(best_segment)

        except ValueError as error:
            parts.append({
                "model": model_name,
                "years_range": (int(start_year), int(end_year)),
                "status": f"error: {error}",
            })

    valid_parts = [part for part in parts if part.get("status") == "ok"]

    if not valid_parts:
        raise ValueError("None of the predefined segments could be fitted.")

    return {"fit_type": "segments", "model": "forced_segments", "parts": parts}