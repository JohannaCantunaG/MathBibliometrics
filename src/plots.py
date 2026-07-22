import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from .utils_plots import (
    _format_growth_axis, 
    _add_fit_summary,
    _plot_author_community_panel,
    _add_segment_fit_summary,
    _plot_community_growth_field
)

def plot_publication_series(
        df,
        columns,
        ax,
        ylabel,
        title,
        year_min=2008,
        year_max=2025,
        add_legend=False,
        single_series_color="black",
        fontsize=20,
    ):
    
    if isinstance(columns, str):
        columns = [columns]

    colors = plt.cm.tab20.colors

    for index, column in enumerate(columns):
        plot_kwargs = {"marker": "o", "label": column.replace("_", " ")}

        if len(columns) == 1:
            plot_kwargs["color"] = single_series_color
        else:
            plot_kwargs["color"] = colors[index % len(colors)]

        ax.plot(df["Year"], df[column], **plot_kwargs)

    ax.set_xlabel("Year", fontname="Times New Roman", fontsize=fontsize)
    ax.set_ylabel(ylabel, fontname="Times New Roman", fontsize=fontsize)
    ax.set_title(title, fontname="Times New Roman", fontsize=24, pad=15)
    ax.set_xlim(year_min, year_max)
    ax.set_xticks(range(year_min, year_max + 1, 2))
    ax.tick_params(axis="both", labelsize=fontsize)

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontname("Times New Roman")

    ax.grid(True, alpha=0.3)
    if add_legend:
        legend_font = FontProperties(family="Times New Roman", size=10)
        ax.legend(prop=legend_font, ncol=2 if len(columns) > 1 else 1)

    return ax

def plot_publications_annual_cumulative(
        annual_df,
        cumulative_df,
        columns,
        year_min, 
        year_max,
        outdir, 
        outname,
        cumulative_ylabel="Number of cumulative publications",
        annual_ylabel="Number of publications",
        add_legend=False,
        cumulative_plain_ticks=False,
        file_format = "pdf"
    ):
    
    fig, axes = plt.subplots(1, 2, figsize=(20, 6), constrained_layout = True)

    plot_publication_series(
        df=cumulative_df,
        columns=columns,
        ax=axes[0],
        ylabel=cumulative_ylabel,
        title="Cumulative publications",
        year_min=year_min,
        year_max=year_max,
        add_legend=add_legend,
        fontsize=21,
    )

    plot_publication_series(
        df=annual_df,
        columns=columns,
        ax=axes[1],
        ylabel=annual_ylabel,
        title="Annual publications",
        year_min=year_min,
        year_max=year_max,
        add_legend=add_legend,
        fontsize=21,
    )

    if cumulative_plain_ticks:
        axes[0].ticklabel_format(style="plain", axis="y")
    fig.savefig(outdir / f"{outname}.{file_format}", format=file_format)
    plt.show()

