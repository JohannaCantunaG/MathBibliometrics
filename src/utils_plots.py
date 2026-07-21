import numpy as np

def _format_growth_axis(
        ax,
        year_min,
        year_max,
        ylabel,
        title,
        fontsize=20,
    ):
    
    ax.set_xlim(year_min, year_max)
    ax.set_xticks(range(year_min, year_max + 1, 2))
    ax.set_xlabel("Year", fontname="Times New Roman", fontsize=fontsize)
    ax.set_ylabel(ylabel, fontname="Times New Roman", fontsize=fontsize)
    ax.set_title(title, fontname="Times New Roman", fontsize=24, pad=15)
    ax.tick_params(axis="both", labelsize=fontsize)

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontname("Times New Roman")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend(prop={"family": "Times New Roman", "size": 11})

    return ax

def _add_fit_summary(
        ax,
        fit_result,
        location="tl",
        period=None,
    ):
    
    locations = {"tl": (0.03, 0.95), "tr": (0.97, 0.95),
                 "bl": (0.03, 0.05), "br": (0.97, 0.05)}

    if location not in locations:
        raise ValueError("location must be 'tl', 'tr', 'bl', or 'br'.")

    x_position, y_position = locations[location]
    text_lines = []

    if period is not None:
        text_lines.append(period)

    text_lines.extend([
        f"Best fit: {fit_result['model']}",
        f"R² = {fit_result['r2']:.3f}",
        f"AIC = {fit_result['aic']:.1f}",
    ])

    if fit_result["model"] == "exponential":
        doubling_time = fit_result["params"].get("doubling_time", np.nan)
        if np.isfinite(doubling_time):
            text_lines.append(f"T = {doubling_time:.1f} years")

    ax.text(x_position, y_position, "\n".join(text_lines),
            transform=ax.transAxes,
            fontsize=12,
            fontname="Times New Roman",
            va="top" if y_position > 0.5 else "bottom",
            ha="left" if x_position < 0.5 else "right",
            bbox={"facecolor": "white", "alpha": 0.7, "edgecolor": "none"},
    )

    return ax

def _plot_author_community_panel(
        community_df,
        best_fit,
        ax,
        year_min,
        year_max,
        title,
        ylabel,
        fontsize=20,
        add_legend=True,
        text_loc="br",
        legend_loc="best"
    ):
    
    years = community_df["Year"].to_numpy(dtype=float)
    authors_5y = community_df["Authors_5y"].to_numpy(dtype=float)
    authors_5y_gt1 = community_df["Authors_5y_gt1pub"].to_numpy(dtype=float)
    active_community = community_df["Community_c"].to_numpy(dtype=float)
    ax.semilogy(years, authors_5y, "x", label="Authors within 5 years")
    ax.semilogy(years, authors_5y_gt1, "^", label="Authors within 5 years with pubs > 1")
    ax.semilogy(years, active_community, "o", label="Definition (c)")
    ax.semilogy(best_fit["years_dense"], np.maximum(best_fit["ycurve"], 1e-12), "-", label=f"Best fit: {best_fit['model']}")
    #ax.set_xlim(year_min, year_max)
    ax.set_xticks(range(year_min, year_max + 1, 2))
    ax.set_xlabel("Year", fontname="Times New Roman", fontsize=fontsize)
    ax.set_ylabel(ylabel, fontname="Times New Roman", fontsize=fontsize)
    ax.set_title(title, fontname="Times New Roman", fontsize=24, pad=12)
    ax.tick_params(axis="both", labelsize=18)

    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_fontname("Times New Roman")
    ax.grid(True, which="both", linestyle="--", alpha=0.6)

    _add_community_fit_summary(
        ax=ax,
        fit_result=best_fit,
        location=text_loc,
    )
    if add_legend:
        ax.legend(fontsize = 8)

    return ax

def _add_community_fit_summary(
        ax,
        fit_result,
        location="br",
    ):
    
    locations = {"tl": (0.03, 0.95), "tr": (0.97, 0.95), 
                 "bl": (0.03, 0.05), "br": (0.97, 0.05)}
    if location not in locations:
        raise ValueError("location must be 'tl', 'tr', 'bl', or 'br'.")
    x_position, y_position = locations[location]
    text = (
        f"Best fit: {fit_result['model']}\n"
        f"R² = {fit_result['r2']:.3f}\n"
        f"AIC = {fit_result['aic']:.1f}"
    )
    if fit_result["model"] == "exponential":
        doubling_time = fit_result["params"].get("doubling_time", np.nan)
        if np.isfinite(doubling_time):
            text += (f"\nT = {doubling_time:.1f} years")

    ax.text(x_position, y_position, text,
            transform=ax.transAxes,
            fontname="Times New Roman",
            fontsize=12,
            va="top" if y_position > 0.5 else "bottom",
            ha="left" if x_position < 0.5 else "right",
            bbox={"facecolor": "white", "alpha": 0.7, "edgecolor": "none"},
    )

    return ax

