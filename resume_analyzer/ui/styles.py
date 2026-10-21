"""
Custom CSS injected into the Streamlit page.

Kept in its own module so the presentation layer can be restyled without
touching any logic.
"""

CSS = """
<style>
.big-score {
    font-size: 3rem;
    font-weight: 700;
}
.score-card {
    padding: 1.2rem 1.5rem;
    border-radius: 12px;
    background-color: #f5f7fa;
    border: 1px solid #e3e6ea;
}
.skill-pill {
    display: inline-block;
    padding: 4px 12px;
    margin: 4px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 500;
}
.matched { background-color: #d4edda; color: #155724; }
.missing { background-color: #f8d7da; color: #721c24; }
</style>
"""