def plot_global_segmented_fits(
        df,
        name_column,
        best_global,
        best_pre,
        best_post,
        break_year,
        year_min,
        year_max,
        outdir, 
        outname,
        use_semilogy=True,
        text_loc_global="tl",
        text_loc_pre="tl",
        text_loc_post="tr",
        file_format = "pdf"
    ):

    fig, axes = plt.subplots(1, 2, figsize=(18, 6))
    plot_function_left = axes[0].semilogy if use_semilogy else axes[0].plot
    plot_function_right = axes[1].semilogy if use_semilogy else axes[1].plot
    plot_function_left(df["Year"], df[name_column], "o", color="black", label="Data",)
    plot_function_left(best_global["years_dense"], best_global["ycurve"], "-", label=f"Best fit: {best_global['model']}",)

    _add_fit_summary(
        ax=axes[0],
        fit_result=best_global,
        location=text_loc_global,
    )

    _format_growth_axis(
        ax=axes[0],
        year_min=year_min,
        year_max=year_max,
        ylabel="Publications per year",
        title="Global Fit",
    )

    plot_function_right(df["Year"], df[name_column], "o", color="black", label="Data")
    plot_function_right(best_pre["years_dense"], best_pre["ycurve"], "-", label=f"{year_min}–{break_year}: {best_pre['model']}")
    plot_function_right(best_post["years_dense"], best_post["ycurve"], "-", label=f"{break_year + 1}–{year_max}: {best_post['model']}")
    axes[1].axvline(break_year, linewidth=1, label=f"Break year: {break_year}")
    _add_fit_summary(
        ax=axes[1],
        fit_result=best_pre,
        location=text_loc_pre,
        period=f"{year_min}–{break_year}",
    )
    _add_fit_summary(
        ax=axes[1],
        fit_result=best_post,
        location=text_loc_post,
        period=f"{break_year + 1}–{year_max}",
    )
    _format_growth_axis(
        ax=axes[1],
        year_min=year_min,
        year_max=year_max,
        ylabel="",
        title="Piecewise Fit",
    )

    fig.subplots_adjust(wspace=0.2)
    fig.savefig(outdir / f"{outname}.{file_format}", format=file_format, bbox_inches="tight")
    plt.show()

def plot_document_type_analysis(
        document_type_counts,
        document_type_shares,
        count_column,
        share_columns,
        share_labels,
        year_min,
        year_max,
        outdir,
        outname,
        title_share,
        histogram_log_scale=True,
        share_ylim=(0,100),
        file_format = "pdf"
    ):

    if len(share_columns) != len(share_labels):
        raise ValueError("share_columns and share_labels must have the same length.")
    
    counts_plot = document_type_counts.drop(
        index="Total",
        errors="ignore",
    )

    fig, axes = plt.subplots(1, 2, figsize=(18, 6))
    axes[0].bar(range(len(counts_plot)), counts_plot[count_column], edgecolor="black",)
    axes[0].set_ylabel("Number of publications", fontname="Times New Roman", fontsize=20,)
    axes[0].set_xticks(range(len(counts_plot)))
    axes[0].set_xticklabels(counts_plot.index, rotation=45, ha="right", fontname="Times New Roman", fontsize=20,)

    if histogram_log_scale:
        axes[0].set_yscale("log")
    axes[0].set_title("Document type distribution (log scale)", fontname="Times New Roman", fontsize=24, pad=12,)
    axes[0].grid(axis="y", alpha=0.3,)

    for label in axes[0].get_yticklabels():
        label.set_fontname("Times New Roman")
        label.set_fontsize(20)

    markers = ["o", "s", "^", "D", "v", "P", "X"]
    for index, (column, label) in enumerate(zip(share_columns, share_labels)):
        axes[1].plot(document_type_shares["Year"], document_type_shares[column], marker=markers[index % len(markers)], label=label,)

    axes[1].set_xlabel("Year", fontname="Times New Roman", fontsize=20,)
    axes[1].set_ylabel("Share of total publications (%)", fontname="Times New Roman", fontsize=20,)
    axes[1].set_xlim(year_min, year_max,)  
    axes[1].set_ylim(*share_ylim)
    axes[1].set_xticks(range(year_min, year_max + 1, 2))
    axes[1].set_title(title_share, fontname="Times New Roman", fontsize=24, pad=12,)
    axes[1].grid(True, alpha=0.3,)
    axes[1].legend(prop={"family": "Times New Roman", "size": 14,})

    for label in (axes[1].get_xticklabels() + axes[1].get_yticklabels()):
        label.set_fontname("Times New Roman")
        label.set_fontsize(20)

    fig.subplots_adjust(wspace=0.35)
    fig.tight_layout()
    fig.savefig(outdir / f"{outname}.{file_format}", format=file_format, bbox_inches="tight")
    plt.show()