def _add_segment_fit_summary(
        ax,
        fit_result,
        segment_label,
        location,
    ):
    
    locations = {"tl": (0.03, 0.95), "tr": (0.97, 0.95),
                 "bl": (0.03, 0.05), "br": (0.97, 0.05)}
    x_position, y_position = locations[location]
    text = (
        f"{segment_label}\n"
        f"Best: {fit_result['model']}\n"
        f"R² = {fit_result['r2']:.3f}\n"
        f"AIC = {fit_result['aic']:.1f}"
    )
    if fit_result["model"] == "exponential":
        doubling_time = fit_result["params"].get("doubling_time", np.nan,)
        if np.isfinite(doubling_time):
            text += f"\nT = {doubling_time:.1f} years"
    ax.text(x_position, y_position, text,
            transform=ax.transAxes,
            fontname="Times New Roman",
            fontsize=10,
            va="top" if y_position > 0.5 else "bottom",
            ha="left" if x_position < 0.5 else "right",
            bbox={"facecolor": "white", "alpha": 0.7, "edgecolor": "none"},
    )
    return ax

def _plot_community_growth_field(
        ax,
        community_df,
        fit_result,
        fontsize=14,
        add_ylabel=True,
        add_legend=False,
    ):
    
    community_df = (
        community_df
        .sort_values("Year")
        .reset_index(drop=True)
    )

    years = community_df["Year"].to_numpy(dtype=float)
    ax.semilogy(years, community_df["Authors_5y"], "x", label="Authors within 5 years")
    ax.semilogy(years, community_df["Authors_5y_gt1pub"], "^", label="Authors within 5 years with pubs>1")
    ax.semilogy(years, community_df["Community_c"], "o", label="Definition (c)")

    if fit_result["fit_type"] == "segments":
        valid_parts = [ part for part in fit_result["parts"] if part.get("status") == "ok"]

        for part in valid_parts:
            ycurve = np.maximum(np.asarray(part["ycurve"], dtype=float), 1e-12)
            ax.semilogy(part["years_dense"], ycurve, "-", label=f"Fit: {part['model']}")

        box_positions = [(0.02, 0.98), (0.98, 0.98), (0.02, 0.72)]
        for index, part in enumerate(valid_parts):
            text = (
                f"Best fit: {part['model']}\n"
                f"R² = {part['r2']:.3f}\n"
                f"AIC = {part['aic']:.1f}"
            )
            if part["model"] == "exponential":
                doubling_time = part["params"].get("doubling_time", np.nan)
                if np.isfinite(doubling_time):
                    text += (f"\nT = {doubling_time:.1f} years")
            x_position, y_position = box_positions[min(index, len(box_positions) - 1)]
            ax.text(x_position, y_position, text, transform=ax.transAxes, fontname="Times New Roman",
                    fontsize=12,
                    ha=("left" if x_position < 0.5 else "right"),
                    va="top",
                    bbox={"facecolor": "white", "alpha": 0.7, "edgecolor": "none"},
                    clip_on=True,
            )
    else:
        best_fit = fit_result["best_fit"]
        ycurve = np.maximum(np.asarray(best_fit["ycurve"], dtype=float), 1e-12)
        ax.semilogy(best_fit["years_dense"], ycurve, "-", label=f"Best fit: {best_fit['model']}")
        text = (
            f"Best fit: {best_fit['model']}\n"
            f"R² = {best_fit['r2']:.3f}\n"
            f"AIC = {best_fit['aic']:.1f}"
        )
        if best_fit["model"] == "exponential":
            doubling_time = best_fit["params"].get("doubling_time", np.nan)
            if np.isfinite(doubling_time):
                text += (f"\nT = {doubling_time:.1f} years")

        ax.text(0.02, 0.98, text, transform=ax.transAxes, fontname="Times New Roman", fontsize=12,
                ha="left",
                va="top",
                bbox={"facecolor": "white", "alpha": 0.7, "edgecolor": "none"},
                clip_on=True,
        )

    ax.set_xlabel("Year", fontname="Times New Roman", fontsize=fontsize)
    if add_ylabel:
        ax.set_ylabel("Number of scientists", fontname="Times New Roman", fontsize=fontsize)
    else:
        ax.set_ylabel("")

    ax.grid(True, which="both", linestyle="--", alpha=0.6)
    year_min = int(years.min())
    year_max = int(years.max())
    ax.set_xlim(year_min - 0.3, year_max + 0.3)
    ax.set_xticks(range(year_min, year_max + 1, 2))
    ax.tick_params(axis="both", labelsize=max(fontsize - 2, 8))

    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_fontname("Times New Roman")
    if add_legend:
        ax.legend(prop={"family": "Times New Roman", "size": 8})

    return ax