"""Módulo 4 — Visualização de Dados.

Complete cada função com o apoio do GitHub Copilot. Cada função deve **gerar um
gráfico e salvá-lo** no caminho ``out_path`` (formato PNG). Use ``matplotlib`` e
``seaborn``. Em ambientes sem interface gráfica (CI), mantenha o backend "Agg".

Valide com:  ``python lab/check.py --module viz``
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")  # backend sem interface gráfica (funciona no CI)
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import seaborn as sns  # noqa: E402


def plot_rating_distribution(df: pd.DataFrame, out_path: str):
    """Histograma da distribuição da coluna ``rating``. Inclua título e labels em
    português e salve a figura em ``out_path``."""
    fig, ax = plt.subplots()
    ax.hist(df["rating"].dropna(), bins=20)
    ax.set_title("Distribuição das notas")
    ax.set_xlabel("Nota")
    ax.set_ylabel("Quantidade")
    fig.tight_layout()
    fig.savefig(out_path, dpi=100)
    plt.close(fig)
    return fig


def plot_top_varieties(df: pd.DataFrame, out_path: str):
    """Gráfico de barras horizontais com as 10 variedades (``variety``) com maior
    quantidade de vinhos. Salve a figura em ``out_path``."""
    top_varieties = df["variety"].value_counts().head(10).sort_values()

    fig, ax = plt.subplots()
    ax.barh(top_varieties.index, top_varieties.values)
    ax.set_title("10 variedades mais frequentes")
    ax.set_xlabel("Quantidade")
    ax.set_ylabel("Variedade")
    fig.tight_layout()
    fig.savefig(out_path, dpi=100)
    plt.close(fig)
    return fig


def plot_boxplot_by_variety(df: pd.DataFrame, out_path: str):
    """Boxplot de ``rating`` para as 5 variedades mais frequentes. Salve a figura
    em ``out_path``."""
    top_varieties = df["variety"].value_counts().head(5).index
    filtered = df[df["variety"].isin(top_varieties)]

    fig, ax = plt.subplots()
    sns.boxplot(data=filtered, x="variety", y="rating", ax=ax)
    ax.set_title("Distribuição das notas pelas 5 variedades mais frequentes")
    ax.set_xlabel("Variedade")
    ax.set_ylabel("Nota")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    fig.savefig(out_path, dpi=100)
    plt.close(fig)
    return fig