def plot_author_communities_truncation_comparison(
        community_truncated,
        community_full,
        best_truncated,
        best_full,
        year_min,
        year_max,
        outdir,
        outname,
        fontsize=20,
        add_legend=True,
        text_loc_truncated="br",
        text_loc_full="br",
        file_format = "pdf"
    ):
    
    fig, axes = plt.subplots(1, 2, figsize=(18, 6))
    _plot_author_community_panel(
        community_df=community_truncated,
        best_fit=best_truncated,
        ax=axes[0],
        year_min=year_min,
        year_max=year_max,
        title="Window truncated at start",
        ylabel="Number of scientists",
        fontsize=fontsize,
        add_legend=add_legend,
        text_loc=text_loc_truncated,
    )
    _plot_author_community_panel(
        community_df=community_full,
        best_fit=best_full,
        ax=axes[1],
        year_min=year_min,
        year_max=year_max,
        title="Full 5-year window",
        ylabel="",
        fontsize=fontsize,
        add_legend=add_legend,
        text_loc=text_loc_full,
    )
    fig.subplots_adjust(wspace=0.1, bottom=0.18)
    fig.savefig(outdir / f"{outname}.{file_format}", format=file_format, bbox_inches="tight",)
    plt.show()

def plot_author_productivity_twofits_auto(
        mean_prod,
        best,
        name, 
        outdir,
        outname,
        file_format = "pdf"
    ):
    
    x = best["x"]
    y = best["y"]
    k = best["k"]
    x1, y1 = x[:k], y[:k]
    x2, y2 = x[k:], y[k:]
    f1 = best["fit1"]
    f2 = best["fit2"]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.loglog(x, y, "o", markersize=4, label="Data")
    y1_hat = f1["a"] * x1 ** (-f1["b"])
    y2_hat = f2["a"] * x2 ** (-f2["b"])
    ax.loglog(x1, y1_hat, "-", linewidth=2, label=f"Fit 1: a={f1['a']:.2f}, b={f1['b']:.2f} (R²={f1['r2']:.3f})")
    ax.loglog(x2, y2_hat, "--", linewidth=2, label=f"Fit 2: a={f2['a']:.2f}, b={f2['b']:.2f} (R²={f2['r2']:.3f})")
    ax.axvline(best["break_x"], linestyle=":", linewidth=1)
    ax.set_xlabel("Number of publications per author", fontname="Times New Roman", fontsize=24)
    ax.set_ylabel("Author frequency", fontname="Times New Roman", fontsize=24)
    ax.set_title(name.replace("_", " "), fontname="Times New Roman", fontsize=24)

    for lab in ax.get_xticklabels() + ax.get_yticklabels():
        lab.set_fontname("Times New Roman")
        lab.set_fontsize(20)

    ax.grid(True, which="both", linestyle="--", alpha=0.5)
    ax.text(0.05, 0.05, f"Mean productivity = {mean_prod:.2f}\nBreak at x ≈ {best['break_x']:.0f}",
            transform=ax.transAxes, fontsize=12, fontname="Times New Roman", va="bottom", ha="left", bbox=dict(facecolor="white", alpha=0.7, edgecolor="none"))
    ax.legend(prop={"family": "Times New Roman", "size": 12})
    plt.tight_layout()
    plt.savefig(outdir / f"{outname}.{file_format}", format=file_format, bbox_inches="tight")
    plt.show()
    print("\n=== Two power-law fits (auto) ===")
    print("Break x ≈", best["break_x"])
    print("Fit 1:", f"y = {f1['a']:.2f} / x^{f1['b']:.2f}", "R2 =", round(f1["r2"], 4))
    print("Fit 2:", f"y = {f2['a']:.2f} / x^{f2['b']:.2f}", "R2 =", round(f2["r2"], 4))

    return {"mean_prod": mean_prod, "break_x": best["break_x"], "fit1": f1, "fit2": f2}

def plot_bradford_single(
        ranks,
        cumulative,
        percent_top,
        leimkuhler_compute,
        x_dense,
        outdir,
        outname,
        top_frac=0.10,
        file_format = "pdf"
    ):
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.loglog(ranks, cumulative, 'o', markersize=3, label="Data")
    ax.loglog(x_dense, leimkuhler_compute, '-', label="Leimkuhler fit")
    ax.set_xlabel("Number of periodicals ranked by decreasing productivity", fontname="Times New Roman", fontsize=24)
    ax.set_ylabel("Cumulative number of publications", fontname="Times New Roman", fontsize=24)
    ax.set_ylim(1e4, 2e6)
    ax.set_title("Mathematics", fontname="Times New Roman", fontsize=24)
    ax.grid(True, which="both", linestyle="--", alpha=0.5)

    for lab in ax.get_xticklabels() + ax.get_yticklabels():
        lab.set_fontname("Times New Roman")
        lab.set_fontsize(20)

    ax.text(0.05, 0.10, f"Top {int(top_frac*100)}% → {percent_top:.1f}%",
            transform=ax.transAxes, fontsize=12, fontname="Times New Roman", bbox=dict(facecolor="white", alpha=0.7, edgecolor="none"))
    ax.legend(prop={"family": "Times New Roman", "size": 14})
    plt.tight_layout()
    plt.savefig(outdir / f"{outname}.{file_format}", format=file_format, bbox_inches="tight")
    plt.show()
    print(ax.get_ylim())

def plot_field_segmented_growth_group(
        fields_group,
        publications_by_field,
        growth_fits_by_field,
        outdir,
        outname,
        figsize_unit=(6, 6),
        fontsize=20,
        use_semilogy=False,
        file_format = "pdf"
    ):
    
    n_fields = len(fields_group)
    fig, axes = plt.subplots(1, n_fields, figsize=( figsize_unit[0] * n_fields, figsize_unit[1]), squeeze=False)
    axes = axes.ravel()

    for index, (ax, field) in enumerate(zip(axes, fields_group)):
        publications_field = publications_by_field[field]
        segment_results = growth_fits_by_field[field]
        plot_function = ax.semilogy if use_semilogy else ax.plot
        plot_function(
            publications_field["Year"], 
            publications_field[field], 
            "o", 
            label="Data"
        )

        for segment_result in segment_results:
            best_fit = segment_result["best_fit"]
            plot_function(
                best_fit["years_dense"],
                np.maximum(best_fit["ycurve"], 1e-12) if use_semilogy else best_fit["ycurve"],
                "-",
                label=(f"{segment_result['label']}: {best_fit['model']}")
            )
            _add_segment_fit_summary(
                ax=ax,
                fit_result=best_fit,
                segment_label=segment_result["label"],
                location=segment_result["text_location"],
            )
        year_min = int(publications_field["Year"].min())
        year_max = int(publications_field["Year"].max())
        ax.set_xticks(range(year_min, year_max + 1, 2))
        ax.set_xlabel("Year", fontname="Times New Roman", fontsize=fontsize)

        if index == 0:
            ax.set_ylabel("Publications per year", fontname="Times New Roman", fontsize=fontsize)
        else:
            ax.set_ylabel("")
        ax.set_title(field.replace("_", " "), fontname="Times New Roman", fontsize=fontsize)
        ax.grid(True, which="both", alpha=0.3,)
        ax.legend(prop={"family": "Times New Roman", "size": 9})

        for label in (ax.get_xticklabels() + ax.get_yticklabels()):
            label.set_fontname("Times New Roman")
            label.set_fontsize(19)

    fig.tight_layout()
    fig.savefig(outdir / f"{outname}.{file_format}", format=file_format, bbox_inches="tight")
    plt.show()

def plot_community_fields_in_pages(
        fields,
        community_by_field,
        growth_fits_by_field,
        outdir,
        outname_prefix="authorsGrowthFields",
        fontsize=14,
        ncols=3,
        figsize=(18, 5),
        add_legend=False,
        file_format = "pdf"
    ):

    pages = [fields[index:index + ncols] for index in range(0, len(fields), ncols)]
    for page_number, page_fields in enumerate(pages, start=1):
        n_fields = len(page_fields)
        fig, axes = plt.subplots(1, ncols, figsize=figsize, squeeze=False)
        axes = axes.ravel()
        for unused_ax in axes[n_fields:]:
            fig.delaxes(unused_ax)
        for index, field in enumerate(page_fields):
            _plot_community_growth_field(
                ax=axes[index],
                community_df=community_by_field[field],
                fit_result=growth_fits_by_field[field],
                fontsize=fontsize,
                add_ylabel=index == 0,
                add_legend=add_legend,
            )
            axes[index].set_title(field.replace("_", " "), fontname="Times New Roman", fontsize=fontsize)

        fig.tight_layout()
        output_file = (outdir / f"{outname_prefix}_{page_number:02d}.{file_format}")
        fig.savefig(output_file, format=file_format, bbox_inches="tight")
        plt.show()

def plot_bradford_ax(
        stats,
        ax,
        top_frac=0.10,
        fontsize=14,
        add_ylabel=True,
        add_legend=False,
        fixed_ylim=None,
    ):
    
    ranks = stats["ranks"]
    cumulative = stats["cumulative"]
    x_dense = stats["x_dense"]
    y_dense = stats["y_dense"]
    ax.loglog(ranks, cumulative, "o", markersize=3, label="Data",)
    ax.loglog(x_dense, y_dense,"-", label="Leimkuhler fit")
    ax.set_xlabel("Periodicals ranked by decreasing productivity", fontname="Times New Roman", fontsize=fontsize)

    if add_ylabel:
        ax.set_ylabel("Cumulative number of publications", fontname="Times New Roman", fontsize=fontsize)
    else:
        ax.set_ylabel("")

    if fixed_ylim is not None:
        ax.set_ylim(*fixed_ylim)
    ax.grid(True, which="both", linestyle="--", alpha=0.5,)
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_fontname("Times New Roman")
        label.set_fontsize(fontsize)
    ax.text(0.05, 0.10,(f"Top {int(top_frac * 100)}% → {stats['percent_top']:.1f}%"), transform=ax.transAxes,
            fontsize=max(fontsize - 4, 8), fontname="Times New Roman", bbox={"facecolor": "white", "alpha": 0.7, "edgecolor": "none"},)

    if add_legend:
        ax.legend(prop={"family": "Times New Roman", "size": max(fontsize - 2, 8)})

    return ax

def plot_bradford_fields_in_pages(
        fields,
        bradford_stats_by_field,
        outdir,
        top_frac=0.10,
        fontsize=20,
        ncols=3,
        fixed_ylim=None,
        outname_prefix="BradfordFields",
        file_format = "pdf"
    ):
    
    missing_fields = [ field for field in fields if field not in bradford_stats_by_field]
    if missing_fields:
        raise KeyError("Missing Bradford results for: " f"{missing_fields}")

    pages = [fields[index:index + ncols] for index in range(0, len(fields), ncols)]
    for page_number, page_fields in enumerate(pages, start=1):
        n_fields = len(page_fields)
        fig, axes = plt.subplots(1, ncols, figsize=(18, 5), squeeze=False)
        axes = axes.ravel()

        for unused_ax in axes[n_fields:]:
            fig.delaxes(unused_ax)
        for index, field in enumerate(page_fields):
            ax = axes[index]
            plot_bradford_ax(
                stats=bradford_stats_by_field[field],
                ax=ax,
                top_frac=top_frac,
                fontsize=fontsize,
                add_ylabel=index == 0,
                add_legend=(index == 0 and page_number == 1),
                fixed_ylim=fixed_ylim,
            )
            ax.set_title(field.replace("_", " "), fontname="Times New Roman", fontsize=fontsize)
        fig.tight_layout()
        output_file = (outdir / f"{outname_prefix}_{page_number:02d}.{file_format}")
        fig.savefig(output_file, format=file_format, bbox_inches="tight")

        plt.show()